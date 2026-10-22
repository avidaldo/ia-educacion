---
title: Que é a intelixencia artificial
description: De onde vén o que hoxe chamamos «a IA», por que despegou agora e que distingue un modelo, un chatbot e un axente.
derived_from:
  es/intro-ia/index.md: "092b9369e10fe8c4f69fb793a24a4bab55e19b09"
---

## Catro conceptos, un dentro doutro

O que hoxe se chama «a IA» na linguaxe cotiá é só a parte máis recente dun campo con setenta anos de historia. Convén distinguir catro conceptos, cada un contido no anterior.

![Diagrama de catro conxuntos aniñados: a intelixencia artificial contén a aprendizaxe automática, que contén a aprendizaxe profunda, que contén a IA xerativa](../../assets/intro-ia/ia-aprendizaje-generativa.svg)

### Intelixencia artificial

O termo nace en 1956, nun seminario en Dartmouth (Estados Unidos), e designa o desenvolvemento de sistemas que realizan tarefas que asociamos á intelixencia humana. Durante décadas, a maioría deses sistemas funcionaban con **regras escritas a man**:

- ELIZA (1966) simulaba unha conversa cun terapeuta buscando palabras clave e respondendo con frases predefinidas.
- Deep Blue (1997) derrotou Kasparov ao xadrez combinando estratexias programadas cunha enorme capacidade de cálculo.

### Aprendizaxe automática

A aprendizaxe automática (*machine learning*, termo que aparece en 1959) cambia o enfoque: en lugar de escribir as regras, dánselle ao programa **datos coas súas respostas** e o adestramento extrae as regras. O resultado é un **modelo**: un conxunto de parámetros que, aplicado a datos novos, produce respostas.

![Esquema: na programación clásica, regras e datos entran nun programa que produce respostas; na aprendizaxe automática, datos e respostas entran nun adestramento que produce un modelo](../../assets/intro-ia/programacion-y-aprendizaje.svg)

É a técnica detrás dos filtros de *spam*, das recomendacións de vídeos ou da predición do tempo, moito antes dos *chatbots*.

### Redes neuronais e aprendizaxe profunda

As redes neuronais artificiais son un tipo de modelo inspirado, de forma moi simplificada, nas neuronas biolóxicas: a neurona artificial descríbese en 1943, o perceptrón en 1957, e a técnica que permite adestrar redes de varias capas (a retropropagación) popularízase en 1986.

A **aprendizaxe profunda** (*deep learning*) usa redes con moitas capas. Despega en 2012, cando unha rede deste tipo, AlexNet, reduce o erro na principal competición de recoñecemento de imaxes do 26 % ao 15 %.

### IA xerativa

A IA xerativa usa aprendizaxe profunda para **xerar contido novo**: texto, imaxes, audio, vídeo ou código. É o que se popularizou como «a IA» desde finais de 2022, con ChatGPT.

## O paradoxo de Moravec

Na década de 1980, Hans Moravec e outros investigadores sinalaron algo que segue a sorprender: é relativamente doado que un ordenador faga o que ás persoas nos custa (cálculo, lóxica formal, xadrez) e moi difícil que faga o que calquera neno fai sen esforzo (recoñecer obxectos, moverse por un cuarto, entender unha frase ambigua).

A aprendizaxe profunda resolveu boa parte da percepción e da linguaxe, pero o paradoxo axuda a entender por que a IA actual pode redactar un informe impecable e fallar nunha pregunta de sentido común, ou por que a robótica avanza moito máis amodo ca os *chatbots*.

## Por que agora

O auxe dos últimos anos non se debe a unha idea nova, senón á coincidencia de catro factores:

- **Capacidade de cálculo**: procesadores gráficos (GPU) e chips específicos que permiten adestrar redes enormes.
- **Datos**: a web, os libros dixitalizados e o código público ofrecen cantidades de texto e imaxes sen precedentes.
- **Arquitecturas**: o *transformer* (2017) permite adestrar modelos de linguaxe moito máis grandes de forma eficiente.
- **Investimento**: desde 2022 a industria dedica á IA recursos que antes non tiña ningún campo de investigación.

## Unha liña temporal

- **2012**: AlexNet inicia o auxe da aprendizaxe profunda na visión por ordenador.
- **2014**: as redes xerativas adversarias (GAN) abren a xeración de imaxes sintéticas, aínda pequenas e borrosas.
- **2016**: AlphaGo, de DeepMind, derrota o campión mundial de go Lee Sedol.
- **2017**: publícase a arquitectura *transformer*, base dos modelos de linguaxe actuais.
- **2020**: GPT-3 mostra que un modelo de linguaxe moi grande pode facer tarefas para as que non se adestrou especificamente.
- **2022**: os modelos de difusión xeran imaxes realistas a partir de texto; en novembro, ChatGPT populariza os asistentes conversacionais.
- **2023**: chegan os modelos multimodais, que traballan con texto e imaxes á vez.
- **2024**: aparecen os modelos que «razoan» antes de responder (OpenAI o1).
- **2025**: DeepSeek-R1 publica os seus pesos cun rendemento comparable ao de o1 e un custo de uso moito menor; o vídeo xerado incorpora son (Veo 3); chegan os navegadores con axentes (Comet) e os modelos que deciden por si mesmos canto razoar (GPT-5).

Para o estado actual das ferramentas, consulta [Chatbots](../chatbots/index.md).

## Modelo, *chatbot* e axente

Son tres cousas distintas, e confundilas leva a malentendidos:

Modelo de linguaxe
: O sistema adestrado que, dado un texto, xera unha continuación. GPT-5, Gemini ou Claude Sonnet son nomes de modelos ou de familias de modelos.

*Chatbot* ou asistente
: O produto co que conversamos (ChatGPT, Gemini, Claude, Perplexity…). Usa un ou varios modelos e engádelles unha interface, memoria, busca web, ficheiros adxuntos e outras ferramentas.

Axente
: Un sistema que, a partir dun obxectivo, **actúa**: planifica pasos, usa ferramentas (un navegador, un programa, o correo) e decide que facer a continuación segundo o que observa, ata cumprir o obxectivo ou deterse.

A diferenza práctica: a un *chatbot* pregúntaslle e respóndeche; a un axente encargáslle unha tarefa e execútaa, cos riscos que iso implica. Vese en detalle en [Navegadores con axentes](../navegadores-agenticos/index.md).

Como funciona por dentro un modelo de linguaxe, e por que iso explica os seus acertos e os seus erros, está en [Como funciona un modelo de linguaxe](funcionamiento.md).
