# Second Shift

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Cryptography · **Puntos en el catálogo:** 90 · **Estado:** Verificado

Recuperar una orden cifrada aprovechando la reutilización del flujo de cifrado de otro mensaje cuyo texto se
conoce.
Evidencia: Reproducido con el archivo original

Herramientas: Python 3, zipfile y XOR


## Procedimiento

1. Abrir secondshift.zip. Contiene relay-heartbeat.enc, relay-heartbeat.json y relay-tasking.enc. El JSON
    proporciona el texto en claro del primer mensaje, incluidos su codificación y salto final.

2. Leer los tres archivos como bytes. Los tamaños observados son 250 bytes para el heartbeat cifrado y 220
     para la orden cifrada; el texto conocido cubre toda la segunda carga.

3. En CTR, C = P XOR K. Si dos mensajes reutilizan K, entonces C2 XOR C1 XOR P1 = P2. No hace falta
    recuperar la clave AES para explotar esta reutilización.

4. Aplicar XOR posición por posición. El texto recuperado identifica target aurora-vpn, action stage-access,
    window 00:30Z y operator mort1cia.

5. Extraer la bandera del campo note. En el texto recuperado aparece el prefijo DEADFACE en mayúsculas; la
    entrega registrada usa el envoltorio deadface en minúsculas.

6. Verificar que la salida completa es JSON coherente, no solo una palabra legible. La recuperación se limita a
    los bytes cubiertos por el texto conocido.


## Comandos o lógica reproducible

```text
import zipfile, json
with zipfile.ZipFile("secondshift.zip") as z:
    c1 = z.read("relay-heartbeat.enc")
    p1 = z.read("relay-heartbeat.json")
    c2 = z.read("relay-tasking.enc")
assert len(p1) >= len(c2) and len(c1) >= len(c2)
p2 = bytes(a ^ b ^ c for a, b, c in zip(c2, c1, p1))
print(json.loads(p2))


```

## Resultado conservado

```text
deadface{ctr_nonce_reuse_breaks_confidentiality}

```

## Por qué funciona

El fallo está en reutilizar el mismo flujo, no en una debilidad del algoritmo AES. El XOR cancela el material
compartido.


## Aprendizaje para el análisis

Garantizar la unicidad del nonce con una misma clave y usar un esquema autenticado correctamente
implementado.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 09, página 20. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
