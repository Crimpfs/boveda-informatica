---
title: "El Concepto de Objeto Gráfico (Graphics Object)"
type: concept
created: 2026-08-19
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - math/geometry
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Objeto Gráfico"
  - "Graphics Object"
  - "Abstracción Unificadora en CG"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 📦 El Concepto de Objeto Gráfico (*Graphics Object*)

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.1.2: Graphics Objects** (Págs. 3–4).

---

## 🎯 1. La Necesidad de una Abstracción Superior

Al comparar los esquemas de las 4 subdisciplinas estáticas ($\text{Datos} \leftrightarrow \text{Imágenes}$) con los esquemas dinámicos ($\text{Datos}\times t \leftrightarrow \text{Video}$), Gomes y Velho señalan que este proceso repetitivo es una señal clara de que se requiere un **concepto matemático superior y unificador**.

Ese concepto clave es el **Objeto Gráfico (*Graphics Object*)**.

```
           ┌──────────────────────────────────────────────┐
           │            OBJETO GRÁFICO (GO)               │
           │  (Geometrías, Imágenes, Video, Volúmenes)    │
           └──────────────────────────────────────────────┘
             ▲                 ▲              ▲        ▲
             │                 │              │        │
      [ 1. MODELADO ]   [ 2. SÍNTESIS ]  [ 3. FILTRO ] [ 4. ANÁLISIS ]
```

---

## 🌐 2. ¿Qué Engloba un Objeto Gráfico?

La noción de **Objeto Gráfico** es lo suficientemente amplia para encapsular bajo un mismo marco formal:
1. **Modelos Geométricos 2D y 3D**: Curvas de Bézier, mallas poligonales, superficies implícitas, sólidos CSG.
2. **Imágenes Rasterizadas**: Mapas de bits 2D, texturas, fotografías digitales.
3. **Entidades Temporales**: Trayectorias, esqueletos articulados, animaciones y secuencias de video.
4. **Campos Volumétricos 3D**: Nubes de densidad, simulaciones de fluidos, datos tomográficos médicos.

---

## ⚙️ 3. Las Cuatro Operaciones Universales sobre un Objeto Gráfico

Al unificar todo bajo la entidad *Objeto Gráfico*, las subdisciplinas pasan a ser **cuatro operadores fundamentales**:

1. **Modelado**: Creación, estructuración y modificación de la representación matemática del objeto gráfico.
2. **Síntesis / Renderizado**: Transformación del objeto gráfico hacia una representación perceptual visible en pantalla.
3. **Procesamiento / Filtrado**: Modificación interna de un objeto gráfico para alterar sus propiedades intrínsecas o estéticas.
4. **Análisis**: Extracción de propiedades métricas, topológicas o físicas a partir del objeto gráfico.

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]]
- [[modelado-geometrico|Modelado Geométrico]]
- [[renderizado-sintesis-de-imagen|Renderizado y Síntesis de Imagen]]
- [[computacion-grafica-en-movimiento|Computación Gráfica en Movimiento]]
- [[integracion-multidisciplinar-grafica|Integración Multidisciplinar en Computación Gráfica]]
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
