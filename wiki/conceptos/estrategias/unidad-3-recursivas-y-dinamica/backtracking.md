---
title: "Vuelta Atrás (Backtracking)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - unidad/3
  - domain/busqueda-exhaustiva
aliases:
  - "Backtracking"
  - "Retroceso Recursivo"
sources:
  - "[[estrategias/backtracking.md]]"
---

# Vuelta Atrás (Backtracking)

> [!NOTE] Definición
> **Backtracking** es un método algorítmico **exacto** para resolver problemas de **Satisfacción de Restricciones (CSP)** mediante la exploración sistemática de un árbol de decisiones en profundidad (DFS), abandonando una rama tan pronto como se determina que no puede conducir a una solución válida.

---

## 🎯 Las 3 Preguntas Clave

1. **¿Es una estrategia rápida y eficiente?**
   - Es un refinamiento inteligente de la Fuerza Bruta. Su peor caso sigue siendo exponencial ($O(b^d)$), pero la poda temprana de ramas inconsistentes ahorra enormes cantidades de tiempo.
2. **¿Problemas Fáciles (P) o Difíciles (NP)?**
   - Pertenece a **Problemas Difíciles / Clase NP** (Problema de las N-Reinas, Sudoku, Coloreo de Grafos, Salida de Laberintos).
3. **¿Método Exacto o Aproximado?**
   - **Método Exacto.** Si existe una solución válida, la encontrará sin falta.

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
- **Evolución para Optimización**: [[wiki/conceptos/branch-and-bound|Branch and Bound]]
