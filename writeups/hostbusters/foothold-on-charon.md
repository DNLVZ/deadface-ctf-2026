# Foothold on Charon

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Hostbusters · **Puntos en el catálogo:** 10 · **Estado:** Documentado

Ubicar la bandera inicial en el entorno de la cuenta de acceso al host.
Evidencia: Documentado en la sesión

Herramientas: Shell Linux del laboratorio


## Procedimiento

1. Entrar mediante el mecanismo de acceso proporcionado por el reto. La sesión identificó la cuenta
    svc-deploy.

2. Ejecutar whoami para comprobar la identidad efectiva y pwd para conocer el directorio actual. Registrar
     ambos antes de explorar.

3. Listar el directorio con ls -la para incluir archivos ocultos y sus permisos. En este reto la bandera inicial se
     encontraba en el entorno de la cuenta.

4. Leer /home/svc-deploy/flag.txt. La salida documentada fue f00th0ld_0n_ch4r0n.

5. Separar este resultado de Dangerous Capability. La bandera c4p_s3tu1d_pwn3d corresponde a la elevación
    mediante capacidades, no al acceso inicial.


## Comandos o lógica reproducible

```text
whoami
pwd
ls -la
cat /home/svc-deploy/flag.txt


```

## Resultado conservado

```text
deadface{f00th0ld_0n_ch4r0n}

```

## Por qué funciona

Una revisión básica del contexto puede resolver la fase inicial sin necesidad de escalamiento. La identidad y la
ruta permiten atribuir correctamente la evidencia.


## Aprendizaje para el análisis

Documentar cada cambio de usuario y no mezclar banderas obtenidas en fases diferentes.


## Alcance de la reconstrucción

La sesión recuperada registra esta bandera como aceptada; la bitácora no conserva una exportación independiente del marcador de
CTFd.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 16, página 27. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
