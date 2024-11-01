## A. Resultados evaluación dataset tennis.csv

![[Pasted image 20241031235536.png]]

## B. Estrategias para datos de tipo real

Las principales estrategias para construir árboles de decisión con datos de tipo real (también llamados continuos o numéricos), son:

1. **Selección de Puntos de Corte**: Cuando una variable es continua, en lugar de dividir los datos en categorías discretas, el árbol de decisión elige puntos de corte específicos que dividen el rango de valores en dos subconjuntos. Por ejemplo, para una variable como "edad", el modelo podría decidir dividir en "edad < 30" y "edad ≥ 30". Estos puntos de corte se seleccionan para maximizar la homogeneidad de los grupos resultantes en términos de la variable objetivo.
	- _Algoritmo de Umbral Óptimo_ (_Optimal Split Point Algorithm_): Este algoritmo examina múltiples puntos de corte en los datos para encontrar aquel que maximice la pureza de los nodos. Una técnica común es probar cada valor de la variable continua y calcular la métrica de impureza en cada punto, eligiendo el que mejor divide los datos.
	- _Método de Cuarteo_ (_Quantile-based Split_): Para grandes conjuntos de datos, en lugar de probar cada valor, se prueban cuartiles, deciles u otros percentiles como puntos de corte, lo cual reduce la carga computacional sin perder precisión.


2. **Medidas de Impureza (Criterios de División)**: Para seleccionar el mejor punto de corte, el árbol calcula alguna medida de impureza, como el _Gini impurity_, la _entropía_ o la _ganancia de información_. Estas métricas permiten identificar el punto de corte que genera los subconjuntos más puros en términos de la variable objetivo. Se elige el valor que minimiza la impureza en los nodos hijos, logrando que cada subconjunto sea lo más homogéneo posible.
    - _Impureza de Gini_: Utilizado en algoritmos como CART (_Classification and Regression Trees_), mide la probabilidad de clasificar incorrectamente un elemento si se elige aleatoriamente. El punto de corte se selecciona para minimizar la impureza Gini de los nodos resultantes.
	- _Entropía_ y _Ganancia de Información_: Utilizados en árboles de decisión basados en información (como ID3 o C4.5), calculan la entropía de los nodos. El objetivo es maximizar la ganancia de información, es decir, la diferencia de entropía entre el nodo padre y los nodos hijos después de cada división.
	- _Reducción de la Varianza_: En problemas de regresión, el punto de corte puede seleccionarse minimizando la varianza de los valores de la variable objetivo en los nodos hijos, una técnica utilizada en árboles de regresión.
	
3. **Divisiones Recursivas**: Una vez que se encuentra el mejor punto de corte para una variable continua, el proceso se repite de forma recursiva en cada subconjunto creado, permitiendo múltiples cortes en una misma variable si esto mejora la precisión del modelo. Así, un árbol puede tener varios cortes en la misma variable continua, dividiendo en diferentes rangos que representen distintos niveles de la variable.
    - _CART (Classification and Regression Trees)_: Este algoritmo aplica divisiones recursivas para clasificar o predecir valores continuos, ajustando múltiples cortes en una misma variable si mejora la precisión del árbol.
	- _CHAID (Chi-square Automatic Interaction Detection)_: Aunque originalmente desarrollado para datos categóricos, CHAID puede adaptar sus divisiones recursivas a variables continuas mediante agrupación basada en pruebas de Chi-cuadrado.
	
1. **Parada y Poda del Árbol**: Para evitar el sobreajuste, se pueden aplicar técnicas de parada y poda. El árbol de decisión puede detener la creación de nodos adicionales si la ganancia en pureza es mínima o si el subconjunto de datos en un nodo es muy pequeño. La poda (post-poda) consiste en reducir nodos o ramas que no aportan significativamente a la precisión, mejorando la generalización.
    - _Poda de Costo-Complejidad_ (_Cost Complexity Pruning_): En este método (usado en CART), se aplica una penalización por complejidad al modelo y se reducen ramas completas cuando la mejora en precisión no justifica el incremento en la complejidad.
	- _Error de Validación Cruzada_: Durante la construcción, se pueden evaluar distintos tamaños de árbol usando validación cruzada. Una vez determinado el tamaño óptimo, se detiene la construcción de ramas adicionales.
	- _Post-Poda con Reducción de Error_: Primero se construye el árbol completo, y luego se evalúan ramas y nodos para ver si eliminarlos mejora la precisión en un conjunto de validación.
1. **Escalado de Datos**: Aunque no es estrictamente necesario en los árboles de decisión, en algunos casos se puede realizar un escalado de los datos para mejorar la estabilidad del modelo. Esto puede ser útil si se usa junto a algoritmos como _random forests_, donde cada árbol puede considerar distintas combinaciones de variables.
    - Aunque el escalado no es obligatorio en árboles de decisión, el _Escalado Estándar_ (_Standard Scaling_) o la _Normalización_ pueden ser útiles si se combinan con otros métodos (como en los _Random Forests_), ayudando a equilibrar el impacto de diferentes variables continuas.
	- _Ponderación de Variables_: En algunos árboles más avanzados, se pueden aplicar pesos a las variables continuas escaladas, haciendo que algunas divisiones sean preferidas en función de su importancia relativa.

Estas estrategias permiten que los árboles de decisión puedan trabajar de manera eficiente y precisa con datos continuos, encontrando divisiones significativas sin perder la interpretabilidad que caracteriza a estos modelos.