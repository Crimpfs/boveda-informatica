---
title: "Visión por Computadora (Computer Vision)"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - domain/computer-vision
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Visión por Computadora"
  - "Análisis de Imagen"
  - "Computer Vision"
  - "Image Analysis"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 🟢 Visión por Computadora (*Computer Vision*)

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.1: Data, Images, and Computer Graphics** (Págs. 1–2).

---

## 🎯 1. Definición y Clasificación Entrada/Salida

La **Visión por Computadora** (o *Análisis de Imágenes*) es la subdisciplina cuyo objetivo es **extraer información geométrica, topológica y física sobre los objetos representados en una imagen**.

$$\LARGE \text{Imágenes} \xrightarrow{\quad\text{Visión por Computadora}\quad} \text{Datos}$$

```
   [ 🖼️ Imagen Capturada ] ──► [ Algoritmos de Detección / Reconstrucción ] ──► [ Modelos 3D / Coordenadas ]
          (Imagen)                                                                    (Datos)
```

* **Entrada**: Una o más imágenes 2D (fotografías, secuencias de video, imágenes médicas).
* **Salida**: Datos estructurados (coordenadas espaciales 3D, nubes de puntos, etiquetas semánticas, vectores de movimiento).

---

## 👁️ 2. Propósito Central: "Hacer que la Máquina Vea"

Mientras que el [[renderizado-sintesis-de-imagen|Renderizado]] se enfoca en la *generación* de imágenes, la visión por computadora se enfoca en su **interpretación**:

1. **Reconstrucción 3D (Fotogrametría)**: A partir de varias fotos de un objeto o terreno desde diferentes ángulos, deducir la posición tridimensional de cada punto y construir una malla 3D.
2. **Estimación de Pose y Cámara**: Determinar la posición $(x,y,z)$ y orientación $(\theta_x, \theta_y, \theta_z)$ de la cámara física respecto al entorno real.
3. **Realidad Aumentada y Mixta (AR/MR)**: Anclar objetos virtuales 3D sobre mesas o pisos reales detectados por la cámara del teléfono o visor.
4. **Robótica y Vehículos Autónomos**: Detección de obstáculos, cálculo de distancias y navegación en tiempo real.

---

## ⚖️ 3. El Problema Inverso (Mal Condicionado)

Matemáticamente, la visión por computadora es un **problema inverso mal condicionado (*ill-posed inverse problem*)**:
* Al proyectar el mundo 3D sobre una imagen 2D (renderizado o fotografía), se pierde la información de profundidad ($Z$).
* Recuperar el mundo 3D a partir de la imagen 2D requiere resolver ambigüedades geométricas mediante restricciones ópticas, sombras, movimiento relativo o estereoscopía (dos cámaras).

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]]
- [[renderizado-sintesis-de-imagen|Renderizado y Síntesis de Imagen]] ($\text{Datos} \to \text{Imágenes}$)
- [[modelado-geometrico|Modelado Geométrico]] ($\text{Datos} \to \text{Datos}$)
- [[procesamiento-de-imagenes|Procesamiento de Imágenes]] ($\text{Imágenes} \to \text{Imágenes}$)
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
