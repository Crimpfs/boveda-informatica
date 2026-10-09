---
title: "Modelado de Terrenos (Terrain Modeling)"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - math/surfaces
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Modelado de Terrenos"
  - "Terrain Modeling"
  - "Mapas de Altura"
  - "Heightmaps"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 🏔️ Modelado de Terrenos (*Terrain Modeling*)

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.4.1: Terrain Modeling** (Págs. 8–9).

---

## 🎯 1. El Problema Físico y el Modelo de Elevación

En el universo físico ($\mathcal{P}$), deseamos representar y almacenar en el computador la topografía de una porción de tierra (por ejemplo, una cadena montañosa).

Para ello se utiliza el concepto de **mapa de alturas (*height map*)**:
* Se establece un plano de referencia base (nivel del mar o cota cero).
* Para cada punto del terreno en el plano horizontal, se mide su elevación vertical $z$.

---

## 🧮 2. El Modelo en el Universo Matemático ($\mathcal{M}$)

Matemáticamente, el terreno se modela mediante una **función escalar real de dos variables**:

$$f : U \subset \mathbb{R}^2 \longrightarrow \mathbb{R}, \qquad z = f(x, y)$$

Donde:
* $(x, y)$ son las coordenadas en el plano horizontal bidimensional $U$.
* $z$ es la elevación o altura correspondiente en ese punto.

Geométricamente, la superficie física del terreno es la **gráfica de la función** $\mathcal{G}(f)$:

$$\mathcal{G}(f) = \left\{ (x, y, f(x, y)) \in \mathbb{R}^3 \;\middle|\; (x, y) \in U \right\}$$

---

## 📐 3. Discretización y Muestreo Uniforme ($\mathcal{R}$ e $\mathcal{I}$)

Si el dominio $U$ es una región rectangular $[x_{\min}, x_{\max}] \times [y_{\min}, y_{\max}]$, se realiza un **muestreo uniforme (*uniform sampling*)**:

1. **Partición de los ejes**:
   $$P_x = \{x_0 < x_1 < \dots < x_n\}, \qquad P_y = \{y_0 < y_1 < \dots < y_m\}$$
   donde el espaciado entre muestras consecutivas es constante:
   $$x_{i+1} = x_i + \Delta x, \qquad y_{j+1} = y_j + \Delta y$$

2. **Malla de Muestreo**: El producto cartesiano $P_x \times P_y$ genera una cuadrícula regular de puntos $(x_i, y_j)$.

3. **Matriz de Elevación**: En cada vértice de la malla se evalúa la función de altura:
   $$z_{ij} = f(x_i, y_j)$$

4. **Implementación en C++ ($\mathcal{I}$)**: Se almacena como un arreglo bidimensional o matriz `float elevationGrid[N][M]`.

---

## 🖼️ Figura Oficial del Libro (Gomes & Velho)

![Figura 1.4: (a) Gráfica 3D de la función de altura de la Sierra de Aboboral, São Paulo (Yamamoto 98). (b) Malla regular de muestreo asociada.](file:///C:/Users/USER/Desktop/informatica/fuentes/assets/figura-1-4-modelado-terreno-y-malla.png)

* **(a)**: Visualización continua de la superficie $\mathcal{G}(f) = (x, y, f(x,y))$ en $\mathbb{R}^3$.
* **(b)**: Cuadrícula regular en el plano $\mathbb{R}^2$ donde cada celda $[x_i, x_{i+1}] \times [y_j, y_{j+1}]$ es un rectángulo congruente.

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[modelado-de-imagenes-2d|Modelado de Imágenes 2D en Escala de Grises]]
- [[dualidad-terreno-imagen|Dualidad Matemática: Terreno vs. Imagen 2D]]
- [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]]
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
