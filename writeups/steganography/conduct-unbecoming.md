# Conduct Unbecoming

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Steganography · **Puntos en el catálogo:** 75 · **Estado:** Parcial

Leer una marca de puntos amarillos tenue en un documento fotografiado.
Evidencia: Documentado en la sesión

Herramientas: Inspección de imagen, canales de color y decodificación binaria


## Procedimiento

1. Usar la imagen original Doc_20261017_0915.jpg. Evitar una copia recomprimida: pequeños puntos de color
    pueden deteriorarse durante una conversión.

2. Examinar la zona inferior derecha a gran aumento. La sesión localizó una cuadrícula de puntos amarillos
    apenas visibles sobre el fondo claro.

3. Aumentar el contraste entre amarillo y blanco mediante inspección de canales o una transformación de color.
    Guardar la imagen procesada como copia, junto con el original.

4. Reconocer las posiciones regulares de la cuadrícula. Registrar presencia como 1 y ausencia como 0 según
    la orientación de lectura de la marca.

5. Agrupar las posiciones en octetos y convertir de binario a ASCII. El identificador recuperado es
    NVU-PRINT-17.

6. Revisar que la lectura produce una cadena completa y consistente. Invertir el orden de bits o leer por
    columnas en vez de filas puede producir caracteres sin sentido.


## Comandos o lógica reproducible

```text
# Conversión de octetos ya transcritos de la cuadrícula.
def octetos_a_texto(octetos):
    assert all(len(x) == 8 and set(x) <= {"0", "1"} for x in octetos)
    return "".join(chr(int(x, 2)) for x in octetos)


```

## Resultado conservado

```text
deadface{NVU-PRINT-17}

```

## Por qué funciona

La marca codifica información mediante diferencias de color, no mediante texto visible convencional. El
tratamiento de imagen facilita leer un patrón que ya existe.


## Aprendizaje para el análisis

Preservar el original y explicar cualquier realce aplicado. Una transcripción binaria debe acompañarse de su
cuadrícula para ser auditable.


## Alcance de la reconstrucción

Se recuperaron la técnica y el identificador; no la transcripción completa de los puntos. El código es una función de conversión, no una
extracción automática de coordenadas.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 15, página 26. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
