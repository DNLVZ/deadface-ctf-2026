# Bedside Manner

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Brain Scans · **Puntos en el catálogo:** 15 · **Estado:** Documentado

Encontrar una pista en el HTML de la interfaz de un dispositivo médico simulado.
Evidencia: Documentado en la sesión

Herramientas: Navegador y herramientas de desarrollo


## Procedimiento

1. Abrir el dispositivo del laboratorio y seleccionar Touchscreen para acceder al panel de inicio de sesión.

2. Abrir las herramientas de desarrollo y examinar Elements o el documento HTML recibido. Buscar deadface{ y
    comentarios TODO.

3. Localizar el comentario que conserva v13w_s0urc3_sav3s_l1v3s. Los comentarios no aparecen en la página
     renderizada, pero se entregan al navegador.

4. Registrar el fragmento HTML y su ubicación en la interfaz. No era necesario escanear puertos ni probar
    contraseñas.

5. Mantener el resultado separado de Factory Settings: aquí se inspecciona código fuente; allí se utilizan
    credenciales del manual.


## Resultado conservado

```text
deadface{v13w_s0urc3_sav3s_l1v3s}

```

## Por qué funciona

Un comentario HTML es contenido del cliente. Ocultarlo de la vista normal no evita su lectura.


## Aprendizaje para el análisis

Revisar los artefactos enviados al navegador y respetar las restricciones del laboratorio, que excluía escaneo y
fuerza bruta.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 40, página 51. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
