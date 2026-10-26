# Chatty Cathy

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** OSINT · **Puntos en el catálogo:** 15 · **Estado:** Documentado

Seguir una pista OSINT desde GhostTown hasta un recurso expuesto en un sitio relacionado.
Evidencia: Documentado en la sesión

Herramientas: Navegador y revisión de robots.txt


## Procedimiento

1. Leer la conversación correspondiente en GhostTown y seguir la referencia a Wander with Alice.

2. Inspeccionar las pistas públicas del sitio. La ruta robots.txt se encuentra en la raíz del dominio y comunica
     preferencias de rastreo a buscadores.

3. Revisar su contenido y las rutas que revela. La sesión obtuvo la bandera mediante esta cadena GhostTown,
    Wander with Alice y robots.txt.

4. Conservar la relación entre la publicación inicial y el sitio. Un resultado de búsqueda sin ese vínculo no
    demuestra que corresponda al reto.

5. Registrar la bandera exacta, incluyendo el signo de admiración de k!ds.


## Resultado conservado

```text
deadface{y0u_m3ddling_k!ds}

```

## Por qué funciona

robots.txt es público y puede revelar rutas que el autor prefería que los buscadores no indexaran. No impone
autenticación.


## Aprendizaje para el análisis

No utilizar instrucciones para rastreadores como sustituto de controles de acceso.


## Alcance de la reconstrucción

El resumen histórico no conserva la URL completa de Wander with Alice; no se reconstruye un dominio por suposición.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 34, página 45. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
