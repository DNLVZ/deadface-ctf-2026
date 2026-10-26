# Ghost of Squares Past

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** OSINT · **Puntos en el catálogo:** 150 · **Estado:** Parcial

Relacionar cuatro plazas y un monumento central para construir la respuesta ordenada.
Evidencia: Documentado en la sesión

Herramientas: OSINT geográfico y contraste de hitos históricos


## Procedimiento

1. Identificar las plazas correspondientes a las pistas: Johnson, Oglethorpe, Chippewa y Telfair.

2. Anotar las fechas requeridas para cada plaza en el mismo orden del reto. La secuencia documentada es
    1733, 1742, 1815 y 1733.

3. Usar la relación espacial descrita para localizar el elemento central. La sesión identificó el monumento
    Gordon.

4. Componer la respuesta con guiones y el apellido final en minúsculas: 1733-1742-1815-1733-gordon.

5. Guardar las referencias geográficas e históricas por separado: el año de creación de una plaza puede diferir
    del año de instalación de una estatua.


## Resultado conservado

```text
deadface{1733-1742-1815-1733-gordon}

```

## Por qué funciona

La solución combina identificación espacial con atributos históricos. El orden forma parte de la respuesta.


## Aprendizaje para el análisis

En OSINT, documentar qué pregunta responde cada fuente y no intercambiar fechas de objetos próximos.


## Alcance de la reconstrucción

Se conservan las identificaciones y la respuesta histórica; faltan los enlaces originales de cada hito para una reproducción documental
completa.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 39, página 50. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
