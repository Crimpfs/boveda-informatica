---
title: "Modelado de Imágenes 2D en Escala de Grises (2D Image Modeling)"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - domain/image-processing
  - math/surfaces
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Modelado de Imágenes 2D"
  - "Función de Imagen"
  - "Image Function"
  - "2D Image Modeling"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 🖼️ Modelado de Imágenes 2D en Escala de Grises (*2D Image Modeling*)

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.4.2: 2D Image Modeling** (Págs. 9–10).

---

## 🎯 1. El Objeto Físico y el Soporte Espacial

Consideremos una fotografía física en blanco y negro (escala de grises) como un objeto de estudio en sí mismo:
* **Soporte Espacial**: Un trozo rectangular de papel plano, representado por un subconjunto compacto $U \subset \mathbb{R}^2$.
* **Tono de Gris / Luminancia**: A cada punto $(x, y)$ de la fotografía se le asocia un valor de oscuridad o brillo.

---

## 🧮 2. La Función de Imagen en el Universo Matemático ($\mathcal{M}$)

Normalizando los tonos de gris en el intervalo continuo $[0, 1]$:
* $0 \longrightarrow$ Negro absoluto.
* $1 \longrightarrow$ Blanco puro.
* Valores intermedios $(0, 1) \longrightarrow$ Gradaciones tonales de gris.

El modelo matemático de una imagen en escala de grises es la **Función de Imagen (*Image Function*)**:

$$f : U \subset \mathbb{R}^2 \longrightarrow [0, 1], \qquad z = f(x, y)$$

Al igual que en los terrenos, la imagen se describe geométricamente como la **gráfica de la función** $\mathcal{G}(f)$ en el espacio tridimensional:

$$\mathcal{G}(f) = \left\{ (x, y, f(x, y)) \in \mathbb{R}^3 \;\middle|\; (x, y) \in U \right\}$$

Donde el "relieve" o altura $z$ representa la **intensidad lumínica** del píxel.

---

## 📐 3. Discretización: La Matriz de Píxeles ($\mathcal{R}$ e $\mathcal{I}$)

Al aplicar muestreo uniforme sobre la región rectangular $U$:
* La cuadrícula bidimensional de celdas conforma los **píxeles**.
* El valor medio evaluado en cada celda $z_{ij} = f(x_i, y_j)$ se almacena en memoria como una matriz de enteros de 8 bits `uint8_t image[Height][Width]` (con valores de $0$ a $255$).

---

## 🖼️ Figura Oficial del Libro (Gomes & Velho)

![Figura 1.5: (Izquierda) Imagen 2D en escala de grises. (Derecha) Gráfica 3D de la función de imagen asociada z = f(x, y), donde las zonas más brillantes aparecen como montañas y las oscuras como valles.](file:///C:/Users/USER/Desktop/informatica/fuentes/assets/figura-1-5-modelado-imagen-2d-y-grafica.png)

* **Izquierda**: La imagen 2D vista perceptualmente por el ojo humano.
* **Derecha**: La superficie tridimensional $\mathcal{G}(f)$ que el computador procesa matemáticamente. Las zonas blancas tienen mayor altura ($z \to 1$), mientras que el fondo negro tiene altura nula ($z = 0$).

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[modelado-de-terrenos|Modelado de Terrenos (Terrain Modeling)]]
- [[dualidad-terreno-imagen|Dualidad Matemática: Terreno vs. Imagen 2D]]
- [[procesamiento-de-imagenes|Procesamiento de Imágenes (Image Processing)]]
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
