# Challenge Accepted

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** De Monne Breach · **Puntos en el catálogo:** 100 · **Estado:** Parcial

Conservar el valor hexadecimal identificado en la investigación del incidente.
Evidencia: Documentado en la sesión

Herramientas: Wireshark y revisión de autenticación


## Procedimiento

1. La sesión del 18 de octubre registró como resultado 5a2342014fe7f28997ce4dcd09f6b7f8 para este reto.

2. Para auditarlo, ubicar el intercambio de autenticación al que apunta el enunciado y distinguir desafío,
    respuesta y hash. No son valores intercambiables.

3. Copiar el campo requerido sin separadores ni prefijos y comprobar su longitud: el valor conservado tiene 32
    caracteres hexadecimales.

4. Contrastar la cadena completa con el resultado histórico. Una coincidencia parcial no permite confirmar el
    campo.

5. La bandera se conserva como resultado documentado, pero no se presenta como una nueva reproducción
     técnica del paquete de red.


## Resultado conservado

```text
deadface{5a2342014fe7f28997ce4dcd09f6b7f8}

```

## Por qué funciona

Los protocolos de autenticación incluyen varios campos binarios. El nombre del reto no basta para decidir cuál
se debe extraer.


## Aprendizaje para el análisis

Registrar el número de trama, el nombre del campo y sus bytes al resolver retos de autenticación.


## Alcance de la reconstrucción

No se recuperó el número de paquete ni el campo exacto. El procedimiento queda incompleto hasta contar con esa evidencia; se evita
denominarlo MD5 o NTLM sin respaldo.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 26, página 37. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
