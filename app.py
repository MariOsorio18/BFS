from flask import Flask, render_template, request, jsonify
from collections import deque

app = Flask(__name__)

# =========================
# CLASE NODO (tu código base)
# =========================
class Nodo:
    def __init__(self, datos, padre=None): 
        self.datos = datos
        self.hijos = []
        self.padre = padre  

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

# =========================
# BFS
# =========================
def bfs(inicio, objetivo):
    cola = deque()
    visitados = set()
    
    cola.append((inicio, [inicio]))  # (estado, camino)

    while cola:
        actual, camino = cola.popleft()

        if actual == objetivo:
            return camino

        visitados.add(tuple(actual))

        # Generar vecinos (intercambiando posiciones)
        for i in range(len(actual) - 1):
            nuevo = actual[:]
            nuevo[i], nuevo[i+1] = nuevo[i+1], nuevo[i]

            if tuple(nuevo) not in visitados:
                cola.append((nuevo, camino + [nuevo]))

    return []

# =========================
# RUTAS
# =========================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bfs", methods=["POST"])
def ejecutar_bfs():
    data = request.get_json()

    inicio = data["inicio"]
    objetivo = data["objetivo"]

    resultado = bfs(inicio, objetivo)

    return jsonify(resultado)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(debug=True)