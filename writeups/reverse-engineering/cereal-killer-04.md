# Cereal Killer 04

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Reverse Engineering · **Puntos en el catálogo:** 250 · **Estado:** Parcial

Seguir una segunda etapa incrustada para recuperar el resultado del reto.
Evidencia: Documentado en la sesión

Herramientas: Desensamblado, extracción de DLL, MD5 y AES-256-CBC


## Procedimiento

1. Inspeccionar cereal04.exe y localizar la carga incrustada. La sesión identificó una DLL ofuscada mediante
     XOR con 0xA3.

2. Revertir XOR sobre los bytes de esa carga y guardar la DLL como archivo de análisis. Comprobar que la
    salida presenta una estructura PE coherente antes de continuar.

3. Analizar la lógica de validación y derivación relacionada con MD5. La contraseña recuperada fue booberry,
    asociada a Boo Berry.

4. Seguir la construcción de clave, IV y entrada de AES-256-CBC en el código. No asumir que un MD5 de 16
    bytes es directamente una clave AES-256 de 32 bytes: debe respetarse la derivación real.

5. Descifrar con los valores concretos de la rutina y validar el padding según la implementación. La sesión
    obtuvo la bandera completa.

6. Conservar tanto el ejecutable como payload.dll y el desensamblado. Estos archivos forman parte del
    respaldo de resultados.


## Comandos o lógica reproducible

```text
# Reversión de la capa XOR una vez delimitado el recurso:
def extraer_dll(recurso):
    plain = bytes(b ^ 0xA3 for b in recurso)
    assert plain[:2] == b"MZ", "Revisar límites o clave del recurso"
    return plain


```

## Resultado conservado

```text
deadface{Before_Consenting_to_Med_Exam_Ascertain_Destination_of_Finger!}

```

## Por qué funciona

El ejecutable distribuye su lógica entre una capa contenedora y una DLL. La primera extracción desbloquea la
segunda fase del análisis.


## Aprendizaje para el análisis

Una lista de algoritmos no sustituye la derivación exacta: guardar clave, IV, offsets y formato del ciphertext.


## Alcance de la reconstrucción

Resultado histórico recuperado. El resumen no incluye las constantes necesarias para un descifrado AES completo independiente.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 46, página 57. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
