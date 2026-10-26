# Crown Jewels

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 75 · **Estado:** Documentado

Identificar el documento de interés sustraído durante el incidente.
Evidencia: Documentado en la sesión

Herramientas: Captura de red y resultados de memoria


## Procedimiento

1. Buscar nombres de archivos en las operaciones SMB y en los resultados de memoria relacionados con la
    transferencia.

2. Localizar annual_report.pdf. Revisar su contexto para diferenciar un acceso al documento de una mera
     mención en una lista.

3. Relacionar el archivo con la conversación o el comando de exfiltración documentado en la serie.

4. Registrar el nombre completo y su extensión. No añadir una ruta que el reto no solicite ni confundirlo con otro
    documento del recurso compartido.

5. Mantener la identificación del archivo separada de una recuperación de su contenido: esta bandera responde
    al nombre, no certifica que se haya reconstruido el PDF.


## Resultado conservado

```text
deadface{annual_report.pdf}

```

## Por qué funciona

Los nombres de archivo observados en operaciones de acceso ayudan a identificar el objetivo del robo y a
orientar la búsqueda posterior.


## Aprendizaje para el análisis

Diferenciar metadatos de transferencia, acceso efectivo y contenido recuperado.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 23, página 34. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
