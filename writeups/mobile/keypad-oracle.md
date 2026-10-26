# Keypad Oracle

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Mobile · **Puntos en el catálogo:** 200 · **Estado:** Verificado

Reproducir una transformación del teclado y encontrar el PIN que produce una bandera válida.
Evidencia: Reproducido con el script original

Herramientas: Python, JSON, análisis de binario y enumeración local


## Procedimiento

1. Extraer Keypad-Oracle.app.zip y leer KeypadConfig.json. Contiene un bloque de bytes hexadecimales para
    cada dígito de 0 a 9.

2. Analizar la función de validación para recuperar binarySalt y las operaciones de XOR y rotación. El script
    solve_keypad.py conserva esa lógica.

3. Enumerar permutaciones de cuatro dígitos sin repetición: 10 × 9 × 8 × 7 = 5,040 candidatos. La búsqueda se
    realiza sobre archivos locales, no contra un servicio.

4. Para cada posición, combinar el bloque del dígito con constantes dependientes de posición e índice; rotar el
    byte; acumular mediante XOR.

5. Aplicar al resultado el salt recuperado y buscar una salida coherente con el marcador deadface. El PIN 3719
    y la dirección de rotación positiva producen la bandera.

6. Ejecutar de nuevo únicamente ese candidato y guardar la salida. En la revisión de esta bitácora, el script
     original reprodujo deadface{your-pin-is-valid}.


## Solucionador original disponible

[Script original](../../scripts/originales/solve_keypad.py) · [Configuración de entrada](../../scripts/originales/keypad/Keypad-Oracle.app/KeypadConfig.json) · [Instrucciones y procedencia](../../scripts/originales/README.md)

La repetición local durante la publicación produjo `(3, 7, 1, 9) 1 b'deadface{your-pin-is-valid}'`. Esta comprobación no envió una respuesta nueva a CTFd.

## Comandos o lógica reproducible

```text
def rotate8(x, n):
    n %= 8
    return ((x << n) | (x >> (8 - n))) & 255

# Núcleo documentado, dentro de los bucles de posición e índice:
# x = block[i] ^ ((pos+1)*33) ^ ((digit*19)&255) ^ ((i*7)&255)
# out[i] ^= rotate8(x, (digit+pos+i)%8) ^ ((i+digit+pos*11)&255)
# Al terminar: XOR con binarySalt.
# Script íntegro conservado: solve_keypad.py


```

## Resultado conservado

```text
deadface{your-pin-is-valid}

```

## Por qué funciona

Al disponer de la validación local y un espacio pequeño, puede emularse cada candidato. El reconocimiento del
formato de bandera filtra las salidas.


## Aprendizaje para el análisis

Preservar el solucionador y la configuración juntos; uno sin el otro no permite repetir la prueba.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 57, página 68. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
