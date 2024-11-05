# **Transferencia de características musicales entre canciones**

**CÓDIGO DEL PROYECTO**: MusicTransfer

**INTEGRANTES**: Adrián Zangla y Francisco Alba

**DESCRIPCIÓN**:
Este proyecto tiene como objetivo transferir características musicales específicas de una canción a otra, utilizando técnicas de inteligencia artificial. El objetivo es componer una nueva canción que conserve ciertas propiedades deseadas de dos canciones existentes.

**OBJETIVOS**:
- Identificar y extraer las características musicales clave de cada una de las canciones de origen.
- Desarrollar un algoritmo capaz de transferir estas características de una canción a otra, conservando la estructura y armonía de la canción de destino.
- Evaluar la calidad de la canción resultante en términos de similitud con la canción objetivo y coherencia musical.

**ALCANCE**:
- El proyecto se enfocará en la transferencia de elementos como ritmo, melodía, armonía y timbre entre las canciones.
- Se utilizarán técnicas de aprendizaje de máquina, como algoritmos genéticos y redes neuronales, para lograr la transferencia de características.
- Como alternativa, se explorará el uso de plataformas existentes como Google Magenta o Jukebox para comparar los resultados.

**LIMITACIONES**:
- La calidad de la canción resultante dependerá de la complejidad de las canciones de origen y la dificultad de transferir sus características.
- El proyecto priorizará trabajar con archivos de audio en formatos comunes, como WAV o MP3.
	- Estos formatos conservan la información musical esencial, como la amplitud, frecuencia y duración de las notas.
	- Son ampliamente compatibles y permiten una fácil manipulación y procesamiento con herramientas de IA y software de audio.
	- Evitan la complejidad adicional que implicaría el manejo de formatos de partituras o MIDI, que requieren un mayor procesamiento y conocimiento musical específico.
- En caso de encontrar alguna forma eficiente de trabajar con partituras o con archivos MIDI, sí se considerará su uso para el proyecto.

**FORMA DE EVALUACIÓN**:
- Se utilizarán métricas musicales como similitud de melodía, armonía, ritmo y timbre para evaluar la calidad de la canción resultante:
	- Similitud de melodía: comparar la correspondencia entre las líneas melódicas de las canciones.
	- Similitud armónica: evaluar la coherencia de las progresiones de acordes.
	- Similitud rítmica: comparar la estructura y patrones rítmicos.
	- Similitud tímbrica: analizar la correspondencia entre los timbres y texturas sonoras.
- Como alternativa, y siempre que el tiempo lo permita, se implementará una plataforma web sencilla que permita a los usuarios votar y calificar los resultados obtenidos.

**JUSTIFICACIÓN**:
Aplicar técnicas de inteligencia artificial, como algoritmos genéticos y redes neuronales, es apropiado para este proyecto debido a la complejidad inherente a la manipulación y composición de música. Los algoritmos de IA pueden identificar y transferir las características musicales clave de manera más eficiente y sistemática que un enfoque manual o heurístico.

**ALGORITMOS A UTILIZAR**:
- Genéticos: presentan un rendimiento notable para optimizar la transferencia de características musicales entre canciones, utilizando una función de aptitud basada en métricas musicales.
- Aprendizaje por refuerzo o redes neuronales: pueden aprender a mapear las características musicales de una canción a otra, permitiendo una transferencia más sofisticada. Se considerará su implementación a fin de comparar con los resultados obtenidos por los algoritmos genéticos, tanto en tiempo de ejecución como en calidad, siempre que el tiempo lo permita.
- Modelos generativos como Jukebox o Google Magenta: pueden servir como punto de partida para la generación de la nueva canción o también como punto de comparación para los resultados obtenidos a partir de aplicar algoritmos genéticos, aprovechando sus capacidades de aprendizaje profundo en música.


