![Misión 2: Organizar los archivos](https://raw.githubusercontent.com/mcpalumbo/puzzle-linux/main/.sandboxbio/imagenes/mision-2-organizacion.jpg)

## Situación

El laboratorio separa los datos de secuenciación de los archivos derivados del análisis.

> **Objetivo:** crear una estructura ordenada sin perder los archivos originales ya renombrados.

```text
resultados/
├── secuencias/    FASTA y FASTQ
└── anotaciones/   GFF, BED, VCF y SAM
```

## Paso 1 — Crear directorios

`mkdir` crea directorios y `-p` permite crear una ruta completa. Creá ambos directorios y comprobá:

```bash
ls -lh resultados
```

## Paso 2 — Copiar, no mover

Usá `cp` porque los archivos también deben permanecer en `muestras/`. Su estructura es **`cp ORIGEN DESTINO`** y acepta varios orígenes si el último argumento es un directorio.

| Directorio | Contenido esperado |
|---|---|
| `resultados/secuencias/` | FASTA y FASTQ |
| `resultados/anotaciones/` | GFF, BED, VCF y SAM |

## Paso 3 — Comprobar

```bash
ls -lh resultados/secuencias
ls -lh resultados/anotaciones
ls -lh muestras
```

## 🧭 Comprobá tu avance

```bash
python3 verificar.py 2
```

El verificador revisará esta misión y también te mostrará el progreso total del caso.
