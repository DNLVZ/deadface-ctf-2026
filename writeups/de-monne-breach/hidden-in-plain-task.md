# Hidden in Plain Task

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 75 · **Estado:** Documentado

Identificar el nombre de una tarea programada utilizada como persistencia.
Evidencia: Documentado en la sesión

Herramientas: Lectura de memoria, búsqueda de cadenas y PowerShell


## Código histórico disponible

[scan_memory.py](../../scripts/originales/scan_memory.py) · [scan-memory.ps1](../../scripts/originales/scan-memory.ps1) · [Entradas y límites](../../scripts/originales/README.md).

Estos archivos conservan el análisis histórico y no implican una nueva reproducción completa del reto.

## Procedimiento

1. Verificar el hash de memory.7z y extraer memory.raw en un disco con espacio suficiente. El volcado
    descomprimido ocupa 8 GiB.

2. Buscar cadenas ASCII y UTF-16LE relacionadas con Register-ScheduledTask, TaskName, telemetry y
    WindowsCache. Windows conserva numerosas cadenas en UTF-16LE.

3. Revisar el contexto de los resultados, no solo la coincidencia. En la sesión se recuperó un comando
    Register-ScheduledTask con TaskName WindowsTelemetryCheck.

4. Separar el nombre de la tarea de su acción y del archivo ejecutado. Los tres elementos sustentan retos
    distintos de la misma serie.

5. Guardar el contexto extraído en un archivo de texto y registrar la ruta del volcado. Entregar únicamente el
    nombre de la tarea.


## Comandos o lógica reproducible

```text
# Búsqueda sobre el resultado de extracción ya conservado:
Select-String -LiteralPath .\telemetry_hits.txt `
  -Pattern 'Register-ScheduledTask','WindowsTelemetryCheck' `
  -Context 2,2


```

## Resultado conservado

```text
deadface{WindowsTelemetryCheck}

```

## Por qué funciona

La persistencia deja referencias a su creación en buffers y comandos residentes. Un nombre aparentemente
legítimo puede encubrir una acción no autorizada.


## Aprendizaje para el análisis

Buscar tanto ASCII como UTF-16LE y conservar los offsets cuando el extractor los permita.


## Alcance de la reconstrucción

El comando mostrado analiza el archivo de resultados; no ejecuta ni registra la tarea programada.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 22, página 33. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
