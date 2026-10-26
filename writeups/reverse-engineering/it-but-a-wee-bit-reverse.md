# It But A Wee Bit Reverse

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Reverse Engineering · **Puntos en el catálogo:** 15 · **Estado:** Parcial

Revertir una contraseña ofuscada y utilizarla para descodificar la bandera.
Evidencia: Documentado en la sesión

Herramientas: Análisis estático de re02.bin y Python


## Procedimiento

1. Identificar el formato de re02.bin y conservar su hash. Inspeccionar cadenas y la función que valida la
     entrada antes de ejecutar el binario.

2. Localizar pw_enc y la operación XOR 0x42 aplicada a sus caracteres. Como XOR es reversible, aplicar de
     nuevo 0x42 recupera la contraseña.

3. La contraseña documentada es sunshine42. Validarla volviendo a aplicar XOR y comparando con los bytes
     de pw_enc.

4. Localizar flag_enc y observar cómo se repite la contraseña sobre sus bytes. Usar key[i % len(key)] para
     reproducir el índice circular.

5. Aplicar XOR entre cada byte de flag_enc y el byte correspondiente de sunshine42. La salida registrada es
    x0r_1s_not_encryption.

6. Conservar los arrays originales, sus offsets y el script. Si falta un array, no sustituirlo por la propia bandera
    para simular una recuperación.


## Comandos o lógica reproducible

```text
def xor_repetido(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

# pw_enc y flag_enc deben provenir del binario analizado.
# password = bytes(b ^ 0x42 for b in pw_enc)
# assert password == b"sunshine42"
# print(xor_repetido(flag_enc, password).decode())


```

## Resultado conservado

```text
deadface{x0r_1s_not_encryption}

```

## Por qué funciona

Una clave y un algoritmo incorporados al mismo cliente pueden recuperarse mediante análisis estático. La
repetición de XOR no equivale a cifrado robusto.


## Aprendizaje para el análisis

Registrar offsets y constantes, no solo la contraseña final.


## Alcance de la reconstrucción

Las constantes completas de los arrays no se recuperaron del historial; se conserva el algoritmo y el resultado, con el binario
respaldado para continuar.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 43, página 54. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
