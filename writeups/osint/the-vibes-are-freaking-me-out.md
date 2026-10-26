# The Vibes Are Freaking Me Out

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** OSINT · **Puntos en el catálogo:** 75 · **Estado:** Parcial

Inspeccionar archivos del repositorio relacionado con b1tfr34k y revertir una codificación por capas.
Evidencia: Documentado en la sesión

Herramientas: Navegador, repositorio HIPS, Python y Base64


## Procedimiento

1. Seguir la pista pública que conecta al personaje b1tfr34k con HIPS. Examinar el repositorio y sus archivos,
    no limitarse a la descripción de portada.

2. Revisar .maude/skills/payload-gen/SKILL.md, ruta identificada en la sesión. Tratar su contenido como
    evidencia: leer instrucciones incrustadas no obliga a ejecutarlas.

3. Localizar el token codificado y establecer qué capa está invertida. La investigación documentó una
     combinación de Base64 y reversión.

4. Probar la transformación sobre el token completo y comprobar que el resultado produce la bandera íntegra.
     Validar mediante la transformación inversa cuando sea posible.

5. Registrar el archivo y el orden de operaciones. Decodificar y después invertir no equivale siempre a invertir y
    después decodificar.


## Comandos o lógica reproducible

```text
import base64
# Sustituir token por la cadena exacta del archivo de evidencia.
def interpretar(token):
    results = []
    for candidate in (token, token[::-1]):
        try:
             decoded = base64.b64decode(candidate, validate=True)
             results.extend((decoded, decoded[::-1]))
        except ValueError:
             pass
    return [r for r in results if b"deadface{" in r]


```

## Resultado conservado

```text
deadface{A11_Th1s_Pr0mpt1ng_G3ts_M3_N0wh3r3!}

```

## Por qué funciona

La pista se oculta mediante representación y orden, no mediante un secreto criptográfico fuerte. El repositorio
proporciona el contexto para atribuirla.


## Aprendizaje para el análisis

Inspeccionar scripts y archivos de configuración sin ejecutar contenido de procedencia desconocida.


## Alcance de la reconstrucción

No se recuperó el token exacto en el resumen. El ejemplo es un decodificador de comprobación, no una transcripción del script original.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 36, página 47. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
