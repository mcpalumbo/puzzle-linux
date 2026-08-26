# 🧪 Misión 3 — Recuperar genes de resistencia

## Situación

El equipo necesita una tabla mínima con las coordenadas de genes asociados a resistencia antimicrobiana.

> **Objetivo:** filtrar el GFF y generar `resultados/resistencia.bed` mediante una tubería.

## Paso 1 — Reconocer las columnas

```bash
head -n 5 muestras/anotacion_aislado_17.gff
```

| Columna GFF | Contenido requerido |
|---:|---|
| 1 | Secuencia de referencia |
| 4 | Inicio |
| 5 | Fin |
| 7 | Hebra (`+` o `-`) |
| 9 | Atributos y descripción |

## Paso 2 — Encontrar las filas

Buscá `resistencia` sin distinguir mayúsculas usando `grep -i`. Ejecutá primero solamente la búsqueda y observá cuántas filas devuelve.

## Paso 3 — Elegir columnas

`cut -f1,4,5,7` conserva las columnas necesarias de un archivo tabulado. Conectá las operaciones con una tubería:

```text
grep ... | cut ...
```

Cuando obtengas cuatro columnas, redirigí con `>` a `resultados/resistencia.bed`.

> `|` envía la salida de un comando al siguiente. `>` guarda la salida final en un archivo.

## Paso 4 — Validar

```bash
cat resultados/resistencia.bed
wc -l resultados/resistencia.bed
```

### Entrega

- [ ] Exactamente dos filas.
- [ ] Cuatro columnas tabuladas.
- [ ] Secuencia, inicio, fin y hebra, en ese orden.
- [ ] Ningún encabezado.

```bash
python3 verificar.py
```

Al terminar deberías alcanzar `6/8`.

