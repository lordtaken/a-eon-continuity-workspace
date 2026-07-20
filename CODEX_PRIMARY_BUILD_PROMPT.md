# PROMPT MAESTRO — BUILD_WEEK_C1 PRIMARY CODEX BUILD

Construye desde cero, en esta sesión de Codex, el repositorio concursable:

# A-Eon Continuity Workspace

Módulo central:

# Continuity Auditor

## 0. Declaración de origen

Existe un prototipo previo construido en ChatGPT Work. No está incluido como
código en este paquete. Sus resultados se suministran únicamente como oráculo
de comportamiento.

No busques, solicites ni copies el código de ese prototipo.

La mayoría de la funcionalidad central del repositorio final debe ser creada,
probada y documentada en esta sesión.

## 1. Acceso y costo

Codex se usa mediante el inicio de sesión de ChatGPT Plus.

No:

- solicites `OPENAI_API_KEY`;
- crees una API key;
- añadas crédito o facturación;
- hagas llamadas reales a la API;
- instales el SDK de OpenAI salvo necesidad documental no ejecutable.

El producto C1 debe funcionar completamente en local.

```text
LIVE_API_CALLS = ZERO
OPENAI_API_KEY_REQUIRED = NO
```

## 2. Disciplina de sesión

- Trabaja en una carpeta y repositorio nuevos.
- Inicializa Git antes del primer archivo funcional.
- No abras subhilos ni agentes auxiliares.
- No compares frameworks.
- Usa Python + Streamlit.
- No amplíes el alcance.
- No implementes P1 antes de cerrar P0.
- Corrige únicamente fallos demostrados por pruebas o ejecución.

## 3. Lee en este orden

1. `HANDOFF_MANIFEST.md`
2. `PRODUCT_SPEC.md`
3. `ARCHITECTURE_C1.md`
4. `WORKSPACE_TRANSFER_BRIEF.md`
5. `ACCEPTANCE_CRITERIA_C1.md`
6. `REFERENCE_BEHAVIOR_REPORT.md`
7. `schemas/continuity-package.schema.json`
8. `schemas/audit-report.schema.json`
9. `demo/continuity-package.json`
10. `demo/new-scene.md`
11. `demo/clean-scene.md`
12. `demo/expected-findings.json`
13. `TRACEABILITY_C1.md`
14. `CODEX_USAGE_BUDGET.md`

## 4. Construcción obligatoria

Implementa:

### Datos y esquemas

- modelos tipados;
- validación del paquete;
- validación del informe;
- errores legibles.

### Motor local

Un motor determinista y orientado por reglas/datos que:

- examine las autoridades sintéticas;
- examine la escena;
- detecte los cinco conflictos del caso problemático;
- no detecte conflictos en el caso limpio;
- genere hallazgos estructurados;
- no devuelva un informe completo hardcodeado.

Puedes crear un registro pequeño de detectores por dominio o tipo de restricción.
La solución debe ser comprensible, testeable y suficiente para el corpus
demostrativo.

### Evidencia

- cita exacta de autoridad;
- cita exacta de escena;
- validación de ambos substrings;
- `evidence_validated`;
- exclusión de evidencia inválida del semáforo.

### Semáforo

Recalcular después de validar evidencia:

- rojo con `critical` o `high`;
- ámbar con `medium` y sin mayor severidad;
- verde sin hallazgos validados o solo `low`.

### Exportadores

- Markdown;
- JSON.

### Interfaz Streamlit

Una aplicación con pestañas:

- Workspace;
- Audit;
- Evidence.

Aplica `WORKSPACE_TRANSFER_BRIEF.md` sin copiar Atlas ni usar datos privados.

Mantén siempre visible:

> No changes are applied automatically.

No añadas reescritura automática.

## 5. Fixtures

Copia el corpus autorizado a `demo_data/`.

El caso problemático debe producir:

```text
red
5 findings
5 validated evidence pairs
```

El caso limpio debe producir:

```text
green
0 findings
```

## 6. Pruebas

Crea como mínimo nueve pruebas que cubran:

- carga del paquete;
- caso problemático;
- caso limpio;
- validación de autoridad;
- validación de cita auditada;
- evidencia inválida;
- semáforo rojo;
- semáforo verde;
- exportación Markdown;
- exportación JSON.

Pueden existir más de nueve.

Ejecuta:

```bash
python -m compileall .
pytest
```

Después inicia Streamlit y verifica que la aplicación arranque sin excepción.

## 7. Documentación

Crea:

- `README.md`;
- `BUILD_LOG.md`;
- `CHECKPOINT_BUILD_WEEK_C1_CLOSED.md`;
- manifiesto con hashes de los archivos finales.

README debe explicar:

- problema;
- flujo;
- instalación;
- ejecución;
- corpus sintético;
- motor local;
- ausencia de API;
- uso de Codex en la construcción;
- límites y control humano;
- demostración de menos de tres minutos.

BUILD_LOG debe distinguir:

- decisiones humanas recibidas;
- implementación realizada en Codex;
- pruebas;
- reparaciones;
- estado final.

## 8. Verificación de seguridad

Antes de cerrar:

- busca secretos y claves;
- confirma que no existe `OPENAI_API_KEY` real;
- confirma que no hay llamadas de red a OpenAI;
- confirma que no hay contenido privado;
- confirma que no hay código de Atlas;
- confirma que no hay código del prototipo de Work.

## 9. Resultado material

Genera un ZIP:

```text
AEON_BUILD_WEEK_CONTINUITY_WORKSPACE_CODEX_C1_20260719.zip
```

Excluye:

- `.venv`;
- cachés;
- `.git`;
- secretos;
- logs temporales;
- paquetes anteriores;
- Session ID.

Calcula SHA-256.

## 10. Condición de terminado

Detente cuando:

- todos los P0 estén verdes;
- pruebas completas pasen;
- caso problemático sea rojo con cinco hallazgos;
- caso limpio sea verde con cero;
- Streamlit arranque;
- documentación y manifiesto estén completos;
- ZIP y SHA-256 estén creados.

No despliegues.
No publiques Site.
No envíes Devpost.
No abras M2.

## 11. Respuesta final

Entrega solamente:

1. veredicto;
2. ruta del repositorio;
3. archivos creados;
4. pruebas y resultado;
5. caso problemático;
6. caso limpio;
7. evidencia y semáforo;
8. confirmación de cero API;
9. SHA-256 del ZIP;
10. checkpoint generado;
11. bloqueos reales;
12. próxima operación elegible.

Próxima operación:

```text
BUILD_WEEK_M2 — PREPARACIÓN DE ENTREGA
```

No la ejecutes.
