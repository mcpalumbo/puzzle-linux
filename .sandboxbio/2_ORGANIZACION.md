# 🗂️ Misión 2 — Organizar el lote

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

### Entrega

- [ ] `secuencias/` contiene dos archivos.
- [ ] `anotaciones/` contiene cuatro archivos.
- [ ] `muestras/` conserva los seis originales.

```bash
python3 verificar.py
```

Al terminar deberías alcanzar `5/8`.

