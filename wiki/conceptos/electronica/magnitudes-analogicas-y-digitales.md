---
title: "Magnitudes Analógicas y Digitales"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concepto
  - domain/electronica
  - electronica/fundamentos
aliases:
  - "Magnitudes Analógicas"
  - "Magnitudes Digitales"
---

# 🌊 Magnitudes Analógicas vs. Digitales

En el corazón de la electrónica y la computación, la forma en que representamos la información (los "datos") dicta cómo diseñamos nuestros circuitos. El mundo real es continuo, pero las computadoras "piensan" en pasos discretos.

## 1. Magnitudes Analógicas (El Mundo Real)
Una magnitud analógica es aquella que toma **valores continuos** a lo largo del tiempo. Puede adoptar una infinidad de valores dentro de un rango específico.
* **Características:** Fluida, continua, sensible a la interferencia o ruido.
* **Ejemplos en la vida real:** La temperatura de una habitación (puede ser 24.1°C, 24.15°C, 24.156°C...), la presión acústica de una voz humana, la velocidad de un auto.
* **Matemáticamente:** Se modela como una función continua $f(t)$.

## 2. Magnitudes Digitales (El Mundo de la Computadora)
Una magnitud digital es aquella que toma un conjunto de **valores discretos** (escalonados). En la electrónica digital binaria (la que usamos en computación), los valores se limitan a solo dos estados.
* **Características:** Discreta, robusta contra el ruido eléctrico, fácil de almacenar y procesar.

* **Ejemplos:** Un interruptor de luz (Encendido / Apagado), los píxeles de una pantalla, un archivo de texto en disco.

  computador digital - sistema de procesamiento de información discreta
	Típico de un sistema digital es su manejo de elementos discretos de información, elementos discretos pueden ser impulsos eléctricos, Ios dígitos decimales, las letras de un alfabeto, las operaciones aritméticas, los símbolos de puntuación o cualquier otro conjunto de símbolos significativo.

> [!quote] Definición de M. Morris Mano
> *"Los elementos discretos de información se representan en un sistema digital por cantidades físicas llamadas señales. Las señales eléctricas tales como voltajes y corrientes son las más comunes. Las señales en los sistemas digitales electrónicos de la actualidad tienen solamente dos valores discretos y se dice que son binarios."* 
> — **Lógica Digital y Diseño de Computadores**, Cap. 1, Pág. 11.

* **Símbolos:** 
  * `0` lógico $\to$ Falso $\to$ Bajo voltaje (Ej. 0V)
  * `1` lógico $\to$ Verdadero $\to$ Alto voltaje (Ej. 5V o 3.3V)

---

## 📊 Comparativa Visual
Para entender la diferencia, observa cómo una señal analógica (que varía suavemente) es interpretada por un circuito digital binario. El circuito digital establece un umbral: todo lo que está arriba se lee como `1`, y lo que está abajo como `0`.

![[analog-vs-digital.png]]

---

## 🎨 Esquema Visual (Excalidraw)

![[esquema-magnitudes.excalidraw]]

---

> [!TIP] ¿Por qué las computadoras usan magnitudes digitales?
> Porque los componentes electrónicos que representan dos estados (transistores operando en corte/saturación) son extremadamente rápidos, predecibles, baratos de fabricar a escala nanométrica y no pierden información a causa del ruido eléctrico leve.

---
**Fuente / Contexto:**
* Concepto extraído de *Digital Logic Computer Design (Morris Mano)* - Cap. 1.
* Relacionado con: [[electronica-para-computacion|Hub de Electrónica para Computación]]
