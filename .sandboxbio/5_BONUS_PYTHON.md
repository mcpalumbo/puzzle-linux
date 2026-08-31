![Bonus Python: Automatizar el inventario](https://raw.githubusercontent.com/mcpalumbo/puzzle-linux/main/.sandboxbio/imagenes/bonus-python.jpg)

Esta misión es opcional y no forma parte de los ocho objetivos principales.

> 🎯 **Objetivo:** completar `inventario.py` para contar las líneas de todos los archivos de `muestras/` sin escribir sus nombres manualmente.

El programa debe imprimir una fila por archivo:

```text
nombre_de_archivo<TAB>cantidad_de_lineas
```

## 🧠 Primero, pensá el algoritmo

El **pseudocódigo** describe los pasos de un programa con palabras, sin exigir la sintaxis exacta de Python. En `inventario.py` vas a encontrar este plan escrito como comentarios:

```text
PARA cada elemento dentro de muestras/
    SI el elemento no es un archivo
        continuar con el siguiente
    ABRIR el archivo
    CONTAR sus líneas
    IMPRIMIR nombre, tabulación y cantidad
```

Tu tarea es reemplazar el `pass` del archivo por instrucciones Python que implementen esos pasos.

## ✏️ Editar desde la terminal

La opción más sencilla es `nano`:

```bash
nano inventario.py
```

Dentro de `nano`:

- escribí y borrá como en un editor común;
- guardá con `Ctrl` + `O` y confirmá con `Enter`;
- salí con `Ctrl` + `X`.

Si ya conocés `vim`, también podés usar `vim inventario.py`: presioná `i` para editar, `Esc` para salir del modo de edición y escribí `:wq` para guardar y cerrar.

> 💡 Si un comando deja la terminal esperando, `Ctrl` + `C` suele cancelarlo. Dentro de `nano`, `Ctrl` + `X` vuelve a la terminal.

## 🧩 Piezas que podés necesitar

- `archivo.is_file()` permite preguntar si un elemento es un archivo.
- `archivo.open()` permite abrirlo.
- `sum(1 for linea in manejador)` cuenta las líneas de un archivo abierto.
- `archivo.name` devuelve solamente su nombre.
- `"\t"` representa una tabulación.

## 🧪 Probar el programa

Ejecutalo desde el directorio principal:

```bash
python3 inventario.py
```

Cuando veas seis filas correctas, guardá la salida:

```bash
python3 inventario.py > resultados/inventario.tsv
```

## 🧭 Comprobá tu resultado

```bash
cat resultados/inventario.tsv
wc -l resultados/inventario.tsv
```

Deberías obtener seis filas, separadas por tabulaciones y sin nombres de muestras escritos manualmente en el código.
