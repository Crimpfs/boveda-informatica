---
title: "Cronograma y Tabla de Variables"
type: concept
created: 2026-08-20
updated: 2026-08-20
tags:
  - wiki/concepto
  - domain/electronica
  - electronica/logica-digital
aliases:
  - "Cronograma Digital"
  - "Tabla de Variables"
  - "Tabla de Verdad"
  - "Timing Diagram"
---

# ⏱️ Cronogramas y Tablas de Variables (Digital)

Para analizar el comportamiento de un circuito digital, necesitamos herramientas que nos muestren cómo cambian los valores lógicos (`0` y `1`). Las dos herramientas principales utilizadas en ingeniería electrónica son el **Cronograma de Señales** y la **Tabla de Variables (Tabla de Verdad)**.

---

## 1. La Tabla de Variables (Tabla de Verdad)

Es una tabla matemática que describe de manera exhaustiva y estática el comportamiento de un sistema digital. 
* Muestra **todas las combinaciones posibles** que pueden tener las señales de **entrada** (variables independientes).
* Muestra cuál será la **salida** resultante (variable dependiente) para cada combinación.

### Ejemplo: Un Sistema de Alarma Simple (Compuerta AND)
* `A`: Sensor de Puerta (0=Cerrada, 1=Abierta)
* `B`: Sistema Activado (0=Apagado, 1=Encendido)
* `S (Salida)`: Suena la Alarma (1=Sí)

| Entrada A | Entrada B | Salida S (A AND B) |
| :---: | :---: | :---: |
| `0` | `0` | **0** |
| `0` | `1` | **0** |
| `1` | `0` | **0** |
| `1` | `1` | **1** |

> [!NOTE] Crecimiento Exponencial
> Si un circuito tiene $n$ variables de entrada, su tabla de verdad tendrá exactamente $2^n$ filas. (Ej. 3 variables = 8 filas).

---

## 2. El Cronograma (Timing Diagram)

Mientras que la tabla nos dice *qué* va a pasar teóricamente, el **Cronograma** nos dice *cuándo* está pasando y *cómo fluye* en la realidad.
* Es una gráfica que representa **el nivel lógico (0 o 1) en función del tiempo (eje X)**.
* Permite observar comportamientos dinámicos: retardos, fallos transitorios, y el ritmo del sistema guiado por un reloj (Clock).

### Visualización del Flujo Dinámico

A continuación, un cronograma típico donde observamos una señal del "Reloj" del sistema y una "Señal A" que cambia de estado con el paso del tiempo.

![[cronograma-digital.png]]

### Elementos de un Cronograma
1. **Flancos de Subida (Rising Edge):** El instante exacto donde la señal pasa de `0` a `1`. En circuitos síncronos, muchas acciones se disparan solo en este flanco.
2. **Flancos de Bajada (Falling Edge):** El paso de `1` a `0`.
3. **Señal de Reloj (CLK):** Es el "metrónomo" del hardware digital (como el procesador de tu computadora). Marca el paso rítmico con una onda cuadrada constante.

---
**Contexto Teórico:**
* Estos conceptos son la base del *Diseño Lógico y de Computadoras*. (Basado en el libro de *Morris Mano*).
* Herramientas de visualización esenciales en [[wiki/cursos/electronica-para-computacion|Electrónica para Computación]].
