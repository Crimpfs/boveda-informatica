# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 12:53:27 2025

@author: LENOVO
"""

import pulp

# Crear el modelo
model = pulp.LpProblem("Asignacion_de_Cultivos_Sostenible", pulp.LpMaximize)

# Variables de decisión
x1 = pulp.LpVariable("Trigo_ha", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Maiz_ha", lowBound=0, cat='Continuous')

# Parámetros
ganancia = {x1: 500, x2: 650}
agua = {x1: 90, x2: 120}
costo = {x1: 150, x2: 230}
co2 = {x1: 150, x2: 200}

# Función objetivo
model += ganancia[x1] * x1 + ganancia[x2] * x2, "Ganancia_Total"

# Restricciones
model += x1 + x2 <= 100, "Superficie_Total"
model += agua[x1] * x1 + agua[x2] * x2 <= 12000, "Disponibilidad_Agua"
model += costo[x1] * x1 + costo[x2] * x2 <= 20000, "Presupuesto"
model += co2[x1] * x1 + co2[x2] * x2 <= 16000, "Limite_CO2"

# Resolver
model.solve()

# Resultados
print("Estado:", pulp.LpStatus[model.status])
print(f"Hectáreas de Trigo: {x1.varValue:.2f}")
print(f"Hectáreas de Maíz: {x2.varValue:.2f}")
print(f"Ganancia Total: ${pulp.value(model.objective):,.2f}")
total_emisiones = co2[x1]*x1.varValue + co2[x2]*x2.varValue
print(f"Emisiones Totales: {total_emisiones:.2f} kg CO₂")
