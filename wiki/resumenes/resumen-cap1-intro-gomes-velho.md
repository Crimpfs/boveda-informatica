---
title: "Resumen: Capítulo 1 — Data, Images, and Computer Graphics"
type: resumen
created: 2026-08-19
updated: 2026-08-19
tags:
  - wiki/resumen
  - domain/computacion-grafica
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Intro CG Gomes"
  - "Capítulo 1 Computer Graphics Theory and Practice"
sources:
  - "[[fuentes/grafica/Computer Graphics Theory and Practice (Gomes, Velho, Costa).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# 📖 Cap. 1: Introduction — *Computer Graphics: Theory and Practice*
**Gomes, J. | Velho, L. | Costa, M. (2012) — CRC Press**

> Este resumen cubre el capítulo completo de introducción del libro oficial del sílabo de Computación Gráfica (13635). El hilo conductor del libro —y del curso— es la transformación:
> $$\text{Data} \longrightarrow \text{Images}$$
>
> 🧠 **Conceptos Desarrollados a partir de esta Fuente**:
> - [[paradigma-de-los-cuatro-universos|El Paradigma de los Cuatro Universos]]
> - [[subdisciplinas-computacion-grafica|Subdisciplinas de la Computación Gráfica]]
> - [[reconstruccion-e-interpolacion|Reconstrucción e Interpolación]]
> - [[objeto-grafico|El Concepto de Objeto Gráfico]]

---

## 1.1 Data, Images y Computación Gráfica

La **computación gráfica** se define como el conjunto de métodos y técnicas para transformar datos en imágenes visualizadas en un dispositivo gráfico. El libro (y el curso) dividen este problema central en subproblemas y construyen la teoría matemática para resolverlos.

### Las 4 Sub-Disciplinas Fundamentales

```
         Datos                      Imágenes
           │                            │
           ▼                            ▼
  ┌─────────────────┐         ┌──────────────────┐
  │ Modelado        │──────►  │  Renderizado     │
  │ Geométrico      │         │  (Image Synthesis)│
  └─────────────────┘         └──────────────────┘
  ┌─────────────────┐         ┌──────────────────┐
  │ Visión por      │◄──────  │  Procesamiento   │
  │ Computadora     │         │  de Imágenes     │
  └─────────────────┘         └──────────────────┘
```

| Sub-Disciplina | Entrada | Salida | Descripción |
|---|---|---|---|
| **Modelado Geométrico** | Datos geométricos | Descripción estructurada | Cómo *describir* y *almacenar* objetos geométricos |
| **Renderizado** (*Image Synthesis*) | Datos del modelo geométrico | Imagen | Genera imágenes a partir del modelo para mostrarlas |
| **Procesamiento de Imágenes** | Imagen | Imagen transformada | Colorización, mejora de detalles, combinación de imágenes |
| **Visión por Computadora** (*Computer Vision*) | Imagen | Información geométrica/física | Extraer info sobre los objetos retratados — "ver" |

> **Nota clave**: El renderizado *genera* imágenes; la visión por computadora las *interpreta*. Son procesos inversos.

### Con la Dimensión Temporal (Animación)

Cuando se agrega la variable **tiempo**, aparecen 4 sub-disciplinas análogas:

| Sub-Disciplina | Equivalente estático |
|---|---|
| **Motion Specification** (Modelado de Movimiento) | Modelado Geométrico |
| **Animation** (Visualización de Movimiento) | Renderizado |
| **Video Processing** | Procesamiento de Imágenes |
| **Motion Analysis** | Visión por Computadora |

### Objeto Gráfico — Concepto Unificador
El concepto de **objeto gráfico** (*graphics object*) unifica todos los diagramas: es lo suficientemente amplio para incluir modelos geométricos, imágenes, animaciones y video. El libro desarrollará este concepto formalmente más adelante.

---

## 1.2 Aplicaciones de la Computación Gráfica

La CG tiene aplicaciones en prácticamente todo campo del conocimiento. Las 3 grandes áreas:

| Área                                    | Descripción                                                          | Ejemplos                                                                           |
| --------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **CAD/CAM**                             | Diseño y fabricación asistidos por computadora                       | Prototipado electrónico, manufactura con CNC, desktop publishing                   |
| **Visualización de Datos y Movimiento** | "Una imagen vale más que mil palabras" — análisis cualitativo rápido | Simulación científica, visualización médica (tomografías), datos satelitales       |
| **Interacción Humano-Computadora**      | Interfaces gráficas de usuario                                       | WIMP (Windows/Icon/Menu/Pointing device), sistemas de navegación, realidad virtual |

### 1.2.1 Multimedia
La multimedia es el uso simultáneo de varios medios (texto, audio, imágenes, video, animación) para comunicar información de forma unificada. Sus tres retos fundamentales son:

1. **Representación** — cómo codificar coherentemente los distintos canales
2. **Control** — sincronización del flujo de información
3. **Almacenamiento** — cómo guardar y recuperar información en distintos formatos

La CG contribuye con: interfaces de usuario, síntesis de imágenes, animación y publicación electrónica.

---

## 1.3 El Paradigma de los Cuatro Universos ⭐

Esta es la idea central del libro y del enfoque matemático del curso. Para modelar cualquier objeto en computación gráfica, se usan **cuatro niveles de abstracción**:

$$\text{Universo Físico} \longrightarrow \text{Universo Matemático} \longrightarrow \text{Universo de Representación} \longrightarrow \text{Universo de Implementación}$$

| Universo | Símbolo | Contenido |
|---|---|---|
| **Físico** | $\mathcal{P}$ | Los objetos reales del mundo que queremos estudiar |
| **Matemático** | $\mathcal{M}$ | Descripción abstracta de esos objetos (funciones, geometrías) |
| **Representación** | $\mathcal{R}$ | Descripción simbólica *finita* del objeto matemático (discretización) |
| **Implementación** | $\mathcal{I}$ | Estructuras de datos en la computadora para manipularlo |

> ⚠️ **Problema clave**: Pasar de $\mathcal{M}$ a $\mathcal{R}$ implica **pérdida de información**. La mayor parte de las representaciones son *aproximadas* (lossy), no exactas. Mucha ingeniosidad en CG se dedica a minimizar esta pérdida.

### Ejemplo: Representación Numérica
- **Físico**: medir la longitud de un objeto real
- **Matemático**: un número real en $\mathbb{R}$
- **Representación**: punto flotante IEEE 754 (solo rationales)
- **Implementación**: `float` o `double` en C++

La irracionalidad ($\sqrt{2}$, $\pi$) **no existe** en el universo de representación — eso es pérdida de información.

---

## 1.4 Modelos de Ejemplo: Terrenos e Imágenes 2D

Un resultado importante: **objetos físicos muy distintos pueden compartir el mismo modelo matemático**.

### 1.4.1 Modelado de Terrenos
- **Físico**: topografía de una montaña
- **Matemático**: función de altura $f : U \subset \mathbb{R}^2 \rightarrow \mathbb{R}$, donde $z = f(x, y)$
- El terreno = gráfico de $f$: $\mathcal{G}(f) = \{(x, y, f(x,y))\}$
- **Representación**: muestreo uniforme (*uniform sampling*) en una grilla $(x_i, y_j)$, obteniendo una matriz de elevaciones $z_{ij} = f(x_i, y_j)$
- **Implementación**: array bidimensional / matriz

### 1.4.2 Modelado de Imágenes 2D
- **Físico**: una fotografía en blanco y negro (papel con tonos de gris)
- **Matemático**: función imagen $f : U \subset \mathbb{R}^2 \rightarrow \mathbb{R}$, donde $z = f(x,y)$ es el tono de gris (0=negro, 1=blanco)
- **Representación**: muestreo uniforme → grilla de *píxeles*
- **Implementación**: matrix/array de `uint8` o `float`

> 💡 **Conclusión**: Un terreno y una imagen en escala de grises tienen **exactamente el mismo modelo matemático**: $f : U \subset \mathbb{R}^2 \rightarrow \mathbb{R}$

---

## 1.5 Reconstrucción

La **reconstrucción** es el proceso inverso a la representación: pasar de una representación discreta ($\mathcal{R}$) de vuelta a un objeto matemático ($\mathcal{M}$).

$$\mathcal{R} \xrightarrow{\text{Reconstrucción}} \mathcal{M}$$

- La reconstrucción de un muestreo se llama **interpolación**
- Variantes: interpolación lineal, de Lagrange, splines, etc.
- La mayoría de representaciones son **lossy**: la reconstrucción solo aproxima el original
- Las representaciones **exactas** (lossless) son raras y solo posibles cuando $\mathcal{M}$ ya es discreto

---

## 1.6 Representaciones de Curvas Poligonales (Caso Práctico)

Para representar curvas poligonales cerradas (polígonos), existen al menos dos enfoques:

| Representación | Descripción | Ventaja | Desventaja |
|---|---|---|---|
| **Lista de vértices** | Listar coordenadas $(x_i, y_i)$ de cada vértice | Robusta ante transformaciones; fácil de aplicar $T(P_i)$ | Depende del sistema de coordenadas |
| **Ángulos internos** | Listar longitudes $\ell_i$ y ángulos $\theta_i$ de cada lado | Intrínseca (independiente del sistema de coordenadas) | Difícil de aplicar transformaciones arbitrarias |

La representación por vértices es la base de cómo OpenGL almacena geometría (VBOs — Vertex Buffer Objects).

---

## 1.7 Creación de Imágenes: Mundo Físico vs. Mundo Matemático

El proceso de fotografía tiene equivalentes exactos en CG:

| Proceso Fotográfico Real | Equivalente en CG |
|---|---|
| Entorno físico (espacio) | Modelo matemático del espacio: $\mathbb{R}^3$ |
| Crear los objetos de la escena | Modelos matemáticos de los objetos virtuales |
| Posicionar objetos en la escena | Transformaciones en el espacio (traslación, rotación, escala) |
| Iluminación física | Modelos de iluminación matemáticos (Phong, PBR) |
| La cámara fotográfica | Cámara virtual (proyección del espacio 3D al plano 2D) |
| La fotografía resultante | Función imagen $f: U \subset \mathbb{R}^2 \rightarrow \mathbb{R}^3$ (color) |
| Revelado/retoque | Procesamiento de imagen (filtros, corrección de color) |

---

## 🗺️ Mapa de Contenidos del Libro (Relevante para el Curso)

| Capítulo | Tema | Relevancia para el Semestre |
|---|---|---|
| **Cap. 2** | Geometría (Euclidiana, Afín, Proyectiva) | Semana 2-4: Transformaciones |
| **Cap. 3** | Coordenadas y Cambios de Sistema | Semana 3: Modelo-Vista |
| **Cap. 4** | Espacio de Rotaciones 3D | Semana 4: Transf. 3D |
| **Cap. 5** | Modelos de Color | Semana 7: RGB, HSV, CMYK |
| **Cap. 6** | Imagen y Procesamiento | Semana 6: Viewport |
| **Cap. 11** | Cámara Virtual | Semana 6: Proyección y Viewport |
| **Cap. 14** | Iluminación (Phong) | Semana 8: Luces |
| **Cap. 15** | Rasterización | Semana 14: Bresenham, DDA |
| **Cap. 16** | Texturas y Mappings | Semana 9: UV Mapping |

---

## 📝 Ejercicios Clave del Capítulo (Para Practicar)

1. **Ej. 4** — Media ponderada de $n$ puntos: $p = \sum w_i p_i$. Demostrar que minimiza $f(q) = \frac{1}{2}\sum w_i |q-p_i|^2$. Aplicar a reconstrucción de terrenos.
2. **Ej. 12** — Reconstrucción lineal de $f:\triangle ABC \rightarrow \mathbb{R}$ conociendo $f(A), f(B), f(C)$ (coordenadas baricéntricas).
3. **Ej. 21** — Aplicar el paradigma 4 universos al modelado de un disco metálico.
4. **Ej. 22** — Disco de radio $r$ rotando uniformemente: describir el movimiento con el paradigma 4 universos.
