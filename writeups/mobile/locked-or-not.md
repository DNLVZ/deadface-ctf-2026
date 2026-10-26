# Locked... or Not?

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Mobile · **Puntos en el catálogo:** 150 · **Estado:** Verificado

Recuperar un texto de respaldo incrustado en una aplicación Android.
Evidencia: Reproducible con el paquete conservado

Herramientas: Python 3, ZIP, búsqueda de cadenas DEX y Base64


## Procedimiento

1. Abrir df-securenotes.apk.zip y después df-securenotes.apk. No es necesario instalar la aplicación ni superar
    su pantalla de bloqueo para inspeccionar el paquete.

2. Enumerar los archivos DEX. El dato relevante está en classes2.dex, por lo que revisar solo classes.dex sería
    insuficiente.

3. Buscar getSecureBackupText y apiKeyBackup. La sesión identificó una cadena Base64 cercana a esa
    lógica.

4. Decodificar ZGVhZGZhY2V7ZXotbW9iaWxlLXRvLXN0YXJ0fQ== para obtener deadface{ez-mobile-to-start}.

5. Relacionar el literal con su función en el bytecode. La salida debe atribuirse al respaldo expuesto, no a una
    supuesta vulneración de la contraseña de la interfaz.


## Comandos o lógica reproducible

```text
import zipfile, io, base64
with zipfile.ZipFile("df-securenotes.apk.zip") as outer:
    apk = zipfile.ZipFile(io.BytesIO(outer.read("df-securenotes.apk")))
    dex = apk.read("classes2.dex")
    value = b"ZGVhZGZhY2V7ZXotbW9iaWxlLXRvLXN0YXJ0fQ=="
    assert value in dex
    print(base64.b64decode(value).decode())


```

## Resultado conservado

```text
deadface{ez-mobile-to-start}

```

## Por qué funciona

El contenido estático de una aplicación sigue siendo accesible aunque su interfaz muestre un candado. Base64
no establece control de acceso.


## Aprendizaje para el análisis

Analizar todas las unidades DEX y los recursos, además de la actividad principal.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 56, página 67. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
