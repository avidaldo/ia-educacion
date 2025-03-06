# Ejemplos de Prompts

En esta sección mostraremos ejemplos de conversaciones con modelos de IA como ChatGPT.

## Ejemplo de conversación simple

```chat

USER: Explícame qué es el aprendizaje por refuerzo en inteligencia artificial.

ASSISTANT: El aprendizaje por refuerzo es un tipo de aprendizaje automático en el que un agente aprende a tomar decisiones mediante la interacción con un entorno. Funciona así:

1. El agente realiza una acción en un entorno
2. Recibe una recompensa o penalización basada en esa acción
3. Ajusta su estrategia para maximizar la recompensa a largo plazo

A diferencia del aprendizaje supervisado, no necesita datos etiquetados. En lugar de eso, aprende a través de prueba y error, similar a cómo los humanos aprendemos muchas habilidades.

Ejemplos prácticos incluyen:
- Algoritmos que juegan videojuegos (como AlphaGo)
- Sistemas de recomendación que mejoran con el tiempo
- Robots que aprenden a caminar o manipular objetos
- Vehículos autónomos

USER: ¿Cuáles son las principales diferencias entre el aprendizaje por refuerzo y el aprendizaje supervisado?

ASSISTANT: Las principales diferencias entre el aprendizaje por refuerzo y el aprendizaje supervisado son:

| Aprendizaje por Refuerzo | Aprendizaje Supervisado |
|--------------------------|-------------------------|
| Aprende de la interacción con un entorno | Aprende de ejemplos etiquetados |
| Recibe feedback a través de recompensas/penalizaciones | Recibe feedback comparando predicciones con respuestas correctas |
| No necesita datos etiquetados | Requiere un conjunto grande de datos etiquetados |
| Proceso iterativo de exploración y explotación | Proceso directo de mapeo de entradas a salidas |
| Optimiza para recompensas futuras (visión a largo plazo) | Optimiza para precisión inmediata |
| Ejemplos: robótica, juegos, sistemas de navegación | Ejemplos: clasificación de imágenes, predicción de precios, filtros de spam |

El aprendizaje supervisado es como estudiar con un profesor que te da problemas resueltos, mientras que el aprendizaje por refuerzo es como aprender a andar en bicicleta: caes, te levantas y mejoras gradualmente basándote en tu experiencia.
```

## Ejemplo de prompt con instrucciones específicas

```chat
USER: Actúa como profesor de primaria y explícame el ciclo del agua usando analogías que un niño de 8 años pueda entender. Incluye una pequeña actividad que podría hacer en casa para visualizar el proceso.

ASSISTANT: ¡Hola pequeño explorador! Hoy vamos a descubrir juntos el maravilloso viaje del agua por nuestro planeta. ¿Sabes? El agua es como una viajera incansable que nunca para de moverse.

## El Ciclo del Agua para Pequeños Exploradores

Imagina que el agua es como un grupo de amiguitos diminutos que les encanta jugar al "pilla-pilla" gigante por todo el planeta:

1. **El Sol como despertador**: Cuando el Sol calienta el agua de los océanos, lagos y ríos, es como si sonara un despertador diciendo "¡Arriba, amiguitos del agua! ¡Es hora de subir al cielo!". Los amiguitos del agua se vuelven tan ligeros que se convierten en vapor (como el vapor de la ducha caliente) y suben, suben, suben.

2. **Las nubes como fiestas de pijamas**: Allá arriba en el cielo, hace más fresquito y los amiguitos del agua se juntan formando nubes. ¡Es como una gran fiesta de pijamas en el cielo! Cuando hay muchos amiguitos juntos, la nube se pone gordita y gris.

3. **La lluvia como tobogán**: Cuando la nube está muy llena, es hora de bajar por el tobogán. ¡Splish, splash! Los amiguitos del agua caen como lluvia, o si hace mucho frío, como nieve o granizo.

4. **Ríos como autopistas**: Cuando los amiguitos llegan al suelo, buscan el camino más fácil para volver al mar. Forman ríos, que son como autopistas de agua que viajan hasta llegar al océano. Algunos amiguitos se quedan un tiempo descansando en lagos o se filtran bajo tierra como espías secretos.

5. **¡Y vuelta a empezar!**: Cuando llegan al océano... ¡el Sol vuelve a despertarlos y comienza la aventura otra vez!

## Actividad del Ciclo del Agua en Casa

**Necesitarás**:
- Un vaso transparente
- Agua
- Una bolsa de plástico transparente o film plástico
- Una goma elástica
- Colorante alimentario (opcional)

**Pasos**:
1. Llena el vaso hasta la mitad con agua (puedes añadir colorante para verlo mejor)
2. Cubre el vaso con el plástico y asegúralo con la goma elástica
3. Coloca el vaso en un lugar soleado
4. Observa durante el día: ¡verás gotitas formándose en el plástico!

Lo que sucede es magia científica: el Sol calienta el agua, que sube como vapor, toca el plástico más fresquito y se convierte en gotitas (como una mini nube). Cuando las gotitas son pesadas, ¡caen de nuevo como mini lluvia!

¿No es asombroso que puedas ver todo el ciclo del agua en un vasito? ¡Los amiguitos del agua han hecho su viaje completo frente a tus ojos!
```

Este formato te permite crear y visualizar conversaciones que se mostrarán con un formato similar a ChatGPT en tu página web. Simplemente coloca tus conversaciones dentro de bloques de código con la etiqueta `chat` y utiliza las prefijos `USER:` y `ASSISTANT:` para identificar quién está hablando en cada momento. 


## Ejemplo de prompt utilizado para un GPT personalizado

Los "GPT's" son una función de ChatGPT que te permite trabajar con prompts específicos almacenados por anticipado.

> Ojo, error en el prompt que se ha utilizado para crear este GPT:
> ~~Crea un generador de preguntas de test~~ 
> Aunque estamos definiendo un GPT personalizado, en sus `Instrucciones` debemos escribir directamnte el prompt que se pondrá delante del que luego añadirá el usuario, y no queremos un generador de preguntas de test (nos indicaría como crear un programa que genere preguntas de test), queremos directamente generar las preguntas.

```chat

USER: Crea preguntas de test en formato GIFT importable a Moodle, siguiendo las siguientes reglas.
- Siempre serán preguntas de respuesta múltiple con 4 respuestas y una única correcta.
- Las respuestas incorrectas restarán media pregunta a no ser que se indique lo contrario.
- Todas las respuestas deben tener una longitud similar.
- Se debe priorizar el rigor. La respuesta correcta debe ser la única que lo es. Las otras deben ser manifiestamente incorrectas.
- Deben evitarse preguntas respuestas incorrectas por no ser "la mejor definición" de las que se dan, "la principal desventaja" u otras formas de graduación. Las respuestas incorrectas deben ser manifiestamente incorrectas para evitar ambigüedades y las preguntas deben ser claras.
- Ninguna de las respuestas debe ser trivialmente descartable. Evita el habitual sesgo de que la pregunta correcta siempre sea una de 3 similares y haya otra más absurda.
- El nivel de dificultad esperado es para alumnos de master universitario salvo que se indique lo contrario.
- No incluyas un número antes de las preguntas, serán barajadas.
- Normalmente se pasará material con el que generar las preguntas, evita hacer referencias directas como "según los apuntes". Las preguntas deben contener por si solas toda la información necesaria para responderlas. Los alumnos no podrán consultar los apuntes durante la prueba.
- Se cuidadoso evitando sesgos como que la respuesta correcta sea la más detallada o la que tiene más longitud.

Un ejemplo del formato deseado de pregunta sería el siguiente:


// question: 91483439  name: ¿Qué es el muestreo estratificado?
::¿Qué es el muestreo estratificado?::[html]¿Qué es el muestreo estratificado?{
	~%-50%Dividir el dataset en grupos y garantizar que todas las muestras de un grupo lo están en el mismo conjunto (test, validación o entrenamiento).
	=Dividir el dataset en grupos y tomar un porcentaje de cada estrato manteniendo la proporción original de las clases
	~%-50%Dividir el dataset en grupos y aumentar la presencia de las clases minoritarias mediante la duplicación o generación de nuevas muestras, lo que puede llevar a una representación más equilibrada de las clases en el conjunto de prueba.
	~%-50%Dividir el dataset en grupos y aumentar la complejidad del modelo, lo que puede resultar en un modelo más robusto pero también más difícil de interpretar y ajustar.
}
```

[GPT personalizado creado con este prompt](https://chatgpt.com/g/g-67b721d49a0481918a78bc5104bd22ea-generador-de-preguntas-de-test)

[Ejemplo de chat con él con preguntas sobre los apuntes previos de prompt engineering y pidiendo indicaciones de cómo importar a Moodle](https://chatgpt.com/share/67b732ca-1a94-8002-978e-d2c13676e49a)