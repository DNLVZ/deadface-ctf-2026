# False Telemetry

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 250 · **Estado:** Parcial

Relacionar el destino de red con la periodicidad del mecanismo de falsa telemetría.
Evidencia: Documentado en la sesión

Herramientas: Búsqueda de indicadores y lectura de script en memoria


## Procedimiento

1. Reunir las referencias a telemetry.ps1, la dirección 167.172.132.224 y el puerto 4815 en los resultados de
    memoria.

2. Revisar el bucle o la configuración de espera asociada al envío. La sesión recuperó el valor 30 como
    intervalo requerido por el reto.

3. Distinguir ese intervalo de un timeout, contador de reintentos o número de muestras. La interpretación debe
     provenir del contexto del script.

4. Componer la respuesta IP_puerto_intervalo en ese orden: 167.172.132.224_4815_30.

5. No ejecutar el script del incidente para validar su comportamiento; la lectura estática y la correlación de
    evidencia son suficientes para documentar el hallazgo.


## Resultado conservado

```text
deadface{167.172.132.224_4815_30}

```

## Por qué funciona

La periodicidad puede convertir un destino aislado en un patrón reconocible de comunicación automatizada.


## Aprendizaje para el análisis

Un intervalo útil para detección debe conservar su unidad y la lógica que lo origina.


## Alcance de la reconstrucción

El resumen histórico conserva el valor 30, pero no la línea completa de espera. No se atribuye una unidad sin esa línea o el enunciado
íntegro.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 28, página 39. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
