# Hidden Loot Box

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Steganography · **Puntos en el catálogo:** 15 · **Estado:** Documentado

Revelar un recurso que la página carga pero oculta con una capa visual.
Evidencia: Documentado en la sesión

Herramientas: Navegador y herramientas de desarrollo


## Procedimiento

1. Abrir la página del reto y examinar sus elementos con las herramientas de desarrollo. Localizar la sección
    .secret y las imágenes asociadas.

2. Identificar que cover.jpg se superpone al recurso oculto. La cobertura CSS cambia lo que se ve, pero no
     impide que el navegador descargue el contenido inferior.

3. Leer el atributo src del recurso oculto: /static/hidden.png. Abrir esa ruta en una pestaña dentro del mismo
     sitio del laboratorio, o desactivar la capa que lo tapa.

4. Leer la bandera en la imagen expuesta y conservar una captura junto con el fragmento HTML que demuestra
     cómo estaba oculta.

5. Diferenciar esta técnica de romper un control de acceso: el servidor ya entregaba la imagen al cliente y el
     ocultamiento ocurría en la presentación.


## Resultado conservado

```text
deadface{uh_I_feel_exposed}

```

## Por qué funciona

Todo recurso enviado al navegador puede inspeccionarse. Una capa, opacidad cero o display:none no
constituyen un mecanismo de autorización.


## Aprendizaje para el análisis

Aplicar permisos en el servidor y evitar enviar información que el usuario no deba recibir.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 13, página 24. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
