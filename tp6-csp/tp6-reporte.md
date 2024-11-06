## EJERCICIO 1

Los componentes principales de una formulación CSP para el Sudoku son:

1. Variables: Cada celda vacía en el tablero de Sudoku 9x9 es una variable. En total, hay 81 variables, una para cada celda.
2. Dominios: El dominio de cada variable es el conjunto de números enteros del 1 al 9. Cada celda puede contener cualquiera de estos números.
3. Restricciones: se pueden dividir en tres categorías principales: 
	a) Restricciones de fila: cada número del 1 al 9 debe aparecer sólo una vez en cada fila. 
	b) Restricciones de columna: cada número del 1 al 9 debe aparecer sólo una vez en cada columna. 
	c) Restricciones de cuadrícula 3x3: cada número del 1 al 9 debe aparecer exactamente una vez en cada una de las 9 cuadrículas de 3x3.

Además, para las celdas que ya tienen un valor asignado en el puzzle inicial, se añade una restricción adicional que fija ese valor.

4. Formulación matemática: 
	1. Variables: X[i,j] para i, j ∈ {1, ..., 9} 
	2. Dominio: D(X[i,j]) = {1, 2, 3, 4, 5, 6, 7, 8, 9} 
	3. Restricciones: 
		1. Filas: ∀i ∈ {1, ..., 9}, AllDifferent(X[i,1], X[i,2], ..., X[i,9]) 
		2. Columnas: ∀j ∈ {1, ..., 9}, AllDifferent(X[1,j], X[2,j], ..., X[9,j]) 
		3. Cuadrículas 3x3: ∀k, l ∈ {0, 1, 2}, AllDifferent(X[3k+1,3l+1], X[3k+1,3l+2], X[3k+1,3l+3], X[3k+2,3l+1], X[3k+2,3l+2], X[3k+2,3l+3], X[3k+3,3l+1], X[3k+3,3l+2], X[3k+3,3l+3]) 
		Donde AllDifferent es la restricción global que asegura que todos los valores en el conjunto son diferentes.
5. Resolución: para resolver este CSP, se pueden utilizar algoritmos como backtracking con propagación de restricciones, forward checking, o algoritmos de consistencia de arco.

## EJERCICIO 2

 En primer lugar, asignamos:
-  WA=red y V=blue
-  Dominio inicial para todos los nodos: {red, green, blue}
-  D(WA) = {red}, D(V) = {blue}

Luego creamos una cola con todos los arcos: 
Q = { (WA,NT), (WA,SA), (NT,SA), (NT,Q), (SA,Q), (SA,NSW), (SA,V), (Q,NSW), (NSW,V) }

Y finalmente aplicamos el algoritmo AC-3:

a) Procesamos (WA,NT):

- D(NT) = {green, blue} (eliminamos red)
- Añadimos (NT,SA) y (NT,Q) a la cola

b) Procesamos (WA,SA):

- D(SA) = {green, blue} (eliminamos red)
- Añadimos (SA,NT), (SA,Q), (SA,NSW), (SA,V) a la cola

c) Procesamos (NT,SA): sin cambios

d) Procesamos (NT,Q): sin cambios

e) Procesamos (SA,Q): sin cambios

f) Procesamos (SA,NSW): sin cambios

g) Procesamos (SA,V):

- D(SA) = {green} (eliminamos blue porque V ya es blue)
- Añadimos (SA,NT), (SA,WA), (SA,Q), (SA,NSW) a la cola

h) Procesamos (SA,NT):

- D(NT) = {blue} (eliminamos green porque SA es green)
- Añadimos (NT,Q) a la cola

i) Procesamos (SA,WA): sin cambios (WA ya estaba fijo como red)

j) Procesamos (SA,Q):

- D(Q) = {red, blue} (eliminamos green porque SA es green)
- Añadimos (Q,NT), (Q,NSW) a la cola

k) Procesamos (SA,NSW):

- D(NSW) = {red} (eliminamos green y blue)
- Añadimos (NSW,Q), (NSW,V) a la cola

l) Procesamos (NT,Q):

- D(Q) = {red} (eliminamos blue porque NT es blue)
- Añadimos (Q,NSW) a la cola

m) Procesamos (Q,NSW):

- Detectamos inconsistencia: D(NSW) = {red} y D(Q) = {red}, pero son vecinos

En este punto, el algoritmo AC-3 detecta una inconsistencia. NSW y Q tienen que ser diferentes, pero ambos están forzados a ser rojos. Esto demuestra que la asignación parcial inicial WA=red, V=blue lleva a una inconsistencia en el problema de colorear el mapa de Australia.

## EJERCICIO 3

En un grafo de restricciones con estructura de árbol, cada arco en el algoritmo AC-3 se procesa para analizar la consistencia como máximo una vez.
Si n es el número de variables, en un árbol CSP habrá n-1 arcos.
Revisar un arco toma O(d<sup>2</sup>).
Luego la complejidad del algoritmo AC-3 resulta de O(nd<sup>2</sup>)

## EJERCICIO 4

Para actualizar el número restante de valores consistentes en forma eficiente, al momento de eliminar un valor w del dominio de X<sub>i</sub>, para cada valor v en el dominio de cada X<sub>k</sub> conectado a X<sub>i</sub>, verificamos la consistencia y decrementamos el valor de un contador X<sub>kv</sub> cada vez que w resulte no ser consistente con v. Cuando ese contador llega a 0, se debe eliminar v del dominio de X<sub>k</sub>.

Dado que por cada nodo en el grafo de restricciones, se revisan todos sus posibles nodos adyacentes, esto implica una complejidad de O(n<sup>2</sub>). Y como por cada nodo se revisan los valores del dominio de cada uno, el tiempo total resulta de O(n<sup>2</sup>d<sup>2</sup>).

## EJERCICIO 5

a) 
1. Conceptos preliminares:
    - Un árbol es un grafo conexo sin ciclos.
    - La 2-consistencia (consistencia de arco) significa que para cualquier par de variables adyacentes, cualquier valor en el dominio de una variable es consistente con al menos un valor en el dominio de la otra variable.
    - La n-consistencia implica que cualquier asignación consistente de valores a n-1 variables puede extenderse a una asignación consistente que incluya cualquier n-ésima variable.
2. Hipótesis:
    - Tenemos un CSP cuyo grafo de restricciones es un árbol.
    - El CSP es 2-consistente (tiene consistencia de arco).
3. Demostración por inducción: 
	1. Base: Para n = 2, la 2-consistencia es equivalente a la n-consistencia por definición. 
	2. Paso inductivo: Asumamos que la propiedad se cumple para k variables (2 ≤ k < n). Demostraremos que también se cumple para k+1 variables. 
		a) Consideremos una asignación consistente de k variables en el árbol. 
		b) Sea X la (k+1)-ésima variable que queremos asignar. 
		c) Como el grafo es un árbol, X está conectada al subárbol de las k variables ya asignadas a través de una única arista (restricción binaria) con una variable Y ya asignada. 
		d) Debido a la 2-consistencia, sabemos que existe al menos un valor en el dominio de X que es consistente con el valor asignado a Y. 
		e) Este valor de X será consistente con todas las demás variables ya asignadas, ya que no hay conexión directa entre X y esas variables (por la propiedad del árbol). 
		f) Por lo tanto, podemos extender la asignación consistente de k variables a k+1 variables.
		
b) Lo demostrado en el inciso a es suficiente debido a que la 2-consistencia garantiza que siempre habrá un valor consistente disponible para cada variable. Luego al asignar valores desde las hojas hacia la raíz, por ejemplo, cada nueva asignación solo necesita ser consistente con su padre en el árbol.

## EJERCICIO 7

La siguiente imagen corresponde al análisis de los tiempos de ejecución y del número de estados explorados para los algoritmos Backtracking (BT) y Forward Chaining (FC):

![[times_and_states.png]]

Y las siguientes dos figuras (tiempo y estados explorados, respectivamente) representan el mismo análisis pero para los algoritmos Hill Climbing, Simulated Annealing y Genético implementados en el trabajo práctico anterior:

![[tp5_times.png]]

![[tp5_states.png]]

Del análisis de estas figuras, es posible observar que Forward Checking es el algoritmo que mejores resultados obtiene por un margen significativo, tanto en número de estados explorados como en tiempo de ejecución. El rendimiento de los algoritmos de Backtracking, Hill Climbing y Simulated Annealing resulta similar, con una ligera ventaja por parte del algoritmo de Backtracking. Y por último, el Algoritmo Genético se muestra como aquel con el peor desempeño de todos.  