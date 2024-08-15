# EJERCICIO 1

# **a)** 

The assertion that machines could act as if they were intelligent is called the **weak AI** hypothesis by philosophers.

The assertion that machines are actually thinking (not just simulating thinking) is called the **strong AI** hypothesis.

## Weak AI

**Whether AI is impossible depends on how it is defined**

Philosophers are interested in the problem of comparing two architectures—human and machine. Furthermore, they have traditionally posed the question not in terms of maximizing expected utility but rather as, “Can machines think?”

Edsger Dijkstra (1984) said that “The question of whether Machines Can Think . . . is about as relevant as the question of whether Submarines Can Swim.”

The American Heritage Dictionary’s first definition of swim is “To move through water by means of the limbs, fins, or tail,” and most people agree that submarines, being limbless, cannot swim.

The dictionary also defines fly as “To move through the air by means of wings or winglike parts,” and most people agree that airplanes, having winglike parts, can fly

Neither the questions nor the answers have any relevance to the design or capabilities of airplanes and submarines; rather they are about the usage of words in English (ships do swim in Russian)

Alan Turing, in his famous paper “Computing Machinery and Intelligence” (1950), suggested that instead of asking whether machines can think, we should ask whether machines can pass a behavioral intelligence test, which has come to be called the Turing Test.

Turing himself examined a wide variety of **possible objections to the possibility of intelligent machines**. Some of them are:

1. **The “argument from disability”** makes the claim that “a machine can never do X”

	Algorithms also perform at human levels on tasks that seemingly involve human judgment, or as Turing put it, “learning from experience” and the ability to “tell right from wrong.”

	It is clear that computers can do many things as well as or better than humans, including things that people believe require great human insight and understanding. **One’s first guess about the mental processes required to produce a given behavior is often wrong**. It is also true that there are many tasks at which computers do not yet excel, including Turing’s task of carrying on an open-ended conversation.

2. **The mathematical objection**

	Philosophers such as J. R. Lucas (1961) have claimed that machines are mentally inferior to humans, because machines are formal systems that are limited by the incompleteness theorem—they cannot establish the truth of their own Gödel sentence—while humans have no such limitation.

	We will examine only three of the problems with the claim:

	1. First, Gödel’s incompleteness theorem applies only to formal systems that are powerful enough to do arithmetic. This includes Turing machines, and Lucas’s claim is in part based on the assertion that computers are Turing machines. This is a good approximation, but is not quite true. Turing machines are infinite, whereas computers are finite, and any computer can therefore be described as a (very large) system in propositional logic, which is not subject to G¨odel’s incompleteness theorem
	
	2. Second, an agent should not be too ashamed that it cannot establish the truth of some sentence while other agents can.  Consider the sentence: "J. R. Lucas cannot consistently assert that this sentence is true". Humans were behaving intelligently for thousands of years before they invented mathematics, so it is unlikely that formal mathematical reasoning plays more than a peripheral role in what it means to be intelligent.

	 3. Third, and most important, even if we grant that computers have limitations on what they can prove, there is no evidence that humans are immune from those limitations.

3. **The argument from informality**

	One of the most influential and persistent criticisms of AI as an enterprise was raised by Turing as the “argument from informality of behavior.” Essentially, **this is the claim that human behavior is far too complex to be captured by any simple set of rules** and that because computers can do no more than follow a set of rules, they cannot generate behavior as intelligent as that of humans.

	**The inability to capture everything in a set of logical rules is called the qualification problem in AI**.

	Dreyfus and Dreyfus (1986) propose a five-stage process of acquiring expertise, beginning with rule-based processing (of the sort proposed in GOFAI) and ending with the ability to select correct responses instantaneously. In making this proposal, Dreyfus and Dreyfus propose a neural network architecture organized into a vast “case library,” but point out several problems:
	
	1. Good generalization from examples cannot be achieved without background knowledge.
	2. Neural network learning is a form of supervised learning, requiring the prior identification of relevant inputs and correct outputs. Therefore, they claim, it cannot operate autonomously without the help of a human trainer. In fact, learning without a teacher can be accomplished by unsupervised learning and reinforcement learning.
	3. Learning algorithms do not perform well with many features, and if we pick a subset of features, “there is no known way of adding new features should the current set prove inadequate to account for the learned facts.”
	4. The brain is able to direct its sensors to seek relevant information and to process it to extract aspects relevant to the current situation.
	
	In sum, many of the issues Dreyfus has focused on—background commonsense knowledge, the qualification problem, uncertainty, learning, compiled forms of decision making—are indeed important issues, and have by now been incorporated into standard intelligent agent design. In our view, this is evidence of AI’s progress, not of its impossibility.

	To understand how human (or other animal) agents work, we have to consider the whole agent, not just the agent program. Indeed, the **embodied cognition** approach claims that it makes no sense to consider the brain separately: cognition takes place within a body, which is embedded in an environment.

	Under the embodied cognition program, robotics, vision, and other sensors become central, not peripheral.

## Strong AI

For Turing, only if a machine is aware of its own mental states and actions we could agree that it equals brain (the argument from **consciousness**). Jefferson’s key point actually relates to **phenomenology**, or the study of direct experience: the machine has to actually feel emotions. Others focus on **intentionality**, that is the machine’s representations are actually “about” something in the real world.

Also for Turing, the question of machines being conscious is just as ill-defined as asking "Can machines think?"

Are **mental processes** more like storms (in the sense that simulating them doesn't make anyone wet) or more like addition (in the sense that a computer simulation of addition is addition)? Turing’s answer suggests that the issue will eventually go away by itself once machines reach a certain level of sophistication. This would have the effect of dissolving the difference between weak and strong AI.

Against this, one may insist that there is a factual issue at stake: the **mind-body problem**. That problem was considered by Descartes in what we would now call a dualist theory and airses the question of how the mind can control the body if the two are really separate.

The **monist theory of mind**, often called **physicalism**, avoids this problem by asserting that mental states are physical states.

#### Mental states and the brain in a vat

Physicalist philosophers have attempted to explicate what it means to say that a person—and, by extension, a computer—is in a particular mental state. They have focused in particular on **intentional states**. These are states that refer to some aspect of the external world. For example, the knowledge that one is eating a hamburger is a belief about the hamburger and what is happening to it.

If physicalism is correct, it must be the case that the proper description of a person’s mental state is determined by that person’s brain state.

The simplicity of this view is challenged by some simple thought experiments. Take for example the **brain-in-a-vat** experiment. 

This example seems to contradict the view that brain states determine mental states. One way to resolve the dilemma is to say that the content of mental states can be interpreted from two different points of view. The “**wide content**” view interprets the content of mental states involves both the brain and the environment history. **Narrow content,** on the other hand, considers only the brain state.

Wide content is the setting in which our ordinary language about mental content has evolved. On the other hand, with the question of whether AI systems are really thinking and really do have mental states narrow content is appropriate.

#### Functionalism and the brain replacement experiment

The theory of **functionalism** says that a mental state is any intermediate causal condition between input and output. Under functionalist theory, any two systems with isomorphic causal processes would have the same mental states.

The claims of functionalism are illustrated most clearly by the brain replacement experiment. We are concerned with both the external behavior and the internal experience of the subject, during and after the operation.

There are three possible conclusions:

1. The causal mechanisms of consciousness that generate these kinds of outputs in normal brains are still operating in the electronic version, which is therefore conscious. 
2. The conscious mental events in the normal brain have no causal connection to behavior, and are missing from the electronic brain, which is therefore not conscious. 
3. The experiment is impossible, and therefore speculation about it is meaningless.

The second possibility reduces consciousness to what philosophers call an **epiphenomenal** role, something that happens, but casts no shadow on the observable world. If consciousness is indeed epiphenomenal, then it cannot be the case that the subject says “Ouch” because of the conscious experience of pain.

#### Biological naturalism and the Chinese Room

A strong challenge to functionalism has been mounted by John Searle’s (1980) **biological naturalism**, according to which mental states are high-level emergent features that are caused by low-level physical processes in the neurons, and it is the properties of the neurons that matter. His conclusion is that running the appropriate program is not a sufficient condition for being a mind.

Considering the example of the Chinese Room, Searle concludes that running the right program does not necessarily generate understanding.

The real claim made by Searle rests upon the following four axioms (Searle, 1990): 
1. Computer programs are formal (syntactic). 
2. Human minds have mental contents (semantics). 
3. Syntax by itself is neither constitutive of nor sufficient for semantics. 
4. Brains cause minds.

The axioms are controversial. Axioms 1 and 2 rely on an unspecified distinction between syntax and semantics that seems to be closely related to the distinction between narrow and wide content. On the one hand, we can view computers as manipulating electric current, which happens to be what brains mostly do (according to our current understanding). So it seems we could equally say that brains are syntactic.

The whole argument comes down to whether axiom 3 can be accepted, and the public reaction to Searle argument's shows that it is acting as an **intuition pump**, it amplifies one's prior intuitions so biological naturalists are more convinced of their positions, and functionalists are convinced only that axiom 3 is unsupported.

In the case of the Chinese Room, Searle relies on intuition, not proof: just look at the room; what’s there to be a mind? But one could make the same argument about the brain. Why can a hunk of brain be a mind while a hunk of liver cannot? That remains the great mystery.

#### Consciousness, qualia, and the explanatory gap

The issue of consciousness is often broken down into aspects such as understanding and self-awareness. We focus specifically on the subjective experience carried with consciousness. The technical term for the intrinsic nature of experiences is **qualia**.

Qualia present a challenge for functionalist accounts of the mind because different qualia could be involved in what are otherwise isomorphic causal processes. Consider the **inverted spectrum** tought experiment.

Qualia are challenging not just for functionalism but for all of science. There is simply no currently accepted form of reasoning that would lead from deeply knowing what neural processes do to the conclusion that the entity owning those neurons has any particular subjective experience.

This **explanatory gap** has led some philosophers to conclude that humans are simply incapable of forming a proper understanding of their own consciousness.

Turing himself concedes that the question of consciousness is a difficult one, but denies that it has much relevance to the practice of AI. We agree with Turing—we are interested in creating programs that behave intelligently. The additional project of making them conscious is not one that we are equipped to take on, nor one whose success we would be able to determine.

## Ethics and risks of developing AI

AI seems to pose some fresh problems beyond of building bridges that don’t fall down. We consider the main of them and some conclusions in the following sections:
##### People might lose their jobs to automation. 

So far, automation through information technology in general and AI in particular has created more jobs than it has eliminated, and has created more interesting, higher-paying jobs.
##### People might have too much (or too little) leisure time. 

People working in knowledge-intensive industries have found themselves part of an integrated computerized system that operates 24 hours a day; to keep up, they have been forced to work longer hours.

AI also holds the promise of allowing us to take some time off and let our automated agents handle things for a while.
##### People might lose their sense of being unique. 

AI, if widely successful, may be at least as threatening to the moral assumptions of 21st-century society as Darwin’s theory of evolution was to those of the 19th century.
##### AI systems might be used toward undesirable ends. 

Advanced technologies have often been used by the powerful to suppress their rivals. Autonomous AI systems are now commonplace on the battlefield, and so robotic weapons pose additional risks as they may end up making decisions that lead to the killing of innocent civilians.

AI also has the potential to mass-produce surveillance and loss of privacy is then unavoidable.
##### The use of AI systems might result in a loss of accountability. 

Legal liability becomes an important issue. When a physician relies on the judgment of a medical expert system for a diagnosis, who is at fault if the diagnosis is wrong? If expert systems become reliably more accurate than human diagnosticians, doctors might become legally liable if they don’t use the recommendations of an expert system

If monetary transactions are made “on one’s behalf” by an intelligent agent, is one liable for the debts incurred?

Currently no program has been granted legal status as an individual for the purposes of financial transactions; at present, it seems unreasonable to do so. The law has yet to catch up with the new developments.

##### The success of AI might mean the end of the human race.

Almost any technology has the potential to cause harm in the wrong hands, but with AI and robotics, we have the new problem that the wrong hands might belong to the technology itself.

If ultraintelligent machines are a possibility, we humans would do well to make sure that we design their predecessors in such a way that they design themselves to treat us well.

Yudkowsky (2008) goes into more detail about how to design a Friendly AI, the challenge is to define a mechanism for evolving AI systems under a system of checks and balances, and to give the systems utility functions that will remain friendly in the face of such changes.

Omohundro (2008) says that “social structures which cause individuals to bear the cost of their negative externalities would go a long way toward ensuring a stable and positive future”.

# b) ![AI Mind Map](/tp1-fundamentos/tp1-fundamentos-mind-map.png)

# EJERCICIO 2

1. Según el texto, aunque los LLMs pueden imitar comportamientos humanos y simular características como creencias o intenciones, su naturaleza fundamentalmente diferente (son entidades computacionales desprovistas de cuerpo y experiencia) los aleja de lo que conocemos como consciencia. Se advierte sobre el peligro de caer en el antropomorfismo y  se considera que, por ahora, estos agentes deben verse como simulacros, no como seres conscientes.
2. El texto no menciona explícitamente las implicaciones éticas de atribuir conciencia y derechos morales a los agentes de IA avanzados. Sin embargo, se sugiere que la atribución de estas características podría llevar a errores éticos, ya que se basaría en una falsa equivalencia entre la simulación de conciencia y la conciencia real. Esto podría desviar la atención de las verdaderas preocupaciones éticas relacionadas con el uso y desarrollo de la IA, como la justicia, la transparencia y la responsabilidad humana en la creación y el manejo de estas tecnologías.
# EJERCICIO 3

A lo largo de la de la historia de la humanidad siempre han existido diversos momentos en los cuales la tecnología parece dar un salto abrupto en cuanto a complejidad que abre el abanico a resolver una cantidad de problemas que hasta el momento parecían muy difíciles o imposibles de resolver. Y con la aparición de esas tecnologías, también el levantamiento de voces en contra de su evolución. Sucedió con la revolución industrial, la computadora, internet, etc., y la aparición de los LLMs no resulta una excepción a ese patrón. 

El hecho de que el desarrollo de esta tecnología esté en manos de empresas que muy posiblemente persigan objetivos cuanto menos cuestionables, no quiere decir en mi opinión que la tecnología en sí misma nos esté "deshumanizando", si no que tal vez debemos repensar ciertas malas costumbres nuestras como sociedad que existían antes incluso del auge de los LLMs (como el uso abusivo del celular, la priorización de las interacciones sociales virtuales antes que las presenciales, la tendencia a creer noticias falsas simplemente porque aparecen por internet, etc.), y que en este último tiempo los LLMs simplemente han dejado en evidencia. 

La gran diferencia que destaca en el desarrolo de los modelos generativos actuales es la posibilidad de interactuar con ellos en lenguaje natural, y a pesar de que también considere erróneo tratarlos como "personas" simplemente porque son capaces de escribir por pantalla palabras como "soy" ó "me siento", sí creo que si podemos entender la tecnología que efectivamente está detraś de esas palabras, el potencial de aprovechar la tecnología para construir herramientas útiles es grande.
