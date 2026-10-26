# The Workstation in the Middle

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 40 · **Estado:** Verificado

Recuperar el nombre de la estación afectada a partir de los mensajes de red.
Evidencia: Documentado en la sesión

Herramientas: Wireshark y demonne.pcap


## Procedimiento

1. Trabajar sobre la misma captura del incidente De Monne. Filtrar tráfico de autenticación NTLM y SMB para
     reducir el ruido.

2. Expandir los campos de NTLMSSP y las negociaciones de SMB. Buscar el nombre de estación enviado
    durante la autenticación.

3. Localizar DMF-WS11-042. Comparar las tramas donde aparece para vincularlo con la conversación
     implicada en el incidente.

4. Distinguir nombre de estación, dominio y usuario: pueden aparecer juntos en un mismo mensaje, pero
     responden a preguntas diferentes.

5. Conservar la grafía exacta en la bandera. La sesión confirmó este dato desde el PCAP, no desde el volcado
    de memoria.


## Comandos o lógica reproducible

```text
# Filtro orientativo de visualización:
ntlmssp || smb || smb2


```

## Resultado conservado

```text
deadface{DMF-WS11-042}

```

## Por qué funciona

La autenticación puede transmitir identificadores de la máquina que ayudan a reconstruir el contexto del
acceso.


## Aprendizaje para el análisis

Anotar la fuente de cada identificador y evitar presentar una observación de red como si fuera un hallazgo de
memoria.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 20, página 31. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
