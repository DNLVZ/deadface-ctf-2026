# Método y estados de evidencia

[Inicio](../README.md)

## Método de trabajo

1. Leer qué entidad pide la consigna y el formato de respuesta.
2. Preservar el original y calcular su SHA-256 antes de trabajar sobre una copia.
3. Identificar el formato por su contenido. Revisar nombres, metadatos, cadenas y cabeceras.
4. Formular una hipótesis y anotar qué observación la confirmaría.
5. Conservar entradas, comandos, resultados y errores. Comprobar el resultado mediante recifrado, estructura, hashes o repetición cuando sea posible.
6. Separar una bandera encontrada de una bandera aceptada en CTFd.

## Cómo leer los estados

| Estado | Significado en la bitácora |
| --- | --- |
| Verificado | Se reprodujo un resultado o se comprobó la bandera en el material conservado; algunas fichas registran aceptación en la conversación. No implica una nueva aceptación en CTFd. |
| Documentado | El resultado y una ruta de resolución aparecen en las sesiones recuperadas; no se repitió toda la cadena durante esa edición. |
| Parcial | Hay resultado histórico, pero faltan entradas, constantes, consultas o fuentes para reproducir íntegramente el método. |
| Candidata | Propuesta sin confirmación suficiente; no se cuenta como solución. |
| Intentado | Consulta, descarga o análisis registrado, sin bandera final recuperada. |
| Sin registro | Solo consta en el catálogo. No demuestra que nunca se intentara. |

## Criterios de publicación

Los estados se transcriben de la edición de la bitácora del 19 de octubre de 2026. Las nuevas pruebas sobre ejemplos pequeños se documentan en [scripts](../scripts/README.md); no elevan automáticamente el estado del reto original.

Cuando falta una consulta SQL o una constante de un binario, la ficha conserva esa limitación. Un fragmento ilustrativo no se presenta como el solucionador original completo.

La investigación tuvo apoyo de herramientas de análisis y asistencia de IA. La organización y parte del código se reconstruyeron después de la competencia para estudiar los resultados.

Fuente: bitácora técnica personal, páginas 2 y 8.
