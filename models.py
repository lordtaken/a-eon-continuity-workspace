"""Typed data contracts for the local continuity auditor."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


Domain = Literal[
    "chronology", "character", "object", "relationship", "location", "rule", "other"
]
AuthorityStatus = Literal["protected", "active", "provisional", "deprecated"]
Severity = Literal["critical", "high", "medium", "low"]
FindingType = Literal[
    "contradiction",
    "continuity_leak",
    "risk",
    "ambiguity",
    "protected_state_violation",
]
Signal = Literal["red", "amber", "green"]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class AuthoritySource(StrictModel):
    document: str = Field(min_length=1)
    locator: str = Field(min_length=1)
    quote: str = Field(min_length=1)


class AuthorityRecord(StrictModel):
    id: str = Field(min_length=1)
    domain: Domain
    status: AuthorityStatus
    severity_if_breached: Severity
    statement: str = Field(min_length=1)
    source: AuthoritySource
    notes: str | None = None

    @model_validator(mode="after")
    def source_quote_belongs_to_record(self) -> "AuthorityRecord":
        if self.source.quote not in self.statement:
            raise ValueError("source.quote must appear literally in statement")
        return self


class ContinuityPackage(StrictModel):
    project_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    version: str = Field(min_length=1)
    authority_order: list[str] = Field(default_factory=list)
    records: list[AuthorityRecord] = Field(min_length=1)

    @model_validator(mode="after")
    def authority_ids_are_unique(self) -> "ContinuityPackage":
        ids = [record.id for record in self.records]
        if len(ids) != len(set(ids)):
            raise ValueError("authority record IDs must be unique")
        return self


class Finding(StrictModel):
    finding_id: str = Field(min_length=1)
    type: FindingType
    severity: Severity
    authority_id: str = Field(min_length=1)
    authority_quote: str = Field(min_length=1)
    audited_quote: str = Field(min_length=1)
    explanation: str = Field(min_length=1)
    recommended_action: str = Field(min_length=1)
    confidence: float = Field(ge=0, le=1)
    evidence_validated: bool


class AuditReport(StrictModel):
    audit_id: str = Field(min_length=1)
    created_at: str | None = None
    model: str | None = None
    overall_signal: Signal
    summary: str = Field(min_length=1)
    findings: list[Finding]
    human_decision_required: Literal[True] = True
