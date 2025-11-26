from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora Sani</title>
    <style>
        body {
            background: #eef1f5;
            font-family: Arial;
            display: flex;
            justify-content: center;
            padding-top: 50px;
        }
        .card {
            background: white;
            width: 380px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 0 15px #0003;
        }
        button {
            margin-top: 10px;
            padding: 12px;
            border: none;
            background: #4CAF50;
            color: white;
            width: 100%;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover { background: #45a049; }
        input, select {
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        .resultado {
            margin-top: 20px;
            font-size: 22px;
            font-weight: bold;
            color: #333;
        }
        .ia-box {
            margin-top: 20px;
            padding: 15px;
            background: #dde7ff;
            border-radius: 8px;
        }
    </style>
</head>
<body>

<div class="card">
    <h2>Estefany</h2>

    <form method="POST">
        <label>Número 1:</label>
        <input type="number" step="any" name="n1" required>

        <label>Número 2:</label>
        <input type="number" step="any" name="n2" required>

        <label>Operación:</label>
        <select name="op">
            <option value="suma">Suma (+)</option>
            <option value="resta">Resta (-)</option>
        </select>

        <button type="submit">Calcular</button>
    </form>

    {% if resultado is not none %}
        <p class="resultado">Resultado: {{ resultado }}</p>
    {% endif %}

    <div class="ia-box">
        <h4>IA Mini:</h4>
        <p>{{ frase_ia }}</p>
    </div>
</div>

</body>
</html>
"""

FRASES = [
    "Sani: ¡Vas excelente!",
    "Tu pipeline CI/CD funciona perfecto.",
    "El despliegue será exitoso.",
    "Eres una crack en DevOps."
]

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        op = request.form["op"]

        if op == "suma":
            resultado = n1 + n2
        else:
            resultado = n1 - n2

    frase = random.choice(FRASES)
    return render_template_string(HTML, resultado=resultado, frase_ia=frase)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
