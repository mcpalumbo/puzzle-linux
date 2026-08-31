#!/usr/bin/env python3
"""Muestra el progreso del puzzle sin modificar el trabajo del estudiante."""

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parent
MUESTRAS = ROOT / "muestras"
RESULTADOS = ROOT / "resultados"
EXPECTED = {
    "consenso_plasmido_A.fasta", "Illumina_022026.fastq",
    "anotacion_aislado_17.gff", "regiones_panel_resistencia.bed",
    "variantes_aislado_17.vcf", "mapeo_Illumina_022026.sam",
}
MISSIONS = {
    1: ("🔎", "Identificar los formatos"),
    2: ("🗂️", "Organizar los archivos"),
    3: ("🧪", "Recuperar genes de resistencia"),
    4: ("🧬", "Identificar la secuencia con BLAST"),
}


def nonempty(path):
    return path.is_file() and path.stat().st_size > 0


def evaluate():
    """Devuelve los ocho controles agrupados por misión."""
    present = {p.name for p in MUESTRAS.iterdir() if p.is_file()}
    seq_dir = RESULTADOS / "secuencias"
    ann_dir = RESULTADOS / "anotaciones"

    res_bed = RESULTADOS / "resistencia.bed"
    bed_valid = False
    if nonempty(res_bed):
        rows = [line.split("\t") for line in res_bed.read_text().splitlines() if line.strip()]
        bed_valid = len(rows) == 2 and all(len(row) == 4 for row in rows) and {row[1] for row in rows} == {"5", "310"}

    blast_file = RESULTADOS / "blast.tsv"
    blast_valid = False
    if nonempty(blast_file):
        with blast_file.open(newline="") as handle:
            rows = [row for row in csv.reader(handle, delimiter="\t") if row]
        blast_valid = bool(rows) and len(rows[0]) == 6 and rows[0][1] == "Klebsiella_pneumoniae_blaLAB"

    organism = RESULTADOS / "organismo.txt"
    organism_valid = nonempty(organism) and organism.read_text().strip() == "Klebsiella_pneumoniae_blaLAB"

    return {
        1: [("Los seis archivos tienen el nombre y la extensión correctos", present == EXPECTED,
             "Revisá que haya exactamente seis archivos y que cada nombre conserve su parte original.")],
        2: [
            ("Existe resultados/secuencias", seq_dir.is_dir(), "Creá el directorio resultados/secuencias."),
            ("Existe resultados/anotaciones", ann_dir.is_dir(), "Creá el directorio resultados/anotaciones."),
            ("FASTA y FASTQ están copiados en secuencias",
             all(nonempty(seq_dir / n) for n in ("consenso_plasmido_A.fasta", "Illumina_022026.fastq")),
             "Comprobá que secuencias contenga copias no vacías del FASTA y del FASTQ."),
            ("GFF, BED, VCF y SAM están copiados en anotaciones",
             all(nonempty(ann_dir / n) for n in ("anotacion_aislado_17.gff", "regiones_panel_resistencia.bed", "variantes_aislado_17.vcf", "mapeo_Illumina_022026.sam")),
             "Comprobá que anotaciones contenga copias no vacías de los cuatro formatos esperados."),
        ],
        3: [("resistencia.bed contiene dos genes y cuatro columnas", bed_valid,
             "Revisá el filtro, la cantidad de filas y las columnas separadas por tabulaciones.")],
        4: [
            ("blast.tsv tiene seis columnas y el mejor hit correcto", blast_valid,
             "Revisá el formato de salida de BLAST y cuál es el primer alineamiento."),
            ("organismo.txt contiene solamente el identificador del mejor hit", organism_valid,
             "Extraé la segunda columna de la primera fila de blast.tsv."),
        ],
    }


def bar(done, total, width=20):
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def show_mission(number, checks, total_done, total_checks):
    icon, title = MISSIONS[number]
    print(f"\n{'=' * 54}\n{icon}  MISIÓN {number} · {title.upper()}\n{'=' * 54}\n")
    mission_done = sum(ok for _, ok, _ in checks)
    for label, ok, hint in checks:
        print(f"{'✅' if ok else '❌'} {label}")
        if not ok:
            print(f"   ↳ {hint}")
    print(f"\nProgreso de la misión: {mission_done}/{len(checks)}  {bar(mission_done, len(checks), 12)}")
    print(f"Progreso total:         {total_done}/{total_checks}  {bar(total_done, total_checks)}  {round(100 * total_done / total_checks)} %")
    if mission_done == len(checks):
        print("\n🎉 Misión completada. Ya podés continuar con la siguiente.")
    else:
        print("\n💡 Corregí lo pendiente y volvé a ejecutar este mismo comando.")


def show_dashboard(results):
    all_checks = [check for checks in results.values() for check in checks]
    total_done = sum(ok for _, ok, _ in all_checks)
    total_checks = len(all_checks)
    print("\n🧬 PROGRESO DEL CASO\n")
    for number, checks in results.items():
        done = sum(ok for _, ok, _ in checks)
        _, title = MISSIONS[number]
        state = "✅" if done == len(checks) else ("🔄" if done else "⬜")
        print(f"{state} Misión {number} · {title:<38} {done}/{len(checks)}")
    percent = round(100 * total_done / total_checks)
    print(f"\nProgreso total: {total_done}/{total_checks}  {bar(total_done, total_checks)}  {percent} %")
    if total_done == total_checks:
        print("\n🔬 ¡Caso resuelto! Los archivos están listos para volver al laboratorio.")
    else:
        print("\nPara ver qué revisar en una misión:")
        print("  python3 verificar.py N    # reemplazá N por 1, 2, 3 o 4")


def main():
    results = evaluate()
    all_checks = [check for checks in results.values() for check in checks]
    total_done = sum(ok for _, ok, _ in all_checks)
    total_checks = len(all_checks)
    if len(sys.argv) == 1:
        show_dashboard(results)
    elif len(sys.argv) == 2 and sys.argv[1] in {"1", "2", "3", "4"}:
        number = int(sys.argv[1])
        show_mission(number, results[number], total_done, total_checks)
    else:
        print("Uso: python3 verificar.py [1|2|3|4]")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
