---
title: "Heurísticas y Metaheurísticas"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - unidad/1
  - domain/optimizacion-aproximada
aliases:
  - "Métodos Aproximados"
  - "Algoritmos Genéticos"
  - "Recocido Simulado"
sources:
  - "[[estrategias/Heurística.md]]"
  - "[[estrategias/metaheuristica.md]]"
---

# Heurísticas y Metaheurísticas

> [!NOTE] Definición
> Las **Heurísticas y Metaheurísticas** son métodos de resolución **aproximados** diseñados para problemas NP-Difíciles donde calcular la solución óptima exacta es computacionalmente imposible en tiempo razonable. Sacrifican la garantía de optimalidad del 100% a cambio de encontrar una solución "suficientemente buena" en tiempo polinómico.

---

## 🎯 Las 3 Preguntas Clave

1. **¿Es una estrategia rápida y eficiente?**
   - **Sí, sumamente rápida.** Su objetivo es proporcionar atajos computacionales basados en "reglas de oro", sentido común o analogías con la naturaleza para evitar la explosión combinatoria.
2. **¿Problemas Fáciles (P) o Difíciles (NP)?**
   - Pertenece a la **Clase NP / Problemas Intratables** (ej. Rutas de GPS para millones de nodos, problemas de horarios masivos, diseño de chips VLSI).
3. **¿Método Exacto o Aproximado?**
   - **Método Aproximado.** No garantiza el óptimo global, pero entrega soluciones prácticas de alta calidad operativas en milisegundos.

---

## 🔬 Diferencia entre Heurística y Metaheurística

```
[ Heurística Específica ] ⟵ Regla a medida para UN solo problema (ej. "Vecino más cercano" en TSP)
           ↑
[ Metaheurística ]       ⟵ Marco general independiente del problema (ej. Algoritmos Genéticos)
```

| Dimensión | Heurística Simple | Metaheurística |
| :--- | :--- | :--- |
| **Diseño** | Diseñada específicamente para un problema concreto | Marco algorítmico abstracto aplicable a múltiples problemas |
| **Atrapamiento en Óptimos Locales** | Muy propensa a estancarse en el primer óptimo local | Incorpora mecanismos para **escapar de óptimos locales** |
| **Principales Familias** | Reglas de prioridad, Greedy simple, Vecino más cercano | - **Inspiración Biológica**: Algoritmos Genéticos (GA), Colonia de Hormigas (ACO)<br>- **Inspiración Física**: Recocido Simulado (Simulated Annealing)<br>- **Basadas en Memoria**: Búsqueda Tabú (Tabu Search) |

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
- **Método Exacto Competidor**: [[wiki/conceptos/branch-and-bound|Branch and Bound (Ramificación y Poda)]]
