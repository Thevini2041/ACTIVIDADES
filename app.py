from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 🔥 GRUPOS
grupos = {
    "Grupo A": ["México", "Sudáfrica", "República de Corea", "República Checa"],
    "Grupo B": ["Canadá", "Bosnia y Herzegovina", "Catar", "Suiza"],
    "Grupo C": ["Brasil", "Marruecos", "Haití", "Escocia"],
    "Grupo D": ["Estados Unidos", "Paraguay", "Australia", "Turquía"],
    "Grupo E": ["Alemania", "Curazao", "Costa de Marfil", "Ecuador"],
    "Grupo F": ["Países Bajos", "Japón", "Suecia", "Túnez"],
    "Grupo G": ["Bélgica", "Egipto", "Irán", "Nueva Zelanda"],
    "Grupo H": ["España", "Cabo Verde", "Arabia Saudita", "Uruguay"],
    "Grupo I": ["Francia", "Senegal", "Irak", "Noruega"],
    "Grupo J": ["Argentina", "Argelia", "Austria", "Jordania"],
    "Grupo K": ["Portugal", "República Democrática del Congo", "Uzbekistán", "Colombia"],
    "Grupo L": ["Inglaterra", "Croacia", "Ghana", "Panamá"],
}


@app.route("/")
def home():
    return render_template("index.html", grupos=grupos)


# 🔥 GENERAR ELIMINATORIAS
@app.route("/eliminatorias")
def eliminatorias():
    clasificados = []

    # 2 por grupo
    for grupo in grupos.values():
        temp = grupo.copy()
        random.shuffle(temp)
        clasificados.append(temp[0])
        clasificados.append(temp[1])

    def jugar(equipos):
        ganadores = []
        partidos = []

        for i in range(0, len(equipos), 2):
            if i+1 < len(equipos):
                e1 = equipos[i]
                e2 = equipos[i+1]

                g1 = random.randint(0, 4)
                g2 = random.randint(0, 4)

                if g1 == g2:
                    g1 += 1

                ganador = e1 if g1 > g2 else e2

                partidos.append({
                    "e1": e1,
                    "g1": g1,
                    "g2": g2,
                    "e2": e2,
                    "ganador": ganador
                })

                ganadores.append(ganador)

        return ganadores, partidos

    rondas = ["Octavos", "Cuartos", "Semifinal", "Final"]
    resultado = {}

    equipos_actuales = clasificados

    for ronda in rondas:
        equipos_actuales, partidos = jugar(equipos_actuales)
        resultado[ronda] = partidos

        if len(equipos_actuales) <= 1:
            break

    campeon = equipos_actuales[0] if equipos_actuales else "N/A"

    return jsonify({
        "rondas": resultado,
        "campeon": campeon
    })


if __name__ == "__main__":
    app.run(debug=True)