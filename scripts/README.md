# Ejemplos ejecutables

[Inicio](../README.md)

Estos dos scripts fueron reconstruidos a partir de entradas completas de la bitácora. Son ejemplos de estudio y **no son los archivos históricos originales** de las sesiones.

Se requiere Python 3.10 o posterior. No utilizan paquetes externos, red ni archivos de entrada adicionales.

| Script | Entrada | Comprobación |
| --- | --- | --- |
| [hail_caesar.py](hail_caesar.py) | Transcripción ROT13 de la ficha 05 | Transformación inversa y bandera `deadface{Fetch}` |
| [x_marks_the_spot.py](x_marks_the_spot.py) | Ciphertext hexadecimal de la ficha 07 | Exploración de 256 claves, resultado único y recifrado |

```bash
python scripts/hail_caesar.py
python scripts/x_marks_the_spot.py
```

Salida esperada: el primer ejemplo muestra el nombre Fetch; el segundo encuentra la clave `0x44` y `deadface{xor_1_byt3_4t_4_t1m3}`.

Los fragmentos de otros writeups pueden necesitar archivos del reto, valores recuperados en fichas previas o constantes que no están disponibles. Cada ficha explica esas dependencias.

## Scripts históricos recuperados

Se incluyen [diez originales y su inventario](originales/README.md), conservados sin cambios. Se recuperaron selectivamente como archivos de texto después de verificar las tres partes del respaldo y el SHA-256 del archivo completo. También está incluida la configuración JSON necesaria para Keypad Oracle.

El original de Keypad Oracle y su configuración se ejecutaron localmente: el PIN `3719` produjo `deadface{your-pin-is-valid}`. Los cuatro scripts de tráfico y el escáner PowerShell de memoria se revisaron y se comprobaron sintácticamente. Los cinco scripts Python se analizaron sintácticamente y `decode_hips.py` se ejecutó sobre sus constantes incluidas. No se ejecutó de nuevo la cadena completa de tráfico con PCAP y secretos de sesión ni los análisis que requieren APK o un volcado de memoria.
