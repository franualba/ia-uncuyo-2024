# **Transferencia de características musicales entre canciones**

**CÓDIGO DEL PROYECTO**: MUTRAMI (Music Track Mixer)

**INTEGRANTES**: Adrián Zangla y Francisco Alba

<<<<<<< Updated upstream
## DESCRIPCIÓN:
El mundo de la música, concretamente de la composición musical, se presenta habitualmente complejo y desafiante en el mejor de los casos. En los últimos años, y con la idea de complementar o facilitar el proceso creativo que conlleva producir música, se han desarrollado múltiples enfoques que permiten crear composiciones musicales de forma artificial empleando técnicas de aprendizaje automático.
Este proyecto tiene como objetivo explorar el funcionamiento de algunas de esas técnicas, y utilizarlas para lograr transferir características musicales específicas de una canción a otra. Buscamos así componer una nueva canción que mezcle ciertas propiedades deseadas de dos canciones o pistas musicales existentes.

## OBJETIVOS:
- Identificar y extraer las características musicales clave de cada una de las canciones de origen.
- Desarrollar un algoritmo capaz de transferir estas características de una canción a otra, conservando la estructura y armonía de la canción de destino.
- Evaluar la calidad de la canción resultante en términos de similitud con la canción objetivo y coherencia musical.

## ALCANCE:
- El proyecto se enfocará en la transferencia de elementos como ritmo, melodía, armonía y timbre entre las canciones.
- Se utilizarán técnicas de aprendizaje de máquina, como algoritmos genéticos y redes neuronales, para lograr la transferencia de características.

## LIMITACIONES:
=======
### DESCRIPCIÓN:
El mundo de la música, concretamente de la composición musical, se presenta habitualmente complejo y desafiante en el mejor de los casos. En los últimos años, y con la idea de complementar o facilitar el proceso creativo que conlleva producir música, se han desarrollado múltiples enfoques que permiten crear composiciones musicales de forma artificial empleando técnicas de aprendizaje automático.
Este proyecto tiene como objetivo explorar el funcionamiento de algunas de esas técnicas, y utilizarlas para lograr transferir características musicales específicas de una canción a otra. Buscamos así componer una nueva canción que mezcle ciertas propiedades deseadas de dos canciones o pistas musicales existentes.

### OBJETIVOS:
- Identificar y extraer las características musicales clave de cada una de las canciones de entrada.
- Desarrollar un algoritmo capaz de "transferir" estas características de una canción a otra, conservando la esencia de la canción de destino.
- Evaluar la calidad de la canción resultante en términos de similitud con la canción objetivo y coherencia musical.

### ALCANCE Y LIMITACIONES:
- Se utilizarán técnicas de aprendizaje de máquina, como algoritmos genéticos (y posiblemente redes neuronales) para lograr la transferencia de características.
>>>>>>> Stashed changes
- La calidad de la canción resultante dependerá de la complejidad de las canciones de origen y la dificultad de transferir sus características.
- El proyecto priorizará trabajar con archivos de audio en formato MIDI, ya que:
	- El protocolo MIDI (Musical Instrument Digital Interface) representa la música como una secuencia de eventos discretos (nota encendida, nota apagada, tono, velocidad, etc.) en lugar de como una forma de onda de audio continua. Esto facilita el análisis de la estructura y las características musicales.
	- Los archivos MIDI son compactos y fáciles de procesar en comparación con las grabaciones de audio completas. Esto permite que el sistema de generación de música trabaje de manera eficiente con múltiples pistas de ejemplo.
	- MIDI proporciona acceso a los bloques de construcción fundamentales de la música, como tonos, ritmos y dinámicas. Esto permite que el sistema extraiga y recombine los elementos musicales clave que definen un estilo en particular.
	- MIDI es un formato estándar compatible con una amplia gama de software y hardware musical. Esto facilita la integración del sistema de generación de música con otras herramientas para crear, editar y reproducir la salida.
	- Dado que MIDI constituye un lenguaje, resulta razonable pensar que los modelos de machine learning actuales puedan sacar provecho del mismo como lo hacen con otros lenguajes y mejorar entonces las posibilidades de obtener los resultados esperados.
- Teniendo en cuenta los siguientes conceptos musicales:
	- **Melodía**: secuencia de notas musicales que se perciben como una sola entidad. Suele ser la "línea" o "frase" musical que destaca y es reconocida en una canción o pieza instrumental. Es la parte de la música que se "canta" o que tarareamos, formada por la sucesión de notas (ó silencios) con alturas y duraciones específicas.
	- **Ritmo**: patrón de sonidos y silencios en el tiempo, la estructura temporal de la música. Organiza la duración de las notas, su repetición y el espacio entre ellas, creando patrones y acentuaciones que dan sentido al flujo musical. Define la velocidad o tempo de una pieza.
	- **Armonía**: combinación de varias notas que suenan simultáneamente, creando acordes y progresiones que apoyan a la melodía. Da profundidad y "color" a la música, y suele estar en las notas de acompañamiento. Estas notas se combinan de formas específicas que pueden dar sensaciones de estabilidad (consonancia) o tensión (disonancia), que se resuelven dentro de la estructura musical.
	En primera instancia consideraremos entonces enfocarnos sólamente en el manejo de la melodía, dejando de lado el ritmo y la armonía. Nos concentraremos así en música monofónica, donde se ejecuta a lo sumo una única nota a la vez en un momento determinado. Esto nos permitirá tener una mejor percepción de la complejidad de la tarea, y evaluar la posibilidad de manejar también el ritmo y la armonía una vez lograda la adaptación de la melodía.

<<<<<<< Updated upstream

## FORMA DE EVALUACIÓN:
- Con el propósito de construir una métrica objetiva que permita evaluar la calidad de los resultados obtenidos, se considerarán las siguientes características musicales de los archivos a procesar:

### 1. **Coherencia rítmica y textural**
   - **Definición**: Evalúa la estructura y la densidad rítmica de la canción, incluyendo la distribución de duraciones de las notas y su agrupamiento en patrones.
   - **Objetivo**: Medir cómo el ritmo original influye en la pieza transformada, asegurando que la canción mantiene una consistencia rítmica y una "textura" que le dé carácter (denso, pausado, etc.).
   - **Medición**: 
       - **Patrones rítmicos**: Analizar secuencias de duración y repetición de notas o grupos de notas (motivos rítmicos), comparando con patrones en la canción original.
       - **Densidad**: Calcular la cantidad promedio de notas en intervalos regulares (e.g., cada compás o sección). Una densidad rítmica alta indica más notas por intervalo de tiempo, mientras que una baja sugiere pausas o menor actividad.
       - **Duración media**: Calcular la duración promedio de las notas en ambas canciones y verificar que se mantienen en un rango similar.

### 2. **Cohesión melódica**
   - **Definición**: Mide la forma y continuidad de la melodía a través del contorno melódico, los intervalos entre notas, y el rango de notas en la composición.
   - **Objetivo**: Asegurar que la melodía transformada mantiene un estilo melódico parecido al de la canción de origen, conservando la relación entre notas y la forma general.
   - **Medición**: 
       - **Contorno melódico**: Analizar la dirección de las notas (ascendente, descendente o estática) en ambos temas y calcular la similitud de las secuencias.
       - **Distribución de intervalos**: Determinar la frecuencia de intervalos específicos entre notas (e.g., terceras mayores, cuartas justas) y comparar la proporción de cada uno con la canción de origen.
       - **Rango de notas**: Medir la nota más alta y la más baja en cada canción. El rango de la canción transformada debería mantenerse similar para reflejar la "altura" del estilo original.

### 3. **Estructura y repetición**
   - **Definición**: Evalúa cómo se organizan y repiten frases o motivos musicales, lo cual da forma y cohesión a la estructura de la canción.
   - **Objetivo**: Verificar que la canción transformada no sólo sea rítmica y melódicamente coherente, sino que también respete la organización estructural de frases o motivos, logrando una estructura con sentido.
   - **Medición**: 
       - **Identificación de frases**: Dividir ambas canciones en frases o secciones naturales y medir la duración de cada frase. La canción transformada debería reflejar una estructura similar (por ejemplo, una frase de ocho compases seguida de otra de cuatro).
       - **Patrones de repetición**: Analizar la recurrencia de motivos o frases en ambas canciones. Utilizar técnicas de análisis como la autocorrelación para identificar patrones repetidos y medir su presencia y ubicación.
       - **Similitud de estructura**: A partir de estos análisis, construir una "estructura de frases" que permita comparar la secuencia en ambas canciones y medir la concordancia.

### 4. **Coherencia armónica**
   - **Definición**: Evalúa la progresión de acordes y la tonalidad general de la canción.
   - **Objetivo**: Asegurar que la armonía en la canción transformada mantenga una relación con la tonalidad y la secuencia de acordes del tema original, garantizando que no se rompa la coherencia estilística en la armonía.
   - **Medición**: 
       - **Tonalidad**: Determinar la tonalidad de la canción de origen y la transformada usando análisis de frecuencia de notas y acordes. Asegurarse de que ambas coinciden o que la transformada sigue una tonalidad relacionada (e.g., relativo mayor/menor).
       - **Progresiones armónicas**: Identificar y comparar la secuencia de acordes en ambas canciones. Para hacer esto, se puede emplear un análisis de armonía de acordes en función del tiempo para ver si las progresiones entre canciones mantienen una lógica similar, sin desviarse demasiado del estilo armónico original.

### 5. **Expresividad y dinámica**
   - **Definición**: Mide las variaciones de intensidad y velocidad de notas a lo largo de la canción.
   - **Objetivo**: Capturar el rango dinámico y la "intensidad" emocional de la canción, asegurando que el resultado final no pierda los matices expresivos del tema original.
   - **Medición**: 
       - **Velocidad media de las notas**: Analizar la "velocidad" o intensidad con la que se tocan las notas en ambas canciones. Por ejemplo, una canción suave puede tener valores de velocidad más bajos y menos variación, mientras que una pieza con mayor intensidad emocional tendrá valores altos y fluctuantes.
       - **Variabilidad dinámica**: Medir el cambio de intensidad en secciones de ambas canciones y comparar. Esto puede hacerse midiendo la desviación estándar en la velocidad de las notas y las variaciones en las distintas secciones.

=======
### FORMA DE EVALUACIÓN:
- Con el propósito de construir una métrica objetiva que permita evaluar la calidad de los resultados obtenidos, buscaremos hacer uso de un concepto de teoría de la información denominado "Normalized Information Distance (NID)", que establece una medida universal de distancia entre objetos de distinto tipo. Sin embargo, dado que dicha medida es teóricamente no computable, haciendo uso de algoritmos de compresión puede modificarse para obtener una forma de computarla en lo que se denomina "Normalized Compression Distance (NCD)". Los archivos musicales empleados se codificarán entonces de forma de poder comparar la "distancia" que los separa, y de esta manera poder obtener una medida de similitud entre las distintas composiciones (concretamente, la similitud entre el estilo de la composición objetivo con el estilo de las composiciones generadas por el algoritmo genético).
- Alternativamente, se considerarán las siguientes características musicales de los archivos a procesar:
	1. **COHERENCIA RÍTMICA**
	   - Definición: evalúa la estructura y la densidad rítmica de la canción, incluyendo la distribución de duraciones de las notas y su agrupamiento en patrones.
	   - Objetivo: medir cómo el ritmo original influye en la pieza transformada, asegurando que la canción mantiene una consistencia rítmica y una "textura" que le dé carácter (denso, pausado, etc.).
	   - Medición
		   - **Patrones rítmicos**: analizar secuencias de duración y repetición de notas o grupos de notas (motivos rítmicos), comparando con patrones en la canción original.
		   - **Densidad**: calcular la cantidad promedio de notas en intervalos regulares (e.g., cada compás o sección). Una densidad rítmica alta indica más notas por intervalo de tiempo, mientras que una baja sugiere pausas o menor actividad.
		   - **Duración media**: calcular la duración promedio de las notas en ambas canciones y verificar que se mantienen en un rango similar.
	2. **COHESIÓN MELÓDICA**
	   - Definición: mide la forma y continuidad de la melodía a través del contorno melódico, los intervalos entre notas, y el rango de notas en la composición.
	   - Objetivo: asegurar que la melodía transformada mantiene un estilo melódico parecido al de la canción de origen, conservando la relación entre notas y la forma general.
	   - Medición: 
	       - **Contorno melódico**: analizar la dirección de las notas (ascendente, descendente o estática) en ambos temas y calcular la similitud de las secuencias.
	       - **Distribución de intervalos**: determinar la frecuencia de intervalos específicos entre notas (e.g., terceras mayores, cuartas justas) y comparar la proporción de cada uno con la canción de origen.
	       - **Rango de notas**: medir la nota más alta y la más baja en cada canción. El rango de la canción transformada debería mantenerse similar para reflejar la "altura" del estilo original.
	3. **ESTRUCTURA Y REPETICIÓN**
	   - Definición: evalúa cómo se organizan y repiten frases o motivos musicales, lo cual da forma y cohesión a la estructura de la canción.
	   - Objetivo: verificar que la canción transformada no sólo sea rítmica y melódicamente coherente, sino que también respete la organización estructural de frases o motivos, logrando una estructura con sentido.
	   - Medición: 
	       - **Identificación de frases**: dividir ambas canciones en frases o secciones naturales y medir la duración de cada frase. La canción transformada debería reflejar una estructura similar (por ejemplo, una frase de ocho compases seguida de otra de cuatro).
	       - **Patrones de repetición**: analizar la recurrencia de motivos o frases en ambas canciones. Utilizar técnicas de análisis como la autocorrelación para identificar patrones repetidos y medir su presencia y ubicación.
	       - **Similitud de estructura**: a partir de estos análisis, construir una "estructura de frases" que permita comparar la secuencia en ambas canciones y medir la concordancia.
	4. **COHERENCIA ARMÓNICA**
	   - Definición: evalúa la progresión de acordes y la tonalidad general de la canción.
	   - Objetivo: asegurar que la armonía en la canción transformada mantenga una relación con la tonalidad y la secuencia de acordes del tema original, garantizando que no se rompa la coherencia estilística en la armonía.
	   - Medición: 
	       - **Tonalidad**: determinar la tonalidad de la canción de origen y la transformada usando análisis de frecuencia de notas y acordes. Asegurarse de que ambas coinciden o que la transformada sigue una tonalidad relacionada (e.g., relativo mayor/menor).
	       - **Progresiones armónicas**: identificar y comparar la secuencia de acordes en ambas canciones. Para hacer esto, se puede emplear un análisis de armonía de acordes en función del tiempo para ver si las progresiones entre canciones mantienen una lógica similar, sin desviarse demasiado del estilo armónico original.
	5. **EXPRESIVIDAD Y DINÁMICA**
	   - Definición: mide las variaciones de intensidad y velocidad de notas a lo largo de la canción.
	   - Objetivo: capturar el rango dinámico y la "intensidad" emocional de la canción, asegurando que el resultado final no pierda los matices expresivos del tema original.
	   - Medición: 
	       - **Velocidad media de las notas**: analizar la "velocidad" o intensidad con la que se tocan las notas en ambas canciones. Por ejemplo, una canción suave puede tener valores de velocidad más bajos y menos variación, mientras que una pieza con mayor intensidad emocional tendrá valores altos y fluctuantes.
	       - **Variabilidad dinámica**: medir el cambio de intensidad en secciones de ambas canciones y comparar. Esto puede hacerse midiendo la desviación estándar en la velocidad de las notas y las variaciones en las distintas secciones.
>>>>>>> Stashed changes
- Dependiendo del nivel de complejidad que demande captar cada uno de los aspectos mencionados en el inciso anterior, valoraremos la posibilidad de emplear sólo un subconjunto de los mismos.
- Se investigará también la posibilidad de aplicar el concepto de entropía musical, ya que en conjunto con lo mencionado anteriormente podría ayudar a capturar el "estilo" de una pieza musical. Por ejemplo, una pieza con una entropía más alta podría tener un estilo más variado, con más cambios y saltos melódicos, mientras que una pieza con entropía más baja podría tener un estilo más repetitivo y predecible. Al generar una nueva pieza musical, el programa podría entonces intentar emular la entropía de la pieza de referencia, para que la nueva pieza tenga un estilo similar en términos de la distribución y variedad de las notas. Esto ayudaría a capturar aspectos clave del "estilo" de la pieza de referencia.
- Con el propósito de validar ó complementar la datos calculados por la NCD, y siempre que el tiempo lo permita, se implementará una plataforma web sencilla que permita a los usuarios votar y calificar los resultados obtenidos, con el propósito de utilizar esa información como parte de la función de aptitud.
- Dejamos abierta la posibilildad de incorporar nuevas medidas o mejorar las ya mencionadas a medida que vayamos investigando y mejorando nuestro conocimiento de teoría musical.
- Contemplaremos adicionalmente el tiempo de ejecución de cada estrategia.

<<<<<<< Updated upstream
## JUSTIFICACIÓN:
Aplicar técnicas de inteligencia artificial, como algoritmos genéticos y redes neuronales, es apropiado para este proyecto debido a la complejidad inherente a la manipulación y composición de música. Los algoritmos de IA pueden identificar y transferir las características musicales clave de manera más eficiente y sistemática que un enfoque manual o heurístico.

## ALGORITMOS A UTILIZAR:
- Genéticos: presentan un rendimiento notable para optimizar la transferencia de características musicales entre canciones, utilizando una función de aptitud basada en métricas musicales.
- Aprendizaje por refuerzo o redes neuronales (posibilidad): pueden aprender a mapear las características musicales de una canción a otra, permitiendo una transferencia más sofisticada. Se valorará su implementación a fin de comparar con los resultados obtenidos por los algoritmos genéticos, tanto en tiempo de ejecución como en calidad, siempre que el tiempo lo permita.

## LISTADO DE ACTIVIDADES A REALIZAR:
=======
### JUSTIFICACIÓN:
Aplicar técnicas de inteligencia artificial, como algoritmos genéticos y redes neuronales, es apropiado para este proyecto debido a la complejidad inherente a la manipulación y composición de música. Los algoritmos de IA pueden identificar y transferir las características musicales clave de manera más eficiente y sistemática que un enfoque manual o heurístico.

### ALGORITMOS PRINCIPALES A UTILIZAR:
- Evolutivos (genéticos): presentan un rendimiento notable para optimizar la transferencia de características musicales entre canciones, utilizando una función de aptitud basada en métricas musicales.
- Aprendizaje por refuerzo o redes neuronales (posibilidad): pueden aprender a mapear las características musicales de una canción a otra, permitiendo una transferencia más sofisticada. Se valorará su implementación a fin de comparar con los resultados obtenidos por los algoritmos genéticos, tanto en tiempo de ejecución como en calidad, siempre que el tiempo lo permita.

### LISTADO DE ACTIVIDADES A REALIZAR:
>>>>>>> Stashed changes

1. Lectura de teoría musical básica [2 días]
2. Lectura de trabajos similares ya existentes y técnicas empleadas [2 días]
3. Implementación del código que permita extraer información de las pistas musicales [2 días]
4. Implementación general del algoritmo genético [1 día]
5. Implementación de la/s función/es de aptitud [1 día]
6. Pruebas y reajustes con distintos parámetros y configuraciones [7 días]
7. Análisis y evaluación de resultados [3 días]
8. Elaboración del informe [7 días]
9. Elaboración de la presentación [3 días]
<<<<<<< Updated upstream
=======

### CRONOGRAMA ESTIMADO DE ACTIVIDADES

![[gantt.png]]

### REFERENCIAS
1. [Protocolo MIDI](https://en.wikipedia.org/wiki/MIDI)
2. [Canal de YouTube "Kie Codes"](https://www.youtube.com/watch?v=uQj5UNhCPuo&list=PLuZkwckxno0qjTQcrfaQ3INlCkM4bn5fk) (inspiración)

Papers:
1. [Generation of music through genetic algorithms](https://www.cse.chalmers.se/~abela/supervision/kandidat2014/DATX02_14_11.pdf)
2. [Music recombination using a genetic algorithm](https://scholarworks.indianapolis.iu.edu/bitstreams/fbab5c96-54f9-424b-b298-64bdc1037026/download)
3. [Evolving computer-generated music by means of the normalized compression distance](https://repositorio.uam.es/bitstream/handle/10486/664697/evolving_alfonseca_WTISA_2005.pdf?sequence=1&isAllowed=y)

Libros:
1. AIMA, Fourth Edition
2. Introduction to Evolutionary Computing, Second Edition

>>>>>>> Stashed changes
