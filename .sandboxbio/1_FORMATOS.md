# 🔎 Misión 1 — Identificar los formatos

## Situación

Los nombres se conservaron, pero las extensiones desaparecieron. Tenés seis candidatos dentro de `muestras/`.

> **Objetivo:** determinar qué archivo es FASTA, FASTQ, GFF3, BED, VCF y SAM, y agregar la extensión correspondiente.

## Paso 1 — Ubicate

```bash
pwd
ls -lh muestras
```

Deberías encontrar seis archivos. `ls` muestra nombres y tamaños, pero todavía no alcanza para conocer el formato.

## Paso 2 — Mirá sin abrir todo

Empezá con uno:

```bash
head -n 5 muestras/Illumina_022026
```

Vas a observar registros de cuatro líneas: un identificador que comienza con `@`, una secuencia, una línea con `+` y una línea de calidades. Esa estructura corresponde a un archivo **FASTQ**.

Este es el primer renombrado, usado como ejemplo:

```bash
mv muestras/Illumina_022026 muestras/Illumina_022026.fastq
```

Comprobá que cambió solamente el nombre:

```bash
ls -lh muestras
```

Ahora repetí la investigación con los otros cinco archivos. También podés usar `cat` si son cortos, `tail` para mirar el final, `wc -l` para contar líneas o `less` para recorrerlos y salir con `q`.

Preguntas para cada archivo:

- ¿Tiene encabezado?
- ¿Qué símbolo aparece al comienzo?
- ¿Cuántas columnas hay?
- ¿Están separadas por tabulaciones?
- ¿Se repite una estructura cada cuatro líneas?

## Paso 3 — Compará las firmas

| Formato | Firma característica | Extensión |
|---|---|---|
| FASTA | Encabezado con `>` seguido por secuencia | `.fasta` |
| FASTQ | Bloques de cuatro líneas: `@`, secuencia, `+`, calidad | `.fastq` |
| GFF3 | `##gff-version 3` y nueve columnas | `.gff` |
| BED | Intervalos: secuencia, inicio y fin | `.bed` |
| VCF | Metadatos `##` y encabezado `#CHROM` | `.vcf` |
| SAM | Encabezados `@HD`/`@SQ` y alineamientos | `.sam` |

> **Atención:** FASTQ y SAM pueden comenzar con `@`. No decidas usando solamente el primer carácter.

## Paso 4 — Renombrá los otros cinco

Tomá como modelo el comando usado con `Illumina_022026`. En cada caso, el primer argumento debe ser el nombre actual y el segundo, ese mismo nombre con la extensión que dedujiste.

Después de cada cambio:

```bash
ls -lh muestras
```

## 🧭 Comprobá tu avance

```bash
python3 verificar.py 1
```

El verificador te indicará qué está bien y qué conviene revisar. No modifica tus archivos.
