# **Transferencia de características musicales entre canciones**

**CÓDIGO DEL PROYECTO**: MUTRAMI (Music Track Mixer)

**INTEGRANTES**: Adrián Zangla y Francisco Alba

**DESCRIPCIÓN**:
El mundo de la música, concretamente de la composición musical, se presenta habitualmente complejo y desafiante en el mejor de los casos. En los últimos años, y con la idea de complementar o facilitar el proceso creativo que conlleva producir música, se han desarrollado múltiples enfoques que permiten crear composiciones musicales de forma artificial empleando técnicas de aprendizaje automático.
Este proyecto tiene como objetivo explorar el funcionamiento de algunas de esas técnicas, y utilizarlas para lograr transferir características musicales específicas de una canción a otra. Buscamos así componer una nueva canción que mezcle ciertas propiedades deseadas de dos canciones o pistas musicales existentes.

**OBJETIVOS**:
- Identificar y extraer las características musicales clave de cada una de las canciones de origen.
- Desarrollar un algoritmo capaz de transferir estas características de una canción a otra, conservando la estructura y armonía de la canción de destino.
- Evaluar la calidad de la canción resultante en términos de similitud con la canción objetivo y coherencia musical.

**ALCANCE**:
- El proyecto se enfocará en la transferencia de elementos como ritmo, melodía, armonía y timbre entre las canciones.
- Se utilizarán técnicas de aprendizaje de máquina, como algoritmos genéticos y redes neuronales, para lograr la transferencia de características.

**LIMITACIONES**:
- La calidad de la canción resultante dependerá de la complejidad de las canciones de origen y la dificultad de transferir sus características.
- El proyecto priorizará trabajar con archivos de audio en formato MIDI:
	- El protocolo MIDI (Musical Instrument Digital Interface) representa la música como una secuencia de eventos discretos (nota encendida, nota apagada, tono, velocidad, etc.) en lugar de como una forma de onda de audio continua. Esto facilita el análisis de la estructura y las características musicales.
	- Los archivos MIDI son compactos y fáciles de procesar en comparación con las grabaciones de audio completas. Esto permite que el sistema de generación de música trabaje de manera eficiente con múltiples pistas de ejemplo.
	- MIDI proporciona acceso a los bloques de construcción fundamentales de la música, como tonos, ritmos y dinámicas. Esto permite que el sistema extraiga y recombine los elementos musicales clave que definen un estilo en particular.
	- MIDI es un formato estándar compatible con una amplia gama de software y hardware musical. Esto facilita la integración del sistema de generación de música con otras herramientas para crear, editar y reproducir la salida.
	- Dado que MIDI constituye un lenguaje, resulta razonable pensar que los modelos de machine learning actuales puedan sacar provecho del mismo como lo hacen con otros lenguajes y mejorar entonces las posibilidades de obtener los resultados esperados.


**FORMA DE EVALUACIÓN**:
- Con el propósito de construir una métrica objetiva que permita evaluar la calidad de los resultados obtenidos, se considerarán las siguientes características musicales de los archivos a procesar:
	- Distribución de intervalos cromáticos
	- Rango de notas (notas más altas y más bajas)
	- Duración media de la nota
	- Velocidad media de la nota
	- Patrones rítmicos
	- Contorno melódico
	- Densidad de notas
	- Progresiones armónicas
	- Estructura de frase
	- Patrones de repetición
	- Tonalidad
	- Dinámica
	- Tempo
- Dependiendo del nivel de complejidad que demande captar cada uno de los aspectos mencionados en el inciso anterior, valoraremos la posibilidad de emplear sólo un subconjunto de los mismos.
- Se investigará también el concepto de entropía musical, ya que en conjunto con lo mencionado anteriormente podría ayudar a capturar el "estilo" de una pieza musical. Por ejemplo, una pieza con una entropía más alta podría tener un estilo más variado, con más cambios y saltos melódicos, mientras que una pieza con entropía más baja podría tener un estilo más repetitivo y predecible. Al generar una nueva pieza musical, el programa podría entonces intentar emular la entropía de la pieza de referencia, para que la nueva pieza tenga un estilo similar en términos de la distribución y variedad de las notas. Esto ayudaría a capturar aspectos clave del "estilo" de la pieza de referencia.
- Como alternativa, y siempre que el tiempo lo permita, se implementará una plataforma web sencilla que permita a los usuarios votar y calificar los resultados obtenidos, con el propósito de utilizar esa información como parte de la función de aptitud.

**JUSTIFICACIÓN**:
Aplicar técnicas de inteligencia artificial, como algoritmos genéticos y redes neuronales, es apropiado para este proyecto debido a la complejidad inherente a la manipulación y composición de música. Los algoritmos de IA pueden identificar y transferir las características musicales clave de manera más eficiente y sistemática que un enfoque manual o heurístico.

**ALGORITMOS A UTILIZAR**:
- Genéticos: presentan un rendimiento notable para optimizar la transferencia de características musicales entre canciones, utilizando una función de aptitud basada en métricas musicales.
- Aprendizaje por refuerzo o redes neuronales (posibilidad): pueden aprender a mapear las características musicales de una canción a otra, permitiendo una transferencia más sofisticada. Se valorará su implementación a fin de comparar con los resultados obtenidos por los algoritmos genéticos, tanto en tiempo de ejecución como en calidad, siempre que el tiempo lo permita.

**LISTADO DE ACTIVIDADES A REALIZAR**:

1. Lectura de teoría musical básica [2 días]
2. Lectura de trabajos similares ya existentes y técnicas empleadas [2 días]
3. Implementación del código que permita extraer información de las pistas musicales [2 días]
4. Implementación general del algoritmo genético [1 día]
5. Implementación de la/s función/es de aptitud [1 día]
6. Pruebas y reajustes con distintos parámetros y configuraciones [7 días]
7. Análisis y evaluación de resultados [3 días]
8. Elaboración del informe [7 días]
9. Elaboración de la presentación [3 días]