from datetime import date

from django.shortcuts import render

from .logic import opciones, turno_para, formatear_fecha, proximos_dias


def _parse(valor):
    try:
        return date.fromisoformat(valor)
    except (TypeError, ValueError):
        return None


def calculadora(request):
    hoy = date.today()
    contexto = {
        "opciones": opciones(),
        "fecha_ref": hoy.isoformat(),
        "indice_ref": 0,
        "fecha_obj": "",
    }

    if request.GET.get("fecha_obj"):
        fecha_ref = _parse(request.GET.get("fecha_ref")) or hoy
        fecha_obj = _parse(request.GET.get("fecha_obj"))
        try:
            indice_ref = int(request.GET.get("indice_ref", 0))
            if not 0 <= indice_ref <= 5:
                raise ValueError
        except ValueError:
            indice_ref = 0

        contexto.update(
            fecha_ref=fecha_ref.isoformat(),
            indice_ref=indice_ref,
            fecha_obj=request.GET.get("fecha_obj"),
        )

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

    return render(request, "turnos/index.html", contexto)
