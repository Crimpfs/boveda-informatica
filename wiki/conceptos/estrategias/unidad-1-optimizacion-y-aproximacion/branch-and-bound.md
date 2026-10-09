---
title: "Ramificación y Poda (Branch and Bound)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - unidad/1
  - domain/optimizacion
aliases:
  - "Branch and Bound"
  - "B&B"
  - "Ramificación y Acotación"
sources:
  - "[[estrategias/brand and baund.md]]"
---

# Ramificación y Poda (Branch and Bound)

> [!NOTE] Definición
> **Branch and Bound** es un método algorítmico **exacto** diseñado específicamente para resolver problemas de **Optimización Combinatoria NP-Difíciles** (minimización o maximización de una función objetivo) mediante la exploración sistemática de un árbol de soluciones acotado por límites matemáticos.

---

## 🎯 Las 3 Preguntas Clave

1. **¿Es una estrategia rápida y eficiente?**
   - **No es rápida en términos absolutos**, pero es la estrategia exacta más sofisticada para problemas intratables. En el peor de los casos es exponencial ($O(2^n)$ o $O(n!)$), pero en la práctica descarta el 90-99% del árbol gracias a las podas.
2. **¿Problemas Fáciles (P) o Difíciles (NP)?**
   - Pertenece a la **Clase NP / Problemas Difíciles** (Problema del Viajante TSP, Mochila 0/1, Asignación de Tareas Cuadrática).
3. **¿Método Exacto o Aproximado?**
   - **Método Exacto (100% garantía de optimalidad)**. Las podas no son intuitivas; se sustentan en una cota matemática rigurosa.

---

## ✂️ El Mecanismo de Poda (Bounding Function)

```
                     [ Nodo Raíz ]
                    /             \
            [ Rama A ]          [ Rama B ]
          (Cota = $150)        (Cota = $80)  ⟵ ¡PODA! (Si buscamos Max y ya tenemos $120)
            /        \             ❌ (Se descartan millones de nodos hijos)
      [ Sol. $140 ] [ Sol. $150 ] 
```

1. **Ramificación (Branch)**: Divide el espacio de soluciones en subconjuntos disjuntos (nodos hijos).
2. **Acotación (Bound)**: En cada nodo $x$, calcula un pronóstico matemático:
   - En **Maximización**: Calcula una *cota superior* (Upper Bound). Si $Cota(x) \le MejorSolucionActual$, podar subárbol.
   - En **Minimización**: Calcula una *cota inferior* (Lower Bound). Si $Cota(x) \ge MejorSolucionActual$, podar subárbol.
3. **Estrategia de Selección de Nodos**:
   - **FIFO** (Cola / Búsqueda en Anchura - BFS).
   - **LIFO** (Pila / Búsqueda en Profundidad - DFS).
   - **LC (Least Cost / Best-First)**: Cola de prioridad explorando siempre el nodo con cota más prometedora.

---

## ⚖️ Branch and Bound vs. Backtracking

| Característica | Backtracking | Branch and Bound |
| :--- | :--- | :--- |
| **Propósito Principal** | Satisfacción de Restricciones (encontrar cualquier solución válida) | Optimización (maximizar beneficio o minimizar costo) |
| **Exploración de Árbol** | Típicamente DFS (Profundidad) | BFS o Cola de Prioridad (Best-First) |
| **Criterio de Descarte** | Violación de una restricción booleana | Cota matemática peor que la mejor cota conocida |
| **Memoria Requerida** | Muy baja ($O(altura)$) | Alta ($O(ancho)$ por la lista de nodos vivos) |

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
- **Alternativa Aproximada**: [[wiki/conceptos/heuristica-y-metaheuristica|Heurísticas y Metaheurísticas]]
