# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 10:11:11 2025

@author: LENOVO
"""

import pulp
import networkx as nx
import matplotlib.pyplot as plt

# Conjuntos
trabajadores = ['T1', 'T2', 'T3']
tareas = ['A1', 'A2', 'A3']

# Costos de asignación
costos = {
    ('T1', 'A1'): 8, ('T1', 'A2'): 6, ('T1', 'A3'): 4,
    ('T2', 'A1'): 5, ('T2', 'A2'): 7, ('T2', 'A3'): 6,
    ('T3', 'A1'): 9, ('T3', 'A2'): 8, ('T3', 'A3'): 7
}

# Crear el problema
prob = pulp.LpProblem("Problema_Asignacion", pulp.LpMinimize)

# Variables binarias
x = pulp.LpVariable.dicts("x", [(t, a) for t in trabajadores for a in tareas], cat='Binary')

# Función objetivo
prob += pulp.lpSum(costos[t, a] * x[t, a] for t in trabajadores for a in tareas)

# Restricciones
for t in trabajadores:
    prob += pulp.lpSum(x[t, a] for a in tareas) == 1
    
for a in tareas:
    prob += pulp.lpSum(x[t, a] for t in trabajadores) == 1

# Resolver
prob.solve()

# Mostrar resultados
print(f"Estado: {pulp.LpStatus[prob.status]}")
print(f"Costo total: {pulp.value(prob.objective)}\n")
asignaciones = [(t, a) for t in trabajadores for a in tareas if pulp.value(x[t, a]) == 1]
print("Asignaciones óptimas:")
for t, a in asignaciones:
    print(f"{t} → {a} (costo: {costos[t, a]})")

# Crear grafo bipartito
G = nx.Graph()
G.add_nodes_from(trabajadores, bipartite=0)
G.add_nodes_from(tareas, bipartite=1)
G.add_edges_from(asignaciones)

# Posiciones para visualización bipartita
pos = {}
pos.update((t, (0, i)) for i, t in enumerate(trabajadores))
pos.update((a, (1, i)) for i, a in enumerate(tareas))

# Etiquetas de costo
edge_labels = {(t, a): f"${costos[t, a]}" for (t, a) in asignaciones}

# Dibujar
plt.figure(figsize=(8, 5))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="magenta", font_size=15, font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=asignaciones, width=3, edge_color="blue")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15, font_color="black")

plt.title("Asignaciones Óptimas con Costos", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
