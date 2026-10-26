# Down the Rabbit Hole

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Aurora Patient Zero · **Puntos en el catálogo:** 10 · **Estado:** Verificado

Encontrar el identificador del paciente oculto en los metadatos de la radiografía incluida en la aplicación.
Evidencia: Reproducido con el archivo original

Herramientas: Python 3 y lectura de metadatos XMP


## Procedimiento

1. Reutilizar el contenedor IPA abierto en Info Leaks. Enumerar sus recursos y localizar aurora_chest_xray.jpg.

2. Distinguir los píxeles visibles de los metadatos. XMP permite incluir propiedades XML en una imagen; el
     contenido no tiene por qué aparecer al abrirla en un visor.

3. Buscar dc:identifier dentro de los bytes del JPEG. El prefijo dc corresponde al vocabulario Dublin Core
    empleado en el bloque XMP.

4. Extraer el valor completo PID-847261 y conservar su prefijo y guion para esta bandera. Registrar también el
    número 847261: servirá como clave de consulta en el siguiente reto.

5. Relacionar el hallazgo con el recurso concreto. No confundir el identificador de paciente con el nombre del
    ejecutable, el identificador del paquete o una fecha.


## Comandos o lógica reproducible

```text
import re
jpg = ipa.read(prefix + "aurora_chest_xray.jpg")
for value in re.findall(rb"<dc:identifier>(.*?)</dc:identifier>", jpg):
    print(value.decode())


```

## Resultado conservado

```text
deadface{PID-847261}

```

## Por qué funciona

La imagen actuaba como contenedor de una segunda pista. La combinación de configuración y metadatos
permite correlacionar piezas que, por separado, parecen inofensivas.


## Aprendizaje para el análisis

Inspeccionar y eliminar metadatos sensibles de los recursos que acompañan una aplicación. Mantener
trazabilidad entre un dato y su archivo de origen.


## Alcance de la reconstrucción

El código reutiliza ipa y prefix definidos en el caso anterior.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 02, página 13. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
