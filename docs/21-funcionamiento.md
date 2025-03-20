# Funcionamiento
## ¿Cómo funcionan?

- De manera estadística. Aprenden a predecir la siguiente palabra basándose en las anteriores.
- No parte de cero, predice la siguiente palabra basándose en el prompt que le damos, en las anteriores (memoria) y en el contexto (configuración).
- Están entrenados con datos existentes, pero **no tienen un "conocimiento funcional" de las reglas** (por ejemplo al crear imágenes, no saben cómo funcionan las manecillas de un reloj).


### Razonadores

Los modelos razonadores dan en general un mejor resultado a costa de mayor tiempo. Integran en su funcionamiento la estrategia de cadena de pensamiento (*Chain of Thought* - CoT) habiendo sido entrenados con ejemplos de razonamiento paso a paso.
Han permitido superar nuevos niveles en *benchmarks* matemáticos y lógicos.