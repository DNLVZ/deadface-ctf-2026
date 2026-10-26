# Back to Basics

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Aurora Patient Zero · **Puntos en el catálogo:** 15 · **Estado:** Verificado

Recuperar el nombre de un sistema interno desde el ejecutable del paquete iOS.
Evidencia: Reproducido con el archivo original

Herramientas: Python 3 y extracción de cadenas


## Procedimiento

1. Consultar CFBundleExecutable en Info.plist para identificar el binario correcto: Aurora Health Mobile. Evitar
    elegir un icono o un recurso por su nombre.

2. Extraer cadenas ASCII legibles del binario sin ejecutarlo. Esta primera inspección permite encontrar
    mensajes de diagnóstico, nombres de hosts y rutas.

3. Buscar términos vinculados con las pistas anteriores, especialmente Westlake. Ampliar la búsqueda a
    gateway, gw e internal cuando corresponda.

4. Localizar gw-westlake-int-03 y revisar las cadenas vecinas para comprobar que se trata del identificador
     buscado y no de una coincidencia aislada.

5. Registrar el nombre exactamente, incluidos los guiones y el sufijo numérico. No convertirlo en una dirección
    IP ni añadir un dominio que no aparezca en la evidencia.


## Comandos o lógica reproducible

```text
import re
binary = ipa.read(prefix + info["CFBundleExecutable"])
for text in re.findall(rb"[ -~]{5,}", binary):
    if b"westlake" in text.lower():
        print(text.decode())


```

## Resultado conservado

```text
deadface{gw-westlake-int-03}

```

## Por qué funciona

Compilar una aplicación no elimina automáticamente sus cadenas. Los nombres internos también pueden
revelar detalles de arquitectura.


## Aprendizaje para el análisis

La búsqueda de cadenas es una fase de reconocimiento estático, no una prueba suficiente de que el sistema
interno sea accesible.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 04, página 15. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
