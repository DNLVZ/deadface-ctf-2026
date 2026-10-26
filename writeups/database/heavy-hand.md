# Heavy Hand

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Database · **Puntos en el catálogo:** 100 · **Estado:** Parcial

Identificar al prescriptor con mayor volumen de dispensación de sustancias Schedule II durante el periodo
indicado.
Evidencia: Documentado en la sesión

Herramientas: MySQL, agregaciones y relaciones de farmacia


## Procedimiento

1. Seleccionar aurora_pharmacy y revisar dispenses, prescriptions, drugs y prescribers.

2. Relacionar cada dispensación con su prescripción, medicamento y prescriptor. Inspeccionar las claves antes
    de escribir las uniones.

3. Filtrar dea_schedule = II y el intervalo desde 2025-10-01 inclusive hasta 2026-01-01 exclusivo. El límite
     superior exclusivo incluye todo el último día aunque haya horas en el campo.

4. Sumar quantity_dispensed por prescriptor. El objetivo es volumen dispensado, no número de recetas ni
    número de medicamentos distintos.

5. Ordenar la suma en sentido descendente y tomar el primer resultado. La sesión registró a Marcus Reyes con
    5,220 unidades y número DEA BR2938471.

6. Entregar el número DEA, que es el identificador solicitado. Conservar la suma como evidencia del criterio de
    selección.


## Comandos o lógica reproducible

```text
USE aurora_pharmacy;
DESCRIBE dispenses;
DESCRIBE prescriptions;
DESCRIBE drugs;
DESCRIBE prescribers;
-- Agregación documentada: SUM(quantity_dispensed)
-- Filtro documentado: dea_schedule = 'II'
-- Periodo: >= '2025-10-01' AND < '2026-01-01'
-- Orden: suma DESC, LIMIT 1


```

## Resultado conservado

```text
deadface{BR2938471}

```

## Por qué funciona

El resultado depende de sumar la medida correcta y evitar duplicaciones introducidas por las relaciones. El
identificador DEA no es la cifra agregada.


## Aprendizaje para el análisis

Explicar unidad, periodo y agrupación junto a cualquier clasificación cuantitativa.


## Alcance de la reconstrucción

El bloque conserva los componentes confirmados; no inventa nombres de claves foráneas ni del campo de fecha.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 33, página 44. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
