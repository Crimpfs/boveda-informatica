---
title: "Dividir para Vencer (Divide and Conquer)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - unidad/3
  - domain/algoritmos-recursivos
aliases:
  - "Divide y Vencerás"
  - "Divide and Conquer"
  - "D&C"
sources:
  - "[[estrategias/Divide y Vencerás(Ej. ordenar una lista)..md]]"
---

# Dividir para Vencer (Divide and Conquer)

> [!NOTE] Definición
> **Dividir para Vencer** es un paradigma algorítmico **exacto** que descompone un problema en dos o más **subproblemas disjuntos e independientes** del mismo tipo, los resuelve recursivamente y combina sus soluciones para resolver el problema original.

---

## 🎯 Las 3 Fases Fundamentales

1. **Dividir**: Partir el problema en subproblemas de menor tamaño.
2. **Vencer**: Resolver recursivamente los subproblemas. Si son suficientemente pequeños, resolver directamente (caso base).
3. **Combinar**: Unir las soluciones de los subproblemas en la solución del problema global.

---

## 📈 Complejidad y Teorema Maestro

Para ecuaciones de la forma:
$$T(n) = a \cdot T(n/b) + f(n)$$
- **Ejemplos clásicos**: MergeSort ($O(n \log n)$), QuickSort ($O(n \log n)$ promedio), Búsqueda Binaria ($O(\log n)$), Multiplicación de Matrices de Strassen ($O(n^{2.81})$), Par de Puntos más Cercanos ($O(n \log n)$).

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
- **Diferencia con DP**: En D&C los subproblemas son *disjuntos*; en [[wiki/conceptos/programacion-dinamica|Programación Dinámica]] son *superpuestos*.
