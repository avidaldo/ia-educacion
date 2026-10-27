---
title: Tests para Moodle
description: Generar preguntas con IA en un formato que Moodle importa directamente, y revisarlas antes de usarlas.
reviewed: 2026-04-30
---

> [!IMPORTANT]
> **Página en revisión**
> Faltan las capturas del aula virtual actual (Moodle 4.5 o posterior). Los pasos de importación están descritos por el nombre de los menús hasta que se añadan.

## Formatos que Moodle importa

Moodle importa preguntas desde un fichero de texto en varios formatos. Para trabajar con IA interesan tres:

| Formato | Para qué sirve | Ventajas | Limitaciones |
| --- | --- | --- | --- |
| Aiken | Opción múltiple sencilla | Muy fácil de leer y de generar | Solo opción múltiple con una respuesta correcta; sin penalización ni retroalimentación |
| GIFT | La mayoría de los tipos de pregunta | Compacto; admite penalizaciones, retroalimentación y varios tipos de pregunta | Sus caracteres especiales hay que escaparlos |
| Moodle XML | Todos los tipos de pregunta y todas sus opciones | Es el formato completo de exportación de Moodle | Largo y difícil de leer a simple vista |

Documentación oficial de Moodle: [Aiken](https://docs.moodle.org/all/es/Formato_Aiken), [GIFT](https://docs.moodle.org/all/es/Formato_GIFT) y [Moodle XML](https://docs.moodle.org/all/es/Formato_Moodle_XML).

### Aiken

```aiken
¿Cuál es la capital de Francia?
A. Londres
B. París
C. Berlín
D. Madrid
ANSWER: B
```

### GIFT

Una pregunta de opción múltiple con título, una respuesta correcta (`=`), tres incorrectas (`~`) que restan un 25 % y retroalimentación (`#`) en cada opción:

```gift
::Capital de Francia::¿Cuál es la capital de Francia?{
    =París#Correcto.
    ~%-25%Londres#Londres es la capital del Reino Unido.
    ~%-25%Berlín#Berlín es la capital de Alemania.
    ~%-25%Madrid#Madrid es la capital de España.
}
```

Una pregunta de verdadero o falso con retroalimentación. Ojo al orden: el **primer** mensaje es el que ve quien falla y el segundo, quien acierta.

```gift
::Retropropagación::¿La retropropagación es un algoritmo para ajustar los pesos de una red neuronal?{TRUE#Revisa cómo se entrena una red neuronal.#Correcto.}
```

> [!WARNING]
> **El fallo más habitual al importar GIFT**
> Los caracteres `~ = # { } :` tienen significado en GIFT. Si aparecen dentro del texto de una pregunta o de una respuesta (una fórmula, una hora, un enlace) hay que escribirlos con una barra delante: `\=`, `\:`, `\{`… Pide expresamente a la IA que los escape, y si una importación falla, empieza por buscar estos caracteres.

### Moodle XML

El fichero tiene que ser un documento XML completo: con la cabecera y todas las preguntas dentro de un único elemento `<quiz>`. Una pregunta de respuesta corta que acepta dos respuestas válidas:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="shortanswer">
    <name><text>Redes para imágenes</text></name>
    <questiontext format="html">
      <text><![CDATA[<p>Menciona un tipo de red neuronal muy utilizado en el procesamiento de imágenes.</p>]]></text>
    </questiontext>
    <defaultgrade>1</defaultgrade>
    <answer fraction="100" format="moodle_auto_format">
      <text>CNN</text>
      <feedback format="html"><text><![CDATA[<p>Correcto.</p>]]></text></feedback>
    </answer>
    <answer fraction="100" format="moodle_auto_format">
      <text>red neuronal convolucional</text>
      <feedback format="html"><text><![CDATA[<p>Correcto.</p>]]></text></feedback>
    </answer>
  </question>
</quiz>
```

## Generar las preguntas con IA

### El método más fiable: partir de una exportación de Moodle

En lugar de describirle a la IA el formato, **dale un ejemplo real**. Es la técnica de dar un ejemplo de salida (*one-shot*) aplicada a Moodle:

1. Crea a mano en Moodle una pregunta del tipo que quieres (por ejemplo, opción múltiple con penalización y retroalimentación).
2. Expórtala desde el banco de preguntas en el formato que vayas a usar (GIFT o Moodle XML).
3. Abre el fichero descargado, copia la pregunta y pégala en el *chat* como ejemplo: «Genera 10 preguntas sobre [tema] con exactamente este formato».
4. Añade las preguntas generadas al mismo fichero e impórtalo.

Así la IA copia exactamente lo que tu Moodle espera, incluidos los detalles que nadie recordaría describir (el marcado HTML, las penalizaciones, los caracteres ya escapados).

> [!TIP]
> **Un formato por conversación**
> Si le das ejemplos en formatos distintos a la vez (una pregunta en GIFT y otra en XML), los modelos tienden a mezclarlos. Usa un único formato en cada petición, y si necesitas convertir, pide la conversión como una tarea aparte.

### Un *prompt* base

```text
Genera 10 preguntas de opción múltiple en formato GIFT sobre: [TEMA].

Requisitos:
- 4 opciones por pregunta y una sola respuesta correcta.
- Variedad de dificultad (fácil, media, difícil).
- Distractores plausibles, de longitud parecida a la respuesta correcta.
- Escapa con \ los caracteres ~ = # { } : que aparezcan en el texto.
- Devuelve solo el contenido del fichero, sin comentarios.
```

### Un asistente personalizado para tests

Este *prompt* se usa como instrucciones fijas de un asistente que genera preguntas con criterios de rigor exigentes:

:::: chat model="ChatGPT (GPT personalizado)"
::: user
Crea preguntas de test en formato GIFT importable a Moodle, siguiendo las siguientes reglas.

- Siempre serán preguntas de respuesta múltiple con 4 respuestas y una única correcta.
- Las respuestas incorrectas restarán media pregunta a no ser que se indique lo contrario.
- Todas las respuestas deben tener una longitud similar.
- Se debe priorizar el rigor. La respuesta correcta debe ser la única que lo es. Las otras deben ser manifiestamente incorrectas.
- Deben evitarse respuestas incorrectas por no ser «la mejor definición» de las que se dan, «la principal desventaja» u otras formas de graduación. Las respuestas incorrectas deben ser manifiestamente incorrectas para evitar ambigüedades y las preguntas deben ser claras.
- Ninguna de las respuestas debe ser trivialmente descartable. Evita el habitual sesgo de que la pregunta correcta siempre sea una de 3 similares y haya otra más absurda.
- El nivel de dificultad esperado es para alumnos de máster universitario salvo que se indique lo contrario.
- No incluyas un número antes de las preguntas, serán barajadas.
- Normalmente se pasará material con el que generar las preguntas; evita hacer referencias directas como «según los apuntes». Las preguntas deben contener por sí solas toda la información necesaria para responderlas.
- Sé cuidadoso evitando sesgos como que la respuesta correcta sea la más detallada o la que tiene más longitud.

Un ejemplo del formato deseado:

```gift
::¿Qué es el muestreo estratificado?::[html]¿Qué es el muestreo estratificado?{
    ~%-50%Dividir el dataset en grupos y garantizar que todas las muestras de un grupo están en el mismo conjunto (test, validación o entrenamiento).
    =Dividir el dataset en grupos y tomar un porcentaje de cada estrato manteniendo la proporción original de las clases.
    ~%-50%Dividir el dataset en grupos y aumentar la presencia de las clases minoritarias duplicando o generando nuevas muestras.
    ~%-50%Dividir el dataset en grupos y aumentar la complejidad del modelo para hacerlo más robusto.
}
```
:::
::: assistant collapsed
```gift
::¿Qué es un modelo generativo en inteligencia artificial?::[html]¿Qué es un modelo generativo en inteligencia artificial?{
    ~%-50%Un algoritmo que clasifica datos existentes en categorías predefinidas basándose en características aprendidas durante el entrenamiento.
    ~%-50%Un sistema que optimiza decisiones secuenciales mediante la interacción con un entorno para maximizar una recompensa acumulativa.
    =Un tipo de modelo que aprende la distribución de los datos de entrenamiento y puede generar nuevas muestras similares a estos.
    ~%-50%Un enfoque que reduce la dimensionalidad de datos complejos transformándolos en representaciones más simples mientras preserva información esencial.
}

::¿Qué es la validación cruzada?::[html]¿Qué es la validación cruzada (cross-validation)?{
    ~%-50%Una técnica para reducir la complejidad del modelo eliminando características redundantes del conjunto de datos.
    ~%-50%Un método para evaluar el rendimiento de varios modelos simultáneamente en un único conjunto de entrenamiento.
    ~%-50%Un procedimiento que combina las predicciones de varios modelos para mejorar la precisión general del sistema.
    =Una técnica que divide los datos en múltiples subconjuntos para entrenar y validar el modelo, usando cada subconjunto como datos de prueba una vez.
}
```
:::
::::

Con estas instrucciones hay un [GPT público](https://chatgpt.com/g/g-67b721d49a0481918a78bc5104bd22ea-generador-de-preguntas-de-test) que se puede usar directamente.

> [!WARNING]
> **Qué escribir en las instrucciones de un asistente**
> No escribas «Crea un generador de preguntas de test…»: eso describe el asistente, no lo que debe hacer. Escribe directamente las instrucciones que quieres que se apliquen en cada conversación: «Cuando el usuario te dé un tema o un material, genera preguntas de test en formato GIFT con estas reglas…».

## Revisar antes de importar

Generar es la parte fácil. La revisión es imprescindible y no se puede delegar:

- [ ] **La clave es correcta.** Comprueba que la respuesta marcada como correcta lo es, y que ninguna de las incorrectas también podría serlo.
- [ ] **Sin pistas involuntarias.** La correcta no es sistemáticamente la más larga, la más detallada ni la más matizada.
- [ ] **Sin negaciones confusas.** Las preguntas con «NO» o «EXCEPTO» suelen medir la atención más que el conocimiento.
- [ ] **Autocontenidas.** Se pueden responder sin consultar los apuntes («según el tema 3…»).
- [ ] **El fichero importa.** Pruébalo primero en un banco de preguntas de pruebas y mira la vista previa.

## Importar en Moodle

1. Guarda las preguntas en un fichero de texto (`.txt` para GIFT o Aiken, `.xml` para Moodle XML) con codificación UTF-8.
2. Abre el banco de preguntas:
   - En **Moodle 4.x**: en el curso, **Más → Banco de preguntas**, y en el desplegable de la página, **Importar**.
   - En **Moodle 5.0 o posterior**: los bancos de preguntas son una actividad del curso. Entra en **Más → Bancos de preguntas**, abre el banco donde quieras guardarlas y elige **Importar**.
3. Elige el formato, sube el fichero y pulsa **Importar**. Moodle muestra las preguntas importadas o el error de la línea que falla.
4. En el cuestionario, **Preguntas → Añadir → del banco de preguntas**, selecciona las nuevas y añádelas.
5. Usa la **vista previa** del cuestionario antes de abrirlo al alumnado.

## Para ir más allá

Para bancos grandes generados a partir de los materiales de un curso, el proyecto [tests-generator](https://github.com/avidaldo/tests-generator) automatiza el proceso completo: resume los materiales, genera las preguntas por lotes, permite revisarlas en un editor y exporta a Moodle XML.
