---
title: Exemplos comentados
description: Conversas reais que mostran cada técnica, co porqué de que funcionen.
derived_from:
  es/prompts/ejemplos.md: "e1dc354eed44255b467f904ef5e713b9aef4c074"
---

A idea non é copiar o contido que xera a IA, senón **aprender a pedilo**: con contexto, restricións e verificación.

## Un *prompt* que escribe *prompts*

Este é un caso de [*metaprompting*](index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt): en lugar de pedir unha actividade, pídese o modelo que servirá para pedir calquera actividade.

:::: chat
::: user
Actúa como un asesor pedagóxico especializado en secundaria e FP.

Obxectivo: preciso un prompt reutilizable para pedirlle a unha IA que xere unha actividade de aula (45-60 min) sobre calquera tema.

Requisitos do prompt:

- Debe comezar pedindo 3-5 preguntas de aclaración (nivel, materia, requisitos do centro, tempo, recursos).
- Debe producir unha ficha lista para usar con: obxectivos, criterios de éxito, materiais, pasos minuto a minuto, atención á diversidade (2 adaptacións) e avaliación rápida (*exit ticket*).
- Debe evitar inventar normativa ou «datos do centro»; se falta información debe marcalo como suposto.
- Debe pedir o formato de saída en Markdown con encabezados fixos.

Devólveme SÓ o prompt final (en galego).
:::
::: assistant collapsed
Copia e pega este prompt (é un «prompt modelo»):

```text
Es un asistente de deseño didáctico para secundaria e FP. O teu obxectivo é axudarme a crear unha actividade de aula lista para usar.

1) Antes de propor a actividade, faime 3–5 preguntas de aclaración (só as necesarias) sobre:
- Materia/tema e curso ou nivel
- Tempo dispoñible (45–60 min)
- Recursos (aula, proxector, móbiles, internet, etc.)
- Perfil do grupo (heteroxeneidade, NEAE, nivel lingüístico)
- Criterios ou evidencias de aprendizaxe que quero observar

2) Se falta información crítica, propón supostos explícitos (máximo 3) e continúa.

3) Xera unha ficha de actividade en Markdown con estes encabezados EXACTOS:
- Obxectivo
- Obxectivos de aprendizaxe (3–5)
- Criterios de éxito (observables)
- Materiais
- Desenvolvemento (minuto a minuto)
- Atención á diversidade (2 adaptacións: apoio e ampliación)
- Avaliación rápida (exit ticket de 3 ítems)
- Riscos e como mitigalos

4) Restricións:
- Non inventes normativa, datos do centro nin cifras. Se algo non está no contexto, indícao como suposto.
- Evita xerga innecesaria; escribe para un docente principiante/intermedio.

Tema: [escribe aquí o tema]
```
:::
::::

> [!TIP]
> **Por que funciona**
> - Define o rol (asesoría pedagóxica) e o **obxectivo** (unha actividade lista para usar).
> - Obriga a facer **preguntas de aclaración** antes de escribir a proposta.
> - Controla a saída con **encabezados fixos** e restricións (non inventar datos, marcar supostos).
> - Introduce unha boa práctica de **privacidade**: non usar datos do centro nin do alumnado.

## Dar un exemplo de saída (*one-shot*)

:::: chat
::: user
Quero un exemplo de saída para unha «ficha de actividade» que eu poida usar como patrón.

Exemplo (patrón de formato) para unha actividade calquera:

- Título: ...
- Obxectivo: ...
- Desenvolvemento: 3 pasos numerados
- Avaliación: 2 criterios

Agora crea UNHA ficha nova sobre «como ensinarlle ao meu alumnado a escribir bos prompts», para 4.º ESO ou 1.º FP Básica. Regras:

- Máximo 180 palabras.
- Respecta o mesmo patrón de formato.
:::
::: assistant
- Título: Obradoiro exprés: «Preguntarlle ben a unha IA»
- Obxectivo: Que o alumnado converta unha petición vaga nun prompt claro con contexto, restricións e formato.
- Desenvolvemento:
  1. (10 min) En parellas, reescriben «Explícame X» engadindo: público, extensión e formato.
  2. (20 min) Comparan dous prompts sobre o mesmo tema e escollen cal é máis verificable.
  3. (15 min) Crean o seu propio prompt para xerar unha ficha de estudo e próbano.
- Avaliación:
  - O prompt inclúe contexto (nivel, tema, obxectivo) e restricións (extensión/formato).
  - A saída é avaliable (ten criterios de éxito ou unha lista de comprobación).
:::
::::

## Dar varios exemplos (*few-shot*)

:::: chat
::: user
Estou a crear un asistente para docentes. Preciso que a IA xere «instrucións para unha tarefa» cun estilo consistente.

Aquí tes DOUS exemplos do estilo exacto que quero (formato e ton):

Exemplo 1
Tarefa: Resume un texto.
Entrega: 8-10 liñas.
Criterios: inclúe idea central + 3 ideas clave + 1 dúbida.

Exemplo 2
Tarefa: Debate guiado.
Entrega: 1 postura + 2 argumentos + 1 contraargumento.
Criterios: argumentos baseados en evidencias do material.

Agora xera 3 instrucións de tarefa novas para «aprender a usar a IA de forma responsable na clase». Regras:

- Mantén EXACTAMENTE o mesmo patrón de 3 liñas (Tarefa / Entrega / Criterios).
- Nivel: 2.º FP Grao Medio.
:::
::: assistant
Tarefa: Auditoría dunha resposta de IA.
Entrega: 6-8 liñas con 3 riscos e 3 mitigacións.
Criterios: menciona privacidade, nesgos e verificación.

Tarefa: Deseña un prompt seguro.
Entrega: 1 prompt con contexto + 3 restricións + formato de saída.
Criterios: evita datos persoais e esixe evidencias.

Tarefa: Lista de comprobación de uso responsable.
Entrega: lista de 7 ítems «antes/durante/despois».
Criterios: ítems accionables e verificables.
:::
::::

> [!TIP]
> **Por que funciona**
> - Os exemplos fixan un patrón de saída estable.
> - Controla o **formato** (tres liñas fixas) e o **nivel**.
> - Reduce a ambigüidade: o resultado pódese avaliar.

## Pedir unha crítica do propio *prompt*

Pedir explicitamente que se sinale todo o cuestionable evita a tendencia dos *chatbots* a darche a razón, e obriga a unha análise con criterios.

:::: chat
::: user
Fai unha análise exhaustiva sinalando todo aquilo que poida ser cuestionable, incompleto ou mellorable no seguinte prompt.

Quero que o avalíes criticamente con mentalidade de docente: detecta ambigüidades, posibles nesgos (p. ex. exemplos estereotipados), riscos de privacidade e falta de verificabilidade. Despois propón unha versión mellor.

Prompt: «Crea unha actividade divertida sobre IA para a miña clase e pon exemplos reais dos meus alumnos.»
:::
::: assistant collapsed
**Análise crítica do prompt**

1. **Ambigüidade.** «Actividade divertida» non define obxectivos, duración, nivel nin produto final. «Sobre IA» é demasiado amplo: uso responsable, conceptos, ferramentas, ética, nesgos, avaliación de respostas?
2. **Riscos de privacidade.** «Exemplos reais dos meus alumnos» pode implicar datos persoais ou situacións identificables. É un risco claro e evitable.
3. **Nesgos e estereotipos.** Sen restricións, o modelo pode usar exemplos «típicos» con nesgos (xénero, orixe, etc.) ou situacións sensibles.
4. **Falta de verificabilidade.** Non hai criterios de éxito nin avaliación, e sen formato a resposta pode ser difícil de usar.

**Versión mellorada**

```text
Es un asistente de deseño didáctico para secundaria/FP.

Antes de propor nada, faime 4 preguntas de aclaración sobre: nivel, tema exacto (uso responsable / avaliación de respostas / nesgos), tempo e recursos.

Requisitos:
- NON uses datos persoais nin exemplos baseados en alumnado real. Usa exemplos ficticios e neutrais.
- Inclúe: obxectivos (3), criterios de éxito, materiais, desenvolvemento minuto a minuto, 2 adaptacións (apoio e ampliación) e un exit ticket de 3 ítems.
- Formato: Markdown con encabezados fixos.

Contexto inicial: [describe aquí o teu grupo en termos xerais, sen datos persoais].
```
:::
::::

## Comparar dous *prompts* nunha táboa

Cando dubidas entre dúas versións, unha comparación por criterios dá unha retroalimentación máis concreta ca «cal é mellor?».

:::: chat
::: user
Son docente e teño dúas versións dun prompt para xerar unha ficha de actividade. Quero que compares ambos e me digas cal é mellor e por que, nunha táboa.

Columnas: «Criterio», «Prompt A», «Prompt B», «Recomendación». Criterios mínimos: claridade do obxectivo, información que falta, control do formato, verificabilidade e riscos (nesgos/privacidade).

Prompt A: «Faime unha actividade sobre intelixencia artificial para os meus alumnos.»

Prompt B: «Crea unha actividade de 50 min para 2.º FP sobre como avaliar respostas dunha IA. Inclúe obxectivos, materiais, pasos minuto a minuto, 2 adaptacións e un exit ticket. Non inventes normativa nin datos. Formato Markdown con encabezados.»
:::
::: assistant collapsed
| Criterio | Prompt A | Prompt B | Recomendación |
| --- | --- | --- | --- |
| Claridade do obxectivo | Vago: non indica que se quere conseguir (aprendizaxe, produto, duración). | Claro: define un tema concreto (avaliar respostas de IA) e a duración. | Mantén un obxectivo observable («o alumnado detecta 3 erros típicos…»). |
| Información que falta | Non pide contexto (nivel, recursos, tempo, perfil). | Inclúe nivel e tempo; faltan recursos e perfil do grupo. | Engade 3–5 preguntas de aclaración antes de xerar a actividade. |
| Control do formato | Sen formato: saída imprevisible. | Pide Markdown con encabezados. | Especifica encabezados fixos e límites (p. ex., «máx. 1 páxina»). |
| Verificabilidade | Difícil avaliar se «serve». | Inclúe *exit ticket* e estrutura; máis avaliable. | Engade criterios de éxito e evidencias de aprendizaxe. |
| Riscos | Non menciona riscos: pode introducir exemplos problemáticos ou pedir datos persoais. | Menciona non inventar normativa; non trata a privacidade. | Engade: «non uses datos persoais; inclúe advertencias de nesgo e verificación». |

Mellor prompt: **B**, porque reduce a ambigüidade e controla a saída. Aínda así, melloraríao pedindo aclaracións e engadindo privacidade e verificación.
:::
::::

> [!TIP]
> **Por que funciona**
> - Converte unha opinión nunha revisión **estruturada**.
> - Obriga a falar de formato, verificabilidade e riscos.
> - A recomendación final sae de criterios, non de preferencias de estilo.
