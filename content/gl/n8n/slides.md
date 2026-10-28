---
derived_from:
  es/n8n/slides.md: "1804c0d055df2e30350b0f3ffe252288f28465e9"
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

<!-- .slide: id="cloud-o-local" class="two-col" -->
## n8n: na nube ou no teu equipo

### n8n Cloud
De pago (desde uns 20 € ao mes), sen instalación, cos datos na UE.

### Instalado por ti
Gratuíto, no teu equipo; funciona mentres estea aceso.

Notas:
Licenza *fair-code*: de balde para uso interno, persoal ou non comercial, pero non se pode ofrecer como servizo a terceiros. Non é software libre en sentido estrito.

---

<!-- .slide: id="piezas" -->
## As pezas dun fluxo

- **Disparador**: unha hora, un formulario, un RSS, un correo.
- **Nodos**: cada paso recibe datos, traballa e pásalle o resultado ao seguinte.
- **Expresións**: `{{ $json.title }}` usa un dato dun paso anterior.
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

---

<!-- .slide: id="demo-boe" class="demo" -->
## Un primeiro fluxo, nodo a nodo

O boletín do BOE, vendo que sae de cada paso.

Notas:
**Demo (12 min)**. n8n instalado en local con Docker, ou unha proba de n8n Cloud.

1. Crear o *Schedule Trigger* e o nodo *RSS Read* co enderezo da canle.
2. Executar o RSS e ensinar os elementos que saen.
3. Engadir o nodo de modelo de linguaxe coas instrucións da páxina e a expresión do título.
4. Enviar o correo a unha conta de probas.

**Resultado esperado:** un correo cos resumos e as súas ligazóns.
**Se falla:** ensinar a saída de cada nodo, que é o que explica como viaxan os datos.
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
| Datos do alumnado ou das familias | Con moito coidado e con autorización do centro |
| Decisións sobre o alumnado | Non, sen revisión humana |

---

<!-- .slide: id="ejecuciones" class="statement" -->
## n8n garda os datos de cada execución

O que pasou por cada nodo queda gardado: convén borrar as execucións antigas automaticamente.

Notas:
O que se envía ao modelo de linguaxe chega ao seu provedor, e a responsabilidade do tratamento é do centro. Tampouco hai nodo para Moodle: conectar coa súa API require un permiso que só dá a administración da aula virtual.

---

<!-- .slide: id="alternativas" -->
## Outras opcións

- **Zapier** e **Make**: na nube, sen instalación propia.
- **Power Automate**, se o centro traballa con Microsoft 365.
- Para tarefas sinxelas, as tarefas programadas dalgúns asistentes, como Claude en Chrome.
