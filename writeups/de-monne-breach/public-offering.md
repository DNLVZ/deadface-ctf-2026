# Public Offering

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 75 · **Estado:** Documentado

Identificar el destino externo y el puerto asociados a la salida de información.
Evidencia: Documentado en la sesión

Herramientas: Correlación de tráfico y comandos de memoria


## Procedimiento

1. Revisar connection_hits.txt y el contexto de los comandos recuperados. Buscar la dirección
    167.172.132.224.

2. Identificar el puerto 4815 asociado a esa dirección dentro de la operación relevante.

3. Contrastar origen, destino y sentido del flujo cuando la captura lo permita. No confundir una dirección de
    escucha local con el receptor externo.

4. Expresar la respuesta como IP_puerto, usando un guion bajo como exige el reto.

5. Relacionar esta pareja con False Telemetry, que añade un intervalo. El dato adicional no forma parte de
    Public Offering.


## Comandos o lógica reproducible

```text
Select-String -LiteralPath .\connection_hits.txt `
  -SimpleMatch '167.172.132.224' -Context 2,2


```

## Resultado conservado

```text
deadface{167.172.132.224_4815}

```

## Por qué funciona

Un indicador de red necesita su papel y contexto. El mismo host puede participar en varios servicios; el puerto
delimita el canal observado.


## Aprendizaje para el análisis

Registrar IP, puerto, protocolo y tiempo cuando estén disponibles, sin completar campos ausentes por intuición.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 24, página 35. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
