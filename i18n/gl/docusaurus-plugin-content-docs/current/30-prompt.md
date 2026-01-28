# Deseño de Prompts

## Definición e Propósito

Un prompt eficaz funciona como unha **especificación técnica** precisa.

No contexto educativo, o deseño de prompts debe orientarse á produción de **artefactos funcionais e verificables**, tales como:

- Fichas de actividade con desgloses temporais detallados.
- Bancos de preguntas en formatos estándar de importación (ex. GIFT).
- Rúbricas de avaliación con indicadores observables.
- Adaptacións curriculares que manteñan a aliñamento cos obxectivos de aprendizaxe.

## Estrutura de Referencia (Exemplo)

A seguinte estrutura serve como punto de partida para deseñar prompts robustos, facilitando a interacción con modelos de linguaxe avanzados.

```text
Es un consultor experto en deseño curricular e normativa educativa.

Tarefa:
- Quero crear: [actividade / banco de preguntas / rúbrica / guía de estudo]

Contexto:
- Materia/tema:
- Nível (curso ou FP):
- Duración:
- Recursos dispoñibles:
- Perfil do grupo (xeral, sen datos persoais):

Antes de responder:
- Faime 3–5 preguntas de aclaración (só as necesarias).
- Se falta información crítica, propón ata 3 supostos explícitos e continúa.

Saída:
- Formato: Markdown
- Encabezados fixos: [lista de encabezados]
- Límites: [p. ex. máx. 1 páxina / máx. 12 ítems / táboa]

Restriccións:
- Non uses datos persoais do alumnado.
- Non inventes normativa, datos do centro nin cifras. Se non o sabes, indícao.

Criterios de calidade:
- Debe incluír criterios de éxito observables e unha avaliación rápida.
```

## Técnicas fundamentais (as que máis impacto teñen)

### 1) Definición de Rol (Persona Pattern)

Asignar un rol non serve para facer ao modelo "máis listo", senón para **comprimir instrucións**: activa os seus *priors* (coñecementos e tons pre-asociados) para aliñar a resposta cunha expectativa específica, descartando vocabulario ou estilos irrelevantes. É útil para establecer o **estilo** co que queremos a resposta, pero non é necesario se a definición do resultado que queremos é suficientemente detallada.

- **Mal uso (Lazy Prompting):** "Es un experto en Python."
  - *Problema:* Delegas no modelo a definición de "experto". Pode activar *priors* indesexados (ex. usar librerías obsoletas) se non especificas máis.

- **Buen uso (Filtro de Enfoque):** "Actúa como un Auditor de Seguridade (Senior): revisa este código buscando vulnerabilidades críticas (OWASP Top 10) e suxire correccións defensivas."
  - *Vantaxe:* Usas o rol para establecer a "lente" (perspectiva crítica) e as instrucións para definir a "tarefa" (criterios OWASP).

O rol configura o *quén* (a voz), pero nunca debe substituír ao *qué* (as instrucións). Se confías só no rol para tarefas loxistas ou factuais, aumentas o risco de alucinacións plausibles.

### 2) Claridade do obxectivo (e evidencia)

Mal: “Fai unha actividade sobre IA.”

Mellor: “Crea unha actividade de 50 min para 2º FP sobre como **avaliar respostas dunha IA**. Evidencia: o alumnado identifica 3 erros típicos e propón 1 mellora.”

### 3) Contexto docente mínimo viable

Inclúe sempre: **nivel**, **tempo**, **recursos** e **produto final**. Proporcionar estes datos reduce drasticamente as respostas xenéricas.

### 4) Interacción Inversa (Flipped Interaction)

Consiste en pedir ao modelo que te entreviste antes de xerar a resposta final.

- **Na plantilla:** "Faime 3–5 preguntas de aclaración (só as necesarias)".
- **Por que funciona:** Obriga ao modelo a detectar lagoas na túa petición antes de "alucinar" detalles (ex. asumir que todos teñen portátil).

**Cando usalo?**
- **Úsao só** en tarefas complexas de deseño (proxectos, rúbricas completas) onde o contexto é determinante.
- **Evítao** en consultas rápidas ou directas; neses casos só engade fricción innecesaria.

### 5) Xestión da incerteza (Supostos explícitos)

Se o modelo non ten toda a información, tenderá a encher os ocos (alucinar) ou a ser vago.
- **Na plantilla:** "Se falta información crítica, propón ata 3 supostos explícitos".
- **Por que funciona:** Fai visible a "imaxinación" do modelo. Permíteche corrixir a premisa ("Non, non teñen portátiles, teñen tablets") antes de que xere todo o contido.

### 6) Control do formato (para que sexa usable)

Especifica o formato coma se fose unha “plantilla de entrega”. Exemplos útiles:

- Táboa de comparación con columnas fixas.
- Lista de verificación (checklist).
- Markdown con encabezados exactos.
- As cabeceiras deben ter só a primeira palabra en maiúsculas (norma RAG/RAE), salvo nomes propios.

### 7) Delimitadores (para separar instrucións de datos)

Se inclúes textos longos (temario, contexto, instrucións do centro), sepáraos con delimitadores para que o modelo non confunda as instrucións do prompt co texto a analizar:

```text
Contexto do centro:
"""
[pega aquí o texto]
"""
```

## Prácticas “modernas” que si se notan (calidade e rigor)

### A) Dúas pasadas: borrador → auditoría → versión final

Pide primeiro unha versión 1 e logo unha auditoría contra criterios.

Exemplo de auditoría:

```text
Revisa a túa proposta con esta lista:
1) O obxectivo é observable?
2) Hai riscos de privacidade?
3) A avaliación mide o que se pretende?
4) Hai supostos non declarados?

Devolve: (a) achados, (b) versión mellorada.
```

### B) Comparación A/B (cando iteras)

En lugar de “mellórao”, dá dúas versións e pide unha táboa por criterios:

```text
Compara Prompt A vs Prompt B por: claridade, formato, verificabilidade, riscos.
Devolve unha táboa e unha recomendación.
```

### C) Verificación e límites (anti-alucinacións)

En docencia, o problema non é só “acertar”: é **non inventar**.

Inclúe restricións como:

- “Se necesitas datos (datas, normativa, estatísticas), indícao e suxire como verificalo. Non inventes.”
- “Marca claramente o que sexa suposto.”

## Razoamento e verificación

En educación, moitas tarefas non teñen unha única resposta “correcta” (p. ex. deseñar unha actividade, redactar unha rúbrica ou elixir exemplos). Neses casos funciona mellor pedir **alternativas + criterios + selección** que pedir “a mellor resposta” a secas.

### Tree of Thoughts (ToT): explorar alternativas e elixir con criterios

Pide 2–4 propostas distintas (A/B/C) e unha avaliación cunha rúbrica breve. Despois, solicita **só a versión final** integrando melloras.

Ver exemplo: [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### Self-consistency: consenso (especialmente para checklists)

Pide varias propostas independentes e logo unha versión por “consenso”: conservar o común e xustificar excepcións. É moi útil para **checklists** e pautas de corrección.

Ver exemplo: [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### ReAct (Reasoning + Acting): investigar e verificar con accións observables

Cando a tarefa require ferramentas (busca, extracción, validación de formato), usa un ciclo breve de **Acción → Observación → Axuste**. Importante: pide **accións e evidencias**, non “pensamento paso a paso”.

Ver exemplo: [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)

### Iteración controlada (Self-Refine / Reflexion): borrador → crítica → versión final

O que ás veces se chama “RSIP” adoita corresponder a patróns máis estándar como **Self-Refine** (mellora iterativa con auto-feedback) e **Reflexion** (axentes que melloran con feedback e memoria). En docencia, abonda con 1–2 roldas e **criterios de parada** claros.

Ver exemplo: [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)

### Descomposición con restricións (task decomposition / prompt chaining)

O que ás veces se etiqueta como “CAD” adoita corresponder a **descompoñer** o traballo mantendo restricións globais (nivel, tempo, privacidade, formato). Pide un “blueprint” primeiro e o contido despois, seguido dunha revisión de coherencia.

Ver exemplo: [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

## Modelos con razoamento (como pedir mellor)

Con modelos actuais, adoita funcionar mellor:

- pedir unha resposta **directa**,
- pedir **supostos** se falta información,
- e pedir unha **xustificación breve** baseada en criterios (non un razoamento longo).

Evita converter o prompt nunha receita interminable. Se a saída está ben especificada, o modelo “organízase” só.

## Cando usar one-shot / few-shot

Úsaos sobre todo para **estilo e formato**, non para “ensinar contido”.

- One-shot: un exemplo da saída desexada.
- Few-shot: 2–3 exemplos cando o formato é complexo ou moi sensible (p. ej. rúbricas).

## Axentes e fluxos (cando o chat non abonda)

Un “axente” ten sentido cando queres que o sistema:

- siga un plan,
- use ferramentas (p. ej., converter a GIFT, aplicar unha rúbrica, revisar formato),
- e pare cando cumpra criterios.

Se estás deseñando un fluxo, especifica:

- obxectivo e criterios de parada,
- ferramentas permitidas,
- restricións (privacidade e fontes),
- formato de saída.

Se o modelo debe usar ferramentas ou facer iteracións, pide que rexistre **accións e observacións** (que fixo e que obtivo) e limita o número de ciclos. Evita pedir cadeas de pensamento explícitas.

## Guías oficiais recomendadas

- OpenAI: https://platform.openai.com/docs/guides/prompt-engineering
- Google Gemini: https://ai.google.dev/gemini-api/docs/prompting-intro
