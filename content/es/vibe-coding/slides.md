---
derived_from:
  es/vibe-coding/index.md: "b02ed9a9456be84a9292be0861da9fd0b18571e0"
---

<!-- .slide: id="olvidar-codigo" class="statement" -->
## *Vibe coding*: pedir, aceptarlo todo y olvidarse de que el código existe

Karpathy, febrero de 2025: «para proyectos de fin de semana de usar y tirar».

---

<!-- .slide: id="vibe-o-programar" class="comparison" -->
## No todo lo que se programa con IA es *vibe coding*

### *Vibe coding*
Aceptas lo que propone sin leerlo y le pegas los errores hasta que funciona.

### Programar con IA
Revisas el código, lo pruebas y sabrías explicar cómo funciona.

Notas:
La distinción es de Simon Willison. Importa porque el *vibe coding* es perfecto para un prototipo y arriesgado para cualquier cosa que maneje datos o de la que dependan otras personas.

---

<!-- .slide: id="niveles" class="table dense" -->
## Tres niveles de herramientas

| Nivel | Ejemplos | Qué obtienes |
| --- | --- | --- |
| Chat con vista previa | Canvas, Artifacts, Sites | Una página o una aplicación ligera |
| Generadores de aplicaciones | Google AI Studio, Lovable | Una aplicación completa, publicada |
| Agentes de programación | Claude Code, Codex, Copilot | Trabajo sobre los ficheros de un proyecto |

Notas:
Claude Code está incluido en todos los planes de pago de Claude; Codex, en todos los de ChatGPT, también el gratuito con límites. GitHub ofrece Copilot Pro gratis a los docentes verificados en GitHub Education.

---

<!-- .slide: id="metodo" class="fragments" -->
## Un método: especificar, empezar pequeño, probar

- Primero la especificación, y un plan antes del código.
- Lo mínimo que funcione; después, un cambio cada vez.
- Pruébala como lo haría el alumnado.
- Guarda versiones para poder volver atrás.
- Describe los fallos: qué hiciste, qué esperabas, qué pasó.
- Pide que te explique las partes delicadas.

---

<!-- .slide: id="especificacion" class="prompt dense" -->
## Una especificación antes del código

```text
Quiero una aplicación web para que mi alumnado de 3.º de ESO practique
la formulación inorgánica. Antes de escribir código, hazme las preguntas
que necesites y propónme un plan de pantallas y funciones.
Requisitos: sin registro; no recoge ni envía datos; el progreso se guarda
solo en el navegador; tres niveles, con pista y corrección explicada;
usable en el móvil y con el teclado; sin servicios externos.
```

Notas:
La versión completa está en la página.

---

<!-- .slide: id="demo-app" class="demo" -->
## De la especificación a una aplicación que funciona

Preguntas antes del código y un cambio cada vez.

Notas:
**Demo (10 min)**. Google AI Studio (modo Build) o Lovable, con una cuenta de pruebas.

1. Pegar la especificación de la página y responder a las preguntas.
2. Revisar el plan antes de que escriba código.
3. Probar la primera versión con respuestas equivocadas y en el móvil.
4. Pedir un cambio concreto y volver a la versión anterior desde el historial.

**Resultado esperado:** una aplicación que funciona sin registro ni datos fuera del navegador.
**Si falla:** enseñar el historial de versiones y la vuelta atrás, que es lo que más se usa.
**Mensaje clave:** la especificación y las versiones importan más que el *prompt* perfecto.

---

<!-- .slide: id="limite" class="statement" -->
## Lo que se gana en rapidez se pierde en control si nadie entiende el código

---

<!-- .slide: id="riesgos" class="cards" -->
## Cuatro riesgos concretos

### Seguridad
Bases de datos abiertas a cualquiera, como en aplicaciones de Lovable en 2025.

### Paquetes inventados
Al menos un 5 % de las bibliotecas sugeridas no existen.

### Claves y costes
El consumo de quien use la aplicación corre a tu cuenta.

### Mantenimiento
Si no entiendes el código, cada cambio es una lotería.

Notas:
Los paquetes inventados, según un estudio de USENIX Security 2025 sobre 576.000 fragmentos de código de 16 modelos: un 5,2 % en los comerciales y un 21,7 % en los abiertos. Un atacante puede registrar esos nombres con código malicioso.

---

<!-- .slide: id="gemini-menores" class="statement" -->
## Una aplicación con Gemini dentro no puede darse a menores de edad

Lo prohíben las condiciones de su API; una aplicación sin llamadas a ningún modelo es otra cosa.

Notas:
Las condiciones exigen además los servicios de pago para ofrecer la aplicación a usuarios del Espacio Económico Europeo.

---

<!-- .slide: id="adelante" class="table" -->
## Dónde está el límite

| Adelante | Mejor no, sin revisión del código |
| --- | --- |
| Prototipos y demostraciones | Registro de usuarios |
| Herramientas personales | Datos del alumnado |
| Nada guardado fuera del navegador | APIs de pago |
| Material que se puede rehacer | Herramientas de las que dependen otros |

Notas:
Para lo que maneje datos del alumnado ya existen las herramientas del centro, como el aula virtual.

---

<!-- .slide: id="ciclos" class="section" -->
## En los ciclos de informática

---

<!-- .slide: id="estudio" class="big-number" -->
## Programar con IA puede frenar el aprendizaje

**17 %** menos en un cuestionario sobre los conceptos que acababan de usar.

Anthropic, enero de 2026: ensayo controlado con 52 programadores.

Notas:
Aprendían una biblioteca de Python nueva. La mayor diferencia, en las preguntas de depuración, y no fueron significativamente más rápidos. Es un único estudio, de una empresa del sector y sobre una tarea concreta.

---

<!-- .slide: id="explicaciones" class="statement" -->
## Quien pedía explicaciones obtuvo mejores resultados que quien solo pedía código

---

<!-- .slide: id="aula" -->
## En el aula

- Usar el agente para entender: explicaciones, alternativas, errores señalados.
- Predecir antes de ejecutar.
- Depurar sin ayuda una parte del trabajo.
- Defender el código: no se entrega lo que no sabes explicar.

---

<!-- .slide: id="practica-especificacion" class="practice" -->
## Tu especificación

1. Piensa una aplicación para tu materia que no guarde datos.
2. Escribe su especificación con el modelo del ejemplo.
3. Pide al *chatbot* preguntas y un plan, todavía sin código.
4. Revisa el plan: qué guarda, qué envía fuera.

**15 minutos.** Producto: una especificación lista para construir.

Notas:
Por parejas. Al final, dos parejas leen su especificación y el grupo busca qué datos guardaría la aplicación sin que lo hayan pedido.
