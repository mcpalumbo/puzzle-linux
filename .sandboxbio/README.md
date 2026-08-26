# 🧬 El caso de las muestras sin etiqueta

Una falla durante el procesamiento borró las extensiones de seis archivos. Los datos siguen intactos, pero el laboratorio no puede continuar hasta que reconstruyas el lote.

> **Misión:** identificar los archivos, ordenarlos, recuperar genes de resistencia y determinar el origen de una secuencia mediante BLAST.

## Antes de empezar

No hace falta instalar nada. Trabajás dentro de una terminal Linux temporal: si rompés algo, podés reiniciar el sandbox.

| Etapa | Trabajo | Producto |
|---|---|---|
| 🔎 1 | Reconocer seis formatos | Archivos con extensión |
| 🗂️ 2 | Organizar el lote | Dos directorios ordenados |
| 🧪 3 | Filtrar una anotación | `resistencia.bed` |
| 🧬 4 | Ejecutar BLAST | `blast.tsv` y `organismo.txt` |
| 🐍 5 | Automatizar, opcional | `inventario.tsv` |

## Cómo trabajar

1. Abrí la pestaña **1_FORMATOS**.
2. Completá una misión por vez.
3. Ejecutá `python3 verificar.py` al final de cada etapa.
4. Si un objetivo aparece como `[PENDIENTE]`, revisá la entrega indicada.
5. Usá **PISTAS** solamente cuando lo necesites.

> **Importante:** los comandos distinguen mayúsculas de minúsculas. `Illumina_022026` no es igual a `illumina_022026`.

## Panel de progreso

Este comando no resuelve ni modifica el ejercicio; solamente revisa tus resultados:

```bash
python3 verificar.py
```

Al comenzar es correcto obtener `0/8`. El caso queda resuelto al llegar a `8/8`.

