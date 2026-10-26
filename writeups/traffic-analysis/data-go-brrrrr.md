# Data Go Brrrrr

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Traffic Analysis · **Puntos en el catálogo:** 25 · **Estado:** Documentado

Reconstruir datos transportados dentro de cargas ICMP.
Evidencia: Documentado en la sesión

Herramientas: Wireshark, PCAP01.pcap y Base64


## Procedimiento

1. Abrir PCAP01.pcap y aplicar el filtro icmp. Comparar los pings de carga habitual con los paquetes cuyo
    contenido cambia.

2. Examinar los bytes posteriores a la cabecera ICMP. La captura conserva fragmentos como ZGVhZGZh,
    Y2V7aWNt y cF8zeGZp, compatibles con Base64.

3. Seleccionar el sentido de comunicación relevante y evitar contar la misma carga dos veces si existe una
    respuesta echo que la repite.

4. Ordenar los fragmentos según la secuencia del mensaje, concatenarlos y decodificar Base64.

5. Comprobar que el texto empieza por deadface{ y termina con una llave. El resultado histórico es
    icmp_3xfil_wh3n_th3y_least_susp3ct.

6. Guardar los números de trama seleccionados y la cadena concatenada para que otra persona pueda revisar
    el orden.


## Comandos o lógica reproducible

```text
# Filtro Wireshark:
icmp

# Tras copiar los fragmentos exactos en su orden:
import base64
# print(base64.b64decode("".join(fragmentos)).decode())


```

## Resultado conservado

```text
deadface{icmp_3xfil_wh3n_th3y_least_susp3ct}

```

## Por qué funciona

ICMP permite transportar una carga de datos además de información de control. Una secuencia de pings
puede convertirse en un canal encubierto.


## Aprendizaje para el análisis

Analizar tamaño, contenido y periodicidad; no descartar ICMP como tráfico siempre inocuo.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 49, página 60. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
