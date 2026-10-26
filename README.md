<p align="center"><img src="assets/banner.svg" alt="DEADFACE CTF 2026 — bitácora técnica de Jesús Daniel" width="100%"></p>

# DEADFACE CTF 2026 · Mi primer CTF

Soy **Jesús Daniel Vásquez Bonilla**, estudiante de Seguridad Informática en el ITLA. Participé individualmente con el alias **jesusd.vb**. Este repositorio reúne mis procedimientos, resultados y aprendizajes de **Operation Kingmaker**, con especial interés en análisis de incidentes, tráfico de red y evidencia digital.

Mi objetivo al participar fue aprender. Aquí documento tanto los hallazgos que pude comprobar como los casos donde todavía falta evidencia para reproducir todo el recorrido.

**[Leer la bitácora en PDF](docs/bitacora-tecnica.pdf)** · **[Explorar los writeups](writeups/README.md)** · **[Ver el catálogo](catalogo/README.md)** · **[Método de trabajo](docs/metodologia.md)** · **[Ejemplos ejecutables](scripts/README.md)**

## Qué encontrarás

| Contenido | Alcance |
| --- | --- |
| **57 fichas técnicas** | 13 categorías con resultados recuperados |
| **93 retos catalogados** | 18 categorías, puntos y estado de evidencia |
| **14 fichas verificadas** | Comprobaciones o aceptación registradas en la bitácora |
| **23 fichas documentadas** | Resultado y recorrido conservados, sin repetir toda la cadena |
| **20 fichas parciales** | Resultado histórico con entradas o pasos pendientes |

Las 57 fichas **no equivalen a 57 retos aceptados oficialmente**. La clasificación refleja la evidencia de la bitácora, editada el 19 de octubre de 2026. Esta publicación no implica una nueva validación de todos los casos.

## Por dónde empezar

| Caso | Qué permite estudiar |
| --- | --- |
| [Name to a Face](writeups/de-monne-breach/name-to-a-face.md) | Atribución de usuario y estación desde NTLMSSP |
| [Hidden in Plain Task](writeups/de-monne-breach/hidden-in-plain-task.md) | Rastros de persistencia en memoria y tareas programadas |
| [Twilight Zone Transfer](writeups/traffic-analysis/twilight-zone-transfer.md) | Identificación pasiva de AXFR en una captura DNS |
| [Second Shift](writeups/cryptography/second-shift.md) | Recuperación de texto por reutilización del flujo CTR |
| [Info Leaks](writeups/aurora-patient-zero/info-leaks.md) | Inspección de configuración y Base64 en un paquete iOS |
| [Art Heist: The Forgery](writeups/forensics/art-heist-the-forgery.md) | Comparación de imágenes y lectura de metadatos XMP |

## Áreas de práctica

**Análisis de tráfico y protocolos:** NTLMSSP, SMB, LLMNR, DNS, HTTP e ICMP; reconstrucción documentada de TLS, SIP y SRTP.

**Informática forense:** metadatos de imágenes, cadenas de memoria, artefactos de navegador y correlación de indicadores.

**Criptografía y análisis estático:** ROT13, XOR, reutilización de flujo, contenedores IPA/APK, SQLite y lectura de binarios.

Cada ficha desarrolla el objetivo, las herramientas, el procedimiento, el resultado conservado y el aprendizaje. Los fragmentos incompletos se identifican como tales.

## Documentación

- [Cómo interpreto la evidencia y los estados](docs/metodologia.md)
- [Herramientas y su uso documentado](docs/herramientas.md)
- [Participación y reflexión](docs/participacion.md)
- [Procedencia, límites y materiales](docs/procedencia.md)
- [Intentos y candidatos pendientes](docs/pendientes.md)
- [Inventario de hashes de referencia](evidencias/README.md)
- [Créditos y derechos](CREDITOS.md)

## Reproducir los ejemplos locales

Se requiere **Python 3.10 o posterior**. Los dos ejemplos autocontenidos usan la biblioteca estándar y no necesitan conexión de red:

```bash
python scripts/hail_caesar.py
python scripts/x_marks_the_spot.py
```

Son reconstrucciones didácticas preparadas para esta publicación. Los originales de los retos, volcados, ejecutables y respaldos privados no se distribuyen en el repositorio.

## Lo que me dejó esta experiencia

Una bandera aislada no conserva el aprendizaje. Necesito guardar las entradas, los comandos, los resultados y la razón por la que considero válido un hallazgo. También aprendí a comenzar con lo básico: leer metadatos, revisar una cabecera o distinguir el usuario del nombre de una estación puede ser más útil que cambiar de herramienta.

## English overview

Personal learning portfolio from my first DEADFACE CTF, entered solo as **jesusd.vb**. It contains **57 technical writeups** and a **93-challenge catalog**, with explicit evidence states and reproducibility limits. Documentation is in Spanish. Counts describe recovered records, not an official accepted-solve total.

---

**Autor:** [Jesús Daniel Vásquez Bonilla · DNLVZ](https://github.com/DNLVZ)  
Documentación personal de aprendizaje. DEADFACE CTF y los materiales de los retos pertenecen a sus respectivos autores.
