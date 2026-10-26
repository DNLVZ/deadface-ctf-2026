# Car Crash

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** OSINT · **Puntos en el catálogo:** 50 · **Estado:** Documentado

Identificar una empresa a partir de un número visible en un camión y recuperar la fecha solicitada.
Evidencia: Documentado en la sesión

Herramientas: Inspección de fotografía y OSINT corporativo


## Procedimiento

1. Abrir truck_crash.png con suficiente resolución y localizar la identificación USDOT del vehículo.

2. La lectura registrada fue 080806. Mantener los dígitos iniciales al transcribir, aunque un registro de consulta
     pueda normalizarlos.

3. Relacionar el número con J.B. Hunt mediante la fuente de transporte consultada durante el reto.

4. Buscar la fecha de fundación de esa empresa y contrastar el orden de día y mes exigido por el enunciado. La
    respuesta registrada fue 08_10_1961.

5. Conservar imagen, identificador y fuente de fecha como una cadena de evidencia. La fecha no debe
    deducirse del año del vehículo o del accidente.


## Resultado conservado

```text
deadface{08_10_1961}

```

## Por qué funciona

Un identificador administrativo puede conectar una imagen con una entidad y, posteriormente, con un dato
histórico verificable.


## Aprendizaje para el análisis

Mantener separados el dato leído, la identificación inferida y el hecho consultado.


## Alcance de la reconstrucción

La fecha y su formato se conservan como respuesta histórica del reto; no se presenta una nueva verificación externa de la fundación.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 35, página 46. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
