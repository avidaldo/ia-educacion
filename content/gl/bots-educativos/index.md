---
title: Bots educativos
description: Asistentes configurados polo docente para que o alumnado os use como titor, e o que hai que decidir antes de poñelos nas súas mans.
derived_from:
  es/bots-educativos/index.md: "a9d495ae5a90f82a40f955ca1ec364d910b920cb"
---

## Que é un bot educativo

Un bot educativo é un [asistente personalizado](../skills/index.md) que configura o docente **para que o use o alumnado**: un titor que guía sen dar a solución, un compañeiro de repaso con preguntas sobre o temario, un asistente que axuda a entender unha lectura. O alumnado ve un chat normal, pero o bot segue sempre as instrucións que fixaches.

A idea máis interesante non é que dea respostas, senón que **guíe o razoamento**: facer preguntas, dividir o problema en pasos, sinalar contradicións para que o alumno detecte o seu propio erro.

## O primeiro: con que conta entra o alumnado

Antes de deseñar o bot hai que resolver unha pregunta que condiciona todo o demais: **que conta vai usar cada alumno**. Dela dependen a idade mínima, as condicións sobre os seus datos e se o centro pode responder dese uso.

| Servizo | Idade mínima con conta persoal |
| --- | --- |
| ChatGPT | 13 anos ou a idade de consentimento do país; menores de 18, co consentimento de nai, pai ou titor |
| Gemini | 13 anos ou a idade do país; con conta de centro educativo, habilítaa o seu administrador |
| Perplexity | 13 anos; menores de idade, só se nai, pai ou titor aceptan as condicións |
| Claude | 18 anos |

En España, un menor só pode consentir por si mesmo o tratamento dos seus datos a partir dos 14 anos; por debaixo, fai falta o consentimento de quen ten a patria potestade ou a titoría (artigo 7 da Lei orgánica de protección de datos). Pedirlle ao alumnado que se rexistre nun servizo coa súa conta persoal trasládalle a cada familia unha decisión que lle corresponde ao centro.

A opción con máis garantías é a que **proporciona o centro ou a administración**: contas educativas contratadas con condicións específicas. Con **Google Workspace for Education**, por exemplo, a aplicación de Gemini está dispoñible para alumnado de todas as idades se o administrador a activa, con protección de datos de nivel empresarial; o alumnado menor de 18 anos pode usar Gems, a aprendizaxe guiada, Canvas e os cuestionarios, pero non a investigación a fondo nin Gemini Live. As implicacións legais desenvólvense en [Normativa](../etica-legal/normativa.md#la-edad-del-alumnado).

> [!CAUTION]
> **O que xa non funciona: o espazo de Perplexity sen conta**
> Durante un tempo, un espazo de Perplexity podíase compartir cunha ligazón aberta, e recomendábase para que o alumnado o usase sen rexistrarse. Hoxe os espazos chámanse **proxectos** e, nas contas persoais, só acceden as persoas convidadas: *«Projects cannot be made publicly queryable»*, segundo o seu centro de axuda (outubro de 2026). Ademais, non pedir conta nunca fixo que o seu uso cumprise a normativa por si só: o que o alumnado escribe segue a enviarse a un terceiro, xunto con datos técnicos como o enderezo IP, e a idade mínima das condicións de uso segue a aplicarse.

## Como compartir un bot en cada ferramenta

| Ferramenta | Como se comparte | Para ter en conta |
| --- | --- | --- |
| Gemini (Gems) | Como un ficheiro de Drive: con persoas concretas ou con quen teña a ligazón, segundo o que permita o administrador | Require conta de Google. A partir de novembro de 2026 as Gems pasan a ser *skills* (nas contas de centro, en 2027) |
| ChatGPT (GPTs) | Cunha ligazón ou publicado na tenda de GPTs | Require conta de ChatGPT; ver idade mínima |
| Perplexity (proxectos) | Convidando cada persoa; ata 5 colaboradores, ou 9.999 se o propietario é docente ou estudante verificado | Require conta de Perplexity; ver idade mínima |

## Os modos titor integrados

Antes de construír un titor, comproba se abonda co que xa trae cada ferramenta:

- **ChatGPT, modo de estudo**: guía con preguntas en lugar de dar a resposta, explica por niveis e comproba a comprensión. Dispoñible en todos os plans.
- **Gemini, aprendizaxe guiada**: dispoñible tamén para alumnado menor de 18 anos con contas de Workspace for Education.
- **Perplexity, modo de aprendizaxe**: explica paso a paso e xera tarxetas e cuestionarios a partir dos materiais.

Un bot propio compensa cando precisas algo que estes modos non fan: cinguirte ao teu temario e aos teus materiais, seguir a túa metodoloxía ou un nivel concreto, ou limitarte a un tipo de tarefa.

## Un titor socrático

Estas instrucións son un bo punto de partida. Adáptaas á materia, ao nivel e aos materiais que adxuntes:

```text
Rol:
Es un titor socrático de [materia] para alumnado de [nivel]. O teu obxectivo é axudar a chegar á resposta por si mesmo, nunca dar a solución directa.

Regras:
1. Non resolvas o problema nin deas a resposta final, aínda que cha pidan.
2. Se che piden a resposta, explica con amabilidade que o teu traballo é axudar a pensar.
3. Divide o problema en pasos pequenos e fai só UNHA pregunta cada vez.
4. Se hai un erro, non digas «está mal»: pregunta por que se escolleu ese camiño ou sinala a contradición.
5. Usa unha linguaxe clara e adaptada ao nivel, cun ton paciente.
6. Basea as explicacións nos materiais adxuntos; se algo non está neles, dío.
7. Non pidas nin gardes datos persoais.
8. Se a dúbida non é da materia ou é delicada, recomenda falar co profesorado.

Inicio:
Preséntate nunha frase como asistente de IA e pregunta en que exercicio ou concepto quedou atascado.
```

## Probalo antes de compartilo

Un bot compórtase de forma distinta segundo como lle falen. Antes de darllo ao alumnado, próbao como o faría un alumno:

- [ ] Pide directamente a solución, varias veces e con insistencia.
- [ ] Pídelle que ignore as súas instrucións ou que «faga unha excepción».
- [ ] Fai unha pregunta fóra do temario e outra persoal ou delicada.
- [ ] Comete un erro a propósito e comproba como o trata.
- [ ] Revisa que o que explica coincide cos teus materiais.

> [!WARNING]
> **As instrucións non son unha barreira de seguridade**
> Con insistencia abonda, un alumno pode conseguir que o bot saia das súas instrucións e lle dea a resposta. O bot axuda a quen quere aprender; non substitúe a supervisión nin serve para controlar a quen quere saltalo.

## Na clase

- Explícalle ao alumnado que é unha ferramenta de IA, que pode equivocarse e que as súas respostas se comproban.
- Define para que se pode usar e para que non, sobre todo nas tarefas avaliables.
- Revisa de cando en vez como o están usando e axusta as instrucións.
- A avaliación segue a ser túa: o bot acompaña o estudo, non cualifica.
