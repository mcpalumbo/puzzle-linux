#!/usr/bin/env python3
"""Verifica productos del desafío sin modificar el trabajo del estudiante."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
MUESTRAS = ROOT / "muestras"
RESULTADOS = ROOT / "resultados"
EXPECTED = {
    "consenso_plasmido_A.fasta",
    "Illumina_022026.fastq",
    "anotacion_aislado_17.gff",
    "regiones_panel_resistencia.bed",
    "variantes_aislado_17.vcf",
    "mapeo_Illumina_022026.sam",
}


def check(label, condition):
    print(f"{'✓' if condition else '·'} {label}")
    return bool(condition)


def nonempty(path):
    return path.is_file() and path.stat().st_size > 0


checks = []
present = {p.name for p in MUESTRAS.iterdir() if p.is_file()}
checks.append(check("Los seis archivos tienen la extensión correcta", EXPECTED <= present))

seq_dir = RESULTADOS / "secuencias"
ann_dir = RESULTADOS / "anotaciones"
checks.append(check("Existe resultados/secuencias", seq_dir.is_dir()))
checks.append(check("Existe resultados/anotaciones", ann_dir.is_dir()))
checks.append(check("FASTA y FASTQ fueron copiados a secuencias", all(nonempty(seq_dir / n) for n in ("consenso_plasmido_A.fasta", "Illumina_022026.fastq"))))
checks.append(check("GFF, BED, VCF y SAM fueron copiados a anotaciones", all(nonempty(ann_dir / n) for n in ("anotacion_aislado_17.gff", "regiones_panel_resistencia.bed", "variantes_aislado_17.vcf", "mapeo_Illumina_022026.sam"))))

res_bed = RESULTADOS / "resistencia.bed"
bed_valid = False
if nonempty(res_bed):
    rows = [line.split("\t") for line in res_bed.read_text().splitlines() if line.strip()]
    bed_valid = len(rows) == 2 and all(len(row) == 4 for row in rows) and {row[1] for row in rows} == {"5", "310"}
checks.append(check("resistencia.bed contiene dos genes y cuatro columnas", bed_valid))

blast_file = RESULTADOS / "blast.tsv"
blast_valid = False
if nonempty(blast_file):
    with blast_file.open(newline="") as handle:
        rows = [row for row in csv.reader(handle, delimiter="\t") if row]
    blast_valid = bool(rows) and len(rows[0]) == 6 and rows[0][1] == "Klebsiella_pneumoniae_blaLAB"
checks.append(check("blast.tsv tiene seis columnas y el mejor hit correcto", blast_valid))

organism = RESULTADOS / "organismo.txt"
organism_valid = nonempty(organism) and organism.read_text().strip() == "Klebsiella_pneumoniae_blaLAB"
checks.append(check("organismo.txt identifica el mejor hit", organism_valid))

done = sum(checks)
print(f"\nProgreso: {done}/{len(checks)} objetivos")
if done == len(checks):
    print("\n🔬 Caso resuelto. El lote está listo para volver al laboratorio.")
else:
    print("Abrí la pestaña PISTAS si necesitás ayuda gradual.")
