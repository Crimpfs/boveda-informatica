---
title: "Programación Dinámica (Dynamic Programming)"
type: concept
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/concepto
  - curso/estrategias-algoritmicas
  - unidad/3
  - domain/optimizacion-exacta
aliases:
  - "Programación Dinámica"
  - "DP"
  - "Principio de Bellman"
sources:
  - "[[estrategias/Programación Dinámica.md]]"
---

# Programación Dinámica (Dynamic Programming)

> [!NOTE] Definición
> La **Programación Dinámica** es un método algorítmico **exacto** para problemas de optimización que poseen **subproblemas superpuestos** y **subestructura óptima**. Resuelve cada subproblema una sola vez y almacena su resultado en una tabla o memoria para evitar cálculos redundantes.

---

## 🎯 Las 3 Preguntas Clave

1. **¿Es una estrategia rápida y eficiente?**
   - **Totalmente sí.** Transforma complejidades exponenciales ($O(2^n)$) en polinómicas manejables ($O(n^2)$, $O(n \cdot W)$, $O(n)$) gracias al almacenamiento de estados intermedios.
2. **¿Problemas Fáciles (P) o Difíciles (NP)?**
   - Pertenece a la **Clase P / Problemas Fáciles** (cuando se resuelve con DP exacta sobre subproblemas polinómicos).
3. **¿Método Exacto o Aproximado?**
   - **Método Exacto (100% óptimo).** Se basa en el *Principio de Optimalidad de Bellman*: una política óptima tiene la propiedad de que, cualesquiera que sean el estado y decisión iniciales, las decisiones restantes deben constituir una política óptima respecto al estado resultante.

---

## 🛠️ Enfoques de Implementación

```
                     [ Programación Dinámica ]
                    /                         \
         [ Top-Down (Memoization) ]      [ Bottom-Up (Tabulation) ]
       - Recursivo con caché           - Iterativo desde casos base
       - Llena solo estados requeridos - Llena toda la tabla en orden
```

---

## 🔗 Páginas Relacionadas
- **Mapa General**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa de Estrategias Algorítmicas]]
- **Curso**: [[wiki/cursos/estrategias-algoritmicas|Hub Estrategias Algorítmicas 2026-I]]
- **Concepto Asociado**: [[wiki/conceptos/dividir-para-vencer|Dividir para Vencer]]
