# SQL Skillz

[Índice de writeups](../README.md) · [Catálogo completo](../../catalogo/README.md)

**Categoría:** Aurora Patient Zero · **Puntos en el catálogo:** 50 · **Estado:** Verificado

Consultar la medicación asociada al identificador recuperado y distinguir el fármaco solicitado.
Evidencia: Reproducido con el archivo original

Herramientas: Python 3 y sqlite3


## Procedimiento

1. Localizar aurora_meds.sqlite en el paquete. Extraer una copia de trabajo; SQLite es una base de datos
     contenida en un archivo, no requiere levantar un servidor.

2. Consultar sqlite_master o PRAGMA table_info(medications) para conocer la estructura. La tabla medications
    contiene pid, dos medicamentos y sus respectivas dosis y frecuencias.

3. Filtrar por pid = 847261, obtenido de la radiografía. Usar una condición precisa evita seleccionar a otro
     paciente de la colección.

4. Leer medication_1 y medication_2. Identificar Candesartan como el medicamento distinto de Ibuprofen que
     solicita el reto.

5. Conservar la consulta junto con su resultado. La bandera usa el nombre del medicamento, sin la dosis, el
    identificador ni el nombre del paciente.


## Comandos o lógica reproducible

```text
from pathlib import Path
import sqlite3
Path("aurora_meds.sqlite").write_bytes(ipa.read(prefix + "aurora_meds.sqlite"))
db = sqlite3.connect("file:aurora_meds.sqlite?mode=ro", uri=True)
print(db.execute("PRAGMA table_info(medications)").fetchall())
print(db.execute(
    "SELECT medication_1, medication_2 FROM medications WHERE pid = ?",
    (847261,)).fetchall())
db.close()


```

## Resultado conservado

```text
deadface{Candesartan}

```

## Por qué funciona

El identificador vincula dos fuentes independientes: los metadatos de la radiografía y la tabla de medicación. La
consulta parametrizada expresa esa relación de forma reproducible.


## Aprendizaje para el análisis

Los archivos SQLite incluidos en una aplicación pueden revelar datos aun cuando la interfaz los oculte. Revisar
qué información se distribuye realmente.

---

Fuente: bitácora técnica personal, edición del 19 de octubre de 2026, ficha 03, página 14. Adaptación a Markdown; no constituye una nueva ejecución ni una nueva aceptación en CTFd. Los datos técnicos pertenecen al escenario del CTF.
