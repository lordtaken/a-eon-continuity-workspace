# Workspace Transfer Brief

## Identidad visible

**Nombre:** A-Eon Continuity Workspace  
**Subtítulo:** Evidence-based continuity control for complex creative projects  
**Módulo operativo:** Continuity Auditor

## Vistas mínimas

La aplicación es una sola aplicación Streamlit con tres pestañas:

### Workspace

Mostrar con datos sintéticos:

- identidad del proyecto;
- fuentes activas;
- reglas protegidas;
- riesgos abiertos;
- estado de la última auditoría;
- última operación;
- próxima acción;
- candados activos.

Incluir una tarjeta **Retomar trabajo** con:

- última operación;
- checkpoint sintético;
- próxima acción;
- candados.

### Audit

- cargar ejemplo problemático;
- cargar ejemplo limpio;
- pegar o cargar paquete JSON;
- pegar o cargar escena Markdown o texto;
- ejecutar auditoría local;
- errores legibles;
- advertencia permanente:
  **No changes are applied automatically.**

### Evidence

- semáforo;
- resumen;
- hallazgos;
- tipo;
- severidad;
- autoridad;
- cita exacta de autoridad;
- cita exacta auditada;
- explicación;
- próxima acción;
- validación literal;
- descarga Markdown;
- descarga JSON.

Sin informe, mostrar un estado vacío claro.

## Lenguaje visual

- fondo oscuro estratificado;
- títulos editoriales;
- microtexto técnico sans serif;
- tarjetas densas pero legibles;
- bordes finos;
- transparencias contenidas;
- acentos oro, musgo y óxido;
- símbolos mínimos;
- una columna en móvil;
- respeto por `prefers-reduced-motion`.

No copiar activos, glifos, componentes ni código de Atlas.

## Modelo genérico de estado

```text
identidad
tipo de entrada
estado actual
fuentes
reglas protegidas
riesgos
última operación
checkpoint sintético
próxima acción
candados
salida exportable
```

## Candados

```text
ATLAS_REFERENCE_ONLY
SYNTHETIC_DATA_ONLY
NO_PRIVATE_DATA_TRANSFER
NO_REAL_CANON_TRANSFER
NO_SOURCE_CODE_TRANSFER
NO_VISUAL_ASSET_COPY
NO_DRIVE_CONNECTION
NO_AUTOMATIC_REWRITE
NO_SILENT_CHANGES
NO_DATABASE
NO_AUTHENTICATION
NO_MULTIAGENT
NO_SITE_PUBLICATION
```
