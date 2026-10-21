from datetime import date

from django.shortcuts import render

from .logic import opciones, turno_para, formatear_fecha, proximos_dias, MESES


def _fecha_desde(get, prefijo):
    try:
        return date(
            int(get[f"{prefijo}_a"]),
            int(get[f"{prefijo}_m"]),
            int(get[f"{prefijo}_d"]),
        )
    except (KeyError, ValueError):
        return None


def _partes(f):
    if f:
        return {"d": f.day, "m": f.month, "a": f.year}
    return {"d": "", "m": "", "a": ""}


def calculadora(request):
    hoy = date.today()
    fecha_ref = hoy
    fecha_obj = None
    indice_ref = 0
    contexto = {"opciones": opciones(), "meses": list(enumerate(MESES, 1))}

    if request.GET.get("obj_d"):
        fecha_ref = _fecha_desde(request.GET, "ref") or hoy
        fecha_obj = _fecha_desde(request.GET, "obj")
        try:
            indice_ref = int(request.GET.get("indice_ref", 0))
            if not 0 <= indice_ref <= 5:
                raise ValueError
        except ValueError:
            indice_ref = 0

        if fecha_obj is None:
            contexto["error"] = "La fecha consultada no es válida."
        else:
            turno, dia = turno_para(fecha_ref, indice_ref, fecha_obj)
            contexto["resultado"] = {
                "fecha": formatear_fecha(fecha_obj),
                "turno": turno,
                "dia": dia,
            }
            contexto["proximos"] = proximos_dias(fecha_ref, indice_ref, fecha_obj)

    contexto.update(ref=_partes(fecha_ref), obj=_partes(fecha_obj), indice_ref=indice_ref)
    return render(request, "turnos/index.html", contexto)