# Ética y IA

### 2.1. Muestreo y Representatividad
- **Problema**: Datos no representativos generan modelos sesgados.  
  - *Ejemplo*: Sistema COMPAS (EE.UU.) para predecir reincidencia, entrenado con datos policiales sobre-representando minorías étnicas, perpetuando discriminación ([ProPublica, 2016](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)).
- **Solución**: Técnicas de remuestreo estratificado y verificación de distribución de datos.

### 2.2. Sesgo Histórico
- **Problema**: Datos históricos reflejan prejuicios sociales.  
  - *Ejemplo*: IA de contratación de Amazon (2018) penalizaba CVs con la palabra "mujer", al entrenarse con datos de una industria dominada por hombres.

### 2.3. Transparencia Metodológica
- Necesidad de publicar protocolos de recolección y preprocesamiento de datos para permitir auditorías externas.

### 3.1. Explicabilidad vs. Interpretabilidad
- **Explicabilidad**: Capacidad de describir mecanismos internos (ej.: árboles de decisión).  
- **Interpretabilidad**: Entendimiento humano de las salidas (ej.: SHAP values).  
  - *Ejemplo crítico*: Modelos de deep learning en diagnóstico médico (e.g., IBM Watson Health) con baja interpretabilidad, llevando a errores no detectables ([The Lancet, 2021](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(21)00048-4/fulltext)).

### 3.2. Sesgos de Evaluación
- **Problema**: Métricas inadecuadas (ej.: precisión global vs. equidad entre grupos).  
  - *Ejemplo*: Reconocimiento facial de Amazon Rekognition: 99% de precisión en hombres blancos vs. 65% en mujeres negras ([MIT Study, 2018](https://news.mit.edu/2018/study-finds-gender-skin-type-bias-artificial-intelligence-systems-0212)).

### 3.3. Gobernanza Algorítmica
- Implementación de mecanismos de "circuito breaker" para detener sistemas automáticos ante sesgos detectados (ej.: sistemas de crédito en UE).

### 4.1. Ilusión de Objetividad
- **Efecto**: Usuarios sobreestiman la neutralidad de las IA.  
  - *Ejemplo*: Estudiantes usando chatbots educativos (e.g., ChatGPT) como fuente primaria sin verificar sesgos históricos o culturales.

### 4.2. Sesgos de Automatización
- **Problema**: Delegación acrítica en sistemas opacos.  
  - *Ejemplo*: Jueces en Wisconsin (EE.UU.) usando puntuaciones de COMPAS sin entender su base estadística ([Wisconsin Supreme Court, 2016](https://www.wicourts.gov/sc/opinion/DisplayDocument.pdf?content=pdf&seqNo=168440)).

### 4.3. Diseño Centrado en el Usuario
- Necesidad de interfaces que muestren límites de confianza y márgenes de error (ej.: herramientas educativas como Khan Academy).

