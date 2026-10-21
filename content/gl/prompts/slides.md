---
derived_from:
  es/prompts/slides.md: "c5a6420075e4a9e98d4eb667a35a2ba79043f865"
---

<!-- .slide: id="especificacion" class="statement" -->
## Un bo *prompt* é unha especificación

Di que produto queres, para quen, con que restricións e como saberás que está ben.

Notas:
**Mensaxe clave:** pedirlle algo a unha IA parécese máis a encargarlle un traballo a unha persoa competente ca a buscar en Google. O que non se especifica, o modelo éncheo pola súa conta.

---

<!-- .slide: id="ingredientes" class="cards fragments" -->
## O que máis inflúe no resultado

### Tarefa
Que produto queres: actividade, rúbrica, banco de preguntas…

### Contexto
Nivel, tempo, recursos e perfil do grupo, sen datos persoais.

### Saída
Formato, encabezados fixos e límites de extensión.

### Restricións
Non inventar normativa nin cifras; marcar os supostos.

Notas:
Estas catro pezas son o modelo da páxina. Non fai falta usalas todas en cada consulta: son unha lista de comprobación.

---

<!-- .slide: id="plantilla" class="prompt dense" -->
## Un modelo de partida

```text
Es un consultor experto en deseño curricular.
Tarefa: quero crear [actividade / banco de preguntas / rúbrica].
Contexto: materia, nivel, duración, recursos, perfil do grupo (sen datos persoais).
Antes de responder: faime 3–5 preguntas de aclaración; se falta información, propón ata 3 supostos explícitos.
Saída: Markdown, con estes encabezados: […]; máx. 1 páxina.
Restricións: non inventes normativa, datos nin cifras; se non o sabes, dío.
```

Notas:
A versión completa está na páxina, con todos os apartados. Copiala desde a web, non desde a diapositiva.

---

<!-- .slide: id="rol" class="comparison" -->
## O rol fixa a voz, non a tarefa

### Mal
«Es un experto en Python.»

Delegas no modelo que significa «experto».

### Mellor
«Actúa como auditor de seguridade: revisa este código buscando vulnerabilidades críticas (OWASP Top 10) e suxire correccións.»

O rol dá a perspectiva; as instrucións, a tarefa.

Notas:
Un rol despraza a resposta cara ao vocabulario e os criterios asociados a esa figura. Non fai o modelo «máis listo». Se a tarefa é factual e só damos un rol, aumentamos o risco de respostas plausibles pero falsas.

---

<!-- .slide: id="objetivo" class="comparison" -->
## Un obxectivo claro, coa súa evidencia

### Mal
«Fai unha actividade sobre IA.»

### Mellor
«Crea unha actividade de 50 minutos para 2.º de FP sobre como **avaliar respostas dunha IA**. Evidencia: o alumnado identifica 3 erros típicos e propón 1 mellora.»

Notas:
Preguntarlle ao grupo que lle falta á primeira versión antes de amosar a segunda. Saen soas: nivel, duración, produto final.

---

<!-- .slide: id="contexto" class="fragments" -->
## O contexto docente mínimo

- **Nivel**: curso ou ciclo.
- **Tempo**: duración da sesión ou da tarefa.
- **Recursos**: aula, proxector, móbiles, internet…
- **Produto final**: que entrega o alumnado.

Con estes catro datos desaparece a maioría das respostas xenéricas.

---

<!-- .slide: id="preguntar-primero" class="two-col" -->
## Pedir que che pregunte primeiro

### Úsao
En tarefas de deseño complexas (proxectos, rúbricas completas), onde o contexto o decide todo.

### Evítao
En consultas rápidas: só engade un paso.

Notas:
Formulación: «Faime 3–5 preguntas de aclaración, só as necesarias». Obriga a detectar ocos antes de enchelos, por exemplo supoñendo que todo o grupo ten portátil.

---

<!-- .slide: id="supuestos" -->
## Supostos explícitos

- Se falta información, o modelo enche os ocos ou vólvese vago.
- Pídelle: «se falta información crítica, propón ata 3 supostos explícitos».
- Así ves o que está a supoñer e corríxelo antes de que constrúa todo enriba.

---

<!-- .slide: id="formato" class="two-col" -->
## Formato e delimitadores

### Formato de entrega
- Táboa con columnas fixas.
- Lista de verificación.
- Markdown con encabezados exactos.

### Delimitadores
Separa as túas instrucións do texto que debe analizar:

```text
Contexto do centro:
"""
[texto]
"""
```

---

<!-- .slide: id="demo-metaprompting" class="demo" -->
## Un *prompt* que escribe *prompts*

Pedir o modelo reutilizable en lugar do resultado.

Notas:
**Demo (5 min)**. Calquera *chatbot* (ChatGPT, Gemini ou Claude), nun chat temporal.

1. Pegar o primeiro exemplo da páxina «Exemplos comentados» («Actúa como un asesor pedagóxico… Devólveme SÓ o prompt final»).
2. Ler en voz alta o modelo que devolve: preguntas de aclaración, supostos, encabezados fixos.
3. Abrir un chat novo, pegar o modelo e encher o tema cunha proposta do grupo.
4. Amosar que o modelo fai primeiro as preguntas de aclaración.

**Resultado esperado:** un modelo parecido ao da páxina, e unha actividade que comeza preguntando.
**Se falla:** ensinar a conversa da páxina.
**Mensaxe clave:** para tarefas que se repiten, o modelo vale máis ca o resultado, e pódese converter nun asistente personalizado.

---

<!-- .slide: id="revisar" class="checklist" -->
## Antes de dar por boa unha resposta

- [ ] Pide unha **segunda pasada**: auditoría contra criterios e versión mellorada.
- [ ] Se dubidas entre dúas versións, pide unha **comparación en táboa** por criterios.
- [ ] Esixe que marque os **supostos** e que non invente datos.
- [ ] Comproba **cifras, citas e normativa** na fonte.

---

<!-- .slide: id="no-sabe" class="statement" -->
## Un modelo de linguaxe non sabe cando non sabe

Pode presentar un dato inventado coa mesma seguridade ca un correcto.

Notas:
As instrucións contra a invención reducen o problema, non o eliminan. Por iso a última caixa da diapositiva anterior non é opcional.

---

<!-- .slide: id="razonadores" -->
## Cos modelos que razoan

- Pide unha resposta **directa**.
- Pide **supostos** se falta información.
- Pide unha **xustificación breve** baseada en criterios.
- Non fai falta pedirlles que pensen «paso a paso»: xa o fan.

---

<!-- .slide: id="ejemplos-salida" class="table" -->
## Dar exemplos de saída

| Técnica | Que dás | Cando |
| --- | --- | --- |
| *Zero-shot* | Só a instrución | Tarefas sinxelas |
| *One-shot* | Un exemplo da saída | Formatos concretos (unha ficha, unha pregunta de Moodle) |
| *Few-shot* | Dous ou tres exemplos | Formatos complexos ou delicados (rúbricas) |

Notas:
Os exemplos serven para estilo e formato, non para ensinar contido. Conecta co método dos tests de Moodle: exportar unha pregunta real e dala como exemplo.

---

<!-- .slide: id="practica-reescribir" class="practice" -->
## Reescribe un *prompt* vago

1. Parte de: «Fai unha actividade sobre IA para os meus alumnos.»
2. Engade nivel, tempo, recursos e produto final.
3. Pide preguntas de aclaración e un formato de entrega.
4. Próbao e pide despois unha crítica do propio *prompt*.

**10 minutos.** Produto: o teu *prompt* e a resposta obtida.

Notas:
Se hai tempo, poñer en común dous ou tres *prompts* e comparalos coa táboa da páxina «Exemplos comentados».
