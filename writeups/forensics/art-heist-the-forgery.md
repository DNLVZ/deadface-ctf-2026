# Art Heist: The Forgery

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Forensics · **Puntos en el catálogo:** 25 · **Estado:** Verificado

Distinguir la pintura que contiene una firma oculta en sus metadatos.
Evidencia: Reproducido con el archivo original

Herramientas: ZIP, metadatos XMP y búsqueda de texto


## Procedimiento

1. Abrir CTF_Forgery_Paintings.zip y enumerar Painting_001.png a Painting_005.png. Ignorar los archivos
    auxiliares de __MACOSX al comparar las pinturas.

2. Inspeccionar los metadatos de cada PNG y buscar propiedades XMP, en especial dc:identifier.

3. En Painting_002.png aparece deadface{L4MIA_SIGNS_HER_WORK}. La revisión local confirmó que la
    cadena está en los bytes de esa imagen.

4. Relacionar el identificador con la pregunta de la falsificación, conservando la imagen y el bloque de
    metadatos.

5. Evitar decidir únicamente por diferencias estéticas entre cuadros. El mensaje incrustado aporta la evidencia
    concreta del reto.


## Comandos o lógica reproducible

```text
import zipfile, re
with zipfile.ZipFile("CTF_Forgery_Paintings.zip") as z:
    for name in z.namelist():
        if name.endswith(".png") and not name.startswith("__MACOSX/"):
            for flag in re.findall(rb"deadface\{[^}]+\}", z.read(name)):
                print(name, flag.decode())


```

## Resultado conservado

```text
deadface{L4MIA_SIGNS_HER_WORK}

```

## Por qué funciona

Una firma puede existir como metadato estructurado sin modificar el aspecto visual principal de la obra.


## Aprendizaje para el análisis

Comparar archivos de un conjunto mediante propiedades verificables y registrar cuál produjo el hallazgo.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 55, página 66. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
