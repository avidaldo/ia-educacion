# Ética en Inteligencia Artificial: Guía Esquemática para Docentes

## Principios éticos fundamentales

La Comisión Europea define los siguientes principios éticos fundamentales de la IA:

* **Acción y Supervisión Humanas:** La IA debe actuar como una herramienta para apoyar al ser humano, no para reemplazar su autonomía. Las decisiones finales importantes deben ser tomadas por personas.
* **Robustez Técnica y Seguridad:** Los algoritmos deben ser seguros, fiables y lo suficientemente robustos para no causar daños no intencionados.
* **Privacidad y Gobernanza de los Datos:** Se debe garantizar la privacidad de los datos de los estudiantes y establecer protocolos claros sobre quién tiene acceso a ellos y para qué se utilizan.
* **Transparencia:** Debe ser posible trazar el funcionamiento de un sistema de IA. Los usuarios deben saber que están interactuando con una IA y comprender (en la medida de lo posible) cómo toma sus "decisiones".
* **Diversidad, No Discriminación y Equidad:** Los sistemas de IA deben ser accesibles para todos y no deben introducir o amplificar sesgos que perjudiquen a determinados grupos de estudiantes.
* **Bienestar Social y Medioambiental:** La IA debe usarse para promover un cambio social positivo, incluyendo la educación de calidad.
* **Rendición de Cuentas (Accountability):** Deben existir mecanismos para asegurar la responsabilidad por los sistemas de IA y sus resultados.


## Los sesgos en la IA

El "sesgo" en el contexto de la inteligencia artificial (IA) se refiere a la tendencia sistemática de un sistema de IA a producir resultados que son consistentemente inexactos, injustos o desfavorables para ciertos grupos de personas, o que refuerzan prejuicios y estereotipos existentes. Este sesgo se manifiesta en los resultados, decisiones o predicciones de la IA.

Un modelo de Machine Learning aprende a partir de datos. Si los datos con los que se entrena reflejan prejuicios o desigualdades del mundo real, la IA los aprenderá.

### 2.1. El Error desde la Estadística

En estadística, el error de un modelo predictivo se puede descomponer. Una de las descomposiciones más famosas es la del **Trade-off Sesgo-Varianza**.
El error total de un modelo se puede pensar como:

$$ \text{Error Total} = \text{Sesgo}^2 + \text{Varianza} + \text{Error Irreducible} $$

* **Sesgo (Bias):** Es la diferencia entre la predicción promedio de nuestro modelo y el valor real que intentamos predecir. Un **alto sesgo** significa que el modelo es demasiado simple y no logra capturar la complejidad de los datos (subajuste o *underfitting*). Por ejemplo, asumir que el rendimiento académico depende únicamente del número de horas de estudio, ignorando otros factores.
* **Varianza (Variance):** Es la variabilidad de la predicción del modelo para un punto de dato dado. Una **alta varianza** significa que el modelo es demasiado complejo y se ajusta demasiado al ruido de los datos de entrenamiento (sobreajuste o *overfitting*). Aprende detalles tan específicos de los datos de entrenamiento que no logra generalizar a datos nuevos.
* **Error Irreducible:** Es el ruido inherente a los datos que ningún modelo puede eliminar.

El problema ético surge cuando el **sesgo sistemático** del modelo perjudica a un grupo demográfico particular.

### 2.2. Tipos de Sesgo Relevantes para la Educación

- **Sesgo de muestreo**: Si un conjunto de datos para el reconocimiento facial contiene predominantemente imágenes de personas de piel clara, el modelo resultante puede tener un rendimiento deficiente al reconocer a personas de piel más oscura.

- **Sesgo histórico**: Si los datos de contratación pasados de una empresa muestran una preferencia por candidatos masculinos para ciertos puestos, un algoritmo de IA entrenado con esos datos aprenderá a favorecer a hombres en futuras selecciones.á.

- **Sesgo de medición**: Proviene de errores sistemáticos en la forma en que se miden o recogen los datos. La variable que se mide no representa de forma precisa la característica que se quiere evaluar.

- **Sesgo algorítmico**: Es el sesgo introducido por el propio algoritmo. Puede ser el resultado de simplificaciones o de la optimización de métricas que no capturan la "justicia" (fairness).

- **Sesgo de etiquetado**: Es una manifestación del sesgo de confirmación de los desarrolladores o usuarios. Tienden a crear y confiar en modelos que confirman sus creencias preexistentes, etiquetando los datos o interpretando los resultados de manera que se ajusten a sus prejuicios.

### Ejemplos

#### [El algoritmo de calificaciones en Reino Unido (2020)](https://www.xataka.com/robotica-e-ia/cuando-nota-no-te-pone-profesor-sino-algoritmo-caos-estudiantes-reino-unido)

* **Problema:** Debido a la cancelación de exámenes por la pandemia, el gobierno británico usó un algoritmo para predecir las calificaciones de los estudiantes.
* **El Sesgo:** El modelo daba un peso significativo al rendimiento histórico de la escuela. Esto penalizó sistemáticamente a estudiantes brillantes de escuelas con peores resultados históricos (generalmente en zonas de menores ingresos), mientras que beneficiaba a estudiantes de centros de élite.
* **Consecuencia:** Miles de estudiantes vieron sus calificaciones rebajadas injustamente, lo que les impidió acceder a la universidad deseada. El caso generó protestas masivas y el gobierno tuvo que dar marcha atrás. Fue un claro ejemplo de **sesgo algorítmico y de selección** con un impacto devastador.

#### Sesgos corregidos con sesgos

![](./img/black-ss.png)

> "No puedes tener un sistema que no tenga sesgos, o que sea percibido como no sesgado por todo el mundo" ([Yann LeCun](https://www.youtube.com/watch?v=ZQXHf6gv6s8))


## Consideraciones especiales para docentes

Como docente, no necesitas ser un experto en *machine learning*, pero sí un **usuario crítico y consciente**. Tu rol es fundamental para mitigar los riesgos de la IA en el aula. Al seleccionar herramientas de IA, debes evaluar tres aspectos críticos: la **transparencia** del funcionamiento (evitando "cajas negras" sin explicación), la **ausencia de sesgos** mediante auditorías independientes, y el **cumplimiento de normativas de privacidad** como el RGPD, especialmente tratándose de datos educativos altamente sensibles.

En el uso cotidiano, es esencial **no delegar el juicio crítico** y utilizar la IA como asistente, no como oráculo, supervisando constantemente las recomendaciones para evitar el encasillamiento de estudiantes. El aspecto más importante es **fomentar la alfabetización en IA** entre los estudiantes: enseñándoles cómo funcionan estas herramientas, promoviendo el pensamiento crítico hacia sus resultados, y estableciendo normas éticas claras de uso. Finalmente, debes actuar como **agente de equidad**, observando el impacto diferencial en diversos grupos de estudiantes, informando sobre problemas detectados y garantizando acceso equitativo para evitar que la IA genere nuevas brechas digitales.

La integración ética de la IA es un proceso continuo de aprendizaje y adaptación. Tu papel como docente es insustituible para guiar a los estudiantes en este nuevo paradigma, asegurando que la tecnología sirva para potenciar el aprendizaje humano en un marco de justicia y equidad.