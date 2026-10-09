---
title: "Procesamiento de Imágenes (Image Processing)"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - domain/image-processing
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Procesamiento de Imágenes"
  - "Image Processing"
  - "Filtrado y Transformación de Imágenes"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 🔴 Procesamiento de Imágenes (*Image Processing*)

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.1: Data, Images, and Computer Graphics** (Págs. 1–2).

---

## 🎯 1. Definición y Clasificación Entrada/Salida

El **Procesamiento de Imágenes** es la subdisciplina en la que **la entrada es una imagen digital y la salida es otra imagen transformada**, modificada o mejorada.

$$\LARGE \text{Imágenes} \xrightarrow{\quad\text{Procesamiento de Imágenes}\quad} \text{Imágenes}$$

```
   [ 🖼️ Imagen Original ] ──► [ Filtros / Convolución / Ajustes ] ──► [ 🖼️ Imagen Procesada ]
          (Imagen)                                                            (Imagen)
```

* **Entrada**: Imagen digital (matriz de píxeles $I(x,y)$).
* **Salida**: Imagen digital resultante $I'(x,y)$ con propiedades visuales o métricas alteradas.

---

## 🛠️ 2. Operaciones Típicas

1. **Mejora y Realce (*Enhancement*)**: Aumento de contraste, enfoque de bordes (*sharpening*), ecualización de histogramas.
2. **Restauración y Filtrado**: Eliminación de ruido mediante filtros gaussianos, de mediana o de paso bajo.
3. **Manipulación Cromática**: Colorización de fotos antiguas, mapeo de tonos (*tone mapping*) HDR, corrección gamma.
4. **Composición y Fusión**: Mezcla de múltiples capas con transparencia (*alpha blending*), recorte (*chroma key*) y combinación de bandas espectrales satelitales.

---

## 🎮 3. Relevancia en el Pipeline de Computación Gráfica

El procesamiento de imágenes no es un área aislada; en gráficos 3D modernos es fundamental en:
* **Generación y Filtrado de Texturas**: Creación de *Mipmaps*, compresión de texturas y mapeo de normales.
* **Efectos de Posprocesamiento (*Post-Processing Shaders*)**: Bloom (resplandor), desenfoque de movimiento (*motion blur*), oclusión ambiental en espacio de pantalla (SSAO) y suavizado de bordes (*anti-aliasing* FXAA/SMAA).

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]]
- [[renderizado-sintesis-de-imagen|Renderizado y Síntesis de Imagen]] ($\text{Datos} \to \text{Imágenes}$)
- [[vision-por-computadora|Visión por Computadora]] ($\text{Imágenes} \to \text{Datos}$)
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
