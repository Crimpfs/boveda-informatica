# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:55:11 2025

@author: LENOVO

Cadena de Suministro Multi-producto con Penalización por Demanda Insatisfecha
"""

import pulp


# Centros
centros = ['C1', 'C2']
capacidades = {'C1': 100, 'C2': 100}

# Clientes
clientes = ['CL1', 'CL2', 'CL3', 'CL4']

# Productos
productos = ['P1', 'P2']

# Costos de envío (centro, cliente, producto)
costos = {
    ('C1', 'CL1', 'P1'): 2, ('C1', 'CL2', 'P1'): 4, ('C1', 'CL3', 'P1'): 5, ('C1', 'CL4', 'P1'): 2,
    ('C1', 'CL1', 'P2'): 3, ('C1', 'CL2', 'P2'): 5, ('C1', 'CL3', 'P2'): 6, ('C1', 'CL4', 'P2'): 3,
    ('C2', 'CL1', 'P1'): 3, ('C2', 'CL2', 'P1'): 1, ('C2', 'CL3', 'P1'): 2, ('C2', 'CL4', 'P1'): 4,
    ('C2', 'CL1', 'P2'): 2, ('C2', 'CL2', 'P2'): 2, ('C2', 'CL3', 'P2'): 3, ('C2', 'CL4', 'P2'): 5,
}

# Demanda por cliente y producto
demanda = {
    ('CL1', 'P1'): 20, ('CL2', 'P1'): 30, ('CL3', 'P1'): 10, ('CL4', 'P1'): 25,
    ('CL1', 'P2'): 10, ('CL2', 'P2'): 15, ('CL3', 'P2'): 10, ('CL4', 'P2'): 10,
}

# Penalización por demanda no satisfecha
penalizacion = 10


# Crear el problema
prob = pulp.LpProblem("Cadena_Suministro_MultiProducto", pulp.LpMinimize)

# Variables de envío: x[c, cl, p]
x = pulp.LpVariable.dicts("x", ((c, cl, p) for c in centros for cl in clientes for p in productos),
                          lowBound=0, cat='Integer')

# Variables de demanda no satisfecha: u[cl, p]
u = pulp.LpVariable.dicts("u", ((cl, p) for cl in clientes for p in productos),
                          lowBound=0, cat='Integer')

# Función objetivo: minimizar costos de envío + penalización por demanda no satisfecha
prob += (
    pulp.lpSum(costos[c, cl, p] * x[c, cl, p] for c in centros for cl in clientes for p in productos) +
    pulp.lpSum(penalizacion * u[cl, p] for cl in clientes for p in productos)
)

# Restricciones de capacidad por centro
for c in centros:
    prob += (
        pulp.lpSum(x[c, cl, p] for cl in clientes for p in productos) <= capacidades[c],
        f"Capacidad_{c}"
    )

# Restricciones de demanda: lo recibido + insatisfecho = demanda
for cl in clientes:
    for p in productos:
        prob += (
            pulp.lpSum(x[c, cl, p] for c in centros) + u[cl, p] == demanda[cl, p],
            f"Demanda_{cl}_{p}"
        )

# Resolver
prob.solve()

# Resultados
print(f"Estado de optimización: {pulp.LpStatus[prob.status]}")
print("\n--- Distribución ---")
for c in centros:
    for cl in clientes:
        for p in productos:
            cantidad = pulp.value(x[c, cl, p])
            if cantidad > 0:
                print(f"{c} → {cl} ({p}): {cantidad}")


print("\n--- Demanda Insatisfecha ---")
for cl in clientes:
    for p in productos:
        insatisfecha = pulp.value(u[cl, p])
        if insatisfecha > 0:
            print(f"{cl} ({p}): {insatisfecha}")

print(f"\nCosto total: {pulp.value(prob.objective)}")
