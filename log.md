# 📜 Registro de Operaciones: LLM Wiki

> **Registro cronológico acumulativo de todas las operaciones del agente.**  
> Cada entrada utiliza el prefijo estándar `## [AAAA-MM-DD] <operacion> | <Titulo>` para permitir búsquedas y filtrados rápidos con expresiones regulares.

---

## [2026-08-08] system | Inicialización del Esquema y Estructura del Vault
- **Acción**: Inicialización completa de la arquitectura de 3 capas, jerarquía de carpetas y esquema maestro de reglas en [[CLAUDE.md]] y [[AGENTS.md]] en español.

---

## [2026-08-08] ingest | Semana 1: Estrategias Algorítmicas (Dr. Rodríguez Melquiades)
- **Fuente**: [[fuentes/estrategias/SEMANA 1/Teoria 1.pdf]]
- **Resumen Creado**: [[wiki/resumenes/semana-01-metodologia-y-estrategias-algoritmicas.md]]
- **Conceptos Clave Compilados**:
  - Dualidad Mundo Real vs. Mundo Abstracto (Modelado Matemático).
  - Pipeline de 6 Pasos para Resolver Problemas Computacionales (Decisión Exacta vs. Aproximada, Correctitud y Complejidad).
  - Método Científico, Falsación de Popper y Transferencia Tecnológica CONCYTEC.
- **Hub Actualizado**: [[wiki/cursos/estrategias-algoritmicas.md]] marcado `[x]` en Semana 1.

---

## [2026-08-09] ingest | Sílabo de Estrategias Algorítmicas (UNT)
- **Fuente**: [[fuentes/estrategias/silabo-estrategias-algoritmicas.md]]
- **Resumen Creado**: [[wiki/resumenes/resumen-silabo-estrategias-algoritmicas.md]]
- **Hub Actualizado**: [[wiki/cursos/estrategias-algoritmicas.md]]
- **Catálogo Actualizado**: [[index.md]]
- **Aporte Clave**: Integración del sílabo oficial con sumilla, competencias, programación temática de 16 semanas, fórmulas de evaluación y horarios de tutoría.

---

## [2026-08-16] synthesize | Elección del Mejor Horario (Ciclo IV - 2026-II)
- **Fuente**: [[fuentes/Horarios 2026_ II_final.xls]]
- **Síntesis Creada**: [[wiki/sintesis/analisis-y-mejor-horario-ciclo-iv-2026-II.md]]
- **Catálogo Actualizado**: [[index.md]]
- **Aporte Clave**: Evaluación comparativa rigurosa entre Sección A y Sección B. Determinación de la Sección A como la opción óptima por continuidad horaria, eliminación de huecos muertos de 7h y tardes libres los jueves.

---

## [2026-08-16] update | Integración de Cursos por 2da Matrícula (EA y Matemática Discreta)
- **Síntesis Actualizada**: [[wiki/sintesis/analisis-y-mejor-horario-ciclo-iv-2026-II.md]]
- **Hub Actualizado**: [[wiki/cursos/estrategias-algoritmicas.md]]
- **Catálogo Actualizado**: [[index.md]]
- **Aporte Clave**: Documentación de la Sección A como base ideal por contar con el Jueves libre completo y mañanas/tardes abiertas para acoplar las asignaturas pendientes de 2da matrícula sin provocar cruces.

---

## [2026-08-16] synthesize | Réplica de Malla Curricular UNT 2018 y Ajuste de Cursos Activos
- **Fuente**: `https://inf.unitru.edu.pe/curriculos`
- **Síntesis Creada**: [[wiki/sintesis/malla-curricular-2018-UNT.md]]
- **Hub Creado**: [[wiki/cursos/matematica-discreta.md]]
- **Catálogo Actualizado**: [[index.md]] (Removido Autómatas del ciclo activo, agregados Matemática Discreta y Estrategias Algorítmicas como 2da matrícula).
- **Aporte Clave**: Replicación exacta del plan de estudios 2018 de los 10 ciclos de Ingeniería Informática UNT y reestructuración completa de los cursos de la bóveda.

---

## [2026-08-17] ingest | Sílabo de Computación Gráfica (UNT)
- **Fuente**: [[fuentes/grafica/silabo-computacion-grafica.md]]
- **Resumen Creado**: [[wiki/resumenes/resumen-silabo-computacion-grafica.md]]
- **Hub Actualizado**: [[wiki/cursos/computacion-grafica.md]]
- **Catálogo Actualizado**: [[index.md]]
- **Aporte Clave**: Transcripción e integración del sílabo oficial (Código 13635), identificación de herramientas tecnológicas (OpenGL, GLFW/FreeGLUT, GLEW/GLAD, GLM, C++/IDE) y desglose detallado de los contenidos de la Semana 1.

---

## [2026-08-19] structure & ingest | Modularización de Conceptos y Teoría de Gomes & Velho
- **Fuente**: `fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.).pdf`
- **Reestructuración de Carpetas**:
  - `wiki/conceptos/estrategias/` (Algoritmos voraces, Backtracking, B&B, P vs NP, Dividir y Vencer, Fuerza Bruta, Heurísticas, Prog. Dinámica).
  - `wiki/conceptos/grafica/` (Conceptos teóricos de computación gráfica).
  - `wiki/conceptos/general/` (Patrón LLM Wiki y Conocimiento Acumulativo).
- **Resumen Creado**: [[wiki/resumenes/resumen-cap1-intro-gomes-velho.md]]
- **Nuevos Conceptos Creados**:
  - [[paradigma-de-los-cuatro-universos.md]] ($\mathcal{P} \to \mathcal{M} \to \mathcal{R} \to \mathcal{I}$, pérdida de información, dualidad terreno/imagen).
  - [[subdisciplinas-computacion-grafica.md]] (Modelado, Renderizado, Procesamiento, Visión y dimensión temporal).
  - [[reconstruccion-e-interpolacion.md]] (Muestreo uniforme/disperso, lerp, bilineal, baricéntrica).
  - [[objeto-grafico.md]] (Abstracción unificadora, listas de vértices vs. ángulos internos).
- **Actualizados**: [[index.md]], [[wiki/cursos/computacion-grafica.md]], [[wiki/cursos/estrategias-algoritmicas.md]].
- **Aporte Clave**: Modularización temática de la capa de conceptos y formalización matemática de los fundamentos teóricos del libro guía oficial de Computación Gráfica.

---

## [2026-08-20] concept | Atomización Estricta de la Sección 1.1 (*Data, Images, and Computer Graphics*)
- **Fuente**: `fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.).pdf` (Sección 1.1, Págs. 1–4)
- **Notas Creadas / Separadas Atómicamente**:
  1. [[data-images-and-computer-graphics.md]] (Visión de conjunto de la Sección 1.1).
  2. [[transformacion-datos-a-imagenes.md]] (Definición $\text{Datos} \to \text{Imágenes}$ y propósito de visualización).
  3. [[modelado-geometrico.md]] (Subdisciplina $\text{Datos} \to \text{Datos}$).
  4. [[renderizado-sintesis-de-imagen.md]] (Subdisciplina $\text{Datos} \to \text{Imágenes}$).
  5. [[procesamiento-de-imagenes.md]] (Subdisciplina $\text{Imágenes} \to \text{Imágenes}$).
  6. [[vision-por-computadora.md]] (Subdisciplina $\text{Imágenes} \to \text{Datos}$).
  7. [[computacion-grafica-en-movimiento.md]] (Sección 1.1.1: $\text{Datos}\times t \longleftrightarrow \text{Video}$).
  8. [[objeto-grafico.md]] (Sección 1.1.2: Abstracción unificadora $\mathcal{GO}$).
  9. [[integracion-multidisciplinar-grafica.md]] (Sección 1.1.3: Pipelines satelitales y médicos).
- **Notas Depuradas / Eliminadas**: Eliminadas notas de secciones posteriores no cubiertas aún (1.3 *Paradigma de los 4 Universos* y 1.5 *Reconstrucción e Interpolación*).
- **Actualizados**: [[index.md]], [[wiki/cursos/computacion-grafica.md]].
- **Aporte Clave**: Separación atómica estricta de cada concepto individual de la Sección 1.1 conforme a la lectura progresiva del libro de Gomes, Velho & Costa.

---

## [2026-08-20] concept | Ingestión y Extracción Visual de la Sección 1.4 (*Terrains and 2D Images*)
- **Fuente**: `fuentes/grafica/Computer Graphics  Theory and Practice (Gomes, Jonas Velho, Luiz Costa Sousa etc.).pdf` (Sección 1.4, Págs. 8–10)
- **Imágenes Extraídas a Alta Resolución**:
  - `fuentes/assets/figura-1-4-modelado-terreno-y-malla.png` (Gráfica de terreno de la Sierra de Aboboral y su malla regular).
  - `fuentes/assets/figura-1-5-modelado-imagen-2d-y-grafica.png` (Imagen en escala de grises y su superficie 3D de luminancia).
- **Notas Conceptuales Creadas**:
  1. [[modelado-de-terrenos.md]] (Función de altura $z = f(x,y)$, gráfica $\mathcal{G}(f)$, muestreo uniforme en grilla $P_x \times P_y$).
  2. [[modelado-de-imagenes-2d.md]] (Función de imagen $f: U \subset \mathbb{R}^2 \to [0,1]$, píxeles como muestras de luminancia).
  3. [[dualidad-terreno-imagen.md]] (Equivalencia $f: U \subset \mathbb{R}^2 \to \mathbb{R}$, curvas de nivel vs. isófotas, gradientes).
- **Actualizados**: [[index.md]], [[wiki/cursos/computacion-grafica.md]].
- **Aporte Clave**: Formalización matemática e incrustación directa de las figuras oficiales del libro para explicar la dualidad funcional entre topografía e imágenes digitales.

---

## [2026-08-20] structure | Reorganización Jerárquica de Carpetas en `wiki/conceptos/`
- **Estructura Creada**:
  - `wiki/conceptos/grafica/capitulo-01-introduccion/seccion-1-1-data-images-cg/` (8 notas atómicas de la Sec. 1.1).
  - `wiki/conceptos/grafica/capitulo-01-introduccion/seccion-1-4-modelos-ejemplo/` (3 notas atómicas de la Sec. 1.4 con figuras incrustadas).
  - `wiki/conceptos/estrategias/unidad-1-optimizacion-y-aproximacion/`
  - `wiki/conceptos/estrategias/unidad-2-fuerza-bruta-y-voraces/`
  - `wiki/conceptos/estrategias/unidad-3-recursivas-y-dinamica/`
  - `wiki/conceptos/general/` (Metodología y Arquitectura).
- **Actualizados**: [[index.md]], [[wiki/cursos/computacion-grafica.md]].
- **Aporte Clave**: Jerarquía modular limpia y escalable por capítulos, secciones y unidades académicas.
