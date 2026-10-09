# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 12:26:20 2025

@author: LENOVO
"""

import pulp

# Crear el problema
model = pulp.LpProblem("Asignacion_de_Cultivos", pulp.LpMaximize)

# Variables de decisión
x1 = pulp.LpVariable("Trigo_ha", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Maiz_ha", lowBound=0, cat='Continuous')

# Función objetivo
model += 500 * x1 + 650 * x2, "Ganancia_Total"

# Restricciones
model += x1 + x2 <= 100, "Superficie_Total"
model += 90 * x1 + 120 * x2 <= 12000, "Disponibilidad_Agua"
model += 150 * x1 + 230 * x2 <= 20000, "Presupuesto"

# Resolver
model.solve()

# Resultados
print("Estado:", pulp.LpStatus[model.status])
print(f"Hectáreas de Trigo: {x1.varValue:.2f}")
print(f"Hectáreas de Maíz: {x2.varValue:.2f}")
print(f"Ganancia Total: ${pulp.value(model.objective):,.2f}")
