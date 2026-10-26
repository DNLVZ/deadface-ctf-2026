# You Wouldn't Git It

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** OSINT · **Puntos en el catálogo:** 125 · **Estado:** Documentado

Revelar caracteres Unicode invisibles dentro de un comentario relacionado con el reto.
Evidencia: Documentado en la sesión

Herramientas: Navegador y decodificación Unicode con Python


## Procedimiento

1. Seguir las pistas de contenido y repositorio hasta el comentario de b1tfr34k en DoomScroll señalado por la
    investigación.

2. Copiar el contenido textual completo, no solo lo que se ve. Los Unicode Tag Characters pueden codificar
    letras sin mostrarlas como texto normal.

3. Inspeccionar los puntos de código. Para caracteres del intervalo U+E0020 a U+E007E, restar 0xE0000
     produce el carácter ASCII correspondiente.

4. Concatenar los caracteres decodificados en su orden original. El resultado documentado contiene la bandera
    completa con el juego de palabras r00t_b33r.

5. Conservar el comentario original y la salida del decodificador. Capturar solo una imagen del comentario
    puede perder los caracteres invisibles.


## Comandos o lógica reproducible

```text
from pathlib import Path
text = Path("comentario.txt").read_text(encoding="utf-8")
decoded = "".join(chr(ord(ch) - 0xE0000)
                  for ch in text if 0xE0020 <= ord(ch) <= 0xE007E)
print(decoded)


```

## Resultado conservado

```text
deadface{13_h4ck3r5_walk3d_int0_a_bar_each_says_Ill_h4v3_a_r00t_b33r}

```

## Por qué funciona

La diferencia entre representación visual y contenido Unicode permite esconder texto en una publicación
aparentemente normal.


## Aprendizaje para el análisis

Conservar bytes o texto original cuando la hipótesis involucra Unicode; una captura visual no basta.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 38, página 49. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
