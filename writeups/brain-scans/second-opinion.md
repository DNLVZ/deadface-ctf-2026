# Second Opinion

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Brain Scans · **Puntos en el catálogo:** 50 · **Estado:** Documentado

Mostrar información no redactada a través de la salida de diagnóstico HDMI del dispositivo simulado.
Evidencia: Documentado en la sesión

Herramientas: Interfaz del laboratorio y manual CS-9000


## Procedimiento

1. Leer la sección 3.1 HDMI del manual. Describe una salida externa que refleja la consola y añade un OSD de
     diagnóstico para ingeniería.

2. En el toolkit del laboratorio, conectar HDMI Cable a HDMI Port y seleccionar External Display.

3. Elevar el nivel de diagnóstico con el control de flecha hasta 3/3. El manual indica que el nivel 3 corresponde
     a raw session dump y desactiva la redacción de campos.

4. Examinar la salida RAW SESSION DUMP de la pantalla externa. La sesión recuperó
    hdm1_l34ks_th3_wh0l3_p4t13nt.

5. Relacionar el comportamiento observado con la advertencia del manual: ese nivel no debe activarse con un
    estudio de paciente cargado.


## Resultado conservado

```text
deadface{hdm1_l34ks_th3_wh0l3_p4t13nt}

```

## Por qué funciona

Una interfaz de mantenimiento puede exponer más información que la pantalla de uso normal. La protección
visual debe contemplar todas las salidas.


## Aprendizaje para el análisis

Incluir puertos físicos y modos de diagnóstico en el análisis de exposición de información.


## Alcance de la reconstrucción

Procedimiento referido exclusivamente al simulador del CTF; el manual y los pacientes pertenecen al escenario ficticio.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 42, página 53. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
