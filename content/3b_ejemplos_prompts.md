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