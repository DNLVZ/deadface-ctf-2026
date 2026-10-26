# X Marks the Spot

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Cryptography · **Puntos en el catálogo:** 30 · **Estado:** Verificado

Decodificar una carga hexadecimal cifrada con XOR de un solo byte.
Evidencia: Reproducible desde el enunciado conservado

Herramientas: Python 3 y operaciones sobre bytes


## Procedimiento

1. Copiar el hexadecimal del enunciado sin añadir espacios o saltos dentro de los pares. Dos caracteres
    hexadecimales representan un byte.

2. Convertir la cadena a bytes. Intentar leer el hexadecimal como texto directamente no deshace el cifrado.

3. Probar las 256 claves de un byte. Filtrar los resultados buscando el marcador deadface{ y una frase legible
     alrededor.

4. La clave correcta es 0x44, equivalente a 68 decimal. Aplicarla a todos los bytes produce un mensaje de
     Spectre Technology con la bandera.

5. Volver a aplicar XOR 0x44 al texto recuperado y comprobar que reproduce los bytes originales. Esta
    verificación evita aceptar una coincidencia casual.


## Comandos o lógica reproducible

```text
raw = bytes.fromhex(
 "02362b2964302c2164372c25202b3337642b22641734212730362164"
 "1021272c2a2b282b233d7e6420212520222527213f3c2b361b751b"
 "263d30771b70301b701b3075297739")
for key in range(256):
    plain = bytes(b ^ key for b in raw)
    if b"deadface{" in plain:
        print(hex(key), plain.decode())
        assert bytes(b ^ key for b in plain) == raw


```

## Resultado conservado

```text
deadface{xor_1_byt3_4t_4_t1m3}

```

## Por qué funciona

XOR tiene la propiedad (x XOR k) XOR k = x. Reutilizar un único byte permite probar todas las claves posibles
sin un diccionario.


## Aprendizaje para el análisis

Hexadecimal es codificación; XOR es la transformación aplicada a los bytes. Identificar ambas capas reduce
errores.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 07, página 18. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
