# ¿Cómo hemos llegado hasta aquí?

## Conceptos básicos


<div style={{maxWidth: "600px"}}>

![](./img/venn.gif)

</div>


- **Inteligencia Artificial** (1956): Desarrollo de sistemas que pueden realizar tareas que normalmente requieren inteligencia humana.
    - ELIZA (1966): Chatbot que simula una conversación terapéutica mediante reglas (busca palabras clave y responde con frases predefinidas).
    - Deep Blue (1997): Computadora que derrota a Kasparov en ajedrez. Estrategias programadas y una gran capacidad de cálculo.

- **Machine Learning** o aprendizaje automático (1959): Desarrollo de algoritmos y modelos que permiten a las computadoras aprender de los datos.
    - Árboles de decisión (1960), Regresión logística (1958), K-means (1967), SVM (1995), Random Forest (2001), Gradient Boosting (2001), etc.
    - Predicciones basadas en datos (bolsa, clima, etc.)


<div style={{maxWidth: "600px"}}>

![](./img/reglas_vs_ml.jpg)

</div>


> Paradoja de  Moravec (1980): Es relativamente fácil hacer que las computadoras realicen operaciones matemáticas y lógicas, pero [es difícil hacer que realicen tareas simples que cualquier niño de 4 años puede hacer](https://www.smbc-comics.com/comic/ai-7?fbclid=IwY2xjawItKRFleHRuA2FlbQIxMAABHVZSt2Sks4COowshXz1d-2qcawJEbIr3kF3pCskfK9pFV8Oh0MgTvC1otw_aem_9YONOGize2uCs327bG33gA), como reconocer un objeto o entender un lenguaje natural.

- **Redes neuronales artificiales**: Imitan el funcionamiento de las neuronas del cerebro humano para aplicaciones de Machine Learning.
    - Neurona artificial (1943)
    - [Perceptrón](https://www.youtube.com/watch?v=l-9ALe3U-Fg) (1957)
    - Red de Hopfield (1982)
    - Backpropagation (1986)
    - [LeNet-5](https://www.youtube.com/watch?v=H0oEr40YhrQ) (1998) (reconocimiento de dígitos)

- **Deep Learning**: Subcampo de la IA que se enfoca en el desarrollo de redes neuronales profundas (redes neuronales con muchas capas ocultas) y con el se desarrolla el boom de la IA.
    - AlexNet (2012)

![](./img/deep_learning.jpg)

- **IA Generativa**: Campo de la IA que utiliza *Deep Learning* en la creación de sistemas que pueden generar contenido nuevo y original.
    - ChatGPT, Dall-E, Sora, etc.
    - Lo que hoy se ha dado en llamar **"La IA"** gracias al reciente boom de los modelos generativos.


## El Boom de la IA (del *deep learning*)

- Causas: 
    - Aumento de la capacidad de cómputo (GPUs, TPUs)
    - Disponibilidad de enormes conjuntos de datos (Internet, Big Data)
    - Avances en algoritmos y arquitecturas de redes
    - Gran incremento de la financiación e inversión industrial

- Hitos principales:
    - 2012: **AlexNet** reduce el error en **ImageNet** al 15.3% (antes 26%), demostrando el poder de las CNNs y marcando el inicio del boom.
    - 2014: **DeepFace** de Facebook alcanza precisión casi humana (97.35%) en reconocimiento facial.
    - 2014: Las **GANs** (Generative Adversarial Networks), revolucionan la generación de contenido.
    - 2016: **AlphaGo** de DeepMind derrota al campeón mundial Lee Sedol.
    - 2017: Aparece la arquitectura **Transformer**, transformando el procesamiento de lenguaje.
    - 2020: **GPT-3** de OpenAI demuestra capacidades emergentes en modelos de lenguaje a gran escala.
    - 2021: Los **modelos de difusión** (DALL-E, GLIDE) comienzan a dominar la generación de imágenes realistas.
    - 2022: **ChatGPT** (GPT-3.5) de OpenAI populariza los asistentes conversacionales.
    - 2023: **GPT-4** de OpenAI y proliferación de modelos **multimodales** (texto, imagen, audio, video).
    - 2024: Primeros modelos con capacidades avanzadas de razonamiento (**OpenAI o1**).
    - 2025: **DeepSeek-R1** (open-weights) baja el coste de los modelos de lenguaje con un rendimiento similar al de o1.

## Expectativas futuras:


### **Aumento de las capacidades humanas (*Human Augmentation*)**

La IA se perfila como un colaborador que potenciará nuestras habilidades. Desde la asistencia en tareas complejas y la toma de decisiones hasta la superación de limitaciones físicas o cognitivas, la IA actuará como una extensión de nuestras propias capacidades.

### **Creación Audiovisual Generativa**

Los avances en los modelos de difusión, el vídeo generativo y la síntesis de audio están transformando la producción audiovisual. Entre las expectativas más relevantes se encuentran:

- **Vídeo generativo de alta fidelidad**: Modelos como **Sora** (OpenAI), **Pika** o **Runway Gen-2** permitirán crear secuencias cinematográficas completas a partir de simples descripciones textuales.
- **Música y sonido**: Herramientas como **Stable Audio**, **LMusic** o **Sunshine** compondrán bandas sonoras y efectos adaptados al contexto en tiempo real.
- **Realidad mixta y videojuegos**: Mundos y personajes que se generan dinámicamente, ajustándose al estilo y preferencias de cada jugador.
- **Post-producción automatizada**: Procesos de edición, corrección de color, doblaje y subtitulado guiados por IA, reduciendo drásticamente los tiempos de producción.
- **Accesibilidad incrementada**: Generación automática de audiodescripciones, traducciones y lenguaje de señas, ampliando el alcance del contenido.

Estos avances, aunque centrados en la creatividad, comparten con la automatización la capacidad de acelerar flujos de trabajo y derribar barreras técnicas, razón por la cual merecen un apartado propio.

### **Agentes Autónomos**

Representan la evolución natural de los chatbots hacia sistemas verdaderamente proactivos e independientes.

**¿Qué es un agente de IA?** Diferencias clave:
- **Chatbot tradicional**: "¿En qué puedo ayudarte?" → Responde a cada pregunta individual.
- **Agente autónomo**: "Organiza mi viaje a Roma" → Planifica, busca opciones, compara precios, hace reservas, gestiona imprevistos y te informa del resultado final.

**Características fundamentales de los agentes**:
Se definen por su **autonomía** para actuar a largo plazo, **proactividad** para tomar la iniciativa, **reactividad** para adaptarse al entorno, **capacidad social** para interactuar y el **uso de herramientas** (APIs, Internet, etc.).

**Ejemplos y aplicaciones destacadas**:
- **Gestión personal**: Planificación automática de viajes (**Kayak**), gestión de finanzas o coordinación de tareas domésticas.
- **Ámbito profesional**:
    - **Programación**: Desarrollo de software con **Devin AI** o **GitHub Copilot Workspace**.
    - **Investigación y legal**: Análisis de información con **Perplexity Pro** o revisión de contratos con **Harvey AI**.
- **Sectores de impacto**: Ya se utilizan en atención al cliente (**Zendesk**), logística y trading algorítmico.

### **IA en la Educación**

La inteligencia artificial transformará el panorama educativo, creando un entorno de aprendizaje más personalizado, eficiente y accesible.

-   **Tutoría personalizada e inteligente**: Los sistemas de IA actuarán como tutores individuales para cada estudiante, adaptando el contenido y el ritmo de aprendizaje a sus necesidades específicas. Proporcionarán *feedback* instantáneo, resolverán dudas y ofrecerán refuerzo en las áreas donde el alumno presente dificultades.
-   **Creación de contenido educativo dinámico**: Los docentes podrán utilizar herramientas de IA para generar materiales didácticos a medida, como planes de lecciones, ejercicios, rúbricas de evaluación, presentaciones interactivas y simulaciones. Esto permitirá una enseñanza más rica y diversificada con menos esfuerzo.
-   **Automatización de tareas administrativas**: La IA liberará a los educadores de tareas repetitivas como la corrección de exámenes, la gestión de horarios o la comunicación de rutinas, permitiéndoles centrarse en la interacción directa con los estudiantes y en el diseño de experiencias de aprendizaje significativas.
-   **Accesibilidad e inclusión**: Las tecnologías de IA eliminarán barreras para estudiantes con necesidades especiales. Herramientas como la transcripción en tiempo real, la traducción simultánea o los lectores de pantalla avanzados garantizarán que todos los alumnos tengan las mismas oportunidades de acceso a la información.
-   **Análisis del aprendizaje y detección temprana**: La IA analizará patrones en el rendimiento de los estudiantes para identificar posibles dificultades de aprendizaje de manera proactiva. Esto permitirá a los educadores intervenir a tiempo y ofrecer el apoyo necesario antes de que los problemas se agraven.
-   **Desarrollo profesional para docentes**: La IA también podrá asistir a los propios docentes, ofreciendo análisis sobre sus métodos de enseñanza, sugiriendo nuevas estrategias pedagógicas y facilitando el acceso a recursos de formación continua.

### **Inteligencia Artificial General (AGI)**

**¿Qué es exactamente la AGI?**
- **Definición amplia**: Un sistema que puede realizar cualquier tarea cognitiva que un humano pueda hacer.
- **Definición estricta**: Un sistema que no solo iguala sino que supera significativamente a los humanos en la mayoría de tareas económicamente valiosas.
- **El problema**: No existe consenso científico sobre qué constituye exactamente "inteligencia general" o cómo medirla objetivamente. Investigadores como **Yann LeCun** (Meta) argumentan que el propio término *AGI* es impreciso y que la inteligencia es un espectro multidimensional alcanzable solo mediante avances graduales.

**Hitos esperados hacia la AGI**:
- **Próximos 2-5 años**: Modelos que superen a los humanos en la mayoría de tareas cognitivas individuales (escritura, programación, análisis, etc.).
- **5-10 años**: Sistemas que puedan combinar múltiples habilidades de forma coherente y mantener contexto a largo plazo.
- **10-20 años**: Posible emergencia de sistemas que demuestren razonamiento abstracto, creatividad genuina y aprendizaje autónomo comparables o superiores a los humanos.