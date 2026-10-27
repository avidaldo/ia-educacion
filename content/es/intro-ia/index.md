---
title: Qué es la inteligencia artificial
description: De dónde viene lo que hoy llamamos «la IA», por qué ha despegado ahora y qué distingue a un modelo, un chatbot y un agente.
reviewed: 2026-10-22
review_every: 12
---

## Cuatro conceptos, uno dentro de otro

Lo que hoy se llama «la IA» en el lenguaje cotidiano es solo la parte más reciente de un campo con setenta años de historia. Conviene distinguir cuatro conceptos, cada uno contenido en el anterior.

![Diagrama de cuatro conjuntos anidados: la inteligencia artificial contiene el aprendizaje automático, que contiene el aprendizaje profundo, que contiene la IA generativa](../../assets/intro-ia/ia-aprendizaje-generativa.svg)

### Inteligencia artificial

El término nace en 1956, en un seminario en Dartmouth (Estados Unidos), y designa el desarrollo de sistemas que realizan tareas que asociamos a la inteligencia humana. Durante décadas, la mayoría de esos sistemas funcionaban con **reglas escritas a mano**:

- ELIZA (1966) simulaba una conversación con un terapeuta buscando palabras clave y respondiendo con frases predefinidas.
- Deep Blue (1997) derrotó a Kasparov al ajedrez combinando estrategias programadas con una enorme capacidad de cálculo.

### Aprendizaje automático

El aprendizaje automático (*machine learning*, término acuñado en 1959) cambia el planteamiento: en lugar de escribir las reglas, se le dan al programa **datos con sus respuestas** y el entrenamiento extrae las reglas. El resultado es un **modelo**: un conjunto de parámetros que, aplicado a datos nuevos, produce respuestas.

![Esquema: en la programación clásica, reglas y datos entran en un programa que produce respuestas; en el aprendizaje automático, datos y respuestas entran en un entrenamiento que produce un modelo](../../assets/intro-ia/programacion-y-aprendizaje.svg)

Es la técnica detrás de los filtros de *spam*, las recomendaciones de vídeos o la predicción del tiempo, mucho antes de los *chatbots*.

### Redes neuronales y aprendizaje profundo

Las redes neuronales artificiales son un tipo de modelo inspirado, de forma muy simplificada, en las neuronas biológicas: la neurona artificial se describe en 1943, el perceptrón en 1957, y la técnica que permite entrenar redes de varias capas (la retropropagación) se populariza en 1986.

El **aprendizaje profundo** (*deep learning*) usa redes con muchas capas. Despega en 2012, cuando una red de este tipo, AlexNet, reduce el error en la principal competición de reconocimiento de imágenes del 26 % al 15 %.

### IA generativa

La IA generativa usa aprendizaje profundo para **generar contenido nuevo**: texto, imágenes, audio, vídeo o código. Es lo que se ha popularizado como «la IA» desde finales de 2022, con ChatGPT.

## La paradoja de Moravec

En la década de 1980, Hans Moravec y otros investigadores señalaron algo que sigue sorprendiendo: es relativamente fácil que un ordenador haga lo que a las personas nos cuesta (cálculo, lógica formal, ajedrez) y muy difícil que haga lo que cualquier niño hace sin esfuerzo (reconocer objetos, moverse por una habitación, entender una frase ambigua).

El aprendizaje profundo ha resuelto buena parte de la percepción y del lenguaje, pero la paradoja ayuda a entender por qué la IA actual puede redactar un informe impecable y fallar en una pregunta de sentido común, o por qué la robótica avanza mucho más despacio que los *chatbots*.

## Por qué ahora

El auge de los últimos años no se debe a una idea nueva, sino a la coincidencia de cuatro factores:

- **Capacidad de cálculo**: procesadores gráficos (GPU) y chips específicos que permiten entrenar redes enormes.
- **Datos**: la web, los libros digitalizados y el código público ofrecen cantidades de texto e imágenes sin precedentes.
- **Arquitecturas**: el *transformer* (2017) permite entrenar modelos de lenguaje mucho más grandes de forma eficiente.
- **Inversión**: desde 2022 la industria dedica a la IA recursos que antes no tenía ningún campo de investigación.

## Una línea temporal

- **2012**: AlexNet inicia el auge del aprendizaje profundo en visión por ordenador.
- **2014**: las redes generativas adversarias (GAN) abren la generación de imágenes sintéticas, todavía pequeñas y borrosas.
- **2016**: AlphaGo, de DeepMind, derrota al campeón mundial de go Lee Sedol.
- **2017**: se publica la arquitectura *transformer*, base de los modelos de lenguaje actuales.
- **2020**: GPT-3 muestra que un modelo de lenguaje muy grande puede hacer tareas para las que no se entrenó específicamente.
- **2022**: los modelos de difusión generan imágenes realistas a partir de texto; en noviembre, ChatGPT populariza los asistentes conversacionales.
- **2023**: llegan los modelos multimodales, que trabajan con texto e imágenes a la vez.
- **2024**: aparecen los modelos que «razonan» antes de responder (OpenAI o1).
- **2025**: DeepSeek-R1 publica sus pesos con un rendimiento comparable al de o1 y un coste de uso mucho menor; el vídeo generado incorpora sonido (Veo 3); llegan los navegadores con agentes (Comet) y los modelos que deciden por sí mismos cuánto razonar (GPT-5).

Para el estado actual de las herramientas, consulta [Chatbots](../chatbots/index.md).

## Modelo, *chatbot* y agente

Son tres cosas distintas, y confundirlas lleva a malentendidos:

Modelo de lenguaje
: El sistema entrenado que, dado un texto, genera una continuación. GPT-5, Gemini o Claude Sonnet son nombres de modelos o de familias de modelos.

*Chatbot* o asistente
: El producto con el que conversamos (ChatGPT, Gemini, Claude, Perplexity…). Usa uno o varios modelos y les añade una interfaz, memoria, búsqueda web, ficheros adjuntos y otras herramientas.

Agente
: Un sistema que, a partir de un objetivo, **actúa**: planifica pasos, usa herramientas (un navegador, un programa, el correo) y decide qué hacer a continuación según lo que observa, hasta cumplir el objetivo o detenerse.

La diferencia práctica: a un *chatbot* le preguntas y te responde; a un agente le encargas una tarea y la ejecuta, con los riesgos que eso implica. Se ve en detalle en [Navegadores con agentes](../navegadores-agenticos/index.md).

Cómo funciona por dentro un modelo de lenguaje, y por qué eso explica sus aciertos y sus errores, está en [Cómo funciona un modelo de lenguaje](funcionamiento.md).
