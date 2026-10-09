---
title: "Computación Gráfica (UNT - Ciclo IV)"
type: curso
created: 2026-08-08
updated: 2026-08-08
tags:
  - wiki/curso
  - ciclo/iv
  - domain/graficos-computacionales
aliases:
  - "Gráficos por Computadora"
  - "CG"
docentes:
  - "Ing. José Luis Peralta Luján (jperalta@unitru.edu.pe)"
  - "Ing. José Arturo Díaz Pulido (jdiazpulido@unitru.edu.pe)"
creditos: 4
codigo: 13635
prerequisito: "Geometría Analítica y Estructura de Datos"
---

# 🎨 Computación Gráfica

> **Facultad de Ciencias Físicas y Matemáticas — Departamento de Informática (UNT)**  
> **Ciclo:** IV | **Créditos:** 4 | **Código:** 13635 | **Régimen:** Obligatorio  
> **Tutoría:** Martes 07:00 - 09:00 (Cubil) / Martes 11:00 - 13:00 (Sala Profesores)
>
> 📄 **Documentación del Curso**:
> - 📄 **Sílabo Oficial**: [[fuentes/grafica/silabo-computacion-grafica|Sílabo Crudo]] | [[wiki/resumenes/resumen-silabo-computacion-grafica|Resumen Estructurado del Sílabo]]
> - 📖 **Libro Guía (Gomes & Velho)**: [[wiki/resumenes/resumen-cap1-intro-gomes-velho|Resumen Cap. 1 (Data, Images & CG)]]

---

## 🧠 Conceptos Teóricos: Sección 1.1 (*Data, Images, and Computer Graphics*)

* 🎯 **Definición y Objetivo**: [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]] ($\text{Datos} \to \text{Imágenes}$)
* 🔷 **Subdisciplina 1**: [[modelado-geometrico|Modelado Geométrico (Geometric Modeling)]] ($\text{Datos} \to \text{Datos}$)
* 🔶 **Subdisciplina 2**: [[renderizado-sintesis-de-imagen|Renderizado y Síntesis de Imagen (Rendering)]] ($\text{Datos} \to \text{Imágenes}$)
* 🔴 **Subdisciplina 3**: [[procesamiento-de-imagenes|Procesamiento de Imágenes (Image Processing)]] ($\text{Imágenes} \to \text{Imágenes}$)
* 🟢 **Subdisciplina 4**: [[vision-por-computadora|Visión por Computadora (Computer Vision)]] ($\text{Imágenes} \to \text{Datos}$)
* ⏱️ **Dimensión Temporal**: [[computacion-grafica-en-movimiento|Computación Gráfica en Movimiento (Motion, Animation & Video)]] ($\text{Datos}\times t \leftrightarrow \text{Video}$)
* 📦 **Abstracción Unificadora**: [[objeto-grafico|El Concepto de Objeto Gráfico (Graphics Object)]]
* 🌐 **Pipelines Reales**: [[integracion-multidisciplinar-grafica|Integración Multidisciplinar en Computación Gráfica]]

## 🧠 Conceptos Teóricos: Sección 1.4 (*Example Models: Terrains and 2D Images*)

* 🏔️ **Terrenos**: [[modelado-de-terrenos|Modelado de Terrenos (Terrain Modeling)]] (Función de altura $z = f(x,y)$, Fig. 1.4)
* 🖼️ **Imágenes 2D**: [[modelado-de-imagenes-2d|Modelado de Imágenes 2D en Escala de Grises]] (Función de imagen $z = f(x,y)$, Fig. 1.5)
* ⚖️ **Principio Central**: [[dualidad-terreno-imagen|Dualidad Matemática: Terreno vs. Imagen 2D]] (Equivalencia $f: U \subset \mathbb{R}^2 \to \mathbb{R}$)

---

## 🛠️ Programas y Entorno Tecnológico del Curso

Para las clases teóricas, prácticas y laboratorios de Computación Gráfica se utilizan:

* **Estándar Gráfico**: **OpenGL** (Open Graphics Library, perfil Core 3.3+).
* **Bibliotecas Auxiliares**:
  * **GLFW / FreeGLUT**: Creación y gestión de ventanas y eventos gráficos.
  * **GLEW / GLAD**: Carga de extensiones modernas de OpenGL.
  * **GLM (OpenGL Mathematics)**: Álgebra lineal (vectores `vec3`, `vec4` y matrices de transformación `mat4`).
* **Lenguaje e IDE**: **C++** (o Python con `PyOpenGL` / C# con OpenTK) en IDEs como **Visual Studio**, **VS Code**, **CLion** o **Code::Blocks**.
* **Modelado 3D**: **Blender** (para creación y exportación de modelos `.obj` / `.mtl`).

---

## 📊 Sistema de Evaluación y Fórmulas de Calificación

- **Nota mínima aprobatoria:** 14 (El medio punto 0.5 favorece al estudiante).
- **Fórmulas por Unidad:**
  - $PU_1 = (PL \cdot 0.35) + (DA \cdot 0.35) + (EU \cdot 0.30)$
  - $PU_2 = (PL \cdot 0.35) + (DA \cdot 0.35) + (EU \cdot 0.30)$
  - $PU_3 = (PL \cdot 0.20) + (EU \cdot 0.20) + (TF \cdot 0.60)$
- **Promedio Promocional ($PP$):**
  $$PP = PU_1 \cdot 0.30 + PU_2 \cdot 0.30 + PU_3 \cdot 0.40$$

*(Donde: $PL$ = Prácticas de Laboratorio con OpenGL/C++, $DA$ = Desarrollo de Actividades / Informes, $TF$ = Trabajo Final 3D con impacto 60%, $EU$ = Examen de Unidad).*

---

## 🗺️ Hoja de Ruta Semana a Semana

### 🟡 Unidad I: Fundamentos de Computación Gráfica (Parte 1)
- [ ] **Semana 1: Introducción y Configuración del Entorno Gráfico**
  - 📖 **Teoría**: Presentación del curso, socialización del sílabo, definición de computación gráfica, áreas de aplicación y evolución de las GPU/Shaders.
  - 💻 **Laboratorio / Práctica**: Configuración del entorno de desarrollo (C++, OpenGL, GLFW/FreeGLUT, GLEW, GLM) y primer programa "Hello Window / Hello Triangle".
  - ✍️ **Autoevaluación**: Diagnóstico inicial de prerrequisitos (vectores, matrices y estructuras de datos C++).
- [ ] **Semana 2:** El proceso de formación de imágenes (modelo de cámara sintética). Primitivas gráficas (puntos, líneas, triángulos).
- [ ] **Semana 3:** Transformación Modelo-Vista. Transformaciones geométricas en 2D (traslación, rotación, escalado, cizallamiento con matrices homogéneas).
- [ ] **Semana 4:** Transformaciones geométricas en 3D y composición de transformaciones matriciales.
- [ ] **Semana 5:** 📝 **Examen de Unidad I**.

### 🔵 Unidad II: Fundamentos de Computación Gráfica (Parte 2)
- [ ] **Semana 6:** Modelos de proyección (Ortográfica y Perspectiva) y mapeo al Viewport.
- [ ] **Semana 7:** Modelos de color (RGB, CMYK, HSV). Jerarquía de modelos y grafos de escena 2D/3D.
- [ ] **Semana 8:** Modelos de iluminación y sombreado (Flat, Gouraud, Phong Shading, luz ambiente, difusa y especular).
- [ ] **Semana 9:** Mapeo de texturas (Texture Mapping, coordenadas UV, filtrado). Propuesta del proyecto final.
- [ ] **Semana 10:** 📝 **Examen de Unidad II**.

### 🟢 Unidad III: Carga de Modelos 3D y Algoritmos de Rasterizado
- [ ] **Semana 11:** Carga de modelos y mallas 3D complejas (parsing de archivos `.obj`, buffers VBO/VAO/EBO).
- [ ] **Semana 12:** Animación de modelos 3D y cinemática básica.
- [ ] **Semana 13:** Algoritmos de renderizado y visibilidad (Z-Buffer, eliminación de caras ocultas, Ray Tracing básico).
- [ ] **Semana 14:** Algoritmos clásicos de rasterización: trazado de líneas (Bresenham, DDA), círculos (Punto Medio), recorte de polígonos (Cohen-Sutherland, Sutherland-Hodgman) y llenado por Scanline.
- [ ] **Semana 15:** 📝 **Examen de Unidad III** y Sustentación del Proyecto Final 3D.
- [ ] **Semana 16:** Examen Sustitutorio y Aplazados.

---

## 📚 Bibliografía Oficial
- **Hearn, D. & Baker, M. P. (2006)**: *Gráficos por Computador con OpenGL* (Pearson Educación).
- **Gomes, J., Velho, L. & Costa, M. (2012)**: *Computer Graphics: Theory and Practice* (CRC Press).
- **LearnOpenGL**: *Guía moderna de OpenGL 3.3+ con C++*.
