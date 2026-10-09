### 1. ¿Es una estrategia rápida y eficiente?

**¡Para nada! Es exactamente lo contrario.** Es la estrategia más ineficiente y lenta que existe en el diseño de algoritmos. Su único método es probar absolutamente todas las combinaciones posibles una por una, de principio a fin, sin ningún tipo de atajo.

- **El secreto de su lentitud:** Es "ciega". No tiene memoria, no usa lógica matemática para descartar opciones inútiles y no aprende de sus errores. Al calcular todo de forma completamente exhaustiva, provoca que el procesador de la computadora se sature rápidamente (sufriendo de lo que se conoce como "explosión combinatoria").


### 2. ¿Problemas Fáciles o Difíciles?

**Pertenece a: Problemas Difíciles (Clase NP / Intratables)**

- Aunque a los humanos nos resulte **muy fácil programarla** (casi siempre son solo ciclos repetitivos básicos uno dentro de otro), para la computadora es una pesadilla absoluta. Sus tiempos de ejecución son monstruosos e inmanejables para problemas grandes, creciendo de forma exponencial (como $O(2^n)$) o factorial (como $O(n!)$). Si le das un volumen grande de datos, la computadora colapsará antes de terminar.


### 3. ¿Método Exacto o Aproximado?

**Pertenece a: Método Exacto**

- Nunca te va a dar una respuesta "a medias" o aproximada. Como literalmente genera y evalúa todas y cada una de las posibilidades existentes en el universo del problema sin saltarse ni una sola, te garantiza encontrar la solución **100% óptima y perfecta**... siempre y cuando tengas el tiempo suficiente (horas, años o milenios) para esperar a que termine de calcular.