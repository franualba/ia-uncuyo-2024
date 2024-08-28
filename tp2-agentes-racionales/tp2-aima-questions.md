##### **2.10. Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

a. Can a simple reflex agent be perfectly rational for this environment? Explain.

>El agente no puede actuar en forma racional porque la penalización impide al agente maximizar la medida de rendimiento, ya que los puntos acumulados cada vez que se limpia, se "pierden" luego al moverse a otros casilleros.
 
b. What about a reflex agent with state?

>Si el agente puede almacenar un estado, entonces lus puntos obtenidos al limpiar los casilleros pueden mantenerse guardados en ese estado y entonces la penalización no impide maximizar la medida de rendimiento.

c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty
status of every square in the environment?

> Si el agente conoce el estado de todos los casilleros del entorno, entonces puede minimizar la penalización y entonces lograr que la medida de rendimiento sea la mejor posible, es decir, podría actuar racionalmente y no necesitaría almacenar estado.

##### **2.11. Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right).**

a. Can a simple reflex agent be perfectly rational for this environment? Explain.

> Sí, el agente puede ser racional porque es posible explorar el entorno y limpiar cada vez que se encuentre un casillero sucio, lo cual le permite al agente maximizar la medida de rendimiento.

b. Can a simple reflex agent with a randomized agent function outperform a simple reflex
agent?

> Sería muy difícil que un agente aleatorio obtenga mejor rendimiento que uno reflexivo simple, ya que a cada paso decide en forma aleatoria la acción a seguir, y si su casillero actual está sucio, puede dejarlo así, dando lugar a una menor eficiencia en la limpieza.



