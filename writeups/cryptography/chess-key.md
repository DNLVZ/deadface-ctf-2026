# Chess Key

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Cryptography · **Puntos en el catálogo:** 200 · **Estado:** Parcial

Derivar una clave a partir de movimientos de ajedrez y utilizarla para descifrar el mensaje.
Evidencia: Documentado en la sesión

Herramientas: OSINT de la partida y descifrado Vigenère


## Procedimiento

1. Seguir la pista Carlsen gave me an idea publicada en GhostTown. La sesión vinculó el reto con Carlsen
    contra Aleksandar Indjic, 13 de enero de 2026, Apertura Inglesa.

2. Recuperar la secuencia de movimientos y tomar las casillas de destino en el orden indicado por el reto. No
    sustituirlas por casillas de origen ni mezclar jugadas blancas y negras sin seguir la consigna.

3. Aplicar el mapeo del tablero que proporciona el reto. Entre los pares recuperados están c4=L, g3=S, g2=G,
    f3=F y h4=I; la clave comienza LSGFIWRXFEAV.

4. Descifrar con Vigenère sobre letras. Conservar la caja original de cada letra y no consumir posiciones de
    clave cuando aparezcan números, guiones bajos u otros separadores.

5. Recifrar el resultado con la misma clave. La sesión registró coincidencia exacta con el cifrado de entrada y
    obtuvo cH3ckM8_ch3s5_cryPt0.


## Comandos o lógica reproducible

```text
def vigenere(text, key, decrypt=True):
    result, j = [], 0
    for ch in text:
        if ch.isascii() and ch.isalpha():
            base = ord("A" if ch.isupper() else "a")
            shift = ord(key[j % len(key)].upper()) - 65
            if decrypt: shift = -shift
            result.append(chr((ord(ch)-base+shift) % 26 + base))
            j += 1
        else:
            result.append(ch)
    return "".join(result)


```

## Resultado conservado

```text
deadface{cH3ckM8_ch3s5_cryPt0}

```

## Por qué funciona

Vigenère requiere reproducir tanto la clave como la política de avance. La conservación de números y
separadores forma parte del algoritmo concreto del reto.


## Aprendizaje para el análisis

No reconstruir una clave completa a partir de un prefijo recordado. Guardar el tablero, la partida y el cifrado
como un conjunto de evidencia.


## Alcance de la reconstrucción

La recuperación histórica no contiene el tablero y la clave completos; se presenta el método documentado y un descifrador general, sin
inventar esos datos.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 11, página 22. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
