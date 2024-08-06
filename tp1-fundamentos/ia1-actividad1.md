# Actividad Preliminar

## 1. Buscar 2 ejemplos de aplicaciones de inteligencia artificial.

- OpenAI Five

Es un programa informático de OpenAI que juega al videojuego de cinco contra cinco Dota 2. 

Su primera aparición pública tuvo lugar en 2017, donde fue probado en una partida en vivo de uno contra uno contra el jugador profesional Dendi, que perdió contra él.

Al año siguiente, el sistema había avanzado hasta el punto de actuar como un equipo completo de cinco personas, y empezó a jugar contra equipos profesionales y a demostrar su capacidad para derrotarlos.

Desafíos de la IA en Dota 2:

Dota 2, un juego de estrategia en tiempo real, presenta desafíos únicos para la inteligencia artificial que superan a los juegos clásicos como el ajedrez o el Go:

    Horizontes Temporales Largos: Dota 2 tiene una duración promedio de 45 minutos con 80,000 ticks por juego, mientras que el ajedrez y el Go son juegos mucho más cortos y estratégicos.

    Estado Parcialmente Observado: Los jugadores solo ven partes del mapa cubiertas por niebla, lo que requiere inferencias y modelado del oponente, a diferencia de los juegos de información completa como el ajedrez y el Go.

    Espacio de Acción y Observación Complejo: Cada héroe en Dota 2 puede realizar docenas de acciones y el juego se desarrolla en un mapa extenso con información representada por 20,000 números flotantes. Esto contrasta con los juegos de ajedrez y Go, que tienen espacios de acción y observación mucho más simples.

    Reglas Complejas y Cambios Frecuentes: Dota 2 tiene reglas complejas y se actualiza regularmente, lo que añade dificultad en la implementación de estrategias de IA en comparación con el ajedrez o el Go.

### Enfoque de OpenAI

OpenAI utiliza una versión a gran escala de la Optimización de Política Proximal (PPO) para entrenar su sistema. Tanto OpenAI Five como el bot 1v1 desarrollado anteriormente aprenden únicamente a través del auto-juego, comenzando con parámetros aleatorios y sin recurrir a búsquedas o repeticiones humanas.

Los investigadores en Aprendizaje por Refuerzo (RL) generalmente han pensado que los horizontes temporales largos requerirían avances fundamentales, como el aprendizaje por refuerzo jerárquico. Sin embargo, los resultados de OpenAI sugieren que los algoritmos actuales pueden ser efectivos cuando se ejecutan a una escala suficiente y con una exploración adecuada.

El agente de OpenAI está entrenado para maximizar la suma de recompensas futuras, decaídas exponencialmente, ponderadas por un factor de decaimiento γ. Durante el entrenamiento más reciente de OpenAI Five, γ se ajustó de 0.998 (recompensas futuras con una vida media de 46 segundos) a 0.9997 (recompensas futuras con una vida media de cinco minutos). Para comparación, el PPO tenía una vida media de 0.5 segundos, el Rainbow de 4.4 segundos y el Observe and Look Further de 46 segundos.

Aunque la versión actual de OpenAI Five muestra debilidades en el último golpe (con una estimación de los comentaristas profesionales de Dota que lo sitúa alrededor de la mediana de los jugadores), su priorización de objetivos coincide con estrategias profesionales comunes. Obtener recompensas a largo plazo, como el control estratégico del mapa, a menudo requiere sacrificar recompensas a corto plazo, como el oro ganado de la agricultura, dado que agruparse para atacar torres lleva tiempo. Esto refuerza la creencia de que el sistema está optimizando realmente a lo largo de un horizonte prolongado.

### Estructura del Modelo

Cada una de las redes de OpenAI Five contiene una LSTM (Memoria a Largo Plazo) de una sola capa con 1024 unidades. Esta LSTM recibe el estado actual del juego (extraído de la API de Bots de Valve) y emite acciones a través de varios cabezales de acción posibles. Cada cabezal tiene un significado semántico específico, como el número de ticks para retrasar una acción, qué acción seleccionar, o las coordenadas X o Y de esta acción en una cuadrícula alrededor de la unidad, entre otros. Los cabezales de acción se calculan de manera independiente.

- Hortisys

Un equipo de sensores instalados en la planta registra constantemente su estado y envía los datos a una Unidad central de control.

Los datos se combinan con los obtenidos de estaciones metereológicas situadas en el cultivo y en la zona y son enviados al Sistema central para su proceso.

El Software de ayuda a la toma de decisiones (DSS) procesa los datos recibidos en tiempo real.

La información es consultable desde cualquier dispositivo.

>Anticipa posibles virosis al conocer la climatologia presente y futura y saber el estado nutricial del cultivo.

Ayuda a decicidir cuando recolectar para obtener un precio de mercado más ventajoso.

## ¿Qué se entiende por inteligencia artificial?

La Inteligencia Artificial se refiere al campo de estudio dentro de la informática que se enfoca en la creación de sistemas y algoritmos capaces de realizar tareas que normalmente requieren inteligencia humana. Estas tareas incluyen el reconocimiento de voz, la comprensión del lenguaje natural, la toma de decisiones, y el aprendizaje a partir de datos. La IA puede ser dividida en dos grandes áreas: IA débil, que se especializa en una tarea específica y no tiene una comprensión general del mundo, y IA fuerte, que tiene la capacidad de entender y razonar de manera similar a un ser humano (aunque este tipo de IA aún no se ha logrado completamente).

## ¿Qué se entiende por inteligencia?

La inteligencia es una capacidad mental que permite a los seres vivos (como los humanos) resolver problemas, adaptarse a nuevas situaciones, aprender de la experiencia, entender conceptos complejos y utilizar el conocimiento de manera efectiva. 

En el contexto de la IA, la inteligencia se refiere a la habilidad de un sistema para realizar tareas que normalmente requieren inteligencia humana, como la resolución de problemas y el aprendizaje.

## ¿Qué se entiende por artificial?


El término "artificial" se refiere a algo que no es natural o que es creado por el ser humano, en contraste con algo que ocurre de forma espontánea en la naturaleza. En el contexto de la IA, "artificial" implica que la inteligencia no es innata o biológica, sino que es creada mediante programación y algoritmos diseñados por humanos.

En resumen, la Inteligencia Artificial es el desarrollo de sistemas computacionales que buscan emular o simular aspectos de la inteligencia humana, donde "inteligencia" se refiere a la capacidad de resolver problemas y aprender, y "artificial" indica que esta inteligencia es creada por medios tecnológicos y no es natural.