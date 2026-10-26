# Prying Eyes

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Database · **Puntos en el catálogo:** 55 · **Estado:** Parcial

Identificar la cuenta que consultó repetidamente la historia del paciente VIP.
Evidencia: Documentado en la sesión

Herramientas: Consola SQL, access_log y users


## Procedimiento

1. Reutilizar el identificador AH-0044719 para delimitar las entradas de acceso a la historia clínica.

2. Inspeccionar access_log y users. Identificar las columnas que relacionan cada entrada de auditoría con la
     cuenta del usuario.

3. Filtrar los accesos del paciente y agrupar por usuario. Unir con users para traducir el identificador interno al
     nombre de cuenta.

4. Ordenar los conteos de mayor a menor. La sesión registró 47 accesos asociados a rborden.

5. Comprobar que se cuentan eventos del paciente objetivo, no todos los accesos del usuario. Entregar el
    nombre de cuenta y no su nombre personal.


## Comandos o lógica reproducible

```text
-- Inspección documentada de las tablas implicadas:
DESCRIBE access_log;
DESCRIBE users;
-- La consulta final requiere las claves exactas de ese esquema.
-- Filtrar el MRN, unir con users, agrupar por cuenta y contar eventos.


```

## Resultado conservado

```text
deadface{rborden}

```

## Por qué funciona

La agregación transforma un conjunto de eventos en un patrón por usuario. La unión permite atribuirlo a una
cuenta legible.


## Aprendizaje para el análisis

Un volumen alto es una señal para investigar, no prueba aislada de abuso; en el reto se interpreta dentro del
escenario proporcionado.


## Alcance de la reconstrucción

Se recuperaron las tablas, el identificador, la cuenta y el conteo; no los nombres de todas las columnas del JOIN.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 31, página 42. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
