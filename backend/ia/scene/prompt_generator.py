def generar_prompt(escena):

    return f"""
Videoclip cinematográfico.

Escena:
{escena['tipo']}

Plano:
{escena['plano']}

Cámara:
{escena['camara']['camara']}

Movimiento:
{escena['camara']['movimiento']}

Descripción:
{escena['descripcion']}

Lugar:
{escena["ambiente"]["lugar"]}

Hora:
{escena["ambiente"]["hora"]}

Clima:
{escena["ambiente"]["clima"]}

Personaje:

Ropa:
{escena["personaje"]["ropa"]}

Expresión:
{escena["personaje"]["expresion"]}

Edad:
{escena["personaje"]["edad"]}

Ultra realistic.
8K.
Professional lighting.
Highly detailed.
"""