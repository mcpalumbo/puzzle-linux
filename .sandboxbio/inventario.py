#!/usr/bin/env python3
"""Bonus: completar el inventario automático de muestras."""

from pathlib import Path

MUESTRAS = Path("muestras")

# PSEUDOCÓDIGO
# PARA cada elemento dentro de muestras/
#     SI el elemento no es un archivo
#         continuar con el siguiente
#     ABRIR el archivo
#     CONTAR sus líneas
#     IMPRIMIR nombre, tabulación y cantidad

for archivo in sorted(MUESTRAS.iterdir()):
    # PASO 1: mostrá el nombre del archivo actual.
    # PASO 2: ignorá el elemento si no es un archivo.
    # PASO 3: abrilo y guardá la cantidad de líneas en una variable.
    # PASO 4: imprimí el nombre y la cantidad separados por una tabulación.
    # Reemplazá "pass" a medida que completes los pasos.
    pass
