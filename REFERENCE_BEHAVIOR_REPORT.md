# Reporte de comportamiento de referencia

Un prototipo construido en Work fue verificado como oráculo de comportamiento.

```text
WORK_PROTOTYPE_SHA256:
f63f2fd1c29602c420f317e0f7f8900f808da52b3beb06ff0e38087d4b7852a9

SOURCE_CODE_TRANSFERRED:
NO
```

## Caso problemático

```text
overall_signal: red
finding_count: 5
validated_evidence_count: 5
```

Hallazgos esperados:

1. `AUTH-001` — cronología — `critical`
2. `AUTH-002` — lesión — `high`
3. `AUTH-003` — objeto protegido — `critical`
4. `AUTH-004` — relación — `high`
5. `AUTH-005` — ubicación cerrada — `high`

Las citas exactas están en `demo/expected-findings.json`.

## Caso limpio

```text
overall_signal: green
finding_count: 0
```

## Controles demostrados por el prototipo de referencia

- evidencia dual literal;
- semáforo recalculado;
- Markdown;
- JSON;
- cero llamadas API;
- interfaz sin excepción;
- nueve pruebas aprobadas.

Codex debe reproducir el comportamiento mediante una implementación nueva.
