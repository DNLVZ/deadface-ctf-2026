# Exfiltration

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Steganography · **Puntos en el catálogo:** 75 · **Estado:** Documentado

Recomponer una bandera distribuida entre varias fotografías.
Evidencia: Documentado en la sesión

Herramientas: Metadatos EXIF, Python y conversión hexadecimal


## Procedimiento

1. Extraer exfiltration.zip en una carpeta de trabajo y revisar los metadatos de todas las imágenes, no solo la
    primera.

2. Localizar ImageUniqueID. En este conjunto su valor contiene fragmentos hexadecimales en lugar de un
     identificador fotográfico habitual.

3. Extraer también las fechas y horas de captura. El nombre de archivo no establece necesariamente el orden
    del mensaje.

4. Ordenar las imágenes por su marca temporal de captura, conservando una tabla de archivo, fecha y
    fragmento. Si hubiera empates, no inventar un desempate: revisar las otras propiedades.

5. Concatenar los fragmentos en ese orden y convertir el hexadecimal a bytes. Interpretar la salida como texto
    para recuperar timing-is-everything.

6. Comprobar que la concatenación usa cada fragmento una sola vez y que el número de caracteres
    hexadecimales es par.


## Comandos o lógica reproducible

```text
# Alternativa de extracción en ExifTool:
# exiftool -r -DateTimeOriginal -ImageUniqueID -json exfiltration > meta.json
import json
rows = json.load(open("meta.json", encoding="utf-8"))
rows = [r for r in rows if "ImageUniqueID" in r]
rows.sort(key=lambda r: r["DateTimeOriginal"])
hex_text = "".join(r["ImageUniqueID"] for r in rows)
print(bytes.fromhex(hex_text).decode())


```

## Resultado conservado

```text
deadface{timing-is-everything}

```

## Por qué funciona

La exfiltración se reparte entre un campo aparentemente inocuo y una regla de ordenación temporal.
Decodificar antes de ordenar no reconstruye el mensaje.


## Aprendizaje para el análisis

Al analizar lotes de archivos, correlacionar contenido y cronología. Registrar los campos exactos usados para
ordenar.


## Alcance de la reconstrucción

El comando de ExifTool es una alternativa reproducible; no se afirma que ExifTool estuviera instalado en la laptop durante la
competencia.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 14, página 25. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
