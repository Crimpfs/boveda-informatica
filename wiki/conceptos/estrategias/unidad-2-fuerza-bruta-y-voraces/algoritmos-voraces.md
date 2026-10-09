---
title: "Algoritmos Voraces (Greedy Algorithms)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - unidad/2
  - domain/algoritmos-optimizacion
aliases:
  - "Algoritmo Voraz"
  - "Greedy"
sources:
  - "[[estrategias/algoritmo voraz.md]]"
---

# Algoritmos Voraces (Greedy Algorithms)

> [!NOTE] Definición
> Los **Algoritmos Voraces** construyen una solución paso a paso, tomando en cada momento la **opción localmente óptima** con la esperanza de que conduzca a un óptimo global, sin reconsiderar nunca las decisiones pasadas.

---

## 🎯 Las 3 Preguntas Clave

1. **¿Es una estrategia rápida y eficiente?**
   - **Muy rápida.** Típicamente opera en $O(n \log n)$ (por el ordenamiento inicial) o $O(n)$, ya que toma decisiones miopes e irrevocables sin hacer marcha atrás.
2. **¿Problemas Fáciles (P) o Difíciles (NP)?**
   - Para problemas con **Propiedad de Elección Voraz** (Kruskal, Prim, Huffman, Cambio de Monedas canónico), pertenece a **Clase P (Exacto)**.
   - Para problemas NP-Hard generales (TSP, Mochila 0/1), actúa como una **Heurística de Aproximación**.
3. **¿Método Exacto o Aproximado?**
   - **Exacto** solo si se demuestra matemáticamente la propiedad de elección voraz y subestructura óptima; de lo contrario es **Aproximado**.

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
- **Alternativa con Vuelta Atrás**: [[wiki/conceptos/backtracking|Backtracking]]
