# Prompt Engineering

## Introducción

- ¿Qué es un prompt y por qué es importante?
    - Un prompt es una instrucción que se le da a un modelo de lenguaje para que genere una respuesta (la pregunta que le hacemos al chatbot).
    - Es importante porque determina la calidad de la respuesta.
    - Un buen prompt es aquel que permite al modelo entender bien lo que se le pide y dar una respuesta adecuada.
    - Un mal prompt puede llevar a respuestas incorrectas o incoherentes.

---

## Estrategias básicas

### Lo más básico:
- Usa varios modelos (distintas aplicaciones) y prueba.
- Siempre itera: da correcciones y matices a las respuestas.
    - Sé crítico e inquisitivo ("¿Estás seguro?")
- Pregunta al propio modelo cómo mejorar el prompt / Ofrece al modelo clarificar dudas.
- Estructura: "dado esto, siguiendo estas reglas y estas restricciones, dame esto"

---

## Técnicas fundamentales de prompting

### 1. Especificidad y claridad

Los LLMs son altamente sensibles a la formulación exacta de los prompts.[^maxim2025]

**✅ Buena práctica**:
```
Analiza el impacto económico de la Revolución Industrial en Inglaterra 
entre 1760-1840. Estructura la respuesta en: causas, desarrollo, 
consecuencias económicas y sociales. Usa 500 palabras máximo.
```

**❌ Evitar**:
```
Háblame de la Revolución Industrial
```

### 2. Definición de contexto y perspectiva

Proporcionar contexto relevante y definir una perspectiva o rol mejora significativamente la calidad de las respuestas.[^orq2025]

**Ejemplo**:
```
Eres un profesor de historia especializado en enseñanza secundaria. 
Explica la fotosíntesis a estudiantes de 14 años usando analogías 
cotidianas. Evita jerga técnica.
```

### 3. Especificación del formato de salida

Definir explícitamente la estructura deseada asegura consistencia y usabilidad.[^maxim2025]

**Ejemplo**:
```
Genera un resumen del siguiente texto en formato de lista con:
- 3 puntos clave
- 2 conclusiones principales
- 1 recomendación práctica
```

### 4. Uso de delimitadores

Los delimitadores (comillas triples, XML, Markdown) ayudan al modelo a distinguir diferentes partes del prompt.[^openai2025]

**Ejemplo**:
```
Traduce el siguiente texto al inglés:
"""
[Texto en español aquí]
"""

Después resume la traducción en 2 frases.
```

---

## Técnicas avanzadas de razonamiento

### Chain-of-Thought (CoT) Prompting

Introducido en 2022, CoT anima a los LLMs a descomponer problemas complejos en pasos lógicos intermedios.[^getmaxim2025][^adaline2025]

**Modalidades**:

#### Few-Shot CoT (con ejemplos)
```
P: Si tengo 15 manzanas y doy 4 a mi hermano, ¿cuántas me quedan?
Razonamiento: Empiezo con 15. Si doy 4, resto: 15 - 4 = 11
R: Me quedan 11 manzanas.

P: Si un tren viaja a 60 km/h durante 2.5 horas, ¿qué distancia recorre?
Razonamiento:
```

#### Zero-Shot CoT
```
Resuelve el siguiente problema pensando paso a paso:

Si una clase tiene 24 estudiantes y se dividen en grupos de 4, 
¿cuántos grupos se forman?
```

**Beneficios demostrados**:
- Mejora significativa en razonamiento matemático y lógico
- Reduce errores en tareas de múltiples pasos
- Aumenta la transparencia del proceso de razonamiento

### Tree-of-Thought (ToT)

Generaliza CoT permitiendo al modelo generar múltiples caminos de razonamiento en paralelo, usando algoritmos de búsqueda en árbol.[^getmaxim2025]

**Aplicación**:
- Problemas con múltiples soluciones válidas
- Planificación estratégica
- Análisis de escenarios alternativos

### Self-Consistency

Genera múltiples caminos de razonamiento y selecciona la respuesta más consistente mediante votación por mayoría, reduciendo errores.[^getmaxim2025][^adaline2025]

### ReAct (Reasoning + Acting)

Combina trazas de razonamiento con acciones específicas de tarea, permitiendo al modelo adaptar sus planes basándose en observaciones.[^adaline2025]

**Ejemplo**:
```
Pensamiento: Necesito buscar información sobre el PIB de España en 2024
Acción: búsqueda["PIB España 2024"]
Observación: [resultados de búsqueda]
Pensamiento: Los datos muestran...
```

---

## Prompting para modelos razonadores (GPT-5.x, Gemini 3, Claude 4.5)

Los modelos más recientes (diciembre 2025) como **GPT-5.2**, **Gemini 3 Deep Think** y **Claude Opus 4.5** integran razonamiento interno automático, por lo que requieren estrategias diferentes.[^openai2025][^google2025]

### Mejores prácticas para razonadores

| ❌ Evitar | ✅ Hacer |
|-----------|----------|
| "Piensa paso a paso" | Prompts directos y claros |
| Demasiados ejemplos | Zero-shot primero, few-shot solo si necesario |
| Over-engineering del prompt | Solo contexto esencial |
| Especificar rol demasiado detallado | Especificar formato de salida |
| Ejemplos de CoT explícitos | Dejar que el modelo razone internamente |

**Guía específica**:
- **Sé directo**: prompts simples y claros funcionan mejor que instrucciones elaboradas
- **Zero-shot primero**: intenta sin ejemplos, añádelos solo para formatos específicos
- **No pidas CoT manualmente**: ya lo hacen internamente; pedirlo puede degradar rendimiento
- **Usa delimitadores**: estructura inputs complejos con Markdown o XML
- **Define formato explícitamente**: especifica si quieres JSON, lista, tabla, etc.

> **Nota académica**: En modelos anteriores, ejemplos explícitos de cadenas de pensamiento inducían al modelo a "pensar en voz alta". En GPT-5.x, Gemini 3 y Claude 4.5, el razonamiento se ejecuta internamente y está optimizado; incluir "piensa paso a paso" puede obstaculizar su rendimiento, pues están diseñados para prompts directos.[^openai2025]

---

## Técnicas emergentes (2025)

### Recursive Self-Improvement Prompting (RSIP)

El modelo evalúa críticamente y mejora iterativamente sus propias respuestas.[^reddit2025]

**Ejemplo**:
```
Genera una explicación de la fotosíntesis para niños de 10 años.

Ahora revisa tu respuesta y mejórala considerando:
1. ¿Es el vocabulario apropiado para la edad?
2. ¿Hay analogías más efectivas?
3. ¿Falta algún concepto clave?
```

### Context-Aware Decomposition (CAD)

Descompone tareas complejas manteniendo consciencia del contexto global.[^reddit2025]

### Mega-Prompts

Instrucciones detalladas con contexto enriquecido para tareas específicas complejas.[^godofprompt2025]

---

## Estrategias de validación

### *Contrarian Prompting*

Solicita a otro modelo (o chat temporal sin memoria) que haga una valoración crítica de las respuestas.

> "Haz un análisis exhaustivo señalando todo aquello que pueda ser cuestionable, incompleto o mejorable en el siguiente texto. Sé exhaustivo y crítico: [texto]."

**Ventaja**: Evita el sesgo de "dar siempre la razón" o "no cuestionar lo previo".

### Multi-Agent Orchestration

Coordinar prompts entre múltiples agentes especializados para tareas complejas.[^getmaxim2025]

---

## Documentación oficial y recursos académicos

### Guías oficiales
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Google AI Prompting Guide](https://ai.google.dev/gemini-api/docs/prompting-intro)

### Investigación académica clave

**The Prompt Report** (Febrero 2025)[^aakashg2025]  
Revisión sistemática catalogando 58 técnicas de prompting para texto y 40 para otras modalidades.

**SOPL: Sequential Optimal Learning** (EMNLP 2025)[^emnlp2025]  
Aproximación de aprendizaje óptimo secuencial a la ingeniería automática de prompts.

**Prompt Engineering and LLM Productivity** (arXiv 2025)[^arxiv2025]  
Investiga cómo la estructura y claridad de prompts impacta la efectividad y productividad.

---

## El futuro del prompt engineering

En 2025, el campo evoluciona hacia:[^renierbotha2025][^getmaxim2025]

1. **Context Engineering**: Del prompt al contexto completo (tokens, información, memoria)
2. **Automated Optimization**: LLMs optimizando prompts para otros LLMs
3. **Prompt Libraries**: Bibliotecas versionadas de prompts como código
4. **Multimodal Prompting**: Integración de texto, imagen, audio, vídeo

---

[^maxim2025]: Maxim AI. "Prompt Engineering Trends 2025." [getmaxim.ai](https://getmaxim.ai)
[^orq2025]: Orq.ai. "Best Practices for Prompt Engineering." [orq.ai](https://orq.ai)
[^openai2025]: OpenAI. "Reasoning Guide - GPT-5." [platform.openai.com/docs/guides/reasoning](https://platform.openai.com/docs/guides/reasoning)
[^google2025]: Google AI. "Gemini 3 Release Notes." [blog.google](https://blog.google)
[^getmaxim2025]: Maxim AI. "Advanced Prompting Techniques: CoT, ToT, Self-Consistency." [getmaxim.ai](https://getmaxim.ai)
[^adaline2025]: Adaline AI. "Reasoning Techniques for LLMs." [adaline.ai](https://adaline.ai)
[^godofprompt2025]: God of Prompt. "Prompt Engineering Trends 2025." [godofprompt.ai](https://godofprompt.ai)
[^reddit2025]: Reddit AI. "RSIP and CAD Techniques Discussion." [reddit.com](https://reddit.com)
[^aakashg2025]: Aakash Gupta. "The Prompt Report - A Systematic Survey." [aakashg.com](https://aakashg.com)
[^emnlp2025]: EMNLP. "Accepted Papers 2025." [emnlp.org](https://emnlp.org)
[^arxiv2025]: arXiv. "Prompt Engineering and the Effectiveness of LLMs." [arxiv.org](https://arxiv.org)
[^renierbotha2025]: Renier Botha. "The Future of Prompt Engineering." [renierbotha.com](https://renierbotha.com)
