---
title: Webs educativas
description: Crear con IA pequenas páxinas interactivas para a clase (simuladores, repasos, xogos) e publicalas onde o alumnado as poida usar.
derived_from:
  es/webs-educativas/index.md: "738bad2789a5baa7ac8e4bee0f328d088d2bf28b"
---

## Que se pode crear

Cunha descrición en linguaxe natural, os *chatbots* xeran **páxinas web interactivas** que funcionan no navegador: non fai falta saber programar para obter un primeiro resultado útil. Algúns exemplos que funcionan ben na clase:

- un simulador sinxelo (un circuíto, un plano inclinado, unha economía con dúas variables);
- un repaso interactivo con preguntas, pistas e corrección inmediata;
- unha liña temporal ou un mapa conceptual que se explora con clics;
- unha calculadora específica da materia (escalas, porcentaxes, unidades);
- un xogo de vocabulario ou de emparellar conceptos.

Unha páxina así é un único ficheiro HTML co seu deseño e o seu código. Cando o proxecto medra (varias pantallas, datos gardados, usuarios), xa non é unha páxina senón unha aplicación: trátase no módulo de *vibe coding*.<!-- TODO: enlazar ../vibe-coding/index.md cuando exista -->

## Onde crealas

| Ferramenta | Como se crea | Compartir o resultado |
| --- | --- | --- |
| Claude | Os Artifacts mostran a páxina funcionando xunto ao chat | Cunha ligazón, pero **quen a abra precisa conta de Claude** (e Claude esixe 18 anos). Para o alumnado, descarga o código e publícao noutro sitio |
| Gemini | Canvas, tamén no plan gratuíto | Cunha ligazón pública que se abre en gemini.google.com. Segundo Google, quen teña a ligazón pode ver e editar os datos asociados á aplicación |
| ChatGPT | Canvas para código e, desde GPT-6, respostas con elementos interactivos | Descarga o código para publicalo fóra de ChatGPT |

En todos os casos, o camiño máis robusto é o mesmo: **pedir a páxina como un único ficheiro HTML, descargalo e publicalo ti** onde o alumnado xa entra.

## Como pedila

```text
Crea unha páxina web interactiva nun único ficheiro HTML, sen dependencias externas
(nada de CDN, fontes nin imaxes doutras webs), para [nivel] sobre [tema].

Debe permitir: [o que fará o alumnado, paso a paso].
Deseño: claro e lexible no móbil e no proxector, con bo contraste,
manexable co teclado e con textos alternativos nas imaxes.
Lingua: [galego / castelán].
Non recollas nin envíes ningún dato do usuario.
Ao final, explica en tres liñas como se usa.
```

Despois, itera como con calquera outro texto: proba a páxina, describe o que falla ou o que queres cambiar («o botón de comprobar non reinicia as respostas», «engade unha pista en cada pregunta») e pide a versión corrixida completa.

> [!TIP]
> **Contido primeiro, deseño despois**
> Se a páxina explica algo, revisa primeiro o contido (en texto, ou nun diagrama Mermaid) e pide despois a páxina con ese contido xa validado. Mesturar nunha soa petición o razoamento e o deseño aumenta os erros, como se explica en [Técnicas avanzadas](../prompts/avanzado.md#separar-contenido-y-diseño).

## Publicala en Moodle

| Opción | Como | Cando usala |
| --- | --- | --- |
| Recurso **Páxina** | Pega o HTML na vista de código do editor | O máis sinxelo para unha páxina autocontida |
| **Área de texto e medios** (antes «Etiqueta») | Insire un `<iframe>` que apunte á páxina publicada noutro sitio | Para que se vexa directamente na portada do curso |
| Recurso **Ficheiro** | Sobe o ficheiro `.html` | Se prefires que se abra nunha lapela á parte |
| Recurso **URL** | Liga a páxina publicada fóra de Moodle | Se xa está aloxada noutra web |

Un `<iframe>` ten esta forma:

```html
<iframe src="https://direccion-de-tu-pagina" width="100%" height="600" title="Simulador de circuitos"></iframe>
```

> [!NOTE]
> **Por que ás veces Moodle borra o código**
> Moodle «limpa» o HTML que se escribe na maioría dos sitios (por exemplo, nos foros) e elimina os `<iframe>` e o código. O contido dun recurso **Páxina** e as descricións de recursos e actividades, como a área de texto e medios, móstranse sen limpar, así que aí funcionan. A excepción é que a administración do sitio activase a limpeza de contido en todo o sitio: nese caso, a opción que queda é o recurso **Ficheiro** ou unha ligazón.

## Publicala fóra de Moodle

- **[Netlify Drop](https://app.netlify.com/drop)**: arrastras o cartafol coa páxina e obtés un enderezo público en segundos.
- **[GitHub Pages](https://pages.github.com)**: gratuíto e estable para quen xa usa GitHub; é como se publica esta mesma web.
- **Google Sites** permite inserir código HTML nunha páxina do sitio.

Unha vez publicada, o enderezo pódese ligar desde Moodle ou inserir cun `<iframe>`.

## Antes de publicala

- [ ] **O contido é correcto**: revisa datos, fórmulas e textos como revisarías calquera material.
- [ ] **Funciona** no móbil, no ordenador da aula e no proxector.
- [ ] **É accesible**: contraste suficiente, manexable co teclado, textos alternativos.
- [ ] **Non recolle datos** nin carga recursos doutras webs (fontes, analíticas, CDN), que enviarían información do alumnado a terceiros.
- [ ] **As imaxes** son propias ou teñen unha licenza que permita usalas.
