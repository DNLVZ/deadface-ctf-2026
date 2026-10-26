# Alice and Bob Would Like a Word

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** OSINT · **Puntos en el catálogo:** 75 · **Estado:** Parcial

Inspeccionar información expuesta mediante las claves públicas del perfil identificado por el reto.
Evidencia: Documentado en la sesión

Herramientas: OSINT y lectura de claves públicas SSH


## Procedimiento

1. Seguir la pista del personaje hasta el perfil fr34ked0ut en el servicio indicado por el escenario.

2. La sesión recuperó una referencia a fr34ked0ut.keys. Este tipo de recurso permite consultar claves públicas
     SSH asociadas a un perfil.

3. Revisar tanto las líneas completas como comentarios y campos codificados. Una clave pública no es una
    contraseña privada; el reto depende del contenido expuesto en ese recurso.

4. Conservar la respuesta histórica PubM34n5Publ1cDuH y la referencia al recurso que la originó.

5. Para completar la reproducción exacta, recuperar la línea de clave o comentario original. Sin ella no puede
    afirmarse si el mensaje estaba en un comentario, en un componente decodificado o en otra propiedad.


## Resultado conservado

```text
deadface{PubM34n5Publ1cDuH}

```

## Por qué funciona

La información pública vinculada a un perfil puede contener material adicional útil para OSINT.


## Aprendizaje para el análisis

No confundir publicidad intencional de una clave con exposición de una clave privada.


## Alcance de la reconstrucción

Resultado documentado con procedimiento parcial: no se recuperó el contenido exacto de la clave pública.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 37, página 48. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
