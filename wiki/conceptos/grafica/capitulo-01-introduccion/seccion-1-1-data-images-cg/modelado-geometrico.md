---
title: "Modelado Geométrico (Geometric Modeling)"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - math/geometry
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Modelado Geométrico"
  - "Geometric Modeling"
  - "Estructuración de Datos Geométricos"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 📐 Modelado Geométrico (*Geometric Modeling*)

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.1: Data, Images, and Computer Graphics** (Págs. 1–2).

---

## 🎯 1. Definición y Clasificación Entrada/Salida

El **Modelado Geométrico** es la subdisciplina de la computación gráfica encargada de **describir, estructurar y manipular datos geométricos y topológicos** en la memoria del computador.

$$\LARGE \text{Datos} \xrightarrow{\quad\text{Modelado Geométrico}\quad} \text{Datos}$$

```
   [ Parámetros / Fórmulas ] ──► [ Algoritmos de Modelado ] ──► [ Malla de Vértices / Topología ]
            (Datos)                                                          (Datos)
```

* **Entrada**: Datos abstractos (coordenadas, dimensiones, ecuaciones matemáticas, puntos de control).
* **Salida**: Datos estructurados (mallas poligonales, grafos de escena, estructuras B-Rep, árboles CSG).

---

## 🏗️ 2. ¿Qué Problemas Resuelve?

1. **Representación de Formas**: ¿Cómo almacenar una curva suave, una esfera, un automóvil o un terreno en memoria finita?
2. **Topología y Conectividad**: Mantener relaciones de vecindad entre vértices, aristas y caras poligonales.
3. **Operaciones Booleanas y Transformaciones**: Unión, intersección y diferencia de sólidos (CSG), escalado y deformaciones.

---

## 💻 3. Ejemplo Concreto en el Pipeline Gráfico (C++ / OpenGL)

En tu código de C++, el modelado geométrico se manifiesta cuando construyes estructuras de vértices antes de enviarlas a la GPU:

```cpp
// Modelado geométrico: Creación de la estructura de datos del objeto
struct Vertice {
    float x, y, z;       // Posición geométrica 3D
    float nx, ny, nz;    // Vector normal para iluminación
};

std::vector<Vertice> mallaTriangulos; // Contenedor de datos geométricos
```

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]]
- [[renderizado-sintesis-de-imagen|Renderizado y Síntesis de Imagen]] ($\text{Datos} \to \text{Imágenes}$)
- [[objeto-grafico|El Concepto de Objeto Gráfico]]
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
