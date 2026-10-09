# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 21:30:43 2025

@author: LENOVO

Cadena de suministro con penalizaciones y ventana de tiempo
"""

import pulp
import matplotlib.pyplot as plt
import networkx as nx

# Productos
productos = ['Producto_1', 'Producto_2']

# Nodos
planta = 'P'
centros = ['CD1', 'CD2']
clientes = ['C1', 'C2', 'C3', 'C4']

# Cobertura geográfica
cobertura = {
    'CD1': ['C1', 'C2'],
    'CD2': ['C3', 'C4']
}

# Capacidad de los centros de distribución
capacidad_cd = {'CD1': 30, 'CD2': 25}

# Demanda por cliente y producto
demanda = {
    ('C1', 'Producto_1'): 5, ('C1', 'Producto_2'): 3,
    ('C2', 'Producto_1'): 4, ('C2', 'Producto_2'): 6,
    ('C3', 'Producto_1'): 8, ('C3', 'Producto_2'): 2,
    ('C4', 'Producto_1'): 6, ('C4', 'Producto_2'): 4,
}

# Penalización por no entrega
penalizacion = {
    (cli, prod): 10 for cli in clientes for prod in productos
}

# Ventanas de tiempo por cliente (en horas)
ventanas_tiempo = {
    'C1': (8, 12),
    'C2': (9, 14),
    'C3': (10, 16),
    'C4': (7, 11),
}

# Tiempo estimado de entrega (CD -> Cliente)
tiempo_entrega = {
    ('CD1', 'C1'): 9,
    ('CD1', 'C2'): 13,
    ('CD2', 'C3'): 11,
    ('CD2', 'C4'): 6,  # fuera de ventana
}

# Función segura para verificar ventana de tiempo
def in_window(cd, cli):
    if (cd, cli) not in tiempo_entrega:
        return False
    t = tiempo_entrega[(cd, cli)]
    return ventanas_tiempo[cli][0] <= t <= ventanas_tiempo[cli][1]

# Crear modelo
model = pulp.LpProblem("Flujo_Multibien_Tiempo_Penalizaciones", pulp.LpMaximize)

# Variables
flow_vars = pulp.LpVariable.dicts(
    "Flow",
    [(p, cd, cli) for p in productos for cd in centros for cli in cobertura[cd]],
    lowBound=0,
    cat='Continuous'
)
s_vars = pulp.LpVariable.dicts(
    "Shortage",
    [(cli, p) for cli in clientes for p in productos],
    lowBound=0,
    cat='Continuous'
)

# Función objetivo
model += (
    pulp.lpSum(flow_vars[(p, cd, cli)] for (p, cd, cli) in flow_vars if in_window(cd, cli)) -
    pulp.lpSum(penalizacion[(cli, p)] * s_vars[(cli, p)] for cli in clientes for p in productos)
), "Total_Utilidad_Neta"

# Restricción de capacidad de CD
for cd in centros:
    model += (
        pulp.lpSum(flow_vars[(p, cd, cli)] for p in productos for cli in cobertura[cd] if in_window(cd, cli))
        <= capacidad_cd[cd], f"Capacidad_{cd}"
    )

# Restricción de balance demanda
for cli in clientes:
    for p in productos:
        cds_cubren = [cd for cd in centros if cli in cobertura[cd] and in_window(cd, cli)]
        model += (
            pulp.lpSum(flow_vars[(p, cd, cli)] for cd in cds_cubren) + s_vars[(cli, p)] == demanda[(cli, p)],
            f"Demanda_{cli}_{p}"
        )

# Resolver modelo
model.solve()

# Validar si la solución es óptima
if pulp.LpStatus[model.status] != 'Optimal':
    print(" No se encontró una solución óptima o factible.")
else:
    print(" Estado de la solución:", pulp.LpStatus[model.status])
    print(" Utilidad neta total:", pulp.value(model.objective))

    print("\n Flujos entregados:")
    for (p, cd, cli), var in flow_vars.items():
        if var.varValue and var.varValue > 0:
            print(f"  {p}: {cd} -> {cli} = {var.varValue}")

    print("\n No entregado (penalizado):")
    for (cli, p), var in s_vars.items():
        if var.varValue and var.varValue > 0:
            print(f"  {cli} - {p}: {var.varValue} unidades no entregadas")

    # Visualización de la red
    G = nx.DiGraph()
    G.add_node(planta, layer=0)
    for cd in centros:
        G.add_node(cd, layer=1)
    for cli in clientes:
        G.add_node(cli, layer=2)

    pos = {
        'P': (0, 2),
        'CD1': (-1, 1), 'CD2': (1, 1),
        'C1': (-2, 0), 'C2': (-1, 0), 'C3': (1, 0), 'C4': (2, 0)
    }

    edge_labels = {}
    for (p, cd, cli), var in flow_vars.items():
        if var.varValue and var.varValue > 0:
            G.add_edge(cd, cli)
            key = (cd, cli)
            label = f"{p}:{var.varValue:.0f} "
            edge_labels[key] = edge_labels.get(key, '') + label
            if not G.has_edge(planta, cd):
                G.add_edge(planta, cd)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
    plt.title("Cadena de Suministro con Penalizaciones y Ventanas de Tiempo")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
