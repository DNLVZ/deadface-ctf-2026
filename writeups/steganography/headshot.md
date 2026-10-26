# Headshot

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Steganography · **Puntos en el catálogo:** 10 · **Estado:** Verificado

Encontrar un mensaje en los metadatos PNG sin confundirlo con el contenido visual.
Evidencia: Reproducido con el archivo original

Herramientas: Python 3, zipfile y Pillow


## Procedimiento

1. Abrir headshot.zip y enumerar sus cuatro entradas. La presencia de tres PNG y un archivo terminado en
    _original sugiere comparar versiones y propiedades.

2. Leer cada imagen con Pillow y consultar im.info. Esta propiedad expone información que el decodificador
     reconoce, como resolución, transparencia y comentarios.

3. En headshot003.png aparece la clave Comment con la bandera. El hallazgo está en metadatos textuales y
    no exige esteganografía de bits menos significativos.

4. Buscar además el marcador deadface{ en los bytes del archivo para corroborar la lectura del comentario.
    Registrar archivo, propiedad y valor.

5. La revisión del original resolvió una confusión histórica entre este reto y The Attending. La bandera de
     Headshot pertenece exclusivamente a headshot003.png.


## Comandos o lógica reproducible

```text
import zipfile, io
from PIL import Image
with zipfile.ZipFile("headshot.zip") as z:
    for name in z.namelist():
        if name.endswith(".png"):
            image = Image.open(io.BytesIO(z.read(name)))
            print(name, image.info.get("Comment"))


```

## Resultado conservado

```text
deadface{b00m_h34Dsh0TTT}

```

## Por qué funciona

PNG admite bloques de texto que un visor puede ignorar. La ausencia de texto visible sobre la imagen no
implica ausencia de información.


## Aprendizaje para el análisis

Comenzar por metadatos y cadenas antes de aplicar técnicas más complejas.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 12, página 23. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
