# Cache Money

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 150 · **Estado:** Documentado

Recuperar la ruta del script asociado a la tarea de persistencia.
Evidencia: Documentado en la sesión

Herramientas: Análisis de cadenas de memoria


## Procedimiento

1. Usar los mismos hallazgos de memoria que identificaron WindowsTelemetryCheck. Examinar la acción que
    ejecuta PowerShell.

2. Localizar la ruta C:\ProgramData\WindowsCache\telemetry.ps1 en el contexto del comando y comprobar que
     corresponde al script, no a un directorio de salida.

3. Conservar la unidad C:, la estructura del directorio y la extensión .ps1. No sustituir las barras invertidas por
    barras normales.

4. Distinguir evidencia de una referencia a archivo y evidencia de su contenido: una cadena en memoria
     demuestra que la ruta aparece, pero no recupera automáticamente el archivo completo.

5. Formar la bandera con la ruta exacta. En una cadena Python las barras pueden requerir escape; al pegar la
    bandera en CTFd debe aparecer una sola barra por separador.


## Comandos o lógica reproducible

```text
# Buscar el indicador sin modificar la evidencia:
Select-String -LiteralPath .\telemetry_hits.txt `
  -SimpleMatch 'C:\ProgramData\WindowsCache\telemetry.ps1'


```

## Resultado conservado

```text
deadface{C:\ProgramData\WindowsCache\telemetry.ps1}

```

## Por qué funciona

El nombre del directorio imita una ubicación de caché del sistema. La relación con la tarea programada lo sitúa
en la cadena del incidente.


## Aprendizaje para el análisis

La apariencia de una ruta no prueba legitimidad. Correlacionar ubicación, ejecutor y mecanismo de inicio.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 27, página 38. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
