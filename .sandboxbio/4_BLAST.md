# 🧬 Misión 4 — Identificar la secuencia con BLAST

## Situación

La secuencia consenso podría corresponder a uno de tres genes de referencia.

> **Objetivo:** encontrar el mejor hit y guardar la tabla completa y su identificador.

## Paso 1 — Inspeccionar los FASTA

```bash
head muestras/consenso_plasmido_A.fasta
grep '^>' referencias/genes_resistencia.fasta
```

La consulta contiene una secuencia y la referencia contiene tres candidatos.

## Paso 2 — Construir la base

```bash
makeblastdb -in referencias/genes_resistencia.fasta -dbtype nucl
```

- `-in`: FASTA de referencia.
- `-dbtype nucl`: secuencias de nucleótidos.

Es normal que aparezcan archivos auxiliares en `referencias/`.

## Paso 3 — Ejecutar BLAST

Usá `blastn`, la consulta renombrada y la base anterior. El formato requerido es:

```text
6 qseqid sseqid pident length evalue bitscore
```

| Campo | Significado |
|---|---|
| `qseqid` | Consulta |
| `sseqid` | Referencia encontrada |
| `pident` | Porcentaje de identidad |
| `length` | Longitud alineada |
| `evalue` | Significancia |
| `bitscore` | Puntaje |

Redirigí la salida a `resultados/blast.tsv`.

## Paso 4 — Interpretar

```bash
head -n 3 resultados/blast.tsv
```

La primera fila es el mejor alineamiento. Extraé su segunda columna (`sseqid`) y guardala en `resultados/organismo.txt`. Podés combinar `head -n 1` con `cut -f2` o usar `awk`.

### Entrega

- [ ] `blast.tsv` tiene seis columnas.
- [ ] La primera fila es el mejor hit.
- [ ] `organismo.txt` contiene una sola línea y solo el identificador.

```bash
python3 verificar.py
```

Si aparece `8/8`, resolviste el caso.

