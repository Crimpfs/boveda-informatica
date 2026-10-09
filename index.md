# 🗺️ Índice Maestro: Base de Conocimiento LLM Wiki

> **Segundo Cerebro — Ingeniería Informática (UNT - Ciclo IV)**  
> Centro de mando y navegación para tus 6 asignaturas oficiales, conceptos técnicos, resúmenes de clase y guías para exámenes.

---

## 🎓 Cursos Matriculados (Semestre Actual)

### 📌 Hubs de Asignaturas Oficiales
| Asignatura | Enlace al Hub del Curso | Carpeta de Conceptos | Carpeta de Fuentes |
| :--- | :--- | :--- | :--- |
| **💡 Innovación y Emprendimiento** | [[innovacion-y-emprendimiento\|Hub de Innovación y Emprendimiento]] | `wiki/conceptos/innovacion/` | `fuentes/innovacion/` |
| **🗄️ Organización de Archivos** | [[organizacion-de-archivos\|Hub de Organización de Archivos]] | `wiki/conceptos/archivos/` | `fuentes/archivos/` |
| **🎨 Computación Gráfica** | [[computacion-grafica\|Hub de Computación Gráfica]] | `wiki/conceptos/grafica/` | `fuentes/grafica/` |
| **⚡ Electrónica para Computación** | [[electronica-para-computacion\|Hub de Electrónica para Computación]] | `wiki/conceptos/electronica/` | `fuentes/electronica/` |
| **🧮 Análisis Numérico** | [[analisis-numerico\|Hub de Análisis Numérico]] | `wiki/conceptos/analisis-numerico/` | `fuentes/analisis-numerico/` |
| **📐 Matemática Discreta** | [[matematica-discreta\|Hub de Matemática Discreta]] | `wiki/conceptos/mate-discreta/` | `fuentes/mate-discreta/` |

---

## 🔬 Síntesis y Guías de Estudio (`wiki/sintesis/`)

| Página | Descripción | Curso / Dominio |
| :--- | :--- | :--- |
| [[wiki/sintesis/malla-curricular-2018-UNT\|Malla Curricular Oficial (Plan 2018 - UNT)]] | Réplica exacta e interactiva de los 10 ciclos de la Escuela de Informática UNT desde la web oficial. | Malla Curricular |
| [[wiki/sintesis/analisis-y-mejor-horario-ciclo-iv-2026-II\|Horario Personalizado (Sección A) + Control 2da Matrícula]] | Grilla de Sección A (4 cursos) con ventanas disponibles para Estrategias Algorítmicas y Matemática Discreta. | Horarios y Planificación |
| [[wiki/sintesis/mapa-estrategias-algoritmicas\|Mapa Maestro: Taxonomía de Estrategias Algorítmicas]] | Matriz comparativa completa de problemas P vs. NP, métodos exactos vs. aproximados y las 7 estrategias. | Estrategias Algorítmicas |
| [[wiki/sintesis/rag-vs-llm-wiki\|Comparativa: RAG vs. Arquitectura LLM Wiki]] | Análisis comparativo entre recuperación efímera (RAG) y wikis compiladas persistentes. | Sistemas IA |

---

## 🧠 Conceptos Especializados (`wiki/conceptos/`)

### 🎨 Computación Gráfica (`wiki/conceptos/grafica/`)

#### 📂 Capítulo 1 — Sección 1.1: Fundamentos y Subdisciplinas (`.../seccion-1-1-data-images-cg/`)
| Concepto | Tipo / Clasificación | Asignatura / Tema |
| :--- | :--- | :--- |
| [[transformacion-datos-a-imagenes\|La Transformación Fundamental: Datos a Imágenes]] | Definición y Propósito ($\text{D}\to\text{I}$) | Cap. 1.1 Gomes & Velho |
| [[modelado-geometrico\|Modelado Geométrico (Geometric Modeling)]] | Subdisciplina ($\text{Datos} \to \text{Datos}$) | Cap. 1.1 Gomes & Velho |
| [[renderizado-sintesis-de-imagen\|Renderizado y Síntesis de Imagen (Rendering)]] | Subdisciplina ($\text{Datos} \to \text{Imágenes}$) | Cap. 1.1 Gomes & Velho |
| [[procesamiento-de-imagenes\|Procesamiento de Imágenes (Image Processing)]] | Subdisciplina ($\text{Imágenes} \to \text{Imágenes}$) | Cap. 1.1 Gomes & Velho |
| [[vision-por-computadora\|Visión por Computadora (Computer Vision)]] | Subdisciplina ($\text{Imágenes} \to \text{Datos}$) | Cap. 1.1 Gomes & Velho |
| [[computacion-grafica-en-movimiento\|Computación Gráfica en Movimiento (Motion & Video)]] | Dimensión Temporal ($\text{D}\times t \leftrightarrow \text{Video}$) | Cap. 1.1.1 Gomes & Velho |
| [[objeto-grafico\|El Concepto de Objeto Gráfico (Graphics Object)]] | Abstracción Unificadora ($\mathcal{GO}$) | Cap. 1.1.2 Gomes & Velho |
| [[integracion-multidisciplinar-grafica\|Integración Multidisciplinar en CG]] | Pipelines Reales (Satelital y Médico) | Cap. 1.1.3 Gomes & Velho |

#### 📂 Capítulo 1 — Sección 1.4: Modelos de Ejemplo (`.../seccion-1-4-modelos-ejemplo/`)
| Concepto | Tipo / Clasificación | Asignatura / Tema |
| :--- | :--- | :--- |
| [[modelado-de-terrenos\|Modelado de Terrenos (Terrain Modeling)]] | Modelo de Altura $z = f(x,y)$ (Fig. 1.4) | Cap. 1.4.1 Gomes & Velho |
| [[modelado-de-imagenes-2d\|Modelado de Imágenes 2D (Image Modeling)]] | Función de Imagen $z = f(x,y)$ (Fig. 1.5) | Cap. 1.4.2 Gomes & Velho |
| [[dualidad-terreno-imagen\|Dualidad Matemática: Terreno vs. Imagen 2D]] | Equivalencia de Modelos $f: U \subset \mathbb{R}^2 \to \mathbb{R}$ | Cap. 1.4 Gomes & Velho |

---

### ♟️ Estrategias Algorítmicas (`wiki/conceptos/estrategias/`)

#### 📂 Unidad 1: Optimización, Ramificación y Poda y Heurísticas
| Concepto | Tipo / Clasificación | Asignatura / Tema |
| :--- | :--- | :--- |
| [[branch-and-bound\|Branch and Bound (Ramificación y Poda)]] | NP-Hard / Exacto (Optimización) | Unidad I: Estrategias |
| [[heuristica-y-metaheuristica\|Heurísticas y Metaheurísticas]] | NP-Hard / Aproximado | Unidad I: Estrategias |
| [[complejidad-p-vs-np\|Teoría de Complejidad: Clase P vs. NP]] | Clasificación Fundamental | Unidad I / General |

#### 📂 Unidad 2: Fuerza Bruta y Algoritmos Voraces
| Concepto | Tipo / Clasificación | Asignatura / Tema |
| :--- | :--- | :--- |
| [[fuerza-bruta\|Fuerza Bruta (Búsqueda Exhaustiva)]] | NP-Hard / Exacto | Unidad II: Estrategias |
| [[algoritmos-voraces\|Algoritmos Voraces (Greedy)]] | Clase P / Exacto o Aprox. | Unidad II: Estrategias |

#### 📂 Unidad 3: Estrategias Recursivas, Dinámica y Backtracking
| Concepto | Tipo / Clasificación | Asignatura / Tema |
| :--- | :--- | :--- |
| [[dividir-para-vencer\|Dividir para Vencer]] | Clase P / Exacto ($O(n \log n)$) | Unidad III: Estrategias |
| [[programacion-dinamica\|Programación Dinámica]] | Clase P / Exacto (Subproblemas Superpuestos) | Unidad III: Estrategias |
| [[backtracking\|Vuelta Atrás (Backtracking)]] | NP-Hard / Exacto (Restricciones) | Unidad III: Estrategias |

---

### ⚙️ Arquitectura de Conocimiento (`wiki/conceptos/general/`)
| Concepto | Tipo / Clasificación | Dominio |
| :--- | :--- | :--- |
| [[llm-wiki-pattern\|Patrón LLM Wiki]] | Arquitectura de 3 capas | Segundo Cerebro |
| [[compounding-knowledge\|Conocimiento Acumulativo]] | Valor compuesto de notas | Gestión de Conocimiento |

---

## 📚 Resúmenes de Fuentes y Clases (`wiki/resumenes/`)

| Resumen | Documento de Origen | Asignatura / Tema |
| :--- | :--- | :--- |
| [[wiki/resumenes/resumen-cap1-intro-gomes-velho\|Resumen: Cap. 1 — Data, Images & CG (Gomes & Velho)]] | [[fuentes/grafica/Computer Graphics Theory and Practice.pdf]] | Computación Gráfica (13635) |
| [[wiki/resumenes/resumen-silabo-computacion-grafica\|Resumen: Sílabo de Computación Gráfica]] | [[fuentes/grafica/silabo-computacion-grafica.md]] | Computación Gráfica (13635) |
| [[wiki/resumenes/resumen-silabo-estrategias-algoritmicas\|Resumen: Sílabo de Estrategias Algorítmicas]] | [[fuentes/estrategias/silabo-estrategias-algoritmicas.md]] | Estrategias Algorítmicas (2026-I) |
| [[wiki/resumenes/semana-01-metodologia-y-estrategias-algoritmicas\|Resumen: Semana 1 - Ciencia, Método y Pipeline Algorítmico]] | [[fuentes/estrategias/SEMANA 1/Teoria 1.pdf]] | Estrategias Algorítmicas (2026-I) |
| [[wiki/resumenes/source-karpathy-llm-wiki\|Resumen: Patrón LLM Wiki]] | [[fuentes/2026-08-08-andrej-karpathy-llm-wiki.md]] | Arquitectura Segundo Cerebro |

---

## 📁 Fuentes Crudas (`fuentes/`)
- `fuentes/estrategias/`
- `fuentes/electronica/`
- `fuentes/innovacion/`
- `fuentes/automatas/`
- `fuentes/archivos/`
- `fuentes/grafica/`
