# The Typo That Bit

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 75 · **Estado:** Documentado

Identificar el nombre mal escrito que desencadenó la interacción problemática.
Evidencia: Documentado en la sesión

Herramientas: Wireshark y consultas de nombres


## Procedimiento

1. Regresar al tráfico LLMNR y NetBIOS del incidente. Leer las consultas antes de observar las respuestas.

2. Localizar el nombre dmf-field-01 en la secuencia relevante. Compararlo con los nombres de recursos
     legítimos del contexto del reto.

3. Seguir temporalmente la consulta hacia la respuesta del host sospechoso y el intercambio de autenticación
    posterior.

4. Registrar el nombre consultado tal como aparece, con guiones. La pregunta se refiere al nombre erróneo, no
    a la IP que respondió ni al nombre de la estación.

5. Usar dmf-field-01 como contenido de la bandera y conservar la relación entre consulta y respuesta como
    evidencia.


## Resultado conservado

```text
deadface{dmf-field-01}

```

## Por qué funciona

Un error de escritura puede desviar la resolución hacia mecanismos locales menos controlados. El orden de los
paquetes explica la cadena causal.


## Aprendizaje para el análisis

Relacionar el desencadenante con el efecto observado; dos eventos cercanos no bastan sin un vínculo de
protocolo.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 21, página 32. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
