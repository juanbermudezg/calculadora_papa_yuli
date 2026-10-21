# calculadora_papa_yuli
Calculadora web ligera en Django para consultar qué turno tiene un guarda de seguridad en cualquier fecha, con rotación 2x2x2 (2 diurno, 2 nocturno, 2 descanso).

# Calculadora de turnos 2x2x2

Aplicación web ligera hecha con Django para calcular qué turno le corresponde a una persona en cualquier fecha, con rotación **2x2x2**: dos días de turno diurno, dos de turno nocturno y dos de descanso.

Pensada para consultarse rápido desde el celular o el computador, sin registro ni base de datos.

## Cómo funciona

1. Indicas una fecha de referencia (normalmente hoy) y el turno que se tiene ese día, por ejemplo "Diurno - 2do día".
2. Indicas la fecha que quieres consultar.
3. La app muestra el turno correspondiente y los 7 días siguientes.

El cálculo se basa en un ciclo de 6 días que se repite:

| Posición | Turno    | Día     |
|----------|----------|---------|
| 0        | Diurno   | 1er día |
| 1        | Diurno   | 2do día |
| 2        | Nocturno | 1er día |
| 3        | Nocturno | 2do día |
| 4        | Descanso | 1er día |
| 5        | Descanso | 2do día |

Fórmula: `(posición de referencia + días de diferencia) % 6`. Funciona también para fechas pasadas.

## Características

- Una sola página, diseño sobrio y responsive
- Modo oscuro automático
- Sin JavaScript, sin base de datos, sin dependencias aparte de Django
- El resultado queda en la URL, así que se puede guardar o compartir el enlace

## Estructura

```
├── manage.py
├── requirements.txt
├── config/            # configuración del proyecto
└── turnos/
    ├── logic.py       # cálculo del ciclo 2x2x2
    ├── views.py
    ├── urls.py
    └── templates/turnos/index.html
```

## Instalación

```bash
git clone <url-del-repositorio>
cd calculadora_turnos
pip install -r requirements.txt
python manage.py runserver
```

Abre `http://127.0.0.1:8000` en el navegador.

Para probarlo desde el celular en la misma red wifi:

```bash
python manage.py runserver 0.0.0.0:8000
```

y entra con la IP de tu computador, por ejemplo `http://192.168.1.X:8000`.

## Despliegue

Al no usar base de datos, se puede desplegar fácilmente en servicios como PythonAnywhere o Render. Antes de publicarlo:

- Cambia `ALLOWED_HOSTS` en `config/settings.py` por tu dominio.
- Define tu propio `SECRET_KEY` y desactiva `DEBUG`.

## Nota

El turno nocturno suele terminar en la mañana del día siguiente. La calculadora asigna cada turno al día en que **empieza**.
