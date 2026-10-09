### 1. ¿Es una estrategia rápida y eficiente?

**No es rápida, pero es mucho más "inteligente" y eficiente que la Fuerza Bruta.** Backtracking es, en esencia, una Fuerza Bruta optimizada.

- **El secreto de su funcionamiento:** Construye la solución paso a paso (como caminar por un laberinto). En el momento en que se da cuenta de que el camino actual rompe las reglas del problema o choca con una pared, **retrocede** al paso anterior (hace "vuelta atrás") y prueba un camino distinto. Al hacer esto, descarta ramas enteras de posibilidades inútiles de golpe, ahorrándole muchísimo trabajo inútil a la computadora.
    

### 2. ¿Problemas Fáciles o Difíciles?

**Pertenece a: Problemas Difíciles (Clase NP / Intratables)**

- Se utiliza principalmente en problemas de "Satisfacción de Restricciones" (como resolver un Sudoku, el problema de las N-Reinas en ajedrez o salir de un laberinto). Aunque es más inteligente que la Fuerza Bruta porque corta caminos muertos, en el peor de los casos su tiempo de ejecución sigue siendo exponencial ($O(2^n)$) o factorial ($O(n!)$). Por lo tanto, la computadora colapsará si intentas usarlo para millones de datos.
    

### 3. ¿Método Exacto o Aproximado?

**Pertenece a: Método Exacto**

- Nunca hace estimaciones ni tira dados al azar. Explora el árbol de decisiones de forma metódica, garantizando al 100% que encontrará la solución perfecta y correcta (o que te devolverá absolutamente todas las soluciones posibles si el problema tiene más de una). Solo se detendrá cuando haya evaluado o descartado lógicamente todos los caminos.