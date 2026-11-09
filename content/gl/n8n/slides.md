---
derived_from:
  es/n8n/slides.md: "33fb9b6b5d8ffb970486b3ad37f5eea957522585"
---

<!-- .slide: id="receta" class="statement" -->
## Unha automatización é unha receita que o ordenador segue sen ti

Un disparador e uns pasos fixos, cada vez que se dan as condicións.

---

<!-- .slide: id="tres-formas" class="cards" -->
## *Chatbot*, automatización e axente

### *Chatbot*
Responde cando lle preguntas.

### Automatización
Sempre os mesmos pasos, sen ti: predicible.

### Axente
Decide el os pasos: flexible e menos predicible.

Notas:
Unha automatización pode incluír un modelo de linguaxe nun paso, e mesmo un axente, pero o esqueleto decídelo ti.

---

<!-- .slide: id="herramientas" class="cards" -->
## Varias ferramentas, as mesmas pezas

### Zapier
Datos nos Estados Unidos; o seu plan gratuíto non admite pasos de IA.

### Make
Plan gratuíto, cos datos na UE se o escolles ao rexistrarte.

### n8n Cloud
Proba gratuíta; os fluxos da súa galería vense sen conta.

### Power Automate
Incluído nas licenzas educativas de Microsoft 365.

Notas:
Prezos e límites, na táboa da páxina, coa súa data de revisión. Os exemplos usan n8n, que ademais se pode instalar nun servidor propio. Para tarefas sinxelas nin sequera fai falla un fluxo: algúns asistentes, como Claude en Chrome, programan tarefas periódicas.

---

<!-- .slide: id="piezas" -->
## As pezas dun fluxo

- **Disparador**: unha hora, un formulario, un RSS, un correo.
- **Nodos**: cada paso recibe datos, traballa e pásalle o resultado ao seguinte.
- **Expresións**: arrastras un dato dun paso anterior e queda como `{{ $json.title }}`.
- **Credenciais**: contas e claves, gardadas á parte.
- Os fluxos son JSON: cópianse e péganse no lenzo.

---

<!-- .slide: id="ejemplo-boe" class="fragments" -->
## As novidades do BOE, resumidas cada luns

1. Cada luns ás 8:00.
2. Ler o RSS de «Educación y enseñanza».
3. Quedar coas da semana.
4. Resumir cada disposición cun modelo de linguaxe.
5. Enviarche un único correo coas ligazóns.

Notas:
Un bo primeiro fluxo: non manexa datos persoais, cada resumo vai coa súa ligazón para comprobalo e, se falla, non pasa nada grave.

**Demo (12 min): un primeiro fluxo, nodo a nodo**. Unha conta de proba de n8n Cloud, creada poucos días antes da sesión.

1. Crear o *Schedule Trigger* e o nodo *RSS Read* co enderezo da canle.
2. Executar o RSS e ensinar os elementos que saen.
3. Engadir o nodo de modelo de linguaxe coas instrucións da páxina e a expresión do título.
4. Enviar o correo a unha conta de probas.

**Resultado esperado:** un correo cos resumos e as súas ligazóns.
**Se falla:** ensinar a saída de cada nodo, que é o que explica como viaxan os datos. Sen conta, percorrer o fluxo de exemplo da galería que se cita na páxina.
**Mensaxe clave:** cada nodo recibe elementos e pásallelos ao seguinte; o esqueleto decídelo ti.

---

<!-- .slide: id="agente-en-flujo" class="statement" -->
## Un axente dentro dun fluxo trae consigo os riscos dos axentes

Ler correos de calquera e poder envialos é a tríade letal completa.

---

<!-- .slide: id="aprobacion" class="statement" -->
## Aprobación humana antes de enviar, publicar ou borrar

n8n detén o fluxo ata que alguén aproba ou rexeita a acción.

---

<!-- .slide: id="que-automatizar" class="table" -->
## Que automatizar nun centro

| Que | Como |
| --- | --- |
| Boletíns, recordatorios, avisos | Adiante |
| Datos do alumnado ou das familias | Só en ferramentas que autorice a administración |
| Decisións sobre o alumnado | Non, sen revisión humana |

---

<!-- .slide: id="ejecuciones" class="statement" -->
## n8n Cloud garda os datos de cada execución

O que pasou por cada nodo queda gardado durante o tempo que fixe o teu plan.

Notas:
O que se envía ao modelo de linguaxe chega ao seu provedor. Un servizo de automatización coa túa conta é, coma un *chatbot* con conta persoal, unha plataforma externa: os datos do alumnado só van a ferramentas que a administración contratase ou autorizase. Tampouco hai nodo para Moodle: conectar coa súa API require un permiso que só dá a administración da aula virtual.
