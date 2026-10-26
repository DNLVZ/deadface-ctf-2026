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

Se incluyen [cinco originales y su inventario](originales/README.md), conservados sin cambios. Se recuperaron selectivamente como archivos de texto de las partes 001 y 002 del respaldo. La parte 003, marcada como infectada por Drive, no se descargó.

El original de Keypad Oracle y su configuración se ejecutaron localmente: el PIN `3719` produjo `deadface{your-pin-is-valid}`. Los cuatro scripts de tráfico se revisaron y se comprobaron sintácticamente, pero no se ejecutó de nuevo su cadena completa con PCAP y secretos de sesión.
