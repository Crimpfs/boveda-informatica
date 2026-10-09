### 1. ¿Es una estrategia rápida y eficiente?

**Totalmente sí.** De hecho, su único propósito de existir es agarrar un problema que tomaría años resolver y aplastarlo para que se resuelva en milisegundos.

- **El secreto de su velocidad:** Tiene "memoria". Mientras que la Fuerza Bruta recalcula el mismo subproblema tontamente una y otra vez, la Programación Dinámica lo calcula **una sola vez**, lo anota en una tabla (técnica de Tabulación) y lo recicla cada vez que lo vuelve a necesitar. Al no repetir trabajo, la computadora vuela.

### 2. ¿Problemas Fáciles o Difíciles?

**Pertenece a: Problemas Fáciles (Clase P)**

- Aunque a los humanos nos cueste mucho programarla y plantear su ecuación matemática sea un dolor de cabeza, para la computadora es un gran alivio. Transforma tiempos de ejecución monstruosos e intratables (exponenciales como $O(2^n)$) en tiempos rápidos y manejables (polinómicos, como $O(n^2)$ u $O(n)$).


### 3. ¿Método Exacto o Aproximado?

**Pertenece a: Método Exacto**

- Nunca te va a dar una respuesta heurística, "a medias" o aproximada. Como siempre evalúa el panorama completo (gracias a que guarda el historial de las mejores decisiones en su tabla) y se basa en el Principio de Optimalidad matemático, te garantiza encontrar la solución **100% óptima y perfecta** en cada ejecución.