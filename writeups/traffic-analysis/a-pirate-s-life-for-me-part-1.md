# A Pirate's Life for Me: Part 1

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Traffic Analysis · **Puntos en el catálogo:** 25 · **Estado:** Documentado

Encontrar fragmentos de una bandera en cabeceras HTTP de un cliente particular.
Evidencia: Documentado en la sesión

Herramientas: Wireshark y pirateslife.pcap


## Procedimiento

1. Verificar pirateslife.7z, extraer pirateslife.pcap y abrir la captura. La sesión conservó un script de
    enumeración de HTTP, hosts y User-Agent.

2. Aplicar http.user_agent contains "Sunstalker". El agente registrado es SunstalkerDFBrower/2.0 (Linux;
    Android 14). Mantener la escritura Brower tal como aparece.

3. Revisar las tramas 19114, 43516 y 56543, asociadas al origen 172.16.14.43.

4. Extraer las cabeceras X-1-Trace-Part, X-2-Mark y X-3-Spot. Su numeración indica el orden de
    concatenación.

5. Unir los tres fragmentos sin añadir separadores. La bandera resultante es X-M4rk5_th3_sp0t_I_gu355.

6. No confundir este resultado con X Marks the Spot, cuyo reto criptográfico usa XOR 0x44 y produce otra
    bandera.


## Comandos o lógica reproducible

```text
# Filtro en Wireshark:
http.user_agent contains "Sunstalker"

# Filtro complementario:
ip.src == 172.16.14.43 && http.request


```

## Resultado conservado

```text
deadface{X-M4rk5_th3_sp0t_I_gu355}

```

## Por qué funciona

Las cabeceras HTTP personalizadas pueden transportar información fuera del cuerpo principal. La identidad
del cliente reduce la búsqueda en una captura extensa.


## Aprendizaje para el análisis

Guardar el nombre exacto de cada cabecera y su trama; las palabras parecidas de dos retos no justifican
mezclar resultados.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 50, página 61. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
