# 🐍 Bonus — Automatizar el inventario

Esta misión es opcional y no forma parte de los ocho objetivos principales.

> **Objetivo:** escribir un script que cuente las líneas de todos los archivos de `muestras/`.

El programa debe imprimir una fila por archivo:

```text
nombre_de_archivo<TAB>cantidad_de_lineas
```

Guardalo como `resultados/inventario.py` y probalo:

```bash
python3 resultados/inventario.py
```

Cuando funcione:

```bash
python3 resultados/inventario.py > resultados/inventario.tsv
```

## Plan sugerido

1. Importar `Path` desde `pathlib`.
2. Crear `Path("muestras")`.
3. Recorrer sus elementos con `for`.
4. Ignorar elementos que no sean archivos.
5. Abrir cada archivo y contar sus líneas.
6. Imprimir nombre y cantidad separados por `"\t"`.

### Autocontrol

- [ ] Funciona desde el directorio principal.
- [ ] Produce seis filas.
- [ ] Usa tabulaciones como separador.
- [ ] No contiene nombres de muestras escritos manualmente.

