---
title: "Taxonomía Maestra: Mapa de Estrategias Algorítmicas"
type: synthesis
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/sintesis
  - curso/estrategias-algoritmicas
  - domain/algoritmos-optimizacion
aliases:
  - Mapa de Estrategias
  - Matriz P vs NP Algorítmica
sources:
---

# ♟️ Mapa Maestro: Taxonomía de Estrategias Algorítmicas

> [!IMPORTANT] Clave para el Éxito en Estrategias Algorítmicas (2026-I)
> Para dominar los exámenes del **Dr. José A. Rodriguez Melquiades**, ante cualquier problema debes responder inmediatamente 3 preguntas fundamentales:
> 1. **¿A qué clase de complejidad pertenece el problema?** (Fácil / Clase P vs. Difícil / Clase NP-Hard).
> 2. **¿Qué tipo de solución requiere?** (Método Exacto / Óptimo Global vs. Método Aproximado / Heurístico).
> 3. **¿Cuál es la estrategia algorítmica óptima y su cota de complejidad?** ($O(n \log n)$, $O(n^k)$, $O(2^n)$, $O(n!)$).

---

## 📊 Matriz Taxonómica Completa

| Clase de Problema | Naturaleza de Solución | Estrategia Algorítmica | Mecanismo Central | Complejidad Típica | Garantía Óptima |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Fáciles (Clase P)** | **Exacto** | **[[wiki/conceptos/dividir-para-vencer\|Dividir para Vencer]]** | Descomposición en subproblemas disjuntos independientes. | $O(n \log n)$ | ✅ 100% |
| **Fáciles (Clase P)** | **Exacto** | **[[wiki/conceptos/programacion-dinamica\|Programación Dinámica]]** | Subproblemas superpuestos + Memorización / Tabulación. | $O(n^2)$ a $O(n^3)$ | ✅ 100% |
| **Fáciles / Casos Especiales** | **Exacto** | **[[wiki/conceptos/algoritmos-voraces\|Algoritmos Voraces (Greedy)]]** | Elección localmente óptima con subestructura óptima (ej. Kruskal, Huffman). | $O(n \log n)$ | ✅ 100% *(solo si cumple propiedad voraz)* |
| **Difíciles (Clase NP)** | **Exacto** | **[[wiki/conceptos/fuerza-bruta\|Fuerza Bruta (Exhaustiva)]]** | Generación y prueba de todo el espacio de soluciones. | $O(2^n)$ o $O(n!)$ | ✅ 100% |
| **Difíciles (Clase NP)** | **Exacto** | **[[wiki/conceptos/backtracking\|Backtracking (Vuelta Atrás)]]** | Árbol DFS + poda cuando se violan restricciones. | Exponencial acotado | ✅ 100% |
| **Difíciles (Clase NP)** | **Exacto (Optimización)** | **[[wiki/conceptos/branch-and-bound\|Branch and Bound (Ramificación y Poda)]]** | Árbol BFS / Best-First + **cotas matemáticas (Bounds)** para podar ramas subóptimas. | Exponencial optimizado | ✅ 100% |
| **Difíciles (Clase NP)** | **Aproximado** | **[[wiki/conceptos/heuristica-y-metaheuristica\|Heurísticas]]** | Reglas prácticas de sentido común / atajos computacionales. | Polinómico rápido | ❌ Solución "Buena" |
| **Difíciles (Clase NP)** | **Aproximado** | **[[wiki/conceptos/heuristica-y-metaheuristica\|Metaheurísticas]]** | Algoritmos Genéticos, Recocido Simulado, Búsqueda Tabú, Colonia de Hormigas. | Controlado por iteraciones | ❌ Óptimo Local / Cuasi-Global |

---

## 🎯 Plan de Estudio Estratégico por Unidades (Sílabo 2026-I)

```mermaid
graph LR
    subgraph U1["🟡 UNIDAD 1: Semanas 1 a 5"]
        BB["Branch and Bound<br>(Cotas y Poda)"]
        HEU["Heurísticas y Metaheurísticas<br>(Aproximación)"]
        OPT["Optimización Matemática<br>(Función Objetivo)"]
    end

    subgraph U2["🔵 UNIDAD 2: Semanas 6 a 10"]
        FB["Fuerza Bruta<br>(Exhaustividad)"]
        VOR["Algoritmos Voraces<br>(Elección Voraz)"]
        REC["Recursividad<br>(Teorema Maestro)"]
    end

    subgraph U3["🟢 UNIDAD 3: Semanas 11 a 16"]
        DV["Dividir para Vencer<br>(Subproblemas disjuntos)"]
        DP["Programación Dinámica<br>(Tabulación y Bellman)"]
        BT["Backtracking<br>(Espacio de Estados)"]
    end

    U1 --> U2 --> U3
```

---

## 🔗 Páginas de Conceptos Vinculadas

- [[wiki/conceptos/branch-and-bound|Branch and Bound (Ramificación y Poda)]]
- [[wiki/conceptos/heuristica-y-metaheuristica|Heurísticas y Metaheurísticas]]
- [[wiki/conceptos/programacion-dinamica|Programación Dinámica]]
- [[wiki/conceptos/algoritmos-voraces|Algoritmos Voraces]]
- [[wiki/conceptos/backtracking|Backtracking]]
- [[wiki/conceptos/dividir-para-vencer|Dividir para Vencer]]
- [[wiki/conceptos/fuerza-bruta|Fuerza Bruta]]
- [[wiki/conceptos/complejidad-p-vs-np|Clase P vs. Clase NP]]
- Hub Principal: [[wiki/cursos/estrategias-algoritmicas|Hub de Estrategias Algorítmicas 2026-I]]
