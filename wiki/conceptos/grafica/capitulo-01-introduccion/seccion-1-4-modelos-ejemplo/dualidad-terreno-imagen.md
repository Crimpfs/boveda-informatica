---
title: "Dualidad Matemática: Terreno vs. Imagen 2D"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concept
  - domain/computacion-grafica
  - math/foundations
  - math/duality
  - fuente/libro-gomes-velho
  - ciclo/iv
aliases:
  - "Dualidad Terreno vs Imagen"
  - "Equivalencia Funcional Terreno e Imagen"
  - "Terrain-Image Duality"
sources:
  - "[[fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf]]"
curso: "[[wiki/cursos/computacion-grafica]]"
---

# ⚖️ Dualidad Matemática: Terreno vs. Imagen 2D

> **Sección del Libro**: *Computer Graphics: Theory and Practice* (Gomes, Velho & Costa), Capítulo 1, **Sección 1.4: Example Models: Terrains and 2D Images** (Págs. 8–10).

---

## 🎯 1. El Gran Hallazgo Teórico de la Sección 1.4

Uno de los resultados más elegantes demostrados por Gomes, Velho & Costa es que **dos objetos físicos totalmente distintos del mundo real comparten exactamente el mismo modelo en el universo matemático**:

```
      OBJETO FÍSICO 1 (P1)                       OBJETO FÍSICO 2 (P2)
  [ 🏔️ Montaña / Topografía Real ]            [ 🖼️ Fotografía en Escala de Grises ]
                 │                                           │
                 └──────────────────┬────────────────────────┘
                                    │
                                    ▼
                     MODELO MATEMÁTICO ÚNICO (M)
                 f : U ⊂ ℝ² ──► ℝ ,   z = f(x, y)
                 Superficie G(f) = { (x, y, f(x,y)) }
```

| Dimensión | [[modelado-de-terrenos\|Modelado de Terrenos]] | [[modelado-de-imagenes-2d\|Modelado de Imágenes 2D]] |
| :--- | :--- | :--- |
| **Objeto Físico ($\mathcal{P}$)** | Relieve geográfico de una montaña. | Papel fotográfico con tonos de gris. |
| **Soporte $U \subset \mathbb{R}^2$** | Coordenadas cartográficas $(x,y)$ en el suelo. | Coordenadas $(x,y)$ sobre el papel. |
| **Significado de la Altura $z$** | Elevación física en metros sobre el nivel del mar. | Nivel de luminancia o brillo $z \in [0, 1]$. |
| **Modelo Matemático ($\mathcal{M}$)** | **$f: U \subset \mathbb{R}^2 \to \mathbb{R}$** | **$f: U \subset \mathbb{R}^2 \to \mathbb{R}$** |
| **Representación Discreta ($\mathcal{R}$)** | Muestreo uniforme: matriz $(z_{ij})$. | Malla regular de píxeles $(I_{ij})$. |

---

## 🖼️ Comparativa Visual de Ambas Superficies Matemáticas

### 1. Función de Terreno Topográfico (Figura 1.4)
![Figura 1.4: Malla y superficie 3D de un terreno real.](file:///C:/Users/USER/Desktop/informatica/fuentes/assets/figura-1-4-modelado-terreno-y-malla.png)

### 2. Función de Imagen en Escala de Grises (Figura 1.5)
![Figura 1.5: Fotografía 2D interpretada como superficie de elevación 3D z = f(x,y).](file:///C:/Users/USER/Desktop/informatica/fuentes/assets/figura-1-5-modelado-imagen-2d-y-grafica.png)

---

## 💡 ¿Por Qué es Crucial Esta Dualidad?

Dado que la estructura matemática $z = f(x,y)$ es idéntica, **cualquier algoritmo desarrollado para una disciplina se traslada automáticamente a la otra**:

1. **Curvas de Nivel vs. Isófotas**:
   * En topografía, una curva de nivel $f(x,y) = c$ une puntos de igual altura.
   * En imágenes, $f(x,y) = c$ representa una línea de igual brillo (*isófota*).
2. **Detección de Bordes vs. Acantilados**:
   * El gradiente $|\nabla f(x,y)| = \sqrt{\left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2}$ detecta la máxima pendiente en un barranco o la frontera de máximo contraste en una imagen.
3. **Filtrado y Suavizado**:
   * Un filtro Gaussiano elimina el ruido digital en una foto y a la vez erosiona picos espurios en un mapa de relieve LiDAR.

---

## 🔗 Enlaces Relacionados en la Bóveda
- [[modelado-de-terrenos|Modelado de Terrenos (Terrain Modeling)]]
- [[modelado-de-imagenes-2d|Modelado de Imágenes 2D en Escala de Grises]]
- [[transformacion-datos-a-imagenes|La Transformación Fundamental: Datos a Imágenes]]
- [[wiki/cursos/computacion-grafica|Hub de Asignatura: Computación Gráfica]]
