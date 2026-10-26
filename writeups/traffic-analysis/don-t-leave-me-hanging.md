# Don't Leave Me Hanging

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Traffic Analysis · **Puntos en el catálogo:** 500 · **Estado:** Documentado

Reconstruir una cadena de descifrado de telefonía y convertir tonos en un mensaje.
Evidencia: Documentado en la sesión

Herramientas: PCAP, archivo de diagnóstico PBX, TLS/SRTP y análisis DTMF


## Procedimiento

1. Abrir DontLeaveMeHanging.pcap e identificar la transferencia FTP del archivo pbx-diag-20261008.tar.gz.
    Exportar el objeto o reconstruir el flujo que contiene sus bytes.

2. Extraer el paquete de diagnóstico y localizar tls-keys.log. Es un registro de secretos de sesión que permite
    descifrar el tráfico TLS correspondiente; no equivale a recuperar la clave privada del servidor.

3. Descifrar las conversaciones TLS del puerto 5061 y recuperar la señalización SIP. El script decrypt_calls.ps1
    conserva una reconstrucción con HKDF y AES-GCM para los secretos disponibles.

4. En el SDP de las llamadas, recuperar el material de claves SRTP. La sesión guardó srtp_keys.txt con las
    claves encontradas.

5. Verificar la autenticación de los paquetes SRTP, derivar claves y salt y descifrar la carga de audio.
    decode_srtp.ps1 conserva esta fase y escribe flujos .ulaw.

6. Analizar los tonos DTMF con scan_tones.ps1. Cada tono corresponde a una pareja de frecuencias de fila y
    columna; agrupar los eventos sin repetir una tecla por cada ventana de audio.

7. Interpretar la secuencia resultante como los códigos ASCII usados por el reto. El resultado documentado fue
     Pr355_0n3_f0r_D34df4c3.

8. Preservar los archivos intermedios: diagnóstico, secretos, SIP descifrado, claves SRTP y audio. Permiten
     localizar en qué fase aparece un error.


## Scripts originales disponibles

Se publican [analyze_pcap.ps1](../../scripts/originales/analyze_pcap.ps1), [decrypt_calls.ps1](../../scripts/originales/decrypt_calls.ps1), [decode_srtp.ps1](../../scripts/originales/decode_srtp.ps1) y [scan_tones.ps1](../../scripts/originales/scan_tones.ps1), junto con [sus dependencias y límites](../../scripts/originales/README.md). No se ha repetido la cadena completa en esta publicación.

## Comandos o lógica reproducible

```text
# Scripts completos conservados, en orden de análisis:
analyze_pcap.ps1
decrypt_calls.ps1
decode_srtp.ps1
scan_tones.ps1


```

## Resultado conservado

```text
deadface{Pr355_0n3_f0r_D34df4c3}

```

## Por qué funciona

Cada capa proporciona el material necesario para la siguiente: FTP revela diagnósticos, los secretos revelan
SIP, SIP revela SRTP y el audio contiene la codificación final.


## Aprendizaje para el análisis

Comprobar autenticación y orden de paquetes. La existencia de audio reconocible por sí sola no verifica toda la
cadena criptográfica.


## Alcance de la reconstrucción

Los scripts y numerosos intermedios están respaldados. La secuencia final de tonos no se transcribe íntegra en el historial recuperado,
por lo que la bandera se clasifica como documentada y no como una nueva reproducción completa.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 53, página 64. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
