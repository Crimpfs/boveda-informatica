# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 13:08:50 2025

@author: LENOVO

"""


import pulp
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import numpy as np

# Resolver modelo con restricciones adicionales
def resolver_modelo(restricciones):
    #prob = pulp.LpProblem("Z", pulp.LpMaximize)
    prob = pulp.LpProblem("Z", pulp.LpMaximize)

    # Variables con límites generales
   
    x1 = pulp.LpVariable("x1",  lowBound=0,   cat='Continuous')
    x2 = pulp.LpVariable("x2",  lowBound=0,   cat='Continuous')

    # Función objetivo
   
    prob += 4*x1 + 3*x2, "Función Objetivo Max"

          
    # Restricciones
    prob += x1 + 2*x2 >= 8, "Restricción 1"
    prob += 3*x1 + x2 >= 9, "Restricción 2"
    #prob += x1 + x2 <= 12, "Restricción 3"    972631137
    prob += 2*x1 + x2 <= 12, "Restricción 4"
    prob += x1 + 3*x2 <= 15, "Restricción 5"
      
    # Restricciones adicionales del algoritmo Branch and Bound
    for var, signo, valor in restricciones:
        if var == "x1":
            v = x1
        elif var == "x2":
            v = x2        
        else:
            continue

        if signo == "<=":
            prob += v <= valor
        elif signo == ">=":
            prob += v >= valor
    
    
    
    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

    if pulp.LpStatus[status] != 'Optimal':
        return status, None, None

    solucion = {v.name: v.varValue for v in prob.variables()}
    return status, pulp.value(prob.objective), solucion


# Verifica si la solución es entera
def es_entera(solucion):
    return all(v is not None and abs(v - round(v)) < 1e-5 for v in solucion.values())

# Devuelve la primera variable fraccional encontrada
def obtener_variable_fracc(solucion):
    for var, val in solucion.items():
        if val is not None and abs(val - round(val)) > 1e-5:
            return var, val
    return None, None

# Imprime información de un nodo
def mostrar_nodo(id_nodo, z, solucion, restricciones):
    print(f"\nNodo {id_nodo} procesado:")
    print(f" - Z = {z}")
    print(f" - ¿Es entera?: {'Sí' if es_entera(solucion) else 'No'}")
    print(" - Asignaciones:")
    for var, val in solucion.items():
        print(f"    {var} = {val:.2f}")
    if restricciones:
        print(f" - Restricciones adicionales: {restricciones}")

# Graficar el árbol del algoritmo B&B
def graficar_arbol(nodos):
    G = nx.DiGraph()
    for nodo in nodos:
        if nodo['z'] is not None:
            etiqueta = f"P:{nodo['id']}\nZ={nodo['z']:.1f}"
        else:
            etiqueta = f"ID:{nodo['id']}\nZ=?"
        G.add_node(nodo['id'], label=etiqueta)
        if nodo['padre'] is not None:
            G.add_edge(nodo['padre'], nodo['id'])

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_node_attributes(G, 'label')
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=1500, node_color='yellow', font_size=8, font_weight='bold')
   # plt.title("Árbol del algoritmo Branch and Bound")
    plt.show()

# Algoritmo Branch and Bound
def branch_and_bound():
    mejor_z = -float('inf')
    mejor_sol = None
    nodos = []
    cola = []
    id_nodo = 0

    restricciones_iniciales = []
    status, z, solucion = resolver_modelo(restricciones_iniciales)
    nodo_raiz = {'id': id_nodo, 'padre': None, 'z': z, 'solucion': solucion, 'restricciones': restricciones_iniciales}
    cola.append(nodo_raiz)
    nodos.append(nodo_raiz)
    id_nodo += 1

    while cola:
        nodo_actual = cola.pop(0)

        if nodo_actual['z'] is None or nodo_actual['z'] <= mejor_z:
            continue

        # Mostrar información del nodo en consola
        mostrar_nodo(nodo_actual['id'], nodo_actual['z'], nodo_actual['solucion'], nodo_actual['restricciones'])

        if es_entera(nodo_actual['solucion']):
            if nodo_actual['z'] > mejor_z:
                mejor_z = nodo_actual['z']
                mejor_sol = nodo_actual['solucion']
        else:
            var_fracc = obtener_variable_fracc(nodo_actual['solucion'])
            if var_fracc is None:
                continue
            var_name, valor = var_fracc
            floor_val = int(valor)
            ceil_val = floor_val + 1

            for nueva_restriccion in [(var_name, "<=", floor_val), (var_name, ">=", ceil_val)]:
                nuevas_restricciones = nodo_actual['restricciones'] + [nueva_restriccion]
                status, z, solucion = resolver_modelo(nuevas_restricciones)
                nuevo_nodo = {
                    'id': id_nodo,
                    'padre': nodo_actual['id'],
                    'z': z,
                    'solucion': solucion,
                    'restricciones': nuevas_restricciones
                }
                nodos.append(nuevo_nodo)
                cola.append(nuevo_nodo)
                id_nodo += 1

    print("\n======= Mejor solución entera =======")
    if mejor_sol is not None:
        print(f"Z = {mejor_z}")
        for var, val in mejor_sol.items():
            print(f" - {var} = {val}")
    else:
        print("No se encontró solución entera")

    graficar_arbol(nodos)

# Ejecutar
branch_and_bound()
