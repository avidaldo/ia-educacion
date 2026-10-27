---
title: Deseño de prompts
description: Como especificar unha tarefa para que o resultado sexa un material útil e verificable, non unha resposta xenérica.
derived_from:
  es/prompts/index.md: "8aba2aa9d5e0509c6d1923990cef353b92d052ed"
---

## Que é un bo *prompt*

Un *prompt* eficaz funciona como unha **especificación**: di que produto queres, para quen, con que restricións e como saberás que está ben. Canto máis se pareza a un encargo ben redactado a unha persoa competente, mellor funciona.

En docencia convén orientalo a **materiais funcionais e verificables**, por exemplo:

- fichas de actividade coa secuencia e os tempos;
- bancos de preguntas en formatos que Moodle importa directamente (GIFT, XML);
- rúbricas con indicadores observables;
- adaptacións que manteñan o aliñamento cos obxectivos de aprendizaxe.

## Unha estrutura de referencia

Este modelo serve de punto de partida. Non fai falta encher todos os apartados en cada consulta: é unha lista do que máis inflúe no resultado.

```text
Es un consultor experto en deseño curricular e normativa educativa.

Tarefa:
- Quero crear: [actividade / banco de preguntas / rúbrica / guía de estudo]

Contexto:
- Materia/tema:
- Nivel (curso ou FP):
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

Restricións:
- Non uses datos persoais do alumnado.
- Non inventes normativa, datos do centro nin cifras. Se non o sabes, indícao.

Criterios de calidade:
- Debe incluír criterios de éxito observables e unha avaliación rápida.
```

## As técnicas que máis se notan

### Definir un rol

Asignar un rol non fai o modelo «máis listo»: **comprime instrucións**. Un rol despraza a resposta cara ao vocabulario, o ton e os criterios asociados a esa figura nos textos cos que se adestrou o modelo. Serve sobre todo para fixar o **estilo** da resposta, e deixa de ser necesario cando a descrición do resultado xa é dabondo detallada.

Mal uso
: «Es un experto en Python.» Delegas no modelo que significa «experto», e pode botar man de prácticas que non queres (por exemplo, bibliotecas obsoletas).

Bo uso
: «Actúa como auditor de seguridade: revisa este código buscando vulnerabilidades críticas (OWASP Top 10) e suxire correccións.» O rol fixa a perspectiva; as instrucións definen a tarefa.

O rol configura o *quen* (a voz), pero non substitúe o *que* (as instrucións). Se para unha tarefa factual confías só no rol, aumentas o risco de respostas plausibles pero falsas.

### Un obxectivo claro, coa súa evidencia

Mal: «Fai unha actividade sobre IA.»

Mellor: «Crea unha actividade de 50 minutos para 2.º de FP sobre como **avaliar respostas dunha IA**. Evidencia: o alumnado identifica 3 erros típicos e propón 1 mellora.»

### O contexto docente mínimo

Inclúe sempre **nivel**, **tempo**, **recursos** e **produto final**. Con eses catro datos desaparece a maioría das respostas xenéricas.

### Pedir que che pregunte primeiro

Consiste en pedirlle ao modelo que te entreviste antes de xerar a resposta («Faime 3–5 preguntas de aclaración, só as necesarias»). Obrígao a detectar ocos na túa petición antes de enchelos pola súa conta, por exemplo supoñendo que todo o grupo ten portátil.

- **Úsao** en tarefas de deseño complexas (proxectos, rúbricas completas), onde o contexto o decide todo.
- **Evítao** en consultas rápidas: só engade un paso.

### Supostos explícitos

Se ao modelo lle falta información, tenderá a encher os ocos ou a ser vago. Pedirlle «se falta información crítica, propón ata 3 supostos explícitos» fai visible o que está a supoñer, e permíteche corrixilo («non teñen portátiles, teñen tabletas») antes de que constrúa todo enriba.

### O formato de entrega

Especifica o formato coma se fose un modelo de entrega:

- unha táboa de comparación con columnas fixas;
- unha lista de verificación;
- Markdown con encabezados exactos;
- títulos con maiúscula só na primeira palabra (norma da RAG), agás nomes propios.

### Delimitadores

Se inclúes textos longos (temario, normas do centro, un texto do alumnado xa anonimizado), sepáraos con delimitadores para que o modelo non confunda as túas instrucións co texto que debe analizar. Serven as comiñas triplas ou etiquetas con nome, como `<temario>…</temario>`; o importante é usar sempre as mesmas e nomealas na instrución:

```text
Contexto do centro:
"""
[pega aquí o texto]
"""
```

## Revisar antes de dar por boa unha resposta

### Dúas pasadas: borrador, auditoría e versión final

Pide primeiro unha versión e despois unha auditoría contra criterios:

```text
Revisa a túa proposta con esta lista:
1) O obxectivo é observable?
2) Hai riscos de privacidade?
3) A avaliación mide o que se pretende?
4) Hai supostos non declarados?

Devolve: (a) achados, (b) versión mellorada.
```

### Comparar dúas versións

En lugar de «mellórao», dá dúas versións e pide unha táboa por criterios:

```text
Compara o prompt A co B por: claridade, formato, verificabilidade e riscos.
Devolve unha táboa e unha recomendación.
```

### Non inventar

En docencia o problema non é só acertar: é **non inventar**. Inclúe restricións como:

- «Se precisas datos (datas, normativa, estatísticas), indícao e suxire como verificalos. Non inventes.»
- «Marca claramente o que sexa un suposto.»

> [!WARNING]
> **Estas instrucións reducen o problema, non o eliminan**
> Un modelo de linguaxe non sabe cando non sabe: pode presentar un dato inventado coa mesma seguridade ca un correcto. As cifras, as citas e a normativa compróbanse sempre na fonte.

## *Metaprompting*: pedirlle á IA que escriba o *prompt*

Cando unha tarefa se repite (xerar tests, adaptar actividades, redactar rúbricas), compensa pedir primeiro **o *prompt* reutilizable** en lugar do resultado. Describes que debe facer ese *prompt*, que debe preguntar e que formato debe esixir, e o modelo devólveche un modelo de *prompt* que podes revisar, gardar e reutilizar ou converter nun asistente personalizado.

Funciona por dous motivos: obrígate a pensar os requisitos antes de pedir o produto, e o modelo adoita redactar instrucións máis completas das que escribiriamos a man. O risco é o de sempre: hai que ler e probar o *prompt* antes de confiar nel.

Hai un exemplo completo en [Exemplos comentados](ejemplos.md#un-prompt-que-escribe-prompts).

## Modelos que razoan

Os modelos actuais poden dedicar tempo a «pensar» antes de responder. Con eles adoita funcionar mellor:

- pedir unha resposta **directa**;
- pedir **supostos** se falta información;
- e pedir unha **xustificación breve** baseada en criterios, non un razoamento longo.

Non fai falta pedirlles que pensen «paso a paso»: xa o fan. Se a saída está ben especificada, o modelo organízase só.

## Dar exemplos de saída

Os exemplos serven sobre todo para **estilo e formato**, non para ensinar contido.

*Zero-shot*
: Só a instrución, sen exemplos.

*One-shot*
: Un exemplo da saída desexada.

*Few-shot*
: Dous ou tres exemplos, cando o formato é complexo ou delicado (por exemplo, rúbricas ou preguntas para Moodle).

## Cando o chat non abonda

Un **axente** ten sentido cando queres que o sistema siga un plan, use ferramentas (converter a GIFT, aplicar unha rúbrica, revisar un formato) e pare cando se cumpran uns criterios. Se deseñas un fluxo así, especifica:

- o obxectivo e os criterios de parada;
- as ferramentas permitidas;
- as restricións (privacidade, fontes);
- o formato de saída.

As técnicas para tarefas longas ou con varias alternativas están en [Técnicas avanzadas](avanzado.md).

## Guías oficiais

- [OpenAI: *prompt engineering*](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google: estratexias de *prompting* para Gemini](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Anthropic: *prompt engineering* para Claude](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- Para quen queira a visión de conxunto académica: Schulhoff et al. (2024), [*The Prompt Report*](https://arxiv.org/abs/2406.06608), unha revisión sistemática de 58 técnicas de *prompting* de texto.
