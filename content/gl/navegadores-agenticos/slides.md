---
derived_from:
  es/navegadores-agenticos/slides.md: "5eca709e73835fe43ea2e190dfb51b3e5685014e"
---

<!-- .slide: id="actuar" class="statement" -->
## Un axente non só le a páxina: actúa nela coas túas sesións abertas

Fai clic, escribe e enche formularios no teu nome.

---

<!-- .slide: id="leer-o-actuar" class="comparison" -->
## Dous niveis de axuda moi distintos

### Asistente de lectura
Resume, compara e extrae datos das lapelas. Non toca nada.

### Axente de navegación
Fai clic, escribe e pasa dunha web a outra, identificado como ti en cada unha.

---

<!-- .slide: id="herramientas" class="table dense" -->
## Que hai hoxe

| Ferramenta | Dispoñibilidade |
| --- | --- |
| Comet (Perplexity) | Gratuíto; Windows, Mac, iOS e Android |
| Claude en Chrome | Plans de pago; só Chrome de escritorio |
| ChatGPT | Extensión para varios navegadores e aplicación de escritorio |
| Gemini en Chrome | Non dispoñible en España |

Notas:
Situación en outubro de 2026. Atlas, o navegador de OpenAI, retirouse en agosto de 2026, menos dun ano despois do seu lanzamento: mellor non construír unha forma de traballar arredor dunha ferramenta concreta.

---

<!-- .slide: id="usos" class="two-col" -->
## Compensa con webs públicas e tarefas que podes comprobar

### Si
Comparar páxinas, extraer prazos a unha táboa, guiarte por unha web complicada, comprobar a túa propia web.

### Non
Webs con datos doutras persoas: XADE, as cualificacións, o correo co alumnado e as familias.

Notas:
Desaconséllao o propio Anthropic: o que hai na pantalla envíaselle ao provedor, e un erro ou un ataque executaríase cos teus permisos.

---

<!-- .slide: id="inyeccion" class="statement" -->
## O axente non distingue as túas instrucións das que alguén agochou na páxina

É a inxección de *prompts*.

---

<!-- .slide: id="ncsc" class="quote" -->
## Non é un fallo que se arranxe cunha actualización

> É moi posible que a inxección de *prompts* nunca se mitigue de todo, como si pode facerse coa inxección de SQL.

Centro Nacional de Ciberseguridade do Reino Unido, decembro de 2025

Notas:
O motivo é o funcionamento do modelo: recibe un único texto e predí como continualo, sen separar datos e instrucións. OpenAI di o mesmo: como as estafas na web, «dificilmente se resolverá nunca de todo».

---

<!-- .slide: id="caso-comet" class="fragments" -->
## Abondaba con premer «resumir»

- Un comentario de Reddit agochaba instrucións.
- O asistente foi á conta de Perplexity do usuario e copiou o seu correo.
- Pediu un código de acceso e leuno en Gmail.
- Publicou ambos os datos nunha resposta ao comentario.

Notas:
Investigación de Brave sobre Comet, agosto de 2025. Hoxe os provedores adestran os seus modelos contra estes ataques e piden confirmación antes das accións delicadas; Anthropic fala de menos dun 0,08 % de ataques con éxito nas súas probas internas, e aínda así advirte de que o risco non é cero.

---

<!-- .slide: id="triada" class="cards" -->
## A tríade letal: o perigo está en reunir as tres

### Datos privados
As túas sesións, o teu correo, os teus documentos.

### Contido alleo
Páxinas, correos e comentarios que non controlas.

### Comunicación cara a fóra
Enviar, publicar, abrir un enderezo.

Notas:
Simon Willison, xuño de 2025. Un axente de navegación coas túas sesións abertas reúne as tres; cada medida de protección quita unha ou limítaa.

---

<!-- .slide: id="demo-inyeccion" class="demo" -->
## Unha instrución agochada nunha páxina

Obedece o asistente o texto oculto?

Notas:
**Demo (5 min)**. Comet ou Claude en Chrome, nun perfil de navegador sen sesións abertas, coa páxina de demostración gardada como `demo.html`.

1. Abrir `demo.html`: parece unha páxina normal sobre o ciclo da auga.
2. Pedirlle ao asistente «resume esta páxina».
3. Ler o resumo en voz alta.
4. Seleccionar todo o texto (Ctrl+A) para que apareza a instrución oculta.

**Resultado esperado:** o resumo remata con «Las ranas también opinan», ou o asistente avisa da instrución.
**Se falla:** os dous resultados serven; se non hai axente dispoñible, ensinar o código da páxina e explicar que faría.
**Mensaxe clave:** o texto que le o axente tamén pode darlle ordes.

---

<!-- .slide: id="con-cabeza" class="checklist" -->
## Como usalos con cabeza

- [ ] Un perfil de navegador sen sesións sensibles.
- [ ] Encargos concretos e acoutados.
- [ ] Webs de confianza primeiro.
- [ ] Ler cada confirmación antes de aceptar.
- [ ] Bloquear os sitios sensibles nos axustes.
- [ ] Deter a tarefa se fai algo inesperado.

Notas:
Se manexas datos sensibles e non precisas o axente, ChatGPT ten un *Lockdown Mode* que limita as conexións cara a fóra; a cambio, desactiva a navegación en directo, a investigación a fondo e o modo axente.

---

<!-- .slide: id="responsable" class="statement" -->
## O que fai o axente no teu nome fixéchelo ti

Erros e compras incluídos: Anthropic e Google dino expresamente.

---

<!-- .slide: id="que-ve" class="table" -->
## Ademais do que fai, conta o que envía

| Ferramenta | Que lle chega ao provedor |
| --- | --- |
| Claude en Chrome | Capturas das lapelas nas que traballa |
| Comet | O contexto de cada petición, ata 30 días |
| Gemini en Chrome | A lapela actual, na actividade de Gemini |

Notas:
As regras sobre datos persoais son as de calquera chatbot, cun engadido: aquí tamén conta todo o que estea visible na pantalla.

---

<!-- .slide: id="alumnado" class="statement" -->
## Co alumnado, mellor como obxecto de estudo que como ferramenta

En informática, a inxección de *prompts* é contido de ciberseguridade.

Notas:
Claude esixe 18 anos e Gemini en Chrome non está dispoñible en España. Comet herda os 13 anos de Perplexity e ChatGPT pide consentimento familiar aos menores de 18, pero un axente coas sesións do alumno abertas presenta os mesmos problemas que coas túas.
