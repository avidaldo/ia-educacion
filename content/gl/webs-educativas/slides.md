---
derived_from:
  es/webs-educativas/slides.md: "2a2babba44fe60eee9dd7af86401843c8bb28492"
---

<!-- .slide: id="sin-programar" class="statement" -->
## Unha páxina interactiva para a clase, sen saber programar

Simuladores, repasos, liñas temporais, xogos: un único ficheiro HTML.

---

<!-- .slide: id="ejemplos" class="fragments" -->
## O que funciona ben

- Un simulador sinxelo.
- Un repaso con pistas e corrección inmediata.
- Unha liña temporal ou un mapa que se explora con clics.
- Unha calculadora da materia.
- Un xogo de vocabulario ou de emparellar conceptos.

---

<!-- .slide: id="donde-crear" class="table dense" -->
## Onde crealas

| Ferramenta | Compartir o resultado |
| --- | --- |
| Claude (Artifacts) | Quen a abra precisa conta de Claude (18 anos) |
| Gemini (Canvas) | Ligazón pública; quen a teña pode editar os datos da aplicación |
| ChatGPT (Canvas, Sites) | Sites, en Plus e Pro, publícaa cun enderezo propio; se non, descargar o código |

Notas:
En todos os casos, o máis robusto é pedir un único ficheiro HTML, descargalo e publicalo ti onde xa entra o alumnado.

---

<!-- .slide: id="prompt-pagina" class="prompt dense" -->
## Como pedila

```text
Crea unha páxina web interactiva nun único ficheiro HTML, sen dependencias externas,
para [nivel] sobre [tema].
Debe permitir: [o que fará o alumnado, paso a paso].
Deseño lexible no móbil e no proxector, bo contraste, manexable co teclado.
Non recollas nin envíes ningún dato do usuario.
```

---

<!-- .slide: id="demo-pagina" class="demo" -->
## Do encargo a Moodle

Crear, iterar e publicar unha páxina en dez minutos.

Notas:
**Demo (10 min)**. Gemini (Canvas) ou Claude, e un curso de probas de Moodle.

1. Pedir unha páxina co *prompt* da páxina e un tema proposto polo grupo.
2. Probala e pedir dous cambios concretos («engade unha pista en cada pregunta»).
3. Descargar o ficheiro HTML.
4. Crear un recurso Páxina en Moodle e pegar o código na vista de código.

**Resultado esperado:** a páxina funciona dentro de Moodle.
**Se falla:** se Moodle borra o código, subir o ficheiro como recurso Ficheiro.
**Mensaxe clave:** o contido revísase como calquera material; o deseño é o doado.

---

<!-- .slide: id="moodle" class="table" -->
## Publicala en Moodle

| Opción | Cando |
| --- | --- |
| Recurso Páxina, pegando o HTML | O máis sinxelo |
| Área de texto e medios cun `<iframe>` | Para vela na portada do curso |
| Recurso Ficheiro co `.html` | Se Moodle borra o código |
| Recurso URL | Se xa está publicada fóra |

Notas:
Moodle limpa o HTML na maioría dos sitios (os foros, por exemplo), pero non no recurso Páxina nin nas descricións como a área de texto e medios, agás que a administración activase a limpeza en todo o sitio.

---

<!-- .slide: id="fuera" class="two-col" -->
## Publicala fóra de Moodle

### Netlify Drop
Arrastras o cartafol e obtés un enderezo público.

### GitHub Pages
Gratuíto e estable; así se publica esta web.

---

<!-- .slide: id="revisar" class="checklist" -->
## Antes de publicar

- [ ] Contido correcto.
- [ ] Funciona no móbil, no ordenador e no proxector.
- [ ] Accesible: contraste, teclado, textos alternativos.
- [ ] Non recolle datos nin carga recursos doutras webs.
- [ ] Imaxes propias ou con licenza.

---

<!-- .slide: id="presentaciones" class="section" -->
## Presentacións

---

<!-- .slide: id="contenido-primero" class="statement" -->
## Primeiro o esquema; despois o deseño

Pedir de golpe «unha presentación sobre X» dá diapositivas vistosas con contido xenérico.

---

<!-- .slide: id="tres-caminos" class="cards" -->
## Tres camiños

### *Chatbot*
Gemini (Canvas, a Google Slides), cadernos, ChatGPT e Claude (PowerPoint).

### Ferramenta especializada
Gamma ou Canva: o resultado máis vistoso, na súa plataforma.

### Texto e estilo
Markdown convertido con Marp, Slidev ou reveal.js: contido reutilizable, deseño fixo.

---

<!-- .slide: id="practica-presentacion" class="practice" -->
## Do esquema ás diapositivas

1. Pide un esquema de dez diapositivas sobre un tema da túa materia.
2. Corríxeo: datos, orde, o que sobra.
3. Xera as diapositivas por un dos tres camiños.
4. Revisa o que cambiou entre o esquema e o resultado.

**15 minutos.** Produto: unha presentación con contido revisado.
