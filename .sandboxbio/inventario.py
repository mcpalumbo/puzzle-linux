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
    # TODO: reemplazá "pass" por la traducción a Python del pseudocódigo.
    pass
