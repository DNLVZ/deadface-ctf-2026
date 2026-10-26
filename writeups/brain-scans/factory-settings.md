# Factory Settings

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Brain Scans · **Puntos en el catálogo:** 25 · **Estado:** Documentado

Usar la documentación del dispositivo simulado para identificar las credenciales de fábrica.
Evidencia: Credenciales verificadas en el PDF; bandera documentada en la sesión

Herramientas: Manual PDF y navegador


## Procedimiento

1. Revisar Asset Label y abrir el manual CS-9000 asociado al equipo. Conservar
    cs9000-field-service-manual.pdf como evidencia.

2. Ir a la página 2, sección 2.3 Default technician account. El manual especifica usuario emedra-svc y
      contraseña ChangeMe!2019.

3. Leer también la instrucción de cambiar la contraseña en el primer arranque. El reto plantea precisamente un
     despliegue donde ese cambio no se realizó.

4. Introducir las credenciales en ScanWorks, dentro del dispositivo del CTF. La sesión posterior registró acceso
     verificado y la bandera d3fault_cr3ds_n3v3r_ch4ng3d.

5. Guardar el vínculo entre manual, formulario y resultado. No usar un diccionario de contraseñas: la evidencia
    documental proporciona el par exacto.


## Comandos o lógica reproducible

```text
Dispositivo del laboratorio: CerebraScan CS-9000
Documento: EMD-CS9K-FSM Rev. C
Página: 2   Sección: 2.3
Usuario: emedra-svc
Contraseña: ChangeMe!2019


```

## Resultado conservado

```text
deadface{d3fault_cr3ds_n3v3r_ch4ng3d}

```

## Por qué funciona

La debilidad es conservar una cuenta inicial conocida por quienes tienen acceso al manual. No hace falta
vulnerar el algoritmo de autenticación.


## Aprendizaje para el análisis

Exigir cambio de credenciales iniciales y comprobarlo en la puesta en servicio.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 41, página 52. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
