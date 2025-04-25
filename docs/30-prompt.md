# Prompt Engineering

## Introducción

- ¿Qué es un prompt y por qué es importante?
    - Un prompt es una instrucción que se le da a un modelo de lenguaje para que genere una respuesta (la pregunta que le hacemos al chatbot).
    - Es importante porque determina la calidad de la respuesta.
    - Un buen prompt es aquel que permite al modelo entender bien lo que se le pide y dar una respuesta adecuada.
    - Un mal prompt puede llevar a respuestas incorrectas o incoherentes.

## Estrategias de diseño de prompts

### Lo más básico:
    - Usa varios modelos (distintas aplicaciones) y prueba.
    - Siempre itera: da correcciones y matices a las respuestas.
        - crítico e inquisitivo ("¿Estás seguro?")
    - Pregunta al propio modelo cómo mejorar el prompt / Ofrece al modelo clarificar dudas.
    - Estructura: "dado esto, siguiendo estas reglas y estas restricciones, dame esto"

### Reglas ~~básicas~~ tradicionales para definir un buen prompt:
    - Rol que tomará el modelo (rol experto)
    - Público objetivo (alumnos de tal edad)
    - Estilo de lenguaje (formal, explicativo, pedagógico)
    - Ejemplos de respuestas correctas (*few-shot*)
    - Qué no queremos (evita...)
    - Objetivos (qué queremos conseguir)
    - Pedirle que piense paso a paso (*chain of thought* - CoT)
    - Ejemplos concretos de razonamientos similares al que queremos que siga (OJO: ya no hacer esto)

### [Con **modelos razonadores** (GPT-o1 / GPT-o3](https://platform.openai.com/docs/guides/reasoning#advice-on-prompting) / DeepSeek-R1)
    - Mejor prompts más directos (aplica todo lo anterior pero solo lo estricto, claro y necesario)
    - CoT puede ser contraproducente; ya lo hace solo.
    - Especificar un rol podría ser redundante o limitar la capacidad del modelo de aprovechar su razonamiento interno.
    - Demasiados ejemplos pueden inducir una sobreespecialización o incluso interferir con el proceso interno, intenta primero con un prompt (*zero-shot*).

> En modelos anteriores, dar ejemplos explícitos de cadenas de pensamiento inducía al modelo a “pensar en voz alta” y a desplegar sus pasos intermedios. Sin embargo, en o1, o3 y variantes similares, el razonamiento ya se ejecuta de forma interna y optimizada; incluir ejemplos de cadena de pensamiento o indicaciones como “piensa paso a paso” puede incluso obstaculizar su rendimiento, pues estos modelos han sido diseñados para operar con prompts simples y directos


## *Contrarian Prompting*

Lo que le pides a una IA, pide a otra (o a un chat temporal / sin memoria) que haga una valoración crítica. Pedírselo a otra hace que no esté sesgada por su memoria de las conversaciones previas. De este modo, se esquiva el sesgo de "dar siempre la razón" o de "no cuestionar lo que ya ha dicho".

> "Haz un análisis señalando todo aquello que pueda ser cuestionable o mejorable en el siguiente texto. Sé exhaustivo y crítico. El texto es el siguiente: [texto]."


### *Deep Research* (Investigación en profundidad)

Generador de informes detallados y estructurados. Toma un tiempo y un tema, y genera un informe con fuentes y referencias.
