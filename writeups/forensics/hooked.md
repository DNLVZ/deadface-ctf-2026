# Hooked

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Forensics · **Puntos en el catálogo:** 25 · **Estado:** Parcial

Recuperar la URL exacta del señuelo de autenticación identificado en la investigación.
Evidencia: Documentado en la sesión

Herramientas: Artefactos de navegador y lectura de evidencia web


## Procedimiento

1. La sesión conservó como respuesta la URL
     http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc.

2. En una revisión de artefactos de navegador, buscar la dirección en historial y caché antes de abrirla. El
    paquete CTF_Caches_Kampeter_1.zip conserva bases SQLite y objetos de caché para análisis, aunque
    su asociación exacta con este reto debe corroborarse.

3. Preservar esquema http, dominio, ruta /login y parámetros en su orden. La pregunta solicita una URL, no
     solo el dominio.

4. Distinguir el texto visible de un enlace de su destino real. Los parámetros ref y token también forman parte de
     la respuesta.

5. Documentar el objeto y campo que contienen la URL. No es necesario navegar al señuelo para leer el
    indicador.


## Resultado conservado

```text
deadface{http://demonne-secure-portal.net/login?ref=vpn_auth&token=df4e91bc}

```

## Por qué funciona

Los artefactos de navegación pueden conservar el destino utilizado por un señuelo incluso cuando la página ya
no está disponible.


## Aprendizaje para el análisis

Tratar URLs sospechosas como datos durante el análisis y conservar su forma exacta.


## Alcance de la reconstrucción

La bandera está recuperada del historial; no se recuperó la ruta exacta del artefacto que la produjo. No se afirma una asociación
definitiva con el ZIP de cachés.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 54, página 65. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
