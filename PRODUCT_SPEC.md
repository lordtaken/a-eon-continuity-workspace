# Product Specification — A‑Eon Continuity Auditor V0.1

## 1. Problema

En obras largas, las decisiones de continuidad quedan dispersas entre biblias narrativas, fichas de personajes, cronologías, versiones y notas. Una escena nueva puede contradecir esas autoridades sin que el autor lo advierta.

## 2. Usuario primario

- novelistas y guionistas que trabajan obras extensas;
- editores de continuidad;
- equipos narrativos pequeños.

## 3. Propuesta de valor

El usuario entrega:

1. un paquete de continuidad;
2. una escena o capítulo nuevo.

La herramienta devuelve un **dictamen auditable**, no una reescritura: cada hallazgo enlaza una cita exacta de la autoridad con una cita exacta del texto auditado.

## 4. Categoría Build Week

**Work & Productivity.**

## 5. Flujo principal

1. Cargar el ejemplo o pegar datos.
2. Validar entradas.
3. Ejecutar auditoría.
4. Mostrar semáforo general.
5. Mostrar hallazgos ordenados por severidad.
6. Revisar evidencia y recomendación.
7. Exportar Markdown o JSON.

## 6. Tipos de hallazgo

- `contradiction`
- `continuity_leak`
- `risk`
- `ambiguity`
- `protected_state_violation`

## 7. Severidad

- `critical`: contradice una autoridad protegida o hace imposible la continuidad.
- `high`: rompe un estado relevante y exige corrección antes de aprobar.
- `medium`: ambigüedad o riesgo que puede producir contradicción posterior.
- `low`: inconsistencia menor o mejora de trazabilidad.

## 8. Semáforo determinista

- `red`: existe al menos un hallazgo `critical` o `high` validado.
- `amber`: no hay `critical/high`, pero existe al menos un `medium` validado.
- `green`: no existen hallazgos validados o solo existen `low`.

El modelo puede sugerir un semáforo, pero la aplicación debe recalcularlo.

## 9. Restricciones

- Sin reescritura automática.
- Sin aplicación automática de cambios.
- Sin canon.
- Sin corpus real de A‑Eón.
- Sin Drive productivo.
- Sin multiagentes.
- Sin almacenamiento persistente.
- Sin autenticación ni base de datos.
- Sin navegación multipágina.
- Sin endpoint separado salvo que sea estrictamente necesario.

## 10. Diferenciador demostrable

No es “preguntar a un chatbot si hay errores”. El producto exige:

- autoridad identificada;
- evidencia dual;
- estructura estable;
- verificación literal de citas;
- semáforo calculado en código;
- próxima acción bajo control humano.

## 11. Criterio de tamaño

El MVP debe permanecer comprensible como un repositorio Python pequeño. La calidad se mide por el flujo completo y verificable, no por cantidad de componentes.
