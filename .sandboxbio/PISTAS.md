# Pistas

<details><summary>Pista 1 — Reconocer formatos</summary>

- FASTA: cada registro comienza con `>`.
- FASTQ: cada lectura ocupa cuatro líneas; la tercera comienza con `+`.
- GFF3: suele comenzar con `##gff-version 3` y tiene nueve columnas.
- BED: suele tener al menos cromosoma, inicio y fin, sin encabezado obligatorio.
- VCF: contiene líneas `##` y un encabezado `#CHROM`.
- SAM: sus encabezados comienzan con `@`; los alineamientos tienen al menos once columnas.
</details>

<details><summary>Pista 2 — Organizar directorios</summary>

`mkdir -p` puede crear ambos directorios. Usá `cp` para conservar los originales en `muestras/`.
</details>

<details><summary>Pista 3 — Filtrar el GFF</summary>

Probá primero `grep -i resistencia archivo.gff`. Conectalo mediante `|` con `cut -f1,4,5,7` y redirigí con `>`.
</details>

<details><summary>Pista 4 — Interpretar BLAST</summary>

Con `-outfmt 6`, cada alineamiento ocupa una fila. La segunda columna es `sseqid`; la primera fila corresponde al mejor hit.
</details>

<details><summary>Pista 5 — Bonus Python</summary>

Usá `pathlib.Path("muestras").iterdir()` para recorrer archivos y `sum(1 for linea in manejador)` para contar líneas.
</details>

