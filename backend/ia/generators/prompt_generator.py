def generar_prompt(escena):

    emocion = escena.get("emocion", "Épica")

    return f"""
Videoclip cinematográfico.

Emoción principal:
{emocion}

Tipo:
{escena['tipo']}

Plano:
{escena['plano']}

Cámara:
{escena['camara']['camara']}

Movimiento:
{escena['camara']['movimiento']}

Descripción:
{escena['descripcion']}

Paleta de color:
{escena['estilo']['paleta']}

Iluminación:
{escena['estilo']['iluminacion']}

Efectos:
{escena['estilo']['efectos']}

Ultra realistic.
Movie quality.
8K.
Highly detailed.
Professional cinematography.
Dynamic lighting.
"""