# Trazabilidad C1

## Clasificación del prototipo previo

```text
WORK_PROTOTYPE:
REFERENCE_IMPLEMENTATION
BEHAVIORAL_ORACLE
NOT_PRIMARY_CODEX_BUILD
NOT_INCLUDED
```

## Construcción concursable

```text
PRIMARY_BUILD_ENVIRONMENT:
CODEX

PRIMARY_BUILD_SESSION:
PENDING

CORE_IMPLEMENTATION:
MUST_BE_CREATED_IN_THIS_SESSION
```

## Reglas

- crear repositorio nuevo;
- no copiar archivos `.py` del prototipo de Work;
- registrar decisiones y resultados en `BUILD_LOG.md`;
- commits pequeños y fechados;
- conservar el hilo principal;
- no abrir subhilos;
- no publicar ni enviar Devpost;
- no inventar un Session ID.

## Commits sugeridos

1. `chore: initialize primary codex build`
2. `feat: add schemas and synthetic fixtures`
3. `feat: implement deterministic audit engine`
4. `feat: validate evidence and calculate signals`
5. `feat: add workspace audit and evidence views`
6. `feat: add markdown and json exports`
7. `test: cover red clean evidence and exports`
8. `docs: record codex build and demo workflow`

## Cierre esperado

```text
BUILD_WEEK_C1:
CLOSED_GREEN

PRIMARY_CODEX_BUILD:
VERIFIED

LIVE_API_CALLS:
ZERO

NEXT:
BUILD_WEEK_M2_DELIVERY_PREP
```
