# The Original Reading

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Database · **Puntos en el catálogo:** 70 · **Estado:** Documentado

Recuperar el valor original de un resultado clínico que fue sobrescrito.
Evidencia: Documentado en la sesión

Herramientas: MySQL y tabla de auditoría data_changes


## Procedimiento

1. Seleccionar aurora_trials. El reto indica que existe un registro de cambios separado de los valores actuales
    del estudio.

2. Consultar data_changes filtrando field_name = primary_efficacy_delta. Este campo corresponde al resultado
    primario de eficacia que interesa investigar.

3. Leer old_value y new_value por separado. La entrada relevante conserva old_value = 2.3 y new_value = 6.0.

4. Registrar quién y cuándo realizó el cambio: usuario mreyes, 2025-12-06 23:14:00, según la sesión
    recuperada.

5. Entregar 2.3 exactamente. No redondearlo, cambiar el punto por coma ni devolver el valor alterado 6.0.


## Comandos o lógica reproducible

```text
USE aurora_trials;
SELECT *
FROM data_changes
WHERE field_name = 'primary_efficacy_delta'\G


```

## Resultado conservado

```text
deadface{2.3}

```

## Por qué funciona

La tabla principal muestra el estado actual; el historial conserva la transición. old_value responde a la pregunta
por el dato anterior.


## Aprendizaje para el análisis

En investigaciones de integridad, preservar el rastro de auditoría y distinguir valor actual, previo y autor de la
modificación.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 32, página 43. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
