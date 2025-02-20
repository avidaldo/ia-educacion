# ¿Cómo hemos llegado hasta aquí?

## Conceptos básicos

<img src="./img/venn.gif" width="600" alt="AI vs ML vs DL">


- **Inteligencia Artificial** (1956): Desarrollo de sistemas que pueden realizar tareas que normalmente requieren inteligencia humana.
    - ELIZA (1966): Chatbot que simula una conversación terapéutica mediante reglas (busca palabras clave y responde con frases predefinidas).
    - Deep Blue (1997): Computadora que derrota a Kasparov en ajedrez. Estrategias programadas y una gran capacidad de cálculo.

- **Machine Learning** o aprendizaje automático (1959): Desarrollo de algoritmos y modelos que permiten a las computadoras aprender de los datos.
    - Árboles de decisión (1960), Regresión logística (1958), K-means (1967), SVM (1995), Random Forest (2001), Gradient Boosting (2001), etc.
    - Predicciones basadas en datos (bolsa, clima, etc.)

<img src="./img/reglas_vs_ml.jpg" width="600">


> Paradoja de  Moravec (1980): Es relativamente fácil hacer que las computadoras realicen operaciones matemáticas y lógicas, pero es difícil hacer que realicen tareas simples que cualquier niño de 4 años puede hacer, como reconocer un objeto o entender un lenguaje natural.

- **Redes neuronales artificiales**: Imitan el funcionamiento de las neuronas del cerebro humano para aplicaciones de Machine Learning.
    - Neurona artificial (1943)
    - [Perceptrón](https://www.youtube.com/watch?v=l-9ALe3U-Fg) (1957)
    - Red de Hopfield (1982)
    - Backpropagation (1986)
    - [LeNet-5](https://www.youtube.com/watch?v=H0oEr40YhrQ) (1998) (reconocimiento de dígitos)

- **Deep Learning**: Subcampo de la IA que se enfoca en el desarrollo de redes neuronales profundas (redes neuronales con muchas capas ocultas) y con el se desarrolla el boom de la IA.
    - AlexNet (2012)

- **IA Generativa**: Campo de la IA que utiliza *Deep Learning* en la creación de sistemas que pueden generar contenido nuevo y original.
    - ChatGPT, Dall-E, Sora, etc.
    - Lo que hoy se ha dado en llamar **"La IA"** gracias al reciente boom de los modelos generativos.


## El Boom de la IA

- Causas: 

    - Aumento de la capacidad de cómputo (GPGPU)
    - Aumento de la cantidad de datos (Internet, Big Data)
    - Mejoras en los algoritmos

- Hitos:

    - 2012: **AlexNet** baja el error en **ImageNet** al 15% (antes 25%) y comienza el boom de las redes neuronales profundas.

    - 2014: DeepFace de Facebook identifica caras con precisión humana

    - 2016: AlphaGo derrota a Lee Sedol en Go aprendiendo a jugar contra sí mismo (*Reinforcement Learning*)

    - 2017: Aparece el "Transformer" con la publicación de "Attention is all you need"
    - 2018: Primeros modelos de lenguaje de gran escala (BERT, GPT-2?)
    - 2020: GPT-3 de OpenAI
    - 2022: Aparece **ChatGPT** (modelo GPT-3.5) de OpenAI y Stable Diffusion
    - 2024: Primeros modelos de lenguaje con razonamiento (OpenAI o1)
    - Enero 2025: Aparece **DeepSeek-R1** y todo el mundo se pone nervioso.

- ¿Qué está llegando?

    - "Copilotos" para todo (windows, office, etc.)
    - Agentes
    - "Netflix" personalizado a tiempo real
    - Burbuja de las .ai (similares a GPTs)


## ¿Cómo funcionan?

- De manera estadística. Aprenden a predecir la siguiente palabra basándose en las anteriores.
- No parte de cero, predice la siguiente palabra basándose en el prompt que le damos, en las anteriores (memoria) y en el contexto (configuración).
- Están entrenados con datos existentes, pero **no tienen un "conocimiento funcional" de las reglas** (por ejemplo al crear imágenes, no saben cómo funcionan las manecillas de un reloj).


### Razonadores

Los modelos razonadores dan en general un mejor resultado a costa de mayor tiempo. Integran en su funcionamiento la estrategia de cadena de pensamiento (*Chain of Thought* - CoT) habiendo sido entrenados con ejemplos de razonamiento paso a paso.
Han permitido superar nuevos niveles en *benchmarks* matemáticos y lógicos.