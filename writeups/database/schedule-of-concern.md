# Schedule of Concern

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Database · **Puntos en el catálogo:** 20 · **Estado:** Parcial

Conservar el resultado numérico registrado y delimitar lo que falta para reproducir su cálculo.
Evidencia: Documentado en la sesión

Herramientas: Consola SQL del laboratorio


## Procedimiento

1. La respuesta histórica recuperada para este reto fue el valor 9. Se conserva separada de The Attending, que
     quedó pendiente en ese momento.

2. Antes de repetir el cálculo, recuperar el enunciado íntegro y determinar la entidad que se cuenta y la ventana
    temporal aplicable.

3. Inspeccionar las claves de las tablas relacionadas. Un JOIN uno a muchos puede multiplicar filas y alterar el
     conteo.

4. Comparar COUNT(*) con un conteo de la entidad única cuando corresponda al enunciado. No añadir
    DISTINCT sin entender por qué existen duplicados.

5. Guardar consulta, criterios y filas de respaldo. La cifra histórica no sustituye esa evidencia y no permite
    reconstruir por sí sola el cálculo original.


## Resultado conservado

```text
deadface{9}

```

## Por qué funciona

Un resultado SQL es reproducible solo cuando se conocen filtros, relaciones y unidad de conteo.


## Aprendizaje para el análisis

Guardar la consulta completa inmediatamente después de obtener una bandera numérica.


## Alcance de la reconstrucción

Resultado recuperado; procedimiento histórico incompleto. No se inventan tablas ni condiciones para fabricar una consulta que
produzca 9.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 30, página 41. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
