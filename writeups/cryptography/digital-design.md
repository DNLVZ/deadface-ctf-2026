# Digital Design

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Cryptography · **Puntos en el catálogo:** 100 · **Estado:** Parcial

Interpretar una secuencia de operaciones lógicas camuflada como un mensaje de cuatro letras.
Evidencia: Documentado en la sesión

Herramientas: Lógica booleana y conversión binario a A1Z26


## Procedimiento

1. Relacionar la pista de lilith, Four letters. Still too many for you?, con las letras A, O, N y X del material del
    reto.

2. Asignar A a AND, O a OR, N a NOT y X a XOR. AND solo produce 1 cuando ambas entradas son 1; OR
    cuando alguna es 1; XOR cuando difieren; NOT invierte un único bit.

3. Recorrer los bits de izquierda a derecha. NOT consume un bit; AND, OR y XOR consumen dos. Avanzar el
    índice según la operación, no según una longitud fija.

4. Agrupar las salidas respetando los bloques originales. Convertir cada bloque binario a un entero y después a
    una letra mediante A1Z26: 1=A, 2=B y así sucesivamente.

5. El resultado documentado es BINARYLOGIC. Comprobar que todas las entradas se consumen como indican
     los bloques y que cada valor corresponde a una letra válida.


## Comandos o lógica reproducible

```text
def puerta(op, a, b=None):
    if op == "N": return 1 - a
    if op == "A": return a & b
    if op == "O": return a | b
    if op == "X": return a ^ b
    raise ValueError("Operación no reconocida")

def a1z26(bits):
    value = int(bits, 2)
    assert 1 <= value <= 26
    return chr(64 + value)


```

## Resultado conservado

```text
deadface{BINARYLOGIC}

```

## Por qué funciona

El reto combina interpretación de pistas con una máquina de lectura de bits. Un error de consumo desplaza
todas las operaciones posteriores.


## Aprendizaje para el análisis

Documentar índices de entrada y salida ayuda a detectar dónde se desalineó una decodificación.


## Alcance de la reconstrucción

La secuencia completa de operaciones no está recuperada en esta bitácora; el código muestra las funciones empleadas para
reconstruir el método.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 10, página 21. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
