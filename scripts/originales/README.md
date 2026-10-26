# Scripts históricos originales

[Inicio](../../README.md) · [Ejemplos reconstruidos](../README.md)

Estos archivos se recuperaron del respaldo de las sesiones del 17 de octubre de 2026. Los cinco scripts se conservan **sin modificar sus bytes**. Son herramientas puntuales de investigación del CTF, con supuestos sobre nombres, formatos y directorio de trabajo.

| Archivo | Función | Entrada necesaria |
| --- | --- | --- |
| [solve_keypad.py](solve_keypad.py) | Emulación y enumeración local del PIN | Configuración JSON incluida |
| [analyze_pcap.ps1](analyze_pcap.ps1) | Inventario y extracción simplificada de flujos | DontLeaveMeHanging.pcap |
| [decrypt_calls.ps1](decrypt_calls.ps1) | Recuperación documentada de señalización TLS/SIP | PCAP y pbx_diag/pbx-diag-20261008/tls-keys.log |
| [decode_srtp.ps1](decode_srtp.ps1) | Recuperación de audio SRTP | PCAP y srtp_keys.txt |
| [scan_tones.ps1](scan_tones.ps1) | Análisis de tonos DTMF | Archivos .ulaw en call_audio |

## Repetir Keypad Oracle

Desde la raíz del repositorio:

```bash
cd scripts/originales
python solve_keypad.py
```

Python debe tener acceso a `keypad/Keypad-Oracle.app/KeypadConfig.json`, que ya está incluido. El resultado reproducido al publicar fue:

```text
(3, 7, 1, 9) 1 b'deadface{your-pin-is-valid}'
```

El primer valor es el PIN, el segundo la dirección de rotación y el tercero la salida decodificada. La prueba es local y no consulta CTFd.

## Dependencias y límites de los scripts de tráfico

Los cuatro `.ps1` incorporan C# mediante `Add-Type`. La cadena requiere PowerShell y una versión de .NET que disponga de las API criptográficas utilizadas, además del PCAP y los intermedios del laboratorio. Estos datos no se incluyen aquí.

Se hizo revisión del texto y análisis sintáctico de PowerShell, sin repetir la cadena completa. Los lectores implementan un subconjunto de PCAP, Ethernet, IPv4 y los protocolos del caso; no son analizadores generales ni manejan todas las variantes de captura o reensamblado.

En `decode_srtp.ps1`, la selección inicial de una clave no garantiza el rechazo correcto de todo paquete posterior cuya autenticación falle. Se conserva el original por trazabilidad; su contador de paquetes descifrados no demuestra autenticación integral del flujo. Antes de reutilizarlo fuera de esta reproducción hay que corregir y validar ese comportamiento.

## Integridad y procedencia

Las partes 001 y 002 coincidieron con los SHA-256 del manifiesto original. Para recuperar estos archivos se leyeron sus cabeceras ZIP y se comprobaron tamaño y CRC de cada entrada, sin extraer ejecutables o dependencias. La parte 003, marcada como infectada por Drive, no se descargó ni se utilizó.

| Archivo conservado | SHA-256 |
| --- | --- |
| `analyze_pcap.ps1` | `e2a23e5fac0d32de253c306c50d461ad5361ccb756152eadffad521bb67c79ab` |
| `decode_srtp.ps1` | `7b3f5c2b8feeaf3ee19fd7df1dac3f3cce88f05c52089ee45853d128d1913d2b` |
| `decrypt_calls.ps1` | `968067cf67f1594b179105da6e3ec68a1cafdee175800d9764b4602034bc08c7` |
| `scan_tones.ps1` | `9f308712185aebd419a992148ce576ae38fa0321ad43c0a2a15e6658c4a1db78` |
| `solve_keypad.py` | `fd17887e58de7b54aebb8e08c3a898d1b339a81dc9166693f8f746ca3820c8ea` |
| `keypad/Keypad-Oracle.app/KeypadConfig.json` | `5d9445a253b51e2f8ba9239b5e7b0188e9e03309483151f93ad3f64721d999c5` |
