# Return to Sender

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Traffic Analysis · **Puntos en el catálogo:** 80 · **Estado:** Documentado

Recomponer una exfiltración HTTP distribuida entre solicitudes y cabeceras.
Evidencia: Documentado en la sesión

Herramientas: Wireshark, PCAP03.pcap y Base64


## Procedimiento

1. Abrir PCAP03.pcap y filtrar las solicitudes POST del origen 10.20.30.40 hacia 45.66.77.88.

2. Identificar el Host telemetry.deadface-cc.net y separar estas solicitudes del tráfico de navegación de relleno.

3. Extraer los fragmentos numerados seq=1 a seq=5 y ordenarlos por ese campo. El orden lógico no debe
    depender únicamente de cómo se muestran las tramas.

4. Decodificar los fragmentos Base64. Revisar también la cabecera X-Session-Id, que contiene el componente
    business del texto.

5. Combinar cuerpo y cabecera de acuerdo con la secuencia observada para formar
    http_exfil_sneaky_business.

6. Conservar una tabla de secuencia, trama, origen del fragmento y salida decodificada.


## Comandos o lógica reproducible

```text
# Filtros de visualización:
http.request.method == "POST" && ip.src == 10.20.30.40
http.host == "telemetry.deadface-cc.net"


```

## Resultado conservado

```text
deadface{http_exfil_sneaky_business}

```

## Por qué funciona

Los datos pueden dividirse entre campos que normalmente parecen metadatos de sesión y el cuerpo de
solicitudes legítimas.


## Aprendizaje para el análisis

Inspeccionar cabeceras además del payload y mantener la secuencia lógica de los fragmentos.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 52, página 63. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
