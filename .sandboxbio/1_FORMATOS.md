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

Repetí `head -n 5` con los demás nombres. También podés usar `cat` si es corto, `tail` para mirar el final, `wc -l` para contar líneas o `less` para recorrerlo y salir con `q`.

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

## Paso 4 — Renombrá

La estructura es **`mv ORIGEN DESTINO`**. Usá el nombre real y agregale una extensión. No escribas literalmente `ORIGEN` o `DESTINO`.

Después de cada cambio:

```bash
ls -lh muestras
```

### Entrega

- [ ] Hay exactamente seis archivos.
- [ ] Cada uno tiene una extensión coherente.
- [ ] No cambiaste la parte original del nombre.

```bash
python3 verificar.py
```

El primer objetivo debería aparecer como `[OK]`.

