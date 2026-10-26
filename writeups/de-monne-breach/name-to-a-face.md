# Name to a Face

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 10 · **Estado:** Verificado

Identificar la cuenta que aparece en el intercambio de autenticación investigado.
Evidencia: Usuario y estación reproducidos desde la trama 1489 del PCAP

Herramientas: Wireshark y análisis de NTLMSSP en demonne.pcap


## Procedimiento

1. Abrir demonne.pcap y aplicar el filtro ntlmssp.messagetype == 3. El mensaje Authenticate de NTLMSSP
    contiene la identidad que el cliente utiliza para autenticarse.

2. Ir a la trama 1489. Expandir NTLMSSP Authenticate y leer el campo de nombre de usuario.

3. El valor conservado es nkessler. En el mismo mensaje aparece la estación DMF-WS11-042, útil para
     correlacionar el siguiente reto.

4. Revisar mensajes posteriores para comprobar la repetición de la pareja usuario y estación. La revisión local
    reprodujo esos campos en varias tramas.

5. Formar la bandera con el usuario, no con el dominio ni con la estación. La aceptación en CTFd no se volvió a
    consultar durante la preparación de la bitácora.


## Comandos o lógica reproducible

```text
# Filtro de visualización en Wireshark:
ntlmssp.messagetype == 3

# Evidencia reproducida:
# Trama 1489 | User name: nkessler | Workstation: DMF-WS11-042


```

## Resultado conservado

```text
deadface{nkessler}

```

## Por qué funciona

La estructura del protocolo permite atribuir una autenticación a una cuenta y un equipo. La corroboración de
varios mensajes reduce el riesgo de leer un campo equivocado.


## Aprendizaje para el análisis

Distinguir identificación de una cuenta, prueba de compromiso y aceptación de la bandera: cada afirmación
requiere su propia evidencia.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 18, página 29. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
