# Puzzle de Linux y formatos bioinformáticos

Material didáctico de repaso para el **TP — Introducción a Linux**, destinado a estudiantes de Biotecnología del IUDPT.

El repositorio contiene un ejercicio interactivo diseñado para ejecutarse en [sandbox.bio](https://sandbox.bio/). Los estudiantes trabajan desde una terminal Linux dentro del navegador, sin instalar programas ni descargar los archivos manualmente.

## Iniciar la actividad

Ingresar en:

### [Abrir el puzzle en sandbox.bio](https://sandbox.bio/github/mcpalumbo/puzzle-linux)

También se puede copiar esta dirección en el navegador:

```text
https://sandbox.bio/github/mcpalumbo/puzzle-linux
```

## ¿En qué consiste?

Una serie de archivos bioinformáticos perdió sus extensiones. A lo largo del desafío, los estudiantes deben:

- navegar y manipular archivos desde la terminal;
- inspeccionar contenidos con comandos de Linux;
- reconocer los formatos FASTA, FASTQ, GFF3, BED, VCF y SAM;
- organizar los resultados en directorios;
- filtrar anotaciones con `grep`, `cut`, tuberías y redirecciones;
- construir una pequeña base local y ejecutar BLAST;
- comprobar su progreso mediante un verificador en Python;
- resolver, de manera opcional, un ejercicio de automatización con Python.

## Organización del repositorio

El contenido que sandbox.bio carga se encuentra en `.sandboxbio/`:

- los archivos Markdown se presentan como solapas del tutorial;
- `muestras/` contiene los archivos que deben investigarse;
- `referencias/` contiene las secuencias utilizadas en la búsqueda BLAST;
- `verificar.py` revisa los productos generados durante la actividad;
- `sandboxbio.config.json` configura el inicio de la experiencia.

Los cambios publicados en este repositorio se reflejan en la actividad al iniciar un sandbox nuevo o reiniciar el existente.

