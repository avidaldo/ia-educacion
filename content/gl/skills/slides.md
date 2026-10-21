---
derived_from:
  es/skills/slides.md: "1fddd371455f217475433703128de7f1d977a3cf"
---

<!-- .slide: id="no-repitas" class="statement" -->
## Se a tarefa se repite, non repitas o *prompt*

Garda as instrucións, os materiais e o procedemento.

---

<!-- .slide: id="tres-niveles" class="cards fragments" -->
## Tres niveis

### Instrucións personalizadas
Aplícanse a **todas** as túas conversas.

### Asistente personalizado
Instrucións e documentos para **as conversas dese asistente**: GPT, Gem, proxecto, espazo.

### *Skill*
Un **procedemento** que se carga só cando a tarefa o require, en calquera conversa.

---

<!-- .slide: id="asistentes" class="table" -->
## Asistentes personalizados

| Ferramenta | Nome |
| --- | --- |
| ChatGPT | GPTs e proxectos |
| Gemini | Gems (tamén no plan gratuíto) |
| Claude | Proxectos |
| Perplexity | Espazos |

Un *prompt* fixo máis un contexto opcional, reutilizado en moitas conversas.

---

<!-- .slide: id="como-funciona-skill" class="fragments" -->
## Como funciona unha *skill*

- Un cartafol cun ficheiro `SKILL.md`: nome, **cando** usala e **como** facer a tarefa.
- Pode levar exemplos, modelos e código.
- O asistente só le ao principio o nome e a descrición.
- Cando a túa petición encaixa, carga a *skill* completa e segue o procedemento.

Notas:
Por iso pode ter moitas skills dispoñibles sen encher a conversa, e non fai falta escoller o asistente axeitado: abonda con pedir a tarefa. É un estándar aberto (Agent Skills) publicado por Anthropic.

---

<!-- .slide: id="donde" class="table" -->
## Onde se poden usar

| Onde | Dispoñibilidade |
| --- | --- |
| Claude | Todos os plans, coa execución de código activada |
| ChatGPT | Plans Business, Enterprise e Edu |
| Ferramentas de programación con axentes | Desde cartafoles do proxecto |

---

<!-- .slide: id="ejemplo-skill" class="prompt dense" -->
## Unha *skill* para preguntas de Moodle

```markdown
---
name: preguntas-gift
description: Xera preguntas de escolla múltiple en formato GIFT importable en Moodle.
  Úsaa cando pidan preguntas de test, un banco de preguntas ou un exame para Moodle.
---
1. Se non se indica, pregunta o nivel e o número de preguntas.
2. 4 opcións, unha correcta; as incorrectas restan un 25 %.
3. Segue exactamente o formato de exemplo.gift.
4. Escapa ~ = # { } : no texto.
5. Revisa a clave antes de entregar.
```

Notas:
A descrición é o máis importante: é o que o asistente le para decidir se a usa. O cartafol complétase cunha pregunta exportada do teu propio Moodle. A versión completa está na páxina.

---

<!-- .slide: id="demo-crear-skill" class="demo" -->
## Unha *skill* que crea *skills*

Describir a tarefa e deixar que o asistente escriba o procedemento.

Notas:
**Demo (8 min)**. Claude (plan gratuíto, coa execución de código activada en Axustes → Capacidades) ou ChatGPT Edu.

1. Pedir: «Quero unha *skill* que xere preguntas GIFT para Moodle con estas regras…» e pegar as regras da páxina.
2. Revisar a descrición e as instrucións que propón; corrixir o que non encaixe.
3. Instalala e, nun chat novo, pedir «dez preguntas de test sobre…» sen mencionar a *skill*.
4. Comprobar que a usou e revisar as preguntas.

**Resultado esperado:** o asistente recoñece a tarefa e aplica o procedemento sen que llo lembres.
**Se falla:** ensinar a *skill* de exemplo da páxina.
**Mensaxe clave:** é *metaprompting* aplicado a un procedemento; a *skill* próbase con casos reais antes de confiar nela.

---

<!-- .slide: id="error-comun" class="comparison" -->
## Instrucións, non descricións

### Mal
«Crea un xerador de preguntas de test que…»

### Mellor
«Cando o usuario che dea un tema, xera 10 preguntas en formato GIFT…»

---

<!-- .slide: id="ideas" -->
## Ideas para a docencia

- Banco de preguntas co formato do teu Moodle.
- Adaptador de materiais a varios niveis.
- Revisor de actividades cos teus criterios.
- Redactor co estilo do departamento.
- Corrector con rúbrica, sen datos identificativos.

---

<!-- .slide: id="terceros" class="statement" -->
## Instala só *skills* que leses

Coma unha extensión do navegador, unha *skill* de terceiros pode conter instrucións ou código daniños.

---

<!-- .slide: id="antes-de-compartir" class="checklist" -->
## Antes de usalo ou compartilo

- [ ] Obxectivo e formato definidos.
- [ ] Criterios de calidade explícitos.
- [ ] Probado con casos reais, algún difícil.
- [ ] Non pide nin garda datos do alumnado.
- [ ] Os documentos que leva pódense compartir.

---

<!-- .slide: id="practica-asistente" class="practice" -->
## Crea o teu asistente

1. Escolle unha tarefa que repites cada semana.
2. Escribe as súas instrucións co modelo da páxina.
3. Crea unha Gem, un GPT ou un proxecto con elas.
4. Próbao con dous casos reais e corrixe as instrucións.

**15 minutos.** Produto: un asistente que xa funciona.

Notas:
O modelo está na páxina, en «Como escribir as instrucións». Poñer en común que tarefas escolleron: adoitan saír bancos de preguntas, adaptacións e comunicacións ás familias.
