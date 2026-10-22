---
title: Vibe coding
description: Crear aplicaciones a base de prompts, qué herramientas hay para cada nivel, un método que funciona y dónde está el límite entre un prototipo y algo que puede usar el alumnado.
reviewed: 2026-10-22
review_every: 3
---

## Qué es

Andrej Karpathy, que formó parte del equipo fundador de OpenAI, acuñó el término en febrero de 2025 para describir una forma de programar en la que «te entregas a las sensaciones» y te «olvidas de que el código existe»: pides cambios en lenguaje natural, aceptas todo lo que propone la IA sin leerlo y, cuando algo falla, le pegas el mensaje de error hasta que funciona.[^karpathy] Él mismo lo presentaba como algo para «proyectos de fin de semana de usar y tirar». El término se extendió tanto que el diccionario Collins lo eligió palabra del año 2025.[^collins]

Conviene distinguirlo de programar con ayuda de la IA. Simon Willison lo explica así: si revisas el código que escribe el modelo, lo pruebas a fondo y sabrías explicarle a otra persona cómo funciona, eso ya no es *vibe coding*; es desarrollo de software, y que te haya ayudado un modelo es lo de menos.[^willison] La distinción importa porque el *vibe coding* es perfecto para un prototipo o una herramienta personal y arriesgado para cualquier cosa que maneje datos o de la que dependan otras personas.

Respecto a [Webs educativas](../webs-educativas/index.md), la diferencia es de tamaño: allí se trata de una página en un único fichero; aquí, de una **aplicación**, con varias pantallas, datos que se guardan, usuarios o un servidor.

## Tres niveles de herramientas

| Nivel | Ejemplos | Qué obtienes | Para quién |
| --- | --- | --- | --- |
| Chat con vista previa | Canvas en Gemini y ChatGPT, Artifacts en Claude, Sites en ChatGPT | Una página o una aplicación ligera dentro del *chatbot* | Cualquiera; es el punto de partida de [Webs educativas](../webs-educativas/index.md) |
| Generadores de aplicaciones | [Google AI Studio](https://aistudio.google.com) (modo Build), [Lovable](https://lovable.dev) | Una aplicación completa (interfaz, servidor, base de datos, inicio de sesión) publicada en una dirección propia | Sin instalar nada; planes gratuitos con límites |
| Agentes de programación | Claude Code, Codex, GitHub Copilot, Gemini CLI | Un agente que trabaja sobre los ficheros de un proyecto: los lee, los modifica, ejecuta el programa y las pruebas, y corrige lo que falla | Quien ya programa o está aprendiendo, como en los ciclos de informática |

Algunos datos útiles para el último nivel: Claude Code está incluido en todos los planes de pago de Claude, Codex en todos los de ChatGPT (también en el gratuito, con límites) y GitHub ofrece Copilot Pro gratis a los docentes verificados en GitHub Education.[^planes]

## Un método que funciona

1. **Primero, la especificación.** Antes de pedir código, describe qué hace la aplicación, quién la usa, en qué dispositivos y qué datos guarda (idealmente, ninguno). Pídele al *chatbot* que te haga preguntas hasta tenerlo claro, como en [*metaprompting*](../prompts/index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt), y que te proponga un plan antes de escribir nada.
2. **Lo mínimo que funcione.** Una primera versión con una sola función. Después, un cambio cada vez.
3. **Pruébala tú**, como lo haría el alumnado: con el móvil, con respuestas equivocadas, pulsando donde no toca.
4. **Guarda versiones.** Todas estas herramientas tienen historial o se conectan a GitHub: cuando un cambio lo estropea todo, se vuelve atrás en lugar de pedir arreglos encima de arreglos.
5. **Describe los fallos con precisión**: qué hiciste, qué esperabas y qué pasó, mejor que pegar solo el error.
6. **Pide explicaciones de las partes delicadas**: dónde se guardan los datos, qué se envía fuera, qué pasa si alguien escribe algo inesperado.

Un ejemplo de especificación:

```text
Quiero una aplicación web para que mi alumnado de 3.º de ESO practique
la formulación inorgánica. Antes de escribir código, hazme las preguntas
que necesites y proponme un plan de pantallas y funciones.

Requisitos:
- Sin registro ni inicio de sesión. No recoge ni envía ningún dato.
- El progreso se guarda solo en el navegador del alumno.
- Tres niveles de dificultad; en cada pregunta, una pista y la corrección explicada.
- Funciona en el móvil y es manejable con el teclado.
- Sin servicios externos: nada de analíticas, fuentes ni bibliotecas de otras webs.
```

## Dónde está el límite

Lo que se gana en rapidez se pierde en control cuando nadie entiende el código. Estos son los riesgos concretos:

Seguridad de los datos
: En 2025 se registró una vulnerabilidad en aplicaciones generadas con Lovable: unas reglas de acceso insuficientes en la base de datos permitían a cualquiera leer o modificar sus tablas sin identificarse. Lovable la disputó argumentando que la seguridad de cada aplicación es responsabilidad de quien la crea.[^lovable] Esa es justamente la cuestión: si una aplicación guarda datos y tiene usuarios, alguien tiene que entender cómo está protegida.

Paquetes inventados
: Los modelos recomiendan a veces bibliotecas que no existen. Un estudio presentado en USENIX Security 2025 analizó 576.000 fragmentos de código de 16 modelos: al menos un 5,2 % de los paquetes sugeridos por los modelos comerciales, y un 21,7 % en los abiertos, eran inventados.[^paquetes] Un atacante puede registrar esos nombres con código malicioso, y quien no revisa lo que instala se lo descarga.

Claves y costes
: Una aplicación que usa un modelo de lenguaje necesita una clave de acceso a su API, que no debe quedar a la vista en el código del navegador, y cada uso tiene un coste. Las plataformas actuales suelen guardar la clave en el servidor, pero el consumo de quien use la aplicación corre a tu cuenta.

Condiciones de uso
: Las de la API de Gemini, que usan las aplicaciones de Google AI Studio, exigen 18 años, prohíben usarla en aplicaciones dirigidas a menores de 18 años o que probablemente usen menores, y obligan a usar los servicios de pago para ofrecer una aplicación a usuarios del Espacio Económico Europeo.[^gemini-api] Una aplicación con IA dentro hecha en AI Studio no puede darse, por tanto, a alumnado menor de edad. Una aplicación sin llamadas a ningún modelo, como la del ejemplo, es otra cosa: es código como cualquier otro.

Mantenimiento
: Si no entiendes el código, cada cambio es una lotería. Y las herramientas cambian: lo que hoy se hace en una plataforma puede no existir el curso que viene.

| Adelante | Mejor no, salvo que alguien revise el código |
| --- | --- |
| Prototipos y demostraciones para clase | Aplicaciones con registro de usuarios |
| Herramientas personales (un generador de rúbricas, un conversor de formatos) | Aplicaciones que guardan datos del alumnado |
| Aplicaciones que no guardan nada fuera del navegador | Aplicaciones que usan APIs de pago con el dinero de alguien |
| Material que se puede tirar y rehacer | Herramientas de las que van a depender otros docentes |

Para todo lo que maneje datos del alumnado ya existen herramientas del centro, como el aula virtual, con su protección de datos resuelta.

## En los ciclos de informática

Para quien aprende a programar, el riesgo no es solo la calidad del código sino **dejar de aprender**. En un ensayo controlado publicado por Anthropic en enero de 2026, 52 programadores aprendieron una biblioteca de Python nueva: quienes usaron un asistente de IA sacaron un 17 % menos en un cuestionario sobre los conceptos que acababan de usar, y la mayor diferencia estuvo en las preguntas de depuración. No fueron significativamente más rápidos. Pero no todos los que usaron IA aprendieron menos: los que le pedían explicaciones y le hacían preguntas conceptuales obtuvieron mejores resultados que los que solo le pedían código.[^anthropic-aprendizaje] Es un único estudio, hecho por una empresa del sector y sobre una tarea concreta, pero apunta en una dirección clara.

Algunas ideas para el aula:

- **Usar el agente para entender, no solo para producir**: pedirle que explique, que proponga alternativas y que señale errores en lugar de corregirlos.
- **Predecir antes de ejecutar**: qué hará este código y por qué.
- **Depurar sin ayuda una parte del trabajo**, que es justo lo que más se resiente.
- **Defender el código** oralmente o modificándolo en directo. La regla de Willison sirve como criterio de evaluación: no se entrega código que no sepas explicar.[^willison]

[^karpathy]: El mensaje original de Karpathy, de febrero de 2025, está citado completo en el artículo de Simon Willison de la nota siguiente.
[^collins]: Collins, [*Word of the Year 2025*](https://www.collinsdictionary.com/woty).
[^willison]: Simon Willison, [*Not all AI-assisted programming is vibe coding (but vibe coding rocks)*](https://simonwillison.net/2025/Mar/19/vibe-coding/), 19 de marzo de 2025.
[^planes]: Según las páginas de [precios de Claude](https://claude.com/pricing), [precios de Codex](https://developers.openai.com/codex/pricing) y [GitHub Copilot para docentes](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers), consultadas el 22 de octubre de 2026.
[^lovable]: [CVE-2025-48757](https://www.cve.org/CVERecord?id=CVE-2025-48757), publicada el 30 de mayo de 2025, con la nota de que el proveedor la disputa.
[^paquetes]: Spracklen et al., [*We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*](https://arxiv.org/abs/2406.10279), USENIX Security 2025.
[^gemini-api]: Google, [*Gemini API Additional Terms of Service*](https://ai.google.dev/gemini-api/terms), apartados *Age Requirements* y *Use Restrictions*, consultados el 22 de octubre de 2026.
[^anthropic-aprendizaje]: Anthropic, [*How AI assistance impacts the formation of coding skills*](https://www.anthropic.com/research/AI-assistance-coding-skills), 29 de enero de 2026.
