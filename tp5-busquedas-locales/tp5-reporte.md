# INFORME TP5: BÚSQUEDAS LOCALES

## **INTRODUCCIÓN**

En el presente informe se explora y compara el rendimiento de algoritmos de búsqueda local como son Hill Climbing, Simulated Annealing y un tipo de algoritmo evolutivo denominado Algoritmo Genético, aplicados específicamente al problema de las N-Reinas.
## **MARCO TEÓRICO**

Los algoritmos de búsqueda local son técnicas de optimización utilizadas para resolver problemas complejos en los que se busca encontrar la mejor solución dentro de un espacio de búsqueda muy grande. Estos algoritmos comienzan con una solución inicial y la mejoran iterativamente, explorando el "vecindario" de soluciones cercanas.
### 1. Hill Climbing

Hill Climbing es uno de los algoritmos de búsqueda local más simples. Su funcionamiento puede compararse a escalar una colina, busca moverse siempre hacia arriba hasta alcanzar un pico.

#### 1.1. Características principales:

- Comienza con una solución aleatoria.
- En cada iteración, evalúa las soluciones vecinas.
- Se mueve a la mejor solución vecina si es mejor que la actual.
- Se detiene cuando no hay mejores soluciones vecinas.
#### 1.2 Pseudocódigo:

``` 
función HillClimbing(problema):
    actual = generarSoluciónInicial(problema)
    mientras True:
        vecino = mejorVecino(actual)
        si valor(vecino) <= valor(actual):
            retornar actual
        actual = vecino
```
#### 1.3 Ventajas y desventajas:

- Ventaja: simple y rápido.
- Desventaja: puede quedar atrapado en óptimos locales.

### 2. Simulated Annealing

Simulated Annealing se inspira en el proceso de recocido en metalurgia. Permite movimientos a soluciones peores con cierta probabilidad, que disminuye con el tiempo.
#### 2.1 Características principales:

- Comienza con una solución aleatoria y una temperatura alta.
- En cada iteración, considera un vecino aleatorio.
- Acepta mejores soluciones siempre, y peores con una probabilidad que depende de la temperatura.
- La temperatura disminuye gradualmente, reduciendo la probabilidad de aceptar peores soluciones.
#### 2.2 Pseudocódigo

```
función SimulatedAnnealing(problema, tempInicial, tasaEnfriamiento, iteraciones):
    actual = generarSoluciónInicial(problema)
    mejor = actual
    temp = tempInicial
    para i de 1 a iteraciones:
        vecino = vecinoAleatorio(actual)
        delta = valor(vecino) - valor(actual)
        si delta > 0 o random() < exp(delta / temp):
            actual = vecino
        si valor(actual) > valor(mejor):
            mejor = actual
        temp = temp * tasaEnfriamiento
    retornar mejor
```
#### 2.3 Ventajas y desventajas:

- Ventaja: puede escapar de óptimos locales.
- Desventaja: el rendimiento depende de la configuración de los parámetros.

### 3. Algoritmos Genéticos

Los Algoritmos Genéticos se inspiran en la teoría de la evolución, utilizando conceptos como selección natural, cruce y mutación.
#### 3.1 Características principales:

- Trabaja con una población de soluciones.
- Utiliza operadores genéticos (selección, cruce, mutación) para evolucionar la población.
- Cada generación tiende a mejorar la calidad de las soluciones.
#### 3.2 Pseudocódigo:

```
función AlgoritmoGenético(tamañoPoblación, generaciones):
    población = generarPoblaciónInicial(tamañoPoblación)
    para g de 1 a generaciones:
        nuevaPoblación = []
        mientras tamaño(nuevaPoblación) < tamañoPoblación:
            padres = seleccionar(población)
            hijo = cruzar(padres)
            hijo = mutar(hijo)
            nuevaPoblación.agregar(hijo)
        población = nuevaPoblación
    retornar mejorIndividuo(población)
```
#### 3.3 Ventajas y desventajas:

- Ventaja: pueden explorar eficientemente espacios de búsqueda grandes y complejos.
- Desventaja: pueden ser computacionalmente costosos y habitualmente requieren configuraciones de parámetros muy específicas para sacarles provecho.

## **DISEÑO EXPERIMENTAL**

Para evaluar el desempeño de cada tipo de algoritmo, ejecutamos un total de 30 veces cada uno para casos de tableros con 4, 8 y 10 reinas, y volcamos los resultados en diagramas de caja y extensiones que nos permiten visualizar cómo se distribuye el número de estados explorados previamente a encontrar una solución así como el tiempo empleado por cada algoritmo para encontrar dicha solución.

Para una ejecución en particular de cada algoritmo, graficamos también la evolución de la función H a medida que avanzan las iteraciones.

Establecemos en todos los casos un máximo de 10000 estados, y consideramos una población de 100 individuos para el caso del Algoritmo Genético.

## **ANÁLISIS Y EVALUACIÓN DE RESULTADOS**

A continuación se muestran los resultados para el número de estados explorados por cada algoritmo previo a encontrar una solución óptima (se consideran sólo aquellas veces que se llega a un resultado óptimo):

![[n_queens_states_boxplot.png]]

El siguiente gráfico, por otro lado, permite observar la distribución del tiempo de ejecución de cada algoritmo:

![[n_queens_times_boxplot.png]]

En las siguientes figuras, se representa la evolución de la función H para una ejecución en particular, en los casos de 4, 8 y 10 reinas:

![[h_evol_Hill Climbing_4.png]]

![[h_evol_Hill Climbing_8.png]]

![[h_evol_Hill Climbing_10.png]]

![[h_evol_Simulated Annealing_4.png]]

![[h_evol_Simulated Annealing_8.png]]

![[h_evol_Simulated Annealing_10.png]]

![[h_evol_Genetic Algorithm_4.png]]

![[h_evol_Genetic Algorithm_8.png]]

![[h_evol_Genetic Algorithm_10.png]]

## **CONCLUSIÓN**

Teniendo en cuenta el número de veces que cada algoritmo llegó a una solución óptima (que en los gráficos se ve reflejado en una mayor cantidad de estados analizados, ya que sólo se consideran los datos para los cuales se llegó a una solución óptima) y el tiempo en promedio empleado en cada caso, el algoritmo Simulated Annealing se postula como el más adecuado para resolver el problema de las 8 reinas planteado.