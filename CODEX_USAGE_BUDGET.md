# Presupuesto operativo de Codex

## Restricción

Jorge dispone de un margen semanal limitado. Este build debe minimizar exploración y retrabajo.

## Política

- una sola sesión principal;
- sin subhilos;
- sin comparación de frameworks;
- sin prototipos alternativos;
- sin refactorización estética;
- sin dependencias pesadas;
- sin funciones P1 hasta cerrar todos los P0;
- sin despliegue antes de pasar pruebas locales;
- una única ronda de reparación dirigida por resultados.

## Bloques previstos

### Bloque A — Core build

Crear repositorio, lógica, interfaz, exportaciones y pruebas en una sola ejecución coherente.

### Bloque B — Validación

Ejecutar:

- corpus problemático;
- corpus limpio;
- pruebas unitarias;
- verificación manual del flujo.

Corregir solo fallos P0.

### Bloque C — Entrega técnica

Cerrar README, BUILD_LOG y `/feedback`.

## Uso del reinicio disponible

El reinicio queda reservado para:

- corrupción real del contexto;
- sesión bloqueada sin progreso;
- fallo irrecuperable del workspace.

No usarlo para rediseñar ni para mejorar detalles cosméticos.
