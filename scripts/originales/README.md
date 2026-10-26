# Scripts históricos originales

[Inicio](../../README.md) · [Ejemplos reconstruidos](../README.md)

Estos archivos se recuperaron del respaldo de las sesiones del 17 y 18 de octubre de 2026. Los diez scripts se conservan **sin modificar sus bytes**. Son herramientas puntuales de investigación del CTF, con supuestos sobre nombres, formatos y directorio de trabajo.

| Archivo | Función | Entrada necesaria |
| --- | --- | --- |
| [solve_keypad.py](solve_keypad.py) | Emulación y enumeración local del PIN | Configuración JSON incluida |
| [analyze_pcap.ps1](analyze_pcap.ps1) | Inventario y extracción simplificada de flujos | DontLeaveMeHanging.pcap |
| [decrypt_calls.ps1](decrypt_calls.ps1) | Recuperación documentada de señalización TLS/SIP | PCAP y pbx_diag/pbx-diag-20261008/tls-keys.log |
| [decode_srtp.ps1](decode_srtp.ps1) | Recuperación de audio SRTP | PCAP y srtp_keys.txt |
| [scan_tones.ps1](scan_tones.ps1) | Análisis de tonos DTMF | Archivos .ulaw en call_audio |
| [inspect_dex.py](inspect_dex.py) | Inspección de cadenas y referencias DEX | apk-expanded/classes.dex |
| [decode_hips.py](decode_hips.py) | Pruebas de codificaciones del escenario HIPS | Constantes incluidas en el script |
| [scan_pirate.py](scan_pirate.py) | Inventario de tráfico, HTTP y DNS | pirate-work/pirateslife.pcap |
| [scan_memory.py](scan_memory.py) | Contexto de telemetry.ps1 en memoria | memory.raw |
| [scan-memory.ps1](scan-memory.ps1) | Búsqueda de cadenas ASCII y UTF-16LE | memory.raw de 8 GiB |

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

## Otros análisis históricos

Los scripts Python adicionales utilizan la biblioteca estándar. `inspect_dex.py` y `scan_pirate.py` esperan las rutas de entrada indicadas en la tabla; `scan_memory.py` espera el volcado en su directorio de trabajo. Se conserva la sintaxis original y no se incluyen aquí el APK, el PCAP grande ni el volcado.

`decode_hips.py` se ejecutó localmente con sus constantes originales y terminó sin errores. Es una exploración de varias representaciones; que una transformación produzca bytes no prueba por sí solo la aceptación de una bandera.

`scan-memory.ps1` tiene un límite fijo de 8 GiB y espera un segundo si alcanza el final antes de ese límite. Con un archivo menor puede permanecer esperando. Se conserva como original histórico y se comprobó su sintaxis; no se ejecutó sobre una entrada incompleta.

## Integridad y procedencia

Las tres partes del respaldo coincidieron con los SHA-256 del manifiesto original. La concatenación completa también coincidió con `63a9ac8ca42f672e80386f8797593822aa3602b1f5d0c597656226dd0835d4d2`.

Se recuperaron únicamente los diez scripts y la configuración JSON, comprobando tamaño y CRC de cada entrada ZIP. Los archivos originales se conservan byte por byte. Las herramientas y los ejecutables del respaldo no forman parte de esta publicación.

| Archivo conservado | SHA-256 |
| --- | --- |
| `analyze_pcap.ps1` | `e2a23e5fac0d32de253c306c50d461ad5361ccb756152eadffad521bb67c79ab` |
| `decode_srtp.ps1` | `7b3f5c2b8feeaf3ee19fd7df1dac3f3cce88f05c52089ee45853d128d1913d2b` |
| `decrypt_calls.ps1` | `968067cf67f1594b179105da6e3ec68a1cafdee175800d9764b4602034bc08c7` |
| `scan_tones.ps1` | `9f308712185aebd419a992148ce576ae38fa0321ad43c0a2a15e6658c4a1db78` |
| `solve_keypad.py` | `fd17887e58de7b54aebb8e08c3a898d1b339a81dc9166693f8f746ca3820c8ea` |
| `keypad/Keypad-Oracle.app/KeypadConfig.json` | `5d9445a253b51e2f8ba9239b5e7b0188e9e03309483151f93ad3f64721d999c5` |
| `decode_hips.py` | `d6b257f9ed0b957a570331be61d97dcdc254e84e73c7f907c2f528bca943a4a5` |
| `inspect_dex.py` | `524787d461db069e0969060d04e1276b00d656e32b60c8dccd315f8ec953f8e4` |
| `scan_pirate.py` | `402687a599e290c557705ad4448f07e131d4c87c0e7149f59f3f86fb2be5614b` |
| `scan-memory.ps1` | `45f7091f489dd7b0c4d2014c3bf6eaf3d564ef39b9bc70bba2c2aa98c58ce938` |
| `scan_memory.py` | `bfc420fb78989ea399281aed980c990eef4adb95277966fd75e5cf29b2e0101a` |
