# Cereal Killer 03

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Reverse Engineering · **Puntos en el catálogo:** 500 · **Estado:** Parcial

Reconstruir una ruta de descifrado protegida por mecanismos que complican el seguimiento convencional.
Evidencia: Documentado en la sesión

Herramientas: Desensamblado PE, MD5 y análisis de manejo de excepciones


## Procedimiento

1. Inspeccionar cereal03.exe y conservar el desensamblado de las funciones relevantes. La sesión utilizó
     análisis de la lógica del programa.

2. Identificar la comprobación de contraseña basada en MD5. El valor recuperado como entrada fue letmein.

3. Examinar el papel de hardware breakpoints y SEH, el manejo estructurado de excepciones de Windows. Una
    excepción puede transferir el control a una rutina que no aparece en el recorrido lineal esperado.

4. Seguir la rutina de descifrado reconstruida en lugar de asumir que el programa termina en la primera
    excepción.

5. Relacionar la salida con el cereal Krampuffs y recuperar Liz4rds_L0ve_Krampuffs_for_some_odd_reason...
    con sus tres puntos finales.

6. Registrar los saltos y handlers que justifican el flujo. La contraseña por sí sola no explica cómo se obtuvo la
    bandera.


## Resultado conservado

```text
deadface{Liz4rds_L0ve_Krampuffs_for_some_odd_reason...}

```

## Por qué funciona

El flujo de control puede incluir rutas activadas por excepciones. Un desensamblado lineal o una ejecución
superficial pueden omitir la rutina decisiva.


## Aprendizaje para el análisis

Distinguir código de validación, mecanismos de análisis evasivo y rutina que produce la salida.


## Alcance de la reconstrucción

La sesión registra el resultado, pero no se recuperaron todos los offsets ni constantes. Este capítulo conserva el recorrido documentado
sin fabricar un script completo.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 47, página 58. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
