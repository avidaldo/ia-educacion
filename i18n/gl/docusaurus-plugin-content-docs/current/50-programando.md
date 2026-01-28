# Creando aplicacións sen saber programar

## Vibe Coding

**Vibe coding** é un termo acuñado por [Andrej Karpathy](https://twitter.com/karpathy) en febreiro de 2025 para describir unha nova forma de programar onde a IA xera o código e o humano o guía mediante prompts en linguaxe natural.

> "The hottest new programming language is English" — Andrej Karpathy

### Como funciona?

1. **Describes** o que queres en linguaxe natural
2. A IA **xera** o código
3. **Executas** e observas o resultado
4. **Iteras** con correccións ata conseguir o desexado

### Herramientas para Vibe Coding

| Ferramenta | Descrición |
|------------|------------|
| **Claude Artifacts** | Crea aplicacións web e as aloxa automaticamente |
| **ChatGPT Canvas** | Espazo de traballo con edición e execución de código |
| **Gemini** | Xera código con posibilidade de exportar |
| **Cursor / GitHub Copilot** | Editores de código con IA integrada |

### Vantaxes
- ✅ Non necesitas saber programar para crear aplicacións simples
- ✅ Prototipado moi rápido
- ✅ Ideal para ferramentas educativas pequenas

### Limitacións
- ⚠️ O código pode ter erros ou vulnerabilidades
- ⚠️ Difícil de manter se non entendes o código
- ⚠️ Mellor para prototipos que para produción

---

## De Vibe Coding a axentes (automatización con criterios)

O vibe coding adoita describirse como “iterar por sensación” ata que algo funciona. Iso é útil para prototipos, pero en canto queres **fiabilidade**, convén pasar de “chat” a un **fluxo tipo axente**.

### Que é un axente (na práctica)

Un axente non é “unha IA máis lista”, senón un sistema que:

- persegue un **obxectivo** (con criterios de aceptación),
- mantén **estado** (que se intentou, que fallou, que queda),
- pode usar **ferramentas** (tests, linters, busca, conversores de formato, etc.),
- executa un bucle controlado e **detense** cando cumpre o obxectivo.

Se queres ver modelos orientados á docencia, aquí tes exemplos listos para reutilizar:

- [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)
- [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### Patróns que funcionan (e como pedilos)

**1) Planner/Executor (planificar → executar → validar)**

- Pide un plan curto (3–7 pasos), logo execución paso a paso con validación.
- Define unha “Definition of Done”: que probas pasar, que arquivos cambiar, que formato entregar.

**2) Critique loop (borrador → crítica → versión final)**

- Útil para: rúbricas, actividades, bancos de preguntas, textos explicativos.
- Limita roldas (1–2) e define criterios (claridade, privacidade, verificabilidade).

**3) Tool-use / ReAct (Acción → Observación → Axuste)**

- Útil para: investigación con fontes, verificación, extracción e re-formateo.
- Pide “accións e observacións” (que fixo e que obtivo). Evita pedir “pensamento paso a paso”.

**4) Multi‑axente (roles: deseñar → avaliar → editar)**

- Útil cando queres separar creatividade, revisión crítica e edición final.
- Define roles e orde estricta para reducir o sesgo de auto‑confirmación.

### Prompts máis útiles ao programar con IA

Cando uses Copilot/Cursor/Canvas/Artifacts, estes requisitos adoitan mellorar moito a calidade:

- Entradas/saídas como contrato: “devólveme só o código”, “encabezados fixos”, “táboa con columnas X”.
- Criterios de parada: “para cando pase X / cando non haxa warnings / cando compile”.
- Restriccións: “non engadir dependencias”, “non inventar datos”, “non usar datos persoais”.

Para a base de prompting (formato, delimitadores, verificación), ver: [/docs/prompt](/docs/prompt)

### Fontes (fiables) para o concepto de axente

- ReAct (Reasoning + Acting): https://arxiv.org/abs/2210.03629
- Reflexion (axentes con feedback/memoria): https://arxiv.org/abs/2303.11366
- Self-Refine (mellora iterativa con auto-feedback): https://arxiv.org/abs/2303.17651
- AutoGen (multi‑axente): https://arxiv.org/abs/2308.08155
- MetaGPT (multi‑axente): https://arxiv.org/abs/2308.00352

---

## Espazos de traballo en chatbots

### Claude Artifacts

[Claude Artifacts](https://claude.ai/artifacts) permite crear e publicar aplicacións web directamente desde o chat.

**Guía rápida**: 
1. Visita [Claude.ai](https://claude.ai/) e accede coa túa conta
2. Describe a aplicación que necesitas
3. Claude créaa automaticamente e dáche unha ligazón para compartir
4. O código alóxase nos servidores de Anthropic

:::note[Artigo interesante]
[Como crear mini-aplicacións educativas con Claude](https://educacion.bilateria.org/como-crear-aplicaciones-educativas-con-claude)
:::

**Exemplos de uso educativo**:
- Calculadoras interactivas
- Quizzes e xogos educativos
- Visualizacións de conceptos
- Simuladores simples

### ChatGPT Canvas

[Canvas](https://openai.com/index/introducing-canvas/) é o espazo de traballo de ChatGPT para proxectos máis elaborados.

**Características**:
- Panel de chat + editor integrado
- **Edición inline**: selecciona código e pide cambios específicos
- **Execución de Python**: executa código directamente
- **Control de versións**: desfacer cambios, restaurar versións
- **Ferramentas de código**: depurar, comentar, refactorizar, traducir a outras linguaxes

**Como activalo**:
- Automaticamente cando detecta código longo
- Manualmente escribindo "usa canvas" ou "abre un canvas"

### Gemini

Gemini tamén pode xerar código e aplicacións, aínda que con menos capacidade de hosting directo. Porén, permite:
- Xerar código en múltiples linguaxes
- Colaborar na edición
- Exportar para usar noutros sitios

---

## Integrar aplicacións en Moodle

Para inserir unha aplicación (coma un Claude Artifact) en Moodle:

### Usando a URL da aplicación

Podes usar a URL (a ligazón de Claude Artifacts) para inserila en Moodle directamente cun recurso de tipo "URL".

### Usando un iframe

1. Obtén a ligazón da túa aplicación
2. No teu curso de Moodle, activa o modo de edición
3. Engade un recurso ou actividade do tipo "Páxina" ou "Etiqueta"
4. Fai clic na icona de código HTML `<>`
5. Pega un código iframe:
   ```html
   <iframe src="https://a-tua-ligazon-de-aplicacion" width="100%" height="600px" frameborder="0"></iframe>
   ```
6. Garda os cambios

### Creación de páxinas HTML

Calquera chatbot pode crear páxinas HTML facilmente a golpe de prompt. Despois podes:
- Descargar a páxina e pegar o código nun recurso "Páxina" de Moodle
- Usar un recurso "Etiqueta" para que se sexa directamente na páxina do curso

---

## Recursos relacionados

- [Tests para Moodle](./51-tests-moodle.mdx) - Xeración de preguntas importables
- [Asistentes personalizados](./31-ejemplos/09-asistente-personalizado.mdx) - Crear GPTs e Gems
