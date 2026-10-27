---
title: Cómo funciona un modelo de lenguaje
description: Qué hace por dentro un modelo de lenguaje y por qué eso explica tanto sus aciertos como sus errores.
reviewed: 2026-10-22
review_every: 12
---

## Predecir la siguiente palabra

Un modelo de lenguaje hace, en esencia, lo mismo que el teclado del móvil cuando sugiere la siguiente palabra: **calcula qué es más probable que venga a continuación**, dado todo el texto anterior. Después añade esa palabra al texto y repite el proceso, palabra a palabra, hasta completar la respuesta.

La diferencia con el teclado es de escala. El modelo se ha entrenado con una cantidad enorme de texto (libros, webs, artículos, código) y tiene miles de millones de parámetros, de modo que sus predicciones tienen en cuenta párrafos enteros, el tono, la estructura de un documento o lo que se dijo veinte mensajes antes.

Una analogía: alguien que haya leído miles de recetas puede adivinar que después de «añadir sal y…» suele venir «pimienta», sin que eso garantice que la receta concreta lo lleve. El modelo hace algo parecido con todo tipo de textos, a una escala inmensamente mayor.

> [!IMPORTANT]
> **La idea que lo explica casi todo**
> Un modelo de lenguaje no consulta una base de datos de hechos ni comprueba lo que dice: genera la continuación **más plausible** según los patrones que aprendió. Casi siempre lo plausible coincide con lo correcto; cuando no coincide, el error se presenta con la misma fluidez que un acierto.

## *Tokens* y ventana de contexto

En realidad el modelo no trabaja con palabras, sino con ***tokens***: fragmentos de texto que pueden ser una palabra corta, parte de una palabra larga o un signo de puntuación. En español, una palabra ocupa a menudo más de un *token*.

La **ventana de contexto** es la cantidad máxima de *tokens* que el modelo puede tener en cuenta a la vez: tus instrucciones, toda la conversación, los documentos adjuntos y la propia respuesta. Lo que queda fuera de la ventana no existe para el modelo. Por eso, en conversaciones muy largas o con documentos enormes, el modelo puede «olvidar» instrucciones del principio o pasar por alto partes de un fichero. El tamaño de la ventana varía mucho entre modelos y planes; las cifras actuales están en [Chatbots](../chatbots/index.md).

## Del modelo base al asistente

Un *chatbot* como los actuales se construye en dos grandes fases:

1. **Preentrenamiento.** El modelo aprende a predecir el siguiente *token* sobre una cantidad masiva de texto. El resultado, el *modelo base*, sabe continuar textos de cualquier tipo, pero no sigue instrucciones: si le escribes una pregunta, puede continuar con otra pregunta.
2. **Ajuste posterior.** Con ejemplos de conversaciones bien resueltas y con valoraciones humanas de qué respuesta es mejor (el llamado *aprendizaje por refuerzo con retroalimentación humana*), el modelo aprende a comportarse como un asistente: seguir instrucciones, responder con un formato útil, negarse a ciertas peticiones.

Esta segunda fase explica rasgos que a veces se atribuyen a una «personalidad»: el tono servicial, la tendencia a dar la razón o los avisos de seguridad. Son comportamientos aprendidos durante el ajuste.

## Por qué no responde siempre lo mismo

En cada paso el modelo no calcula una única palabra, sino una **distribución de probabilidades** sobre todas las posibles. El *chatbot* elige entre las más probables con un componente de azar controlado. Por eso la misma pregunta puede dar respuestas distintas, y por eso merece la pena **regenerar** una respuesta o hacer la misma petición en un chat nuevo cuando el resultado importa.

Que el texto de entrada condicione las probabilidades explica también por qué funciona el diseño de *prompts*: no es un truco, es dar al modelo el contexto que desplaza sus predicciones hacia lo que quieres. Se ve en [Diseño de prompts](../prompts/index.md).

## Alucinaciones: plausible no es verdadero

Se llama **alucinación** a una respuesta fluida y segura que es falsa: un dato inventado, una cita que no existe, una referencia bibliográfica con autores y título verosímiles pero imaginarios.

No es un fallo puntual que se vaya a corregir en la próxima versión, sino una consecuencia de cómo se entrenan estos modelos. Su objetivo es producir texto plausible, y tanto el entrenamiento como las evaluaciones habituales premian más arriesgar una respuesta que reconocer «no lo sé».[^kalai] Los modelos actuales se equivocan bastante menos que los de hace dos años, sobre todo cuando buscan en la web, pero el riesgo no desaparece.

> [!WARNING]
> **Implicación práctica**
> Toda cifra, cita, referencia o norma que genere un modelo se comprueba en la fuente antes de usarla en clase o en un documento oficial.

> [!TIP]
> **Pruébalo**
> En un chat temporal, y sin búsqueda web si tu *chatbot* permite desactivarla, pide tres referencias académicas sobre un tema muy concreto de tu materia y busca cada título en un buscador académico. Después repite la petición con la búsqueda activada y abre las fuentes que cite. Es habitual encontrar alguna referencia verosímil que no existe, o con autores, año o revista cambiados.

## Lo que sabe y lo que busca

El modelo aprende hasta una **fecha de corte**: lo que pasó después no está en sus parámetros. Los *chatbots* actuales compensan esa limitación **buscando en la web** y citando las páginas que usan. Eso mejora mucho la actualidad y permite verificar, pero introduce otro riesgo: el modelo puede elegir fuentes poco fiables o resumirlas mal.

Tampoco es exacto decir que el modelo «no memoriza nada». Aprende patrones generales, pero también puede reproducir de forma literal fragmentos de sus datos de entrenamiento, sobre todo textos que aparecen muchas veces.[^carlini] Es una de las razones de los conflictos sobre derechos de autor y de la recomendación de no introducir datos personales en estas herramientas ([Ética y normativa](../etica-legal/index.md#privacidad-la-regla-práctica)).

## Modelos que razonan

Desde 2024 existen modelos entrenados para **generar un razonamiento intermedio antes de responder**: descomponen el problema, prueban caminos y revisan pasos. Se entrenan sobre todo con problemas cuya respuesta se puede comprobar (matemáticas, programación, lógica), y en ese tipo de tareas mejoran mucho, a cambio de tardar más y gastar más.

Hoy la mayoría de los *chatbots* deciden por sí mismos cuánto razonar según la pregunta, o permiten activarlo con una opción. Dos matices importantes:

- El razonamiento sigue siendo texto generado por el mismo mecanismo: mejora los resultados, pero no convierte al modelo en un sistema de deducción lógica infalible.
- El razonamiento que muestra el *chatbot* no siempre refleja lo que de verdad determinó la respuesta: los propios desarrolladores han documentado casos en que el modelo usó una pista que no menciona en su razonamiento.[^chen]

## Sesgos: un reflejo de los datos

Si en los textos de entrenamiento ciertas profesiones se asocian más a un género, o ciertos grupos se describen con otros adjetivos, el modelo aprende esas asociaciones, porque eso es exactamente lo que hace: extraer las regularidades de sus datos. Los sesgos no son una «decisión» del modelo, sino un reflejo estadístico de los textos con los que se entrenó, de cómo se seleccionaron y de cómo se hizo el ajuste posterior.

Corregirlos tampoco es trivial: las correcciones introducen sus propios desequilibrios. Los casos documentados, y cómo se detecta un sesgo midiendo el error por grupos, se tratan en [Ética y normativa](../etica-legal/index.md#sesgos).

## Para saber más

<details>
<summary>La arquitectura <em>transformer</em> y la atención</summary>

Los modelos de lenguaje actuales usan la arquitectura *transformer*.[^vaswani] Su pieza central, la **atención**, permite que al procesar cada *token* el modelo pondere la relevancia de todos los anteriores: al leer «lo» en «dejé el libro en la mesa y lo abrí», la atención relaciona «lo» con «libro». Como estos cálculos se pueden hacer en paralelo, la arquitectura aprovecha muy bien las GPU, y eso hizo posible entrenar modelos enormes.

</details>

<details>
<summary>Cómo representa el modelo las palabras</summary>

Cada *token* se convierte en un vector de miles de números (un *embedding*). Durante el entrenamiento, los *tokens* que aparecen en contextos parecidos acaban con vectores próximos, de modo que el modelo trabaja con relaciones de significado aproximadas («rey» queda cerca de «reina» y de «monarca»). Las capas del modelo transforman esos vectores teniendo en cuenta el contexto hasta producir la distribución de probabilidad del siguiente *token*.

</details>

<details>
<summary>Del modelo base al asistente, con más detalle</summary>

El trabajo que popularizó el ajuste con valoraciones humanas, base de ChatGPT, es el de Ouyang et al. (2022).[^ouyang] Hoy el ajuste combina varias técnicas: ejemplos escritos por personas, comparaciones entre respuestas, reglas explícitas que el propio modelo usa para evaluarse y, en los modelos que razonan, aprendizaje por refuerzo con problemas verificables.

</details>

[^kalai]: Kalai, A. T. et al. (2025). [*Why Language Models Hallucinate*](https://arxiv.org/abs/2509.04664).
[^carlini]: Carlini, N. et al. (2021). [*Extracting Training Data from Large Language Models*](https://arxiv.org/abs/2012.07805).
[^chen]: Chen, Y. et al. (2025). [*Reasoning Models Don't Always Say What They Think*](https://arxiv.org/abs/2505.05410).
[^vaswani]: Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762).
[^ouyang]: Ouyang, L. et al. (2022). [*Training language models to follow instructions with human feedback*](https://arxiv.org/abs/2203.02155).
