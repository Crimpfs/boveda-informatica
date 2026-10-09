---
title: "Resumen: Sílabo de Computación Gráfica"
type: summary
created: 2026-08-17
updated: 2026-08-17
tags:
  - wiki/summary
  - domain/computacion-grafica
aliases:
  - "Sílabo Computación Gráfica UNT"
  - "Sílabo CG"
sources:
  - "[[fuentes/grafica/silabo-computacion-grafica.md]]"
---

# 📄 Resumen: Sílabo de la Experiencia Curricular "Computación Gráfica"

> **Resumen Ejecutivo**: El sílabo oficial de Computación Gráfica (UNT - Código 13635, 4 créditos) abarca 16 semanas organizadas en tres unidades: Fundamentos de Gráficos 2D/3D (Parte 1 y 2) y Carga de Modelos 3D con Algoritmos de Rasterizado. Introduce el estándar gráfico **OpenGL**, modelos de cámara sintética, transformaciones matriciales, iluminación, texturas y rasterización.

---

## 📌 Datos Clave del Curso
- **Asignatura**: Computación Gráfica (Código 13635)
- **Créditos / Carga**: 4 Créditos (90 horas totales: 30h teoría, 57h práctica, 3h retroalimentación).
- **Prerrequisitos**: Geometría Analítica y Estructura de Datos.
- **Docentes**: Ing. José Luis Peralta Luján (Coordinador) y Ing. José Arturo Díaz Pulido.

---

## 🛠️ Herramientas y Programas Utilizados en el Curso

De acuerdo al sílabo oficial y su bibliografía central (Hearn & Baker - *Gráficos por Computador con OpenGL*), el entorno tecnológico del curso comprende:

1. **Biblioteca Gráfica Principal**:
   * **OpenGL (Graphics Library)**: Estándar de la industria para renderizado 2D y 3D acelerado por GPU (versiones Core Profile 3.3+).
2. **Bibliotecas Auxiliares de Ventanas y Matemáticas**:
   * **GLFW / FreeGLUT / GLUT**: Para la creación de ventanas, contextos OpenGL y gestión de eventos de teclado y mouse.
   * **GLEW / GLAD**: Para la carga de extensiones y funciones modernas de OpenGL.
   * **GLM (OpenGL Mathematics)**: Biblioteca de álgebra lineal para manejo de vectores (`vec2`, `vec3`, `vec4`) y matrices homogéneas (`mat4`).
3. **Lenguajes y Entornos de Desarrollo (IDE)**:
   * **Lenguaje Principal**: C++ (estándar en computación gráfica por su alto rendimiento y acceso directo al hardware). Alternativamente Python con `PyOpenGL` o C# con OpenTK para prototipado.
   * **IDE Recomendados**: Visual Studio, CLion, VS Code con depurador C++, Code::Blocks o GCC/MinGW.
4. **Herramientas de Modelado y Texturizado (Unidades II y III)**:
   * **Blender / Wavefront OBJ**: Para la exportación y carga de mallas tridimensionales (.obj / .mtl).

---

## 🗓️ Temas de la Semana 1 (Contenido Detallado)

* 📖 **Presentación del Curso**: Presentación de la metodología teórico-práctica y del trabajo final de proyección social (60% de la Unidad III).
* 📜 **Socialización del Sílabo**: Revisión del sistema de evaluación (nota aprobatoria 14), ponderaciones por unidad y normas de asistencia.
* 💡 **Introducción a la Computación Gráfica**:
  * Definición y áreas de aplicación (CGI, videojuegos, simulación médica, CAD/CAM, visualización científica, VR/AR).
  * Historia y evolución del hardware gráfico (de la renderización por software a las GPU dedicadas con Shaders).
* ⚙️ **Configuración del Entorno de Trabajo**:
  * Instalación y compilación del primer proyecto gráfico "Hello Window / Hello Triangle".
  * Vinculación de bibliotecas en C++: OpenGL, GLFW/FreeGLUT, GLEW/GLAD y GLM.
* ✍️ **Autoevaluación Inicial**: Diagnóstico de prerrequisitos en álgebra lineal (vectores, matrices), geometría analítica y estructuras de datos en C++.

---

## 📊 Sistema de Evaluación
- **Promedios de Unidad ($PU$)**:
  - $PU_1 = (PL \cdot 0.35) + (DA \cdot 0.35) + (EU \cdot 0.30)$
  - $PU_2 = (PL \cdot 0.35) + (DA \cdot 0.35) + (EU \cdot 0.30)$
  - $PU_3 = (PL \cdot 0.20) + (EU \cdot 0.20) + (TF \cdot 0.60)$
- **Promedio Promocional ($PP$)**:
  $$PP = 0.3 \cdot PU_1 + 0.3 \cdot PU_2 + 0.4 \cdot PU_3$$

---

## 🔗 Enlaces Relacionados en el Vault
- Hub del Curso: [[wiki/cursos/computacion-grafica|Hub de Computación Gráfica]]
- Fuente Original: [[fuentes/grafica/silabo-computacion-grafica.md]]
