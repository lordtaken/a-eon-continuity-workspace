# Arquitectura C1 — Construcción primaria en Codex

## Principio

Codex debe construir en un repositorio vacío la mayoría de la funcionalidad
central. Los archivos incluidos son especificaciones, esquemas y fixtures;
no contienen la implementación previa de Work.

## Pila

- Python 3.11 o superior;
- Streamlit;
- Pydantic;
- Pytest;
- biblioteca estándar cuando sea suficiente.

No se necesita el SDK de OpenAI para C1.

## Árbol objetivo

```text
a-eon-continuity-workspace/
├── app.py
├── auditor.py
├── evidence.py
├── exporters.py
├── schemas.py
├── demo_data/
│   ├── continuity-package.json
│   ├── new-scene.md
│   └── clean-scene.md
├── tests/
│   ├── test_auditor.py
│   ├── test_evidence.py
│   ├── test_signals.py
│   └── test_exports.py
├── requirements.txt
├── .gitignore
├── README.md
├── BUILD_LOG.md
└── CHECKPOINT_BUILD_WEEK_C1_CLOSED.md
```

Codex puede ajustar nombres o combinar módulos cuando preserve separación clara
entre interfaz, auditoría, evidencia y exportación.

## Motor local

Debe ser:

- determinista;
- orientado por datos;
- trazable;
- capaz de reproducir los cinco hallazgos del corpus problemático;
- capaz de devolver cero hallazgos para el corpus limpio;
- independiente de una API;
- no reducido a devolver un JSON completo hardcodeado.

Puede usar un registro pequeño de reglas y patrones asociados a las autoridades
del paquete sintético. La autoridad y la cita deben proceder del paquete;
la cita auditada debe proceder literalmente de la escena.

## Evidencia

Cada hallazgo contiene:

- ID;
- tipo;
- severidad;
- authority_id;
- authority_quote;
- audited_quote;
- explicación;
- próxima acción;
- evidence_validated.

La aplicación debe validar que:

- la cita de autoridad aparece literalmente en el registro enlazado;
- la cita auditada aparece literalmente en la escena;
- un hallazgo inválido no gobierna el semáforo.

## Semáforo

- rojo: al menos un `critical` o `high` validado;
- ámbar: ningún `critical/high`, pero al menos un `medium` validado;
- verde: ningún hallazgo validado o solo `low`.

Se calcula en Python después de validar la evidencia.

## API

C1 es completamente local:

```text
OPENAI_API_KEY_REQUIRED = NO
LIVE_API_CALLS = ZERO
AI_RUNTIME = DISABLED
```

Puede existir únicamente una interfaz o mensaje de extensión futura. No debe
haber una ruta ejecutable que llame a la API.

## Estado

Streamlit puede usar `st.session_state` para conservar el último informe durante
la sesión. No persistir entradas o reportes fuera de la sesión.

## Exportación

- JSON válido;
- Markdown legible;
- misma información esencial que la vista Evidence.

## Responsive

- una columna efectiva en móvil;
- sin desbordamientos;
- controles utilizables;
- reduced motion contemplado.
