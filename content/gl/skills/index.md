---
title: Asistentes e skills
description: Como fixar instrucións e materiais para as tarefas que se repiten, desde un asistente personalizado ata unha skill.
derived_from:
  es/skills/index.md: "fa6c430c07b027d501291a9b2be186ba3d81ddc7"
---

## Por que fixar as instrucións

Se xeras preguntas de test cada semana, adaptas actividades a varios niveis ou revisas programacións cos mesmos criterios, reescribir o *prompt* cada vez é lento e produce resultados irregulares. Todos os *chatbots* permiten **gardar as instrucións** (e ás veces materiais e procedementos) para reutilizalas. Hai tres niveis:

Instrucións personalizadas
: Aplícanse a **todas** as túas conversas: quen es, que impartes, o ton que prefires. Están nos axustes de cada *chatbot*; vense en [Chatbots](../chatbots/index.md#instrucciones-personalizadas).

Asistente personalizado
: Unhas instrucións fixas, e opcionalmente documentos, que se aplican **ás conversas dese asistente**: un GPT en ChatGPT, unha Gem en Gemini, un proxecto en ChatGPT ou Claude, un espazo en Perplexity.

*Skill*
: Un **procedemento** empaquetado (instrucións, exemplos, modelos e, se fai falta, código) que o asistente **carga só cando a tarefa o require**, dentro de calquera conversa.

## Asistentes personalizados

| Ferramenta | Nome | Que inclúe |
| --- | --- | --- |
| ChatGPT | GPTs | Instrucións, ficheiros de coñecemento e capacidades (busca, imaxes, código). Pódense compartir cunha ligazón |
| ChatGPT e Claude | Proxectos | Instrucións e ficheiros comúns a un grupo de conversas |
| Gemini | Gems | Instrucións e ficheiros. Dispoñibles tamén no plan gratuíto |
| Perplexity | Espazos | Instrucións, ficheiros e busca web. Vense no módulo de bots educativos<!-- TODO: enlazar ../bots-educativos/index.md cuando exista --> |

Os nomes e o que inclúe cada plan cambian a miúdo. O que non cambia é a idea: **un *prompt* fixo máis un contexto opcional**, reutilizado en moitas conversas.

## *Skills*

Unha *skill* é un cartafol cun ficheiro `SKILL.md`: un nome, unha descrición de **cando** usala e as instrucións de **como** facer a tarefa, máis os ficheiros que precise (exemplos, modelos, *scripts*). A diferenza cun asistente é como se usa:

- O asistente só coñece, ao comezar, o nome e a descrición de cada *skill* instalada.
- Cando a túa petición encaixa cunha descrición, carga esa *skill* completa e segue o seu procedemento.
- Así pode ter moitas *skills* dispoñibles sen encher a conversa de instrucións, e ti non tes que escoller o asistente axeitado: abonda con pedir a tarefa.

O formato publicouno Anthropic como estándar aberto ([Agent Skills](https://agentskills.io)) e adoptárono outras ferramentas. En outubro de 2026:

| Onde | Dispoñibilidade |
| --- | --- |
| Claude (web e aplicacións) | Todos os plans, incluído o gratuíto. Require activar a execución de código en Axustes → Capacidades (*Capabilities*) |
| ChatGPT | Plans Business, Enterprise e Edu |
| Ferramentas de programación con axentes (Claude Code, Codex, Gemini CLI…) | Cargan *skills* desde cartafoles do proxecto |

As *skills* poden incluír código que o asistente executa. Por iso **instala só *skills* que leses** ou que veñan dunha fonte de confianza: igual ca unha extensión do navegador, unha *skill* de terceiros pode conter instrucións ou código daniños.

### Unha *skill* de exemplo

Unha *skill* para xerar preguntas de Moodle. A descrición é o máis importante: é o que o asistente le para decidir se a usa.

```markdown
---
name: preguntas-gift
description: Xera preguntas de escolla múltiple en formato GIFT importable en Moodle a partir dun tema ou dun material, con penalizacións e retroalimentación. Úsaa cando pidan preguntas de test, un banco de preguntas ou un exame para Moodle.
---

# Preguntas GIFT para Moodle

1. Se non se indica, pregunta o nivel do alumnado e o número de preguntas.
2. Xera cada pregunta con 4 opcións e unha soa correcta; as incorrectas restan un 25 %.
3. Segue exactamente o formato de `exemplo.gift` (neste mesmo cartafol).
4. Escapa con \ os caracteres ~ = # { } : que aparezan no texto.
5. Revisa antes de entregar: clave correcta, sen pistas pola lonxitude, sen negacións.
6. Entrega só o contido do ficheiro .gift.
```

O cartafol complétase con `exemplo.gift`, unha pregunta exportada do teu propio Moodle, como se explica en [Tests para Moodle](../tests-moodle/index.md#el-método-más-fiable-partir-de-una-exportación-de-moodle).

Non fai falta escribila a man: Claude e ChatGPT inclúen unha *skill* para crear *skills*. Describe a tarefa («quero unha *skill* que xere preguntas GIFT con estas regras…»), revisa o que propón e próbaa con casos reais antes de usala. É [*metaprompting*](../prompts/index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt) aplicado a un procedemento.

## Como escribir as instrucións

Serve para un asistente e para unha *skill*:

```text
Rol e obxectivo:
Es un asistente de deseño didáctico para secundaria e FP.
O teu obxectivo é [tarefa concreta].

Contexto fixo:
- Nivel: [se procede]
- Restricións: non uses datos persoais; non inventes normativa.

Formato de saída:
- [Encabezados fixos / táboa / GIFT]

Procedemento:
1. Fai preguntas de aclaración (só as necesarias).
2. Xera a proposta.
3. Inclúe criterios de éxito observables.
```

> [!WARNING]
> **O erro máis común**
> Non describas o asistente («Crea un xerador de preguntas de test que…»): escribe as instrucións que debe seguir en cada conversa («Cando o usuario che dea un tema, xera 10 preguntas en formato GIFT…»).

## Ideas para a docencia

- **Banco de preguntas**: formato GIFT ou XML, criterios de calidade e un exemplo exportado do teu Moodle.
- **Adaptador de materiais**: converte un texto a varios niveis (apoio e ampliación) sen perder os obxectivos.
- **Revisor de actividades**: comproba que unha proposta ten obxectivos observables, avaliación e atención á diversidade.
- **Redactor co estilo do departamento**: modelos de informes, comunicacións ou programacións co formato do centro.
- **Corrector con rúbrica**: aplica a túa rúbrica e propón unha retroalimentación, que revisas ti. Nunca con datos identificativos do alumnado nunha conta persoal.

Non paga a pena para tarefas únicas ou exploratorias (usa un chat normal) nin cando as instrucións cambian cada vez.

## Antes de usalo ou compartilo

- [ ] **Obxectivo claro**: que produce exactamente?
- [ ] **Formato definido**: táboa, lista, GIFT, encabezados fixos?
- [ ] **Criterios de calidade**: como saberás que o resultado é bo?
- [ ] **Probado**: usáchelo con tres ou catro casos reais, incluído algún difícil?
- [ ] **Privacidade**: evita pedir ou gardar datos persoais do alumnado?
- [ ] **Documentos revisados**: os ficheiros que leva pódense compartir con quen o vaia usar?
