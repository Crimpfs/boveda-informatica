---
title: "Teoría de Complejidad: Problemas Fáciles (P) vs. Difíciles (NP)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - domain/complejidad-computacional
aliases:
  - "Clase P vs NP"
  - "Problemas Fáciles y Difíciles"
sources:
  - "[[estrategias/problemas faciles y dificiles.md]]"
---

# Teoría de Complejidad: Problemas Fáciles (P) vs. Difíciles (NP)

> [!NOTE] Fundamento
> La clasificación de problemas según su complejidad computacional determina si una computadora puede resolverlos de forma exacta en tiempo útil (polinómico) o si requiere podas exhaustivas y métodos de aproximación.

---

## 🟢 Problemas Fáciles (Clase P - Tiempo Polinómico)

Un problema es **fácil (P)** cuando existe un algoritmo determinista que encuentra la **solución óptima en tiempo polinómico**: $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$, $O(n^3)$, etc.
- **Comportamiento**: La computadora resuelve instancias grandes de datos rápidamente.
- **Estrategias Exactas para Clase P**:
  - [[wiki/conceptos/dividir-para-vencer|Dividir para Vencer]] (ej. MergeSort, Búsqueda Binaria).
  - [[wiki/conceptos/programacion-dinamica|Programación Dinámica]] (ej. Fibonacci, Distancia de Edición, Alineamiento de Secuencias).
  - [[wiki/conceptos/algoritmos-voraces|Algoritmos Voraces]] (ej. Árbol de Expansión Mínima de Kruskal/Prim, Dijkstra).

---

## 🔴 Problemas Difíciles (Clase NP-Completo / NP-Hard)

Un problema es **difícil (NP-Hard)** cuando **no se conoce ningún algoritmo que lo resuelva en tiempo polinómico** en el peor de los casos. Su espacio de soluciones crece de forma exponencial ($O(2^n)$) o factorial ($O(n!)$).
- **Comportamiento**: Al superar 30 a 50 elementos de entrada, la computadora colapsa si intenta explorar todas las opciones a ciegas.
- **Estrategias para Problemas Difíciles**:
  1. **Métodos Exactos (Garantizan solución 100% óptima pero son costosos)**:
     - [[wiki/conceptos/fuerza-bruta|Fuerza Bruta]]: Explora todo el universo sin excepción.
     - [[wiki/conceptos/backtracking|Backtracking]]: Explora en profundidad podando ramas inválidas.
     - [[wiki/conceptos/branch-and-bound|Branch and Bound (Ramificación y Poda)]]: Explora podando mediante cotas matemáticas.
  2. **Métodos Aproximados (Renuncian a la perfección para ganar velocidad)**:
     - [[wiki/conceptos/heuristica-y-metaheuristica|Heurísticas Específicas]]: Reglas prácticas de decisión rápida.
     - [[wiki/conceptos/heuristica-y-metaheuristica|Metaheurísticas]]: Algoritmos Genéticos, Recocido Simulado, Búsqueda Tabú.
     - [[wiki/conceptos/algoritmos-voraces|Algoritmos Voraces Heurísticos]]: Decisiones codiciosas sin garantía de óptimo global.

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
