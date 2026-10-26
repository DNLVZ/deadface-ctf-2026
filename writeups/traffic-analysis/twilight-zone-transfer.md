# Twilight Zone Transfer

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Traffic Analysis · **Puntos en el catálogo:** 50 · **Estado:** Verificado

Identificar una transferencia de zona DNS y leer un registro TXT revelado por la respuesta.
Evidencia: Bandera verificada en PCAP04.pcap

Herramientas: Wireshark y PCAP04.pcap


## Procedimiento

1. Abrir PCAP04.pcap y filtrar dns.qry.type == 252. El tipo 252 corresponde a AXFR, una solicitud de
    transferencia de zona.

2. Examinar la trama 36, que solicita la transferencia, y la respuesta de la trama 37 documentadas en la sesión.

3. Expandir las respuestas DNS y localizar el registro TXT _flag.deadface-cc.net.

4. Leer deadface{dns_zone_transfer} dentro del contenido TXT. La revisión local también detectó esta cadena
     directamente en los bytes de PCAP04.

5. Documentar que se trata de análisis de una captura ya proporcionada; no es necesario enviar nuevas
    solicitudes AXFR a un servidor.


## Comandos o lógica reproducible

```text
# Filtros de visualización:
dns.qry.type == 252
dns && tcp.port == 53


```

## Resultado conservado

```text
deadface{dns_zone_transfer}

```

## Por qué funciona

Una transferencia de zona puede revelar registros que no aparecen en una consulta ordinaria. El TXT
transporta el mensaje del reto.


## Aprendizaje para el análisis

Restringir transferencias de zona a los secundarios autorizados y distinguir el análisis pasivo de una
comprobación activa.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 51, página 62. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
