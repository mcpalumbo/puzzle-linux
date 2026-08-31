![Archivo de pistas: ayuda gradual para cada misión](https://raw.githubusercontent.com/mcpalumbo/puzzle-linux/main/.sandboxbio/imagenes/header-pistas.jpg)

Abrí solamente la ayuda que necesites. Cada misión tiene tres niveles: empezá por una orientación y avanzá hasta el comando casi completo si seguís trabado/a.

![Comandos útiles de Linux](https://raw.githubusercontent.com/mcpalumbo/puzzle-linux/main/.sandboxbio/imagenes/comandos-utiles.jpg)

## 🔎 Misión 1 — Formatos

<details><summary>Nivel 1 · Qué observar</summary>

No intentes adivinar por el nombre. Usá `head -n 5` y buscá encabezados, símbolos iniciales, cantidad de columnas y estructuras que se repitan.
</details>

<details><summary>Nivel 2 · Firmas características</summary>

- FASTA: encabezado con `>` y una secuencia debajo.
- FASTQ: bloques de cuatro líneas; comienzan con `@` y la tercera línea es `+`.
- GFF3: encabezado `##gff-version 3` y nueve columnas.
- BED: intervalos tabulados; las primeras tres columnas son secuencia, inicio y fin.
- VCF: metadatos `##` y encabezado `#CHROM`.
- SAM: encabezados `@HD`/`@SQ` y alineamientos con al menos once columnas.
</details>

<details><summary>Nivel 3 · Cómo renombrar</summary>

Conservá el nombre completo y agregá solamente la extensión:

```bash
mv muestras/nombre_actual muestras/nombre_actual.extension
```

FASTQ y SAM pueden comenzar con `@`: verificá la estructura completa antes de elegir.
</details>

## 🗂️ Misión 2 — Organización

<details><summary>Nivel 1 · Pensá el destino</summary>

FASTA y FASTQ son datos de secuencia. GFF, BED, VCF y SAM son resultados o descripciones derivadas del análisis. Los originales deben seguir en `muestras/`.
</details>

<details><summary>Nivel 2 · Crear y copiar</summary>

`mkdir -p` puede crear rutas completas. Después usá `cp`, no `mv`, porque necesitás conservar los originales.
</details>

<details><summary>Nivel 3 · Estructura de los comandos</summary>

```bash
mkdir -p resultados/secuencias resultados/anotaciones
cp ORIGEN1 ORIGEN2 resultados/secuencias/
cp ORIGEN1 ORIGEN2 ORIGEN3 ORIGEN4 resultados/anotaciones/
```

Reemplazá cada `ORIGEN` por la ruta de un archivo ya renombrado.
</details>

## 🧪 Misión 3 — Filtrado

<details><summary>Nivel 1 · Encontrar las filas</summary>

Primero buscá la palabra `resistencia` en el GFF. La opción `-i` permite encontrarla aunque cambien mayúsculas y minúsculas.
</details>

<details><summary>Nivel 2 · Conservar columnas</summary>

La salida de `grep` puede enviarse a `cut` mediante `|`. Necesitás las columnas 1, 4, 5 y 7, en ese orden.
</details>

<details><summary>Nivel 3 · Armar la tubería</summary>

```bash
grep -i resistencia muestras/anotacion_aislado_17.gff | cut -f1,4,5,7 > resultados/resistencia.bed
```

Recordá que `>` reemplaza el contenido del archivo de destino si ya existe.
</details>

## 🧬 Misión 4 — BLAST

<details><summary>Nivel 1 · Preparar la búsqueda</summary>

BLAST necesita una consulta y una base. La consulta es el consenso FASTA; la base se construye desde `referencias/genes_resistencia.fasta` con `makeblastdb`.
</details>

<details><summary>Nivel 2 · Leer el resultado</summary>

Con `-outfmt 6`, cada alineamiento ocupa una fila. La segunda columna es `sseqid`, el identificador de la referencia encontrada. La primera fila contiene el mejor hit.
</details>

<details><summary>Nivel 3 · Extraer el identificador</summary>

Si `blast.tsv` ya está creado, combiná la primera fila con la segunda columna:

```bash
head -n 1 resultados/blast.tsv | cut -f2 > resultados/organismo.txt
```
</details>

## 🐍 Bonus Python

<details><summary>Nivel 1 · Seguir el pseudocódigo</summary>

El `for` inicial de `inventario.py` ya recorre los elementos de `muestras/`. Traducí una instrucción del pseudocódigo por vez.
</details>

<details><summary>Nivel 2 · Ignorar directorios</summary>

Dentro del `for`, podés preguntar `if not archivo.is_file():` y usar `continue` para pasar al elemento siguiente.
</details>

<details><summary>Nivel 3 · Contar e imprimir</summary>

Abrí cada archivo con `with archivo.open() as contenido:`. Contá sus líneas con `sum(1 for linea in contenido)` e imprimí `archivo.name` y la cantidad usando `sep="\t"`.
</details>
