# Borrowed Script

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 100 · **Estado:** Parcial

Recuperar el usuario y host asociados a la procedencia de un script.
Evidencia: Documentado en la sesión

Herramientas: Resultados de memoria y análisis de comandos


## Procedimiento

1. Examinar los comandos y referencias de transferencia conservados del incidente. Buscar d34th y
    10.77.10.66 dentro del mismo contexto.

2. Identificar la pareja d34th@10.77.10.66. El formato usuario@host expresa una cuenta en un sistema remoto,
     no una dirección de correo convencional.

3. Vincular la pareja con el script al que se refiere el reto. Mantener el contexto para evitar atribuir cualquier
     aparición de la IP al mismo propósito.

4. Entregar la pareja exacta, conservando el símbolo @ y la escritura del alias.

5. En una reproducción completa, conservar también el comando de transferencia íntegro. El resumen histórico
    recuperado solo preserva el indicador y su asociación con el reto.


## Resultado conservado

```text
deadface{d34th@10.77.10.66}

```

## Por qué funciona

Correlacionar cuenta y origen permite reconstruir la procedencia del recurso utilizado durante la intrusión.


## Aprendizaje para el análisis

Un indicador puede estar documentado aunque el comando completo no se haya conservado; explicitar ese
nivel de detalle.


## Alcance de la reconstrucción

Resultado histórico recuperado; no se reconstruye una línea de comando original que no está disponible.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 25, página 36. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
