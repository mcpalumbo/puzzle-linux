![Bonus Python: Automatizar el inventario](https://raw.githubusercontent.com/mcpalumbo/puzzle-linux/main/.sandboxbio/imagenes/bonus-python.jpg)

Esta misión es opcional y no forma parte de los ocho objetivos principales. No necesitás experiencia previa programando: vamos a construir el script de a poco y probarlo después de cada cambio.

> 🎯 **Objetivo:** completar `inventario.py` para obtener automáticamente el nombre y la cantidad de líneas de cada archivo de `muestras/`.

El resultado final tendrá esta forma:

```text
nombre_de_archivo<TAB>cantidad_de_lineas
```

## 🗺️ El plan en pseudocódigo

Antes de escribir Python, describimos el algoritmo con palabras. Esto se llama **pseudocódigo**:

```text
PARA cada elemento dentro de muestras/
    SI el elemento no es un archivo
        continuar con el siguiente
    ABRIR el archivo
    CONTAR sus líneas
    IMPRIMIR nombre, tabulación y cantidad
```

No es código para ejecutar: es un mapa de lo que el programa tiene que hacer. Los cuatro pasos de esta actividad traducen ese mapa a Python.

## 🧠 ¿Qué es un programa?

Un programa es una lista de instrucciones. Python las lee de arriba hacia abajo y ejecuta una después de otra.

Por ejemplo:

```python
mensaje = "Hola"
print(mensaje)
```

La primera línea guarda el texto `"Hola"` en una **variable** llamada `mensaje`. Una variable es un nombre que usamos para recordar un dato. La segunda línea muestra ese dato en la pantalla.

En nuestro script ya aparece esta variable:

```python
MUESTRAS = Path("muestras")
```

`MUESTRAS` representa el directorio `muestras/`. Usar ese nombre evita repetir la ruta cada vez que la necesitemos.

## 🛠️ Abrí el archivo de trabajo

```bash
nano inventario.py
```

Dentro de `nano`:

- escribí y borrá como en un editor común;
- guardá con `Ctrl` + `O` y confirmá con `Enter`;
- salí con `Ctrl` + `X`.

Si ya conocés `vim`, podés usar `vim inventario.py`: presioná `i` para editar, `Esc` para terminar de editar y escribí `:wq` para guardar y cerrar.

> 💡 Si un comando deja la terminal esperando, `Ctrl` + `C` suele cancelarlo. Dentro de `nano`, `Ctrl` + `X` vuelve a la terminal.

## Paso 1 — Recorrer los archivos

En `inventario.py` ya está escrito:

```python
for archivo in sorted(MUESTRAS.iterdir()):
    pass
```

Un `for` repite instrucciones. En cada vuelta, la variable `archivo` representa un elemento diferente de `muestras/`.

Los cuatro espacios antes de `pass` forman la **sangría**. Le indican a Python qué instrucciones deben repetirse dentro del `for`. La sangría es obligatoria.

Reemplazá `pass` por:

```python
    print(archivo.name)
```

Guardá y probá:

```bash
python3 inventario.py
```

Deberías ver seis nombres. `archivo.name` obtiene solamente el nombre, sin incluir la ruta completa.

## Paso 2 — Tomar una decisión

Un directorio también puede contener otros directorios. Queremos contar líneas solamente si el elemento actual es un archivo.

Agregá estas líneas **antes** de `print`:

```python
    if not archivo.is_file():
        continue
```

Esto se puede leer así:

- `if` significa **si se cumple esta condición**;
- `archivo.is_file()` pregunta si el elemento es un archivo;
- `not` invierte la respuesta;
- `continue` salta a la siguiente vuelta del `for`.

Notá que `continue` tiene ocho espacios: está dentro del `if`, que a su vez está dentro del `for`.

Guardá y ejecutá nuevamente. Los seis nombres deberían seguir apareciendo.

## Paso 3 — Abrir y contar

Ahora reemplazá la línea `print(archivo.name)` por este bloque:

```python
    with archivo.open() as manejador:
        cantidad = sum(1 for linea in manejador)
```

Acá ocurren tres cosas:

1. `archivo.open()` abre el archivo actual.
2. `manejador` es una variable que permite leer su contenido.
3. `sum(1 for linea in manejador)` suma uno por cada línea encontrada.

El resultado se guarda en otra variable, `cantidad`. El nombre podría ser distinto, pero elegimos uno que recuerde qué dato contiene.

`with` también se ocupa de cerrar el archivo cuando termina la lectura.

## Paso 4 — Mostrar una fila

Debajo del bloque `with`, pero todavía dentro del `for`, agregá:

```python
    print(archivo.name, cantidad, sep="\t")
```

`print` recibe dos datos: el nombre y la cantidad. `sep="\t"` indica que debe separarlos con una tabulación.

La estructura final debe verse así:

```text
for ...:
    if ...:
        continue
    with ...:
        cantidad = ...
    print(...)
```

Este bloque muestra la estructura y la sangría, pero los puntos suspensivos deben quedar reemplazados por el código que fuiste agregando.

## 🧪 Probar y guardar el resultado

```bash
python3 inventario.py
```

Cuando veas seis filas con nombre y cantidad, guardá la salida:

```bash
python3 inventario.py > resultados/inventario.tsv
cat resultados/inventario.tsv
wc -l resultados/inventario.tsv
```

Deberías obtener seis filas separadas por tabulaciones. El programa debe descubrir los nombres recorriendo el directorio: no hace falta escribirlos manualmente en el código.

## 🐞 Si aparece un error

- `IndentationError`: revisá la cantidad de espacios al comienzo de cada línea.
- `SyntaxError`: comprobá paréntesis, comillas y los dos puntos `:` después de `for`, `if` y `with`.
- No aparece ninguna salida: verificá que hayas reemplazado `pass` y guardado el archivo.
- Aparece `NameError`: revisá que el nombre de cada variable esté escrito siempre de la misma forma.

Si necesitás una ayuda adicional, abrí **PISTAS** y buscá la sección **Bonus Python**.
