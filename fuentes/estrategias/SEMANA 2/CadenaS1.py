# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 20:44:42 2025

@author: LENOVO

Cadena de suministro simple
"""

import pulp
import matplotlib.pyplot as plt
import networkx as nx

# Productos
productos = ['Producto_1', 'Producto_2']

# Nodos == Conjuntos
planta = 'P'
centros = ['CD1', 'CD2']
clientes = ['C1', 'C2', 'C3', 'C4']
nodos = [planta] + centros + clientes

# Áreas de cobertura: CD -> lista de clientes
cobertura = {
    'CD1': ['C1', 'C2'],
    'CD2': ['C3', 'C4']
}

# Capacidad total de cada CD
capacidad_cd = {'CD1': 30, 'CD2': 25}

# Demanda por cliente y producto
demanda = {
    ('C1', 'Producto_1'): 5,
    ('C1', 'Producto_2'): 3,
    ('C2', 'Producto_1'): 4,
    ('C2', 'Producto_2'): 6,
    ('C3', 'Producto_1'): 8,
    ('C3', 'Producto_2'): 2,
    ('C4', 'Producto_1'): 6,
    ('C4', 'Producto_2'): 4,
}

# Crear el modelo
model = pulp.LpProblem("Flujo_Multibien_Cobertura", pulp.LpMaximize)

# Variables de flujo por producto (P -> CD -> Cliente)
flow_vars = pulp.LpVariable.dicts(
    "Flow",
    [(p, cd, cli) for p in productos for cd in centros for cli in cobertura[cd]],
    lowBound=0, cat='Continuous')

# Función objetivo: satisfacer la mayor demanda posible
model += pulp.lpSum(flow_vars[(p, cd, cli)] for (p, cd, cli) in flow_vars), "Total_Productos_Entregados"

# Restricciones de capacidad de los centros de distribución
for cd in centros:
    model += pulp.lpSum(flow_vars[(p, cd, cli)] for p in productos for cli in cobertura[cd]) <= capacidad_cd[cd], f"Capacidad_{cd}"

# Restricciones de demanda máxima por cliente y producto
for (cli, prod), dem in demanda.items():
    centros_que_cubren = [cd for cd in centros if cli in cobertura[cd]]
    model += pulp.lpSum(flow_vars[(prod, cd, cli)] for cd in centros_que_cubren) <= dem, f"Demanda_{cli}_{prod}"

# Resolver
model.solve()

# Resultados
print("Estado de la solución:", pulp.LpStatus[model.status])
print("Total de bienes entregados:", pulp.value(model.objective))
print("\nFlujo de productos:")
for (p, cd, cli), var in flow_vars.items():
    if var.varValue > 0:
        print(f"  {p}: {cd} -> {cli} = {var.varValue}")

#  Visualización de la red
G = nx.DiGraph()

# Agregar nodos
G.add_node(planta, layer=0)
for cd in centros:
    G.add_node(cd, layer=1)
for cli in clientes:
    G.add_node(cli, layer=2)

# Posiciones en el gráfico
pos = {
    'P': (0, 2),
    'CD1': (-1, 1),
    'CD2': (1, 1),
    'C1': (-2, 0),
    'C2': (-1, 0),
    'C3': (1, 0),
    'C4': (2, 0)
}

# Agregar arcos y etiquetas de flujo
edge_labels = {}
for (p, cd, cli), var in flow_vars.items():
    flow = var.varValue
    if flow > 0:
        G.add_edge(cd, cli)
        edge_labels[(cd, cli)] = edge_labels.get((cd, cli), "") + f"{p}:{flow} "

        if not G.has_edge(planta, cd):
            G.add_edge(planta, cd)

# Dibujar el grafo
plt.figure(figsize=(10,6))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
plt.title("Red de Suministro con Múltiples Bienes y Áreas de Cobertura")
plt.axis('off')
plt.tight_layout()
plt.show()
