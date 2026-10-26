# Hard Kept Secrets

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Slayer · **Puntos en el catálogo:** 20 · **Estado:** Documentado

Localizar un token interno incorporado en la aplicación Android de De Monne.
Evidencia: Documentado en la sesión

Herramientas: Análisis estático APK, classes.dex y búsqueda de cadenas


## Código histórico disponible

[inspect_dex.py](../../scripts/originales/inspect_dex.py) · [Entradas y límites](../../scripts/originales/README.md).

Estos archivos conservan el análisis histórico y no implican una nueva reproducción completa del reto.

## Procedimiento

1. Abrir app-release.zip y localizar el APK. Un APK es un contenedor ZIP; puede inspeccionarse sin instalarlo.

2. Examinar classes.dex, que contiene bytecode y cadenas del programa. La sesión conservó inspect_dex.py
    como apoyo al análisis.

3. Buscar X-Internal-Token, INTERNAL_API_TOKEN e InternalTokenInterceptor. La cabecera conecta el valor
    con su uso en solicitudes de red.

4. Leer la constante completa y comprobar que no se ha truncado en la salida de terminal. El token contiene
     barras y un signo + que deben conservarse.

5. Formar la bandera con ese valor exacto. No enviarlo a servicios ajenos al CTF ni confundirlo con una
    contraseña de un usuario.

6. Como alternativa de inspección, JADX permite descompilar y buscar las mismas referencias; su mención
    aquí no acredita una instalación local durante la competencia.


## Resultado conservado

```text
deadface{zqJRlVwBA9Xm2lE5EPjgbj/4rOxlkYZgDtkdP7jV80rZgLFrlnOEn+VAu31YKQrR}

```

## Por qué funciona

Un secreto incluido en el cliente puede recuperarse incluso cuando la interfaz no lo muestra. El interceptor
confirma cómo se utiliza.


## Aprendizaje para el análisis

Mantener los secretos de confianza del servidor fuera de aplicaciones distribuidas y limitar el alcance de
cualquier token del cliente.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 48, página 59. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
