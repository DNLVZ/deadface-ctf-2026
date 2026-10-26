# Uninvited Guest

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 25 · **Estado:** Documentado

Identificar el dispositivo intruso mediante tráfico de resolución de nombres local.
Evidencia: Documentado en la sesión

Herramientas: Wireshark o análisis de demonne.pcap


## Procedimiento

1. Abrir demonne.pcap y revisar las conversaciones y extremos. El objetivo es identificar un equipo concreto, no
    enumerar indiscriminadamente la red.

2. Aplicar el filtro llmnr || nbns. Estos protocolos resuelven nombres en segmentos locales y pueden exponer
    respuestas de un host que suplanta a otro.

3. Inspeccionar los paquetes 1462, 1468 y 2279 citados en la sesión. Comparar nombre consultado, emisor,
     dirección de respuesta y secuencia temporal.

4. Relacionar las respuestas con 10.77.10.66. No basta con encontrar una IP aislada: su función debe coincidir
    con el comportamiento descrito por el reto.

5. Guardar el filtro y los números de trama junto a la IP. La bandera solicitada contiene solo la dirección del
    invitado no autorizado.


## Comandos o lógica reproducible

```text
# Filtro de visualización en Wireshark:
llmnr || nbns

# Para revisar exclusivamente ese equipo:
ip.addr == 10.77.10.66


```

## Resultado conservado

```text
deadface{10.77.10.66}

```

## Por qué funciona

Las consultas y respuestas permiten reconstruir quién intervino en la resolución. La dirección se atribuye por el
intercambio, no por una etiqueta arbitraria.


## Aprendizaje para el análisis

Correlacionar resolución de nombres y autenticación; limitar LLMNR y NetBIOS cuando no sean necesarios.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 19, página 30. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
