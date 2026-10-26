# Info Leaks

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Aurora Patient Zero · **Puntos en el catálogo:** 25 · **Estado:** Verificado

Identificar información personal expuesta dentro del paquete iOS de Aurora. El análisis comienza en los
archivos de configuración, antes de estudiar el ejecutable.
Evidencia: Reproducido con el archivo original

Herramientas: Python 3, zipfile, plistlib y base64


## Procedimiento

1. Conservar AuroraPatientPortal.ipa.zip como original y calcular su SHA-256. La extensión IPA no implica que
    sea necesario disponer de un iPhone: el contenedor puede inspeccionarse como ZIP.

2. Abrir el ZIP exterior y, dentro de él, AuroraPatientPortal.ipa. Localizar
    Payload/aurora-patient-portal.app/Info.plist. Un plist es un archivo de propiedades de la aplicación; puede
    estar en XML o en formato binario.

3. Leer el plist con plistlib, que admite ambos formatos. Buscar claves propias del producto, además de las
     habituales que empiezan por CFBundle. La propiedad AuroraPatientBootstrap contiene una cadena
     Base64.

4. Decodificar esa propiedad. El JSON resultante identifica a Mara Voss, fecha de nacimiento 1988-04-17 y
    clínica Westlake. Base64 solo representa bytes mediante caracteres; no protege un secreto.

5. Aplicar el formato solicitado por el reto: nombre y apellido en minúsculas separados por guiones, seguidos de
    la fecha. No añadir la clínica a la respuesta.


## Comandos o lógica reproducible

```text
import zipfile, io, plistlib, base64
outer = zipfile.ZipFile("AuroraPatientPortal.ipa.zip")
ipa = zipfile.ZipFile(io.BytesIO(outer.read("AuroraPatientPortal.ipa")))
prefix = "Payload/aurora-patient-portal.app/"
info = plistlib.loads(ipa.read(prefix + "Info.plist"))
print(base64.b64decode(info["AuroraPatientBootstrap"]).decode())


```

## Resultado conservado

```text
deadface{mara-voss-1988-04-17}

```

## Por qué funciona

La información estaba distribuida con el cliente. Cualquier persona que obtenga el paquete puede leerla sin
autenticarse ante el servidor.


## Aprendizaje para el análisis

No incluir datos personales reales ni secretos en configuraciones que se distribuyen al usuario. Revisar el
artefacto de compilación, no solo el código fuente.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 01, página 12. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
