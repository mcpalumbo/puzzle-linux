# 🧬 El caso de las muestras sin etiqueta

Una falla borró las extensiones de varios archivos del laboratorio. Los datos siguen intactos, pero nadie sabe qué contiene cada archivo. Tenés que reconstruir el lote y determinar a qué organismo pertenece una secuencia desconocida.

> No hace falta instalar nada. Todo sucede en esta terminal.

## Tu misión

Dentro de `muestras/` hay seis archivos sin extensión. Inspeccionalos y renombrá cada uno con la extensión correcta:

| Formato | Contenido | Extensión |
|---|---|---|
| FASTA | Secuencias biológicas | `.fasta` |
| FASTQ | Lecturas y calidades | `.fastq` |
| GFF3 | Anotaciones | `.gff` |
| BED | Intervalos genómicos | `.bed` |
| VCF | Variantes | `.vcf` |
| SAM | Alineamientos | `.sam` |

Empezá por orientarte:

```bash
pwd
ls -lh
ls -lh muestras
```

Investigá con `file`, `head`, `tail`, `cat`, `less`, `wc`, `grep` y las combinaciones que consideres útiles. Renombrá con `mv`:

```bash
mv muestras/nombre_actual muestras/nombre_actual.extension
```

No todos los formatos se reconocen por una sola línea: buscá encabezados, columnas, separadores y patrones repetidos.

## Evidencia 1 — Ordenar el lote

Creá `resultados/secuencias/` y `resultados/anotaciones/`. Cuando los archivos estén renombrados:

- copiá FASTA y FASTQ a `resultados/secuencias/`;
- copiá GFF, BED, VCF y SAM a `resultados/anotaciones/`;
- conservá los archivos renombrados en `muestras/`.

## Evidencia 2 — Buscar genes de resistencia

Generá `resultados/resistencia.bed` con **solo** los genes cuyo atributo contenga `resistencia`, sin distinguir mayúsculas y minúsculas.

El resultado debe tener cuatro columnas separadas por tabulaciones:

```text
secuencia    inicio    fin    hebra
```

Necesitarás combinar al menos `grep`, `cut` y una redirección. En GFF3 esos datos están en las columnas 1, 4, 5 y 7.

## Evidencia 3 — Identificar la muestra por BLAST

En `referencias/genes_resistencia.fasta` hay tres genes de referencia. Construí una base BLAST local y compará contra ella la secuencia FASTA recuperada.

Guardá la salida en `resultados/blast.tsv`, con estas columnas:

```text
qseqid sseqid pident length evalue bitscore
```

Comandos útiles:

```bash
makeblastdb -in referencias/genes_resistencia.fasta -dbtype nucl
blastn -query ARCHIVO_FASTA -db referencias/genes_resistencia.fasta -outfmt "6 qseqid sseqid pident length evalue bitscore"
```

Escribí el identificador del mejor hit —solo el identificador— en `resultados/organismo.txt`. Podés obtenerlo de la primera fila con `head` y `cut` o `awk`.

## Comprobar la misión

```bash
python3 verificar.py
```

El verificador informa qué objetivos completaste, pero no modifica tus archivos. Si te trabás, abrí **PISTAS** y revelá una ayuda por vez.

## Bonus — Automatización con Python

Creá `resultados/inventario.py`: debe recorrer `muestras/` e imprimir una línea por archivo con este formato:

```text
nombre_de_archivo<TAB>cantidad_de_lineas
```

Guardá la salida con:

```bash
python3 resultados/inventario.py > resultados/inventario.tsv
```

