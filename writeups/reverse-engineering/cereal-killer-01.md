# Cereal Killer 01

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Reverse Engineering · **Puntos en el catálogo:** 50 · **Estado:** Parcial

Identificar la contraseña y recuperar la pista del cereal favorito de los insectoides.
Evidencia: Documentado en la sesión

Herramientas: Análisis estático del binario Linux, SHA-1, Base64 y RC4


## Procedimiento

1. Seleccionar re01-lin-x86.bin y verificar su SHA-256 contra el proporcionado en la competencia. El respaldo
    conserva también una variante Windows.

2. Revisar las cadenas y la función de comprobación de contraseña. La sesión identificó operaciones SHA-1 y
    Base64 en la validación.

3. Recuperar la contraseña cookiecrisp y comprobar cómo se transforma antes de compararla. No confundir el
    nombre del cereal con la bandera final.

4. Seguir la rutina RC4 que descifra el recurso de salida. El resultado histórico conduce a
    https://cerealkiller.lyttonlabs.org/unwanted-guests/ick.png.

5. Abrir la imagen como recurso del reto y leer la bandera completa. Registrar la URL y la imagen, porque el
    ejecutable puede devolver un enlace en lugar de la bandera.

6. Conservar la puntuación y las mayúsculas exactas de You-Vill-Eat-Ze-Bugz-Und-You-Vill-Be-Happy!!!.


## Resultado conservado

```text
deadface{You-Vill-Eat-Ze-Bugz-Und-You-Vill-Be-Happy!!!}

```

## Por qué funciona

La cadena de resolución cruza validación de entrada, descifrado y un recurso externo. Detenerse en la
contraseña dejaría incompleto el objetivo.


## Aprendizaje para el análisis

Documentar la función de cada transformación y distinguir contraseña, cereal, URL y bandera.


## Alcance de la reconstrucción

Se recuperaron las técnicas, contraseña y URL; faltan los arrays y offsets completos para reproducir RC4 únicamente desde este texto.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 44, página 55. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
