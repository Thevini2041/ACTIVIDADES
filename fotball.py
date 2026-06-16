import tkinter as tk
from tkinter import ttk
import random


API_URL = "https://api.worldcup-data.com/groups"
API_KEY = "4833e303e6msh89862e9acf47b87p15ec07jsncb862453f583"


BG = "#0f172a"
CARD = "#1e293b"
TEXT = "#e2e8f0"
ACCENT = "#22c55e"
RED = "#ef4444"

# -------- GENERAR MUCHOS PARTIDOS --------
equipos = [
    "Barcelona", "Real Madrid", "PSG", "Bayern", "Liverpool",
    "Man City", "Juventus", "Inter", "Milan", "Chelsea",
    "Arsenal", "Dortmund", "Napoli", "Ajax", "Porto",
    "Benfica", "América", "Chivas", "Cruz Azul", "Pumas"
]

def generar_partidos():
    random.shuffle(equipos)
    partidos = []

    for i in range(0, len(equipos), 2):
        if i+1 < len(equipos):
            local = equipos[i]
            visitante = equipos[i+1]

            goles_local = random.randint(0, 4)
            goles_visitante = random.randint(0, 4)

            prob_local = random.randint(40, 60)
            prob_visitante = 100 - prob_local

            ganador = local if prob_local > prob_visitante else visitante

            partidos.append({
                "local": local,
                "visitante": visitante,
                "goles_local": goles_local,
                "goles_visitante": goles_visitante,
                "prob_local": prob_local,
                "prob_visitante": prob_visitante,
                "ganador": ganador
            })

    return partidos


def mostrar_partidos():
    limpiar()

    # 🔥 TUS GRUPOS REALES
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

    columnas = 3  # 🔥 3 grupos por fila

    for i, (nombre, lista) in enumerate(grupos.items()):
        fila = i // columnas
        col = i % columnas

        grupo_frame = tk.Frame(frame, bg=CARD, bd=1, relief="solid")
        grupo_frame.grid(row=fila, column=col + 1, padx=20, pady=20, sticky="n")

        # TÍTULO DEL GRUPO
        tk.Label(grupo_frame,
                 text=nombre,
                 bg=CARD, fg=ACCENT,
                 font=("Segoe UI", 13, "bold")).pack(pady=5)

        # ENCABEZADO
        tk.Label(grupo_frame,
                 text="Equipo",
                 bg=CARD, fg="#94a3b8",
                 font=("Segoe UI", 10)).pack()

        # LISTA DE EQUIPOS
        for pos, equipo in enumerate(lista, start=1):
            fila_equipo = tk.Frame(grupo_frame, bg=CARD)
            fila_equipo.pack(fill="x", padx=10, pady=2)

            tk.Label(fila_equipo,
                     text=f"{pos}",
                     width=3,
                     bg=CARD, fg=TEXT).pack(side="left")

            tk.Label(fila_equipo,
                     text=equipo,
                     bg=CARD, fg=TEXT,
                     font=("Segoe UI", 10, "bold")).pack(side="left")

    # 🔥 CENTRAR TODO
    total_cols = columnas + 2

    for c in range(total_cols):
        frame.grid_columnconfigure(c, weight=1)

    for i in range(columnas):
        frame.grid_columnconfigure(i + 1, weight=2)


def generar_eliminatorias():
    limpiar()

    # 🔥 MISMOS GRUPOS
    grupos = {
        "A": ["México", "Sudáfrica", "República de Corea", "República Checa"],
        "B": ["Canadá", "Bosnia y Herzegovina", "Catar", "Suiza"],
        "C": ["Brasil", "Marruecos", "Haití", "Escocia"],
        "D": ["Estados Unidos", "Paraguay", "Australia", "Turquía"],
        "E": ["Alemania", "Curazao", "Costa de Marfil", "Ecuador"],
        "F": ["Países Bajos", "Japón", "Suecia", "Túnez"],
        "G": ["Bélgica", "Egipto", "Irán", "Nueva Zelanda"],
        "H": ["España", "Cabo Verde", "Arabia Saudita", "Uruguay"],
        "I": ["Francia", "Senegal", "Irak", "Noruega"],
        "J": ["Argentina", "Argelia", "Austria", "Jordania"],
        "K": ["Portugal", "República Democrática del Congo", "Uzbekistán", "Colombia"],
        "L": ["Inglaterra", "Croacia", "Ghana", "Panamá"],
    }

    # 🔥 CLASIFICAN 2 POR GRUPO (aleatorio)
    clasificados = []

    for grupo in grupos.values():
        random.shuffle(grupo)
        clasificados.append(grupo[0])
        clasificados.append(grupo[1])

    # 🔥 FUNCION PARA CREAR PARTIDOS
    def jugar_ronda(equipos):
        ganadores = []
        partidos = []

        for i in range(0, len(equipos), 2):
            if i+1 < len(equipos):
                e1 = equipos[i]
                e2 = equipos[i+1]

                g1 = random.randint(0, 4)
                g2 = random.randint(0, 4)

                if g1 == g2:
                    g1 += 1  # evitar empate

                ganador = e1 if g1 > g2 else e2

                partidos.append((e1, g1, g2, e2, ganador))
                ganadores.append(ganador)

        return ganadores, partidos

    rondas_nombres = ["Octavos", "Cuartos", "Semifinal", "Final"]
    equipos_actuales = clasificados

    columnas = len(rondas_nombres)

    # 🔥 MOSTRAR RONDAS
    for col, nombre_ronda in enumerate(rondas_nombres):

        if len(equipos_actuales) < 2:
            break

        equipos_actuales, partidos = jugar_ronda(equipos_actuales)

        # TÍTULO
        tk.Label(frame,
                 text=nombre_ronda,
                 bg=BG, fg=ACCENT,
                 font=("Segoe UI", 14, "bold")).grid(row=0, column=col+1, pady=10)

        for fila, p in enumerate(partidos):
            e1, g1, g2, e2, ganador = p

            card = tk.Frame(frame, bg=CARD, bd=1, relief="solid")
            card.grid(row=fila+1, column=col+1, padx=15, pady=10)

            tk.Label(card, text=e1,
                     bg=CARD, fg=TEXT,
                     font=("Segoe UI", 10, "bold")).pack()

            tk.Label(card,
                     text=f"{g1} - {g2}",
                     bg=CARD, fg=ACCENT,
                     font=("Segoe UI", 12, "bold")).pack()

            tk.Label(card, text=e2,
                     bg=CARD, fg=TEXT,
                     font=("Segoe UI", 10, "bold")).pack()

            tk.Label(card,
                     text=f"Ganador: {ganador}",
                     bg=CARD, fg=RED,
                     font=("Segoe UI", 9, "bold")).pack(pady=3)

    # 🏆 CAMPEÓN
    if equipos_actuales:
        tk.Label(frame,
                 text=f"🏆 CAMPEÓN: {equipos_actuales[0]}",
                 bg=BG, fg="gold",
                 font=("Segoe UI", 18, "bold")).grid(row=20, column=2, columnspan=2, pady=20)

    # 🔥 CENTRAR
    total_cols = columnas + 2
    for c in range(total_cols):
        frame.grid_columnconfigure(c, weight=1)

    for i in range(columnas):
        frame.grid_columnconfigure(i + 1, weight=2)

# -------- LIMPIAR --------
def limpiar():
    for w in frame.winfo_children():
        w.destroy()


# -------- UI --------
root = tk.Tk()
root.title("Predicciones PRO ⚽")
root.geometry("700x600")
root.configure(bg=BG)

titulo = tk.Label(root, text="⚽ SISTEMA DE PREDICCIONES",
                  bg=BG, fg=TEXT,
                  font=("Segoe UI", 20, "bold"))
titulo.pack(pady=15)

botones = tk.Frame(root, bg=BG)
botones.pack()

tk.Button(botones, text="Generar Partidos",
          command=mostrar_partidos,
          bg=ACCENT, fg="black",
          font=("Segoe UI", 11, "bold")).pack(side="left", padx=10)

tk.Button(botones, text="Ver Eliminatorias",
          command=generar_eliminatorias,
          bg="#38bdf8", fg="black",
          font=("Segoe UI", 11, "bold")).pack(side="left", padx=10)

# SCROLL
canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
scroll = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas, bg=BG)

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll.set)

canvas.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

partidos_actuales = []

root.mainloop()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
