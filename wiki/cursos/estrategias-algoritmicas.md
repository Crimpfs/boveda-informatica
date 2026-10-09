---
title: "Estrategias Algorítmicas (UNT - Semestre 2026-I)"
type: curso
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/curso
  - ciclo/iv
  - domain/algoritmos-optimizacion
  - prioridad/alta
aliases:
  - "Algorítmica Avanzada 2026-I"
  - "Estrategias 2026"
docentes:
  - "Coordinador: Dr. José A. Rodriguez Melquiades (Lic. Matemáticas - jrodriguez@unitru.edu.pe)"
  - "Docente: Dr. Daniel A. Alvarez Campos (Ing. Informático - dalvarezc@unitru.edu.pe)"
  - "Docente: Mg. Max L. Castro Rodríguez (Ing. Informático - mcastror@unitru.edu.pe)"
creditos: 4
codigo: 13631
prerequisito: "Estructura de Datos"
estado: "Segunda Matrícula - Enfoque de Dominio Total"
---

# ♟️ Estrategias Algorítmicas (2026-I)

> [!IMPORTANT] 🎯 Objetivo de Segunda Matrícula: Dominio Total
> Este curso tiene **prioridad alta**. Con el **Dr. José A. Rodriguez Melquiades** (Lic. en Matemáticas), las evaluaciones exigirán **rigor matemático en modelado de optimización, demostraciones de cotas de poda (bounding) y justificación teórica de exacto vs. aproximado**.
>
> 📁 **Materiales e Ingestión**:
> - 📄 **Sílabo Oficial del Curso**: [[fuentes/estrategias/silabo-estrategias-algoritmicas|Sílabo Crudo]] | [[wiki/resumenes/resumen-silabo-estrategias-algoritmicas|Resumen Estructurado del Sílabo]]
> - 📁 **Todo el repositorio de materiales de clase (Teorías, Prácticas y Códigos Python) ha sido integrado exitosamente en `fuentes/estrategias/`**.

---

## 📊 Sistema de Evaluación Oficial 2026-I (Ponderaciones Actualizadas)

- **Nota mínima aprobatoria:** **14** (El medio punto 0.5 favorece en el promedio promocional).
- **Fórmulas Oficiales por Unidad:**
  - $PU_1 = (PL \cdot 0.30) + (DA \cdot 0.30) + (EU \cdot 0.40)$
  - $PU_2 = (PL \cdot 0.30) + (DA \cdot 0.25) + (EU \cdot 0.45)$
  - $PU_3 = (PL \cdot 0.20) + (DA \cdot 0.10) + (TF \cdot 0.25) + (EU \cdot 0.45)$
- **Promedio Promocional ($PP$):**
  $$PP = PU_1 \cdot 0.30 + PU_2 \cdot 0.30 + PU_3 \cdot 0.40$$

*(Donde: $PL$ = Práctica Laboratorio / Programas en C++ o Python, $DA$ = Desarrollo de Actividades / Exposición de problemas resueltos, $TF$ = Trabajo Final de Investigación Formativa 25%, $EU$ = Examen de Unidad 40-45%).*

---

## 🗺️ Hoja de Ruta Semana a Semana con Materiales Vinculados

### 🟡 Unidad I: Optimización, Ramificación y Poda (Branch-and-Bound) y Heurísticas
*(¡Atención! La Unidad 1 arranca directo con problemas NP-Difíciles, Cotas y Optimización).*

- [ ] **Semana 1 (13/04 - 17/04):** Socialización del sílabo. Introducción a las Estrategias Algorítmicas: Ciencia, Método Científico y Estrategias Exactas vs. Aproximadas.
  - 📖 **Resumen de Clase**: [[wiki/resumenes/semana-01-metodologia-y-estrategias-algoritmicas|Resumen Semana 1: Ciencia, Método y Pipeline]]
  - 📄 *Material Fuente*: [[fuentes/estrategias/SEMANA 1/Teoria 1.pdf]] | Concepto: [[complejidad-p-vs-np|Clase P vs. NP]]
- [ ] **Semana 2 (20/04 - 24/04):** Problemas de **Optimización**. Función objetivo, espacio de soluciones y modelado.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 2/Teoria2.pdf]] | [[fuentes/estrategias/SEMANA 2/Practica2.pdf]]
  - 💻 *Códigos*: `Agricultura1.py`, `Agricultura2.py`, `AsignacionTareas.py`, `CSDI.py`, `CadenaS1.py`
- [ ] **Semana 3 (27/04 - 01/05):** Estrategia algorítmica **Branch-and-Bound (Ramificación y Poda)**. Árbol de búsqueda, cotas superior/inferior.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 3/Teoria3.pdf]] | [[fuentes/estrategias/SEMANA 3/Practica3.pdf]] | Concepto: [[branch-and-bound|Branch and Bound]]
- [ ] **Semana 4 (04/05 - 08/05):** Estrategias de aproximación: **Heurísticas y Metaheurísticas**.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 4/Teoria4.pdf]] | [[fuentes/estrategias/SEMANA 4/Practica4.pdf]] | `BranchBound.py`
  - 📖 *Casos de Estudio*: Caso Frutos del Chicama, Explicación formal de la función Branch and Bound.
  - 🧠 *Conceptos*: [[heuristica-y-metaheuristica|Heurísticas y Metaheurísticas]]
- [ ] **Semana 5 (11/05 - 15/05):** 📝 **Examen de Unidad I (Peso: 40%)** + Rúbrica de Laboratorio.

### 🔵 Unidad II: Fuerza Bruta, Algoritmos Voraces y Recursividad
- [ ] **Semana 6 (18/05 - 22/05):** Estrategia algorítmica por **Fuerza Bruta**.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 6/Teoria 6.pdf]] | [[fuentes/estrategias/SEMANA 6/Practica 6.pdf]] | Concepto: [[fuerza-bruta|Fuerza Bruta]]
- [ ] **Semana 7 (25/05 - 29/05):** Estrategia algorítmica **Voraz (Greedy)**.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 7/Teoria 7.pdf]] | [[fuentes/estrategias/SEMANA 7/Practica 7.pdf]] | Concepto: [[algoritmos-voraces|Algoritmos Voraces]]
- [ ] **Semana 8 (01/06 - 05/06):** Estrategia recursiva. Solución de recurrencias y Teorema Maestro.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 8/Teoria 8.pdf]] | [[fuentes/estrategias/SEMANA 8/Practica 8.pdf]] | `Monografia.pdf`
- [ ] **Semana 9 (08/06 - 12/06):** Comparación entre estrategias exactas y aproximadas.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 9/Teoria 9.pdf]] | [[fuentes/estrategias/SEMANA 9/Practica 9.pdf]]
- [ ] **Semana 10 (15/06 - 19/06):** 📝 **Examen de Unidad II (Peso: 45%)** + Exposición de avance de proyecto.

### 🟢 Unidad III: Dividir para Vencer, Programación Dinámica y Backtracking
- [ ] **Semana 11 (22/06 - 27/06):** Estrategia algorítmica **Dividir para Vencer**.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 11/Teoria 11.pdf]] | [[fuentes/estrategias/SEMANA 11/Practica 11.pdf]] | Concepto: [[dividir-para-vencer|Dividir para Vencer]]
- [ ] **Semana 12 (29/06 - 03/07):** Estrategia algorítmica **Programación Dinámica**.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 12/Teoria12.pdf]] | [[fuentes/estrategias/SEMANA 12/Practica12.pdf]] | Concepto: [[programacion-dinamica|Programación Dinámica]]
- [ ] **Semana 13 (06/07 - 10/07):** Estrategia algorítmica **Backtracking**.
  - 📄 *Material*: [[fuentes/estrategias/SEMANA 13/Teoria 13.pdf]] | [[fuentes/estrategias/SEMANA 13/Practica 13.pdf]] | Concepto: [[backtracking|Backtracking]]
- [ ] **Semana 14 (13/07 - 17/07):** Presentación y sustentación de Trabajos de Proyectos de Investigación Formativa.
- [ ] **Semana 15 (20/07 - 24/07):** Repaso integral de los temas del curso.
- [ ] **Semana 16 (27/07 - 31/07):** 📝 **Examen de Unidad III (Peso: 45%)**.
- [ ] **Semana 17 (02/08 - 07/08):** Examen Sustitutorio y Aplazados.

---

## 📚 Bibliografía y Síntesis Central
- **Síntesis del Curso**: [[wiki/sintesis/mapa-estrategias-algoritmicas|Mapa Maestro de Estrategias Algorítmicas]]
- **Cormen, T. et al. (CLRS 2009)**: *Introduction to Algorithms* (3ra Ed.).
- **Lee, R.C.T. et al. (2007)**: *Introducción al diseño y análisis de algoritmos, un enfoque estratégico*.
- **Guerequeta, R. & Vallecillo, A. (1999)**: *Técnicas de diseño de algoritmos*.
