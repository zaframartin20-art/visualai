def generar_plano(tipo):

    planos = {
        "intro": "Plano general",
        "build": "Travelling frontal",
        "drop": "Plano dinámico",
        "break": "Primer plano"
    }

    return planos.get(tipo, "Plano general")