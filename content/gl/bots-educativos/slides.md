---
derived_from:
  es/bots-educativos/slides.md: "9b83d3c77c4d774ad73e00a06a1b291ea86cf7b3"
---

<!-- .slide: id="que-es" class="statement" -->
## Un asistente que configuras ti para que o use o alumnado

O interesante non é que responda, senón que guíe o razoamento.

---

<!-- .slide: id="cuenta-primero" class="statement" -->
## Primeiro: con que conta vai entrar o alumnado?

Dela dependen a idade mínima, as condicións sobre os seus datos e se o centro pode responder dese uso.

---

<!-- .slide: id="edades" class="table" -->
## Idade mínima con conta persoal

| Servizo | Idade mínima |
| --- | --- |
| ChatGPT | 13; menores de 18, con consentimento familiar |
| Gemini | 13 (con conta de centro, habilítaa o administrador) |
| Perplexity | 13; menores, se a familia acepta as condicións |
| Claude | 18 |

Notas:
En España, un menor só consente por si mesmo o tratamento dos seus datos a partir dos 14 anos (artigo 7 da LOPDGDD). Pedir que se rexistren con conta persoal trasládalle a cada familia unha decisión que lle corresponde ao centro.

---

<!-- .slide: id="cuentas-centro" class="statement" -->
## A opción con máis garantías: contas que proporciona o centro

Con Workspace for Education, Gemini está dispoñible para todas as idades se o administrador o activa.

Notas:
Menores de 18 anos con esas contas: Gems, aprendizaxe guiada, Canvas e cuestionarios si; investigación a fondo e Gemini Live, non.

---

<!-- .slide: id="perplexity" class="comparison" -->
## O que xa non funciona

### Antes
Un espazo de Perplexity compartido cunha ligazón aberta, sen rexistrarse.

### Agora
Os espazos son proxectos e, en contas persoais, só acceden as persoas convidadas.

Notas:
E non pedir conta nunca fixo que cumprise a normativa por si só: o que escribe o alumnado envíase igualmente a un terceiro, con datos técnicos como a IP, e a idade mínima das condicións segue a aplicarse.

---

<!-- .slide: id="compartir" class="table dense" -->
## Como se comparte en cada ferramenta

| Ferramenta | Como |
| --- | --- |
| Gemini (Gems) | Como un ficheiro de Drive; pasan a ser *skills* |
| ChatGPT (GPTs) | Cunha ligazón ou na tenda de GPTs |
| Perplexity (proxectos) | Convidando cada persoa |

---

<!-- .slide: id="modos-tutor" class="cards" -->
## Antes de construír un: os modos titor

### ChatGPT
Modo de estudo, en todos os plans.

### Gemini
Aprendizaxe guiada, tamén para menores de 18 con conta de centro.

### Perplexity
Modo de aprendizaxe, con tarxetas e cuestionarios.

Notas:
Un bot propio compensa cando precisas cinguirte ao teu temario, á túa metodoloxía ou a un tipo de tarefa concreto.

---

<!-- .slide: id="tutor-socratico" class="prompt dense" -->
## Un titor socrático

```text
Es un titor socrático de [materia] para [nivel]. Axuda a chegar á resposta,
nunca deas a solución directa, aínda que cha pidan.
Divide o problema en pasos e fai só UNHA pregunta cada vez.
Se hai un erro, pregunta por que se escolleu ese camiño.
Basea as explicacións nos materiais adxuntos; se algo non está neles, dío.
Non pidas datos persoais. Se a dúbida é delicada, recomenda falar co profesorado.
Preséntate como asistente de IA e pregunta en que quedou atascado.
```

Notas:
A versión completa está na páxina.

---

<!-- .slide: id="demo-tutor" class="demo" -->
## Intenta que che dea a resposta

Probar o bot como o faría un alumno.

Notas:
**Demo (6 min)**. Unha Gem ou un GPT co titor socrático da páxina, nunha conta de probas.

1. Formular un exercicio e pedir directamente a solución.
2. Insistir varias veces e pedirlle que «faga unha excepción».
3. Cometer un erro a propósito e ver como o trata.
4. Facer unha pregunta fóra do temario.

**Resultado esperado:** resiste a maioría dos intentos, pero con insistencia algún funciona.
**Se falla:** se cede axiña, axustar as regras diante do grupo.
**Mensaxe clave:** as instrucións non son unha barreira de seguridade; o bot axuda a quen quere aprender.

---

<!-- .slide: id="probar" class="checklist" -->
## Antes de compartilo

- [ ] Pide a solución con insistencia.
- [ ] Pide que ignore as súas instrucións.
- [ ] Fai unha pregunta fóra do temario e outra delicada.
- [ ] Comete un erro a propósito.
- [ ] Comproba que coincide cos teus materiais.

---

<!-- .slide: id="en-clase" -->
## Na clase

- Explica que é IA e que pode equivocarse.
- Define para que se pode usar, sobre todo en tarefas avaliables.
- Revisa como o usan e axusta as instrucións.
- A avaliación segue a ser túa.
