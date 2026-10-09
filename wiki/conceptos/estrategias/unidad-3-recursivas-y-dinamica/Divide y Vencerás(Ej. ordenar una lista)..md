### 1. ¿Es una estrategia rápida y eficiente?
Su propósito es tomar un conjunto de datos grande y hacerlo manejable cortándolo en pedazos cada vez más pequeños.

- **El secreto de su velocidad:**  Su secreto es la ==**recursividad fraccionada**==. Cada vez que partes un problema a la mitad (como buscar en un diccionario), descartas automáticamente miles de operaciones. _Nota clave:_ No guarda datos en tablas; si un subproblema se repite, lo volverá a calcular desde cero (por eso sus subproblemas deben ser siempre **independientes**).

---

### 2. ¿Problemas Fáciles o Difíciles?

**Pertenece a: Problemas Fáciles (Clase P)**
- Es la herramienta estrella para crear algoritmos ultra rápidos en problemas tratables (como ordenar, buscar o multiplicar matrices). Su magia matemática consiste en usar logaritmos; logra tiempos de ejecución increíblemente veloces como:

$O(\log n)$ calcular potencia.
```
def potencia(x, n):
    # 1. Caso Base: Cualquier número elevado a 0 es 1
    if n == 0:
        return 1
    
    # 2. Dividir y Vencer: Calculamos la potencia pero solo hasta la mitad
    mitad = potencia(x, n // 2)
    
    # 3. Combinar: Construimos el resultado final
    if n % 2 == 0:
        # Si el exponente era par (ej. x^4 = x^2 * x^2)
        return mitad * mitad
    else:
        # Si el exponente era impar (ej. x^5 = x^2 * x^2 * x)
        return mitad * mitad * x
```

- **Ecuación de Recurrencia:**
$$T(n) = T(n/2) + O(1)$$

- **Interpretación:** Hacemos **1** sola llamada recursiva con la mitad del exponente ($n/2$). El costo de multiplicar el resultado al final es una operación simple y constante ($O(1)$). Por el Teorema Maestro, esto resulta en una complejidad de $O(\log n)$.

$O(n \log n)$ como en el  3 Merge Sort.
```
def merge_sort_3(lista):
    # 1. Caso Base: Una lista de 1 o 0 elementos ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # 2. Dividir: Partimos la lista en 3 pedazos (tercios)
    tercio = len(lista) // 3
    
    # Cortamos la lista usando índices
    izq = lista[0 : tercio]
    centro = lista[tercio : 2 * tercio]
    der = lista[2 * tercio : len(lista)]
    
    # 3. Vencer: Llamamos a la recursividad para ordenar cada tercio
    izq_ordenado = merge_sort_3(izq)
    centro_ordenado = merge_sort_3(centro)
    der_ordenado = merge_sort_3(der)
    
    # 4. Combinar: Juntamos las 3 listas ordenadas en una sola
    # (Se asume la existencia de una función merge_3 que compara e intercala los datos)
    return fusionar_3_listas(izq_ordenado, centro_ordenado, der_ordenado)

# La función de combinación tomaría el elemento más pequeño 
# de las tres listas uno por uno hasta vaciarlas.
```

- **Ecuación de Recurrencia:**
 
$$T(n) = 3T(n/3) + O(n)$$

- **Interpretación:** Hacemos **3** llamadas recursivas, cada una con un tercio de los datos ($n/3$). Juntar los tres arreglos ordenados nos obliga a recorrer todos los elementos de nuevo, lo que cuesta un tiempo lineal ($O(n)$). El resultado final de esta ecuación es $O(n \log n)$.


$O(\log n)$ como en la Búsqueda Binaria.
```
def busqueda_binaria(lista, inicio, fin, objetivo):
    # 1. Caso Base: Si el inicio supera al fin, el número no existe
    if inicio > fin:
        return -1 
    
    # 2. Dividir: Encontramos el punto medio
    medio = (inicio + fin) // 2
    
    # 3. Combinar / Vencer: 
    if lista[medio] == objetivo:
        return medio  # ¡Lo encontramos!
        
    elif lista[medio] > objetivo:
        # Si el medio es mayor, el objetivo debe estar en la mitad IZQUIERDA.
        # Descartamos la derecha y llamamos a la recursividad.
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)
        
    else:
        # Si el medio es menor, el objetivo debe estar en la mitad DERECHA.
        # Descartamos la izquierda y llamamos a la recursividad.
        return busqueda_binaria(lista, medio + 1, fin, objetivo)
```

- **Ecuación de Recurrencia:**
$$T(n) = T(n/2) + O(1)$$

- **Interpretación:** Aunque el problema se corta en 2 pedazos, solo procesamos **1** pedazo ($a=1$) de tamaño $n/2$. Comparar el número y decidir qué mitad descartar es un simple "if" que toma tiempo constante ($O(1)$). El resultado es un algoritmo ultra rápido de $O(\log n)$.

RECURSIVIDAD 
$$T(n) = aT\left(\frac{n}{b}\right) + O(n^d)$$

- **$a$:** En cuántos pedazos divido el problema.
- **$b$:** De qué tamaño es cada pedazo respecto al original.
- **$O(n^d)$:** Cuánto me cuesta partir el problema y/o volver a unir los pedazos al final.

Ese trabajo se divide en dos acciones: el costo de **Dividir** y el costo de **Mezclar**. Tomas el mayor de los dos, y ese será tu exponente $d$.  

operaciones ,if (0(1))
for,while (0(n))

---

### 3. ¿Método Exacto o Aproximado?

**Pertenece a: Método Exacto**
- Nunca hace estimaciones ni tira dados al azar. Garantiza al 100% que al resolver los problemas pequeños y volver a juntar sus piezas la fase de "combinar", ==el resultado final será matemáticamente perfecto y correcto== en cada ejecución.



