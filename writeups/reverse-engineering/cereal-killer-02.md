# Cereal Killer 02

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Reverse Engineering · **Puntos en el catálogo:** 150 · **Estado:** Parcial

Extraer el material protegido y revertir la transformación de bytes usada por el binario.
Evidencia: Documentado en la sesión

Herramientas: 7-Zip, análisis estático y XOR por bloques


## Procedimiento

1. Abrir ck02.7z con la contraseña KlippyAI, registrada en la sesión. El archivo contiene el material del reto y un
    programa adicional.

2. Trabajar sobre el binario Linux e inspeccionar la rutina de transformación. No fue necesario ejecutar el
     programa adicional ni añadir excepciones al antivirus.

3. Identificar bloques de 256 bytes y la clave utilizada por XOR. La sesión encontró que debía invertirse el
     orden de los bytes de la clave.

4. Aplicar la clave invertida a los bloques siguiendo el índice utilizado por el programa. Revisar límites y longitud
    del último bloque.

5. Interpretar el texto recuperado y relacionarlo con Frankenberry, el cereal de los nórdicos.

6. Guardar la bandera completa. La puntuación interna y las sustituciones numéricas forman parte de la
    respuesta.


## Comandos o lógica reproducible

```text
def xor_con_clave_invertida(data, key):
    reverse_key = key[::-1]
    return bytes(b ^ reverse_key[i % len(reverse_key)]
                 for i, b in enumerate(data))


```

## Resultado conservado

```text
deadface{N0rdics-R3ally-like-Frank3nb3rry-cuz-bro-is-tall-like-they-are!}

```

## Por qué funciona

La reversión de la clave cambia la alineación del flujo XOR. Un resultado ilegible con la clave en orden directo
no descarta el algoritmo.


## Aprendizaje para el análisis

Leer las operaciones reales sobre los bytes, incluida la dirección de recorrido.


## Alcance de la reconstrucción

El fragmento ilustra la transformación recuperada; las constantes del binario no están transcritas en la evidencia histórica disponible.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 45, página 56. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
