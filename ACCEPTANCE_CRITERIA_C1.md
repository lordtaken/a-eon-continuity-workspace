# Criterios de aceptación C1

## P0

- [ ] El repositorio se crea desde cero en esta sesión Codex.
- [ ] Git se inicializa antes del primer archivo funcional.
- [ ] `streamlit run app.py` inicia la aplicación.
- [ ] La aplicación funciona sin API key.
- [ ] No existe una llamada real ejecutable a OpenAI.
- [ ] Existen las pestañas Workspace, Audit y Evidence.
- [ ] Load problematic demo carga el caso rojo.
- [ ] Load clean demo carga el caso limpio.
- [ ] Se admite pegar o cargar el paquete JSON.
- [ ] Se admite pegar o cargar la escena.
- [ ] El motor es local, determinista y orientado por reglas/datos.
- [ ] No devuelve simplemente un reporte completo hardcodeado.
- [ ] Caso problemático: rojo, exactamente cinco hallazgos validados.
- [ ] Caso limpio: verde, cero hallazgos.
- [ ] Cada cita de autoridad se valida contra la autoridad enlazada.
- [ ] Cada cita auditada se valida contra la escena.
- [ ] Evidencia inválida no gobierna el semáforo.
- [ ] El semáforo se recalcula en Python.
- [ ] Exportación Markdown válida.
- [ ] Exportación JSON válida.
- [ ] La tarjeta Retomar trabajo usa datos sintéticos.
- [ ] Los candados son visibles.
- [ ] “No changes are applied automatically.” permanece visible.
- [ ] No existe reescritura automática.
- [ ] No se incorpora información privada.
- [ ] La interfaz es legible en móvil.
- [ ] Reduced motion está contemplado.
- [ ] La suite contiene al menos nueve pruebas relevantes.
- [ ] Todas las pruebas pasan.
- [ ] Compilación Python correcta.
- [ ] README y BUILD_LOG completos.
- [ ] El flujo puede demostrarse en menos de tres minutos.

## P1

No implementar mientras exista un P0 fallido.

- filtros;
- copiar hallazgo;
- pulido visual adicional;
- fixture de contingencia;
- adaptador futuro de IA sin ejecución.

## Cierre

C1 puede cerrarse solo cuando todos los P0 estén verdes.
