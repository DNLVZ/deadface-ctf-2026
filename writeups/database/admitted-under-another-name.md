# Admitted Under Another Name

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Database · **Puntos en el catálogo:** 15 · **Estado:** Parcial

Localizar al paciente VIP ingresado con una identidad alternativa.
Evidencia: Documentado en la sesión

Herramientas: Consola MySQL del laboratorio


## Procedimiento

1. Enumerar las bases y tablas accesibles en el entorno del reto. La investigación se centró en los registros
    clínicos, sin modificar datos.

2. Revisar la estructura de la tabla de pacientes e identificar el campo is_vip. Utilizar el filtro is_vip = 1 para
    reducir el conjunto de registros.

3. Comparar nombre, alias y número de historia clínica. La sesión vinculó Gregory Halloran con el alias George
    Harmon.

4. Recuperar el identificador AH-0044719. El reto pedía ese identificador, no ninguno de los dos nombres.

5. Conservar el registro y la consulta que lo seleccionó; el identificador también sirve como referencia para
    investigar los accesos y encuentros posteriores.


## Comandos o lógica reproducible

```text
SHOW DATABASES;
-- Seleccionar la base indicada por el reto.
SHOW TABLES;
-- Revisar el esquema de la tabla antes de consultar.
-- Condición documentada: WHERE is_vip = 1


```

## Resultado conservado

```text
deadface{AH-0044719}

```

## Por qué funciona

El atributo VIP permite localizar al paciente aunque el nombre visible haya cambiado. El identificador clínico
conecta registros de varias tablas.


## Aprendizaje para el análisis

Comprender qué entidad identifica cada campo antes de construir un JOIN.


## Alcance de la reconstrucción

No se recuperó el nombre exacto de la tabla usada en la consulta original; el bloque muestra la fase de inspección y el filtro confirmado.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 29, página 40. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
