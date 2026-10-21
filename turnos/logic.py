from datetime import date, timedelta

# Ciclo 2x2x2: 6 posiciones que se repiten indefinidamente
CICLO = [
    ("Diurno", "1er día"),
    ("Diurno", "2do día"),
    ("Nocturno", "1er día"),
    ("Nocturno", "2do día"),
    ("Descanso", "1er día"),
    ("Descanso", "2do día"),
]

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def opciones():
    """Lista de (índice, etiqueta) para el selector de 'qué turno tiene hoy'."""
    return [(i, f"{turno} - {dia}") for i, (turno, dia) in enumerate(CICLO)]


def turno_para(fecha_ref: date, indice_ref: int, fecha_objetivo: date):
    """Devuelve (turno, dia_del_turno) para fecha_objetivo.
    El módulo de Python maneja bien fechas pasadas (diferencia negativa)."""
    diferencia = (fecha_objetivo - fecha_ref).days
    return CICLO[(indice_ref + diferencia) % 6]


def formatear_fecha(f: date) -> str:
    return f"{DIAS[f.weekday()]} {f.day} de {MESES[f.month - 1]} de {f.year}"


def proximos_dias(fecha_ref, indice_ref, desde: date, cantidad=7):
    filas = []
    for n in range(cantidad):
        f = desde + timedelta(days=n)
        turno, dia = turno_para(fecha_ref, indice_ref, f)
        filas.append({"fecha": formatear_fecha(f), "turno": turno, "dia": dia})
    return filas
