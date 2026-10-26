# DECODE-DLE

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Cryptography · **Puntos en el catálogo:** 25 · **Estado:** Parcial

Resolver un código de tres dígitos aplicando simultáneamente las pistas de presencia y posición.
Evidencia: Documentado en la sesión

Herramientas: Razonamiento lógico y enumeración local en Python


## Procedimiento

1. Transcribir cada intento de la imagen con sus indicaciones. Separar tres conceptos: un dígito ausente, uno
     presente en lugar incorrecto y uno presente en la posición correcta.

2. Descartar los valores que las pistas excluyen. En la resolución registrada se eliminaron 2, 5, 0, 3 y 8.

3. Cruzar las restricciones de los dígitos restantes en vez de resolver cada fila de forma independiente. Una
    ubicación aceptable en una fila puede contradecir otra.

4. El resultado documentado fue 716. La sesión indicó que solo una de las mil cadenas de tres cifras satisfacía
     todas las condiciones.

5. Para reproducir la comprobación exhaustiva, representar cada pista como una función y evaluar los
    candidatos 000 a 999. Mantener ceros iniciales como texto.


## Comandos o lógica reproducible

```text
# Esqueleto de verificación: completar con las pistas originales.
def candidatos():
    return (f"{n:03d}" for n in range(1000))

def coincidencias_exactas(intento, candidato):
    return sum(a == b for a, b in zip(intento, candidato))


```

## Resultado conservado

```text
deadface{716}

```

## Por qué funciona

El espacio de búsqueda es pequeño y permite demostrar unicidad localmente. La enumeración sustituye
suposiciones por una comprobación sistemática.


## Aprendizaje para el análisis

Guardar la imagen de las pistas junto al resultado; sin esa tabla no es posible auditar la unicidad.


## Alcance de la reconstrucción

Se recuperaron el resultado y los descartes, pero no la tabla completa de pistas. El fragmento es una plantilla didáctica, no el
solucionador histórico íntegro.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 06, página 17. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
