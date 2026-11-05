---
derived_from:
  es/datos-alumnado/slides.md: "bc9d2d6346e271d1e3d4fc31020f224698990513"
---

<!-- .slide: id="idea-central" class="statement" -->
## A IA case nunca necesita ver o alumnado

Pide o modelo de documento ou o procedemento; anonimiza só cando faga falla o contido.

Notas:
**Mensaxe clave:** antes de preguntarse como anonimizar, a pregunta é se fai falla enviar datos. Na maioría das tarefas, o que achega a IA é redactar, estruturar ou calcular, e iso pídese sen datos reais.

---

<!-- .slide: id="tres-vias" class="cards fragments" -->
## Tres vías, nesta orde

### 1. Sen datos
A IA escribe o modelo de documento, a fórmula ou o procedemento; ti aplícalo no teu equipo.

### 2. Anonimizado de verdade
Só o contido do traballo, sen nada que diga de quen é.

### 3. Datos persoais
Só en ferramentas contratadas ou autorizadas pola administración.

Notas:
A terceira é unha obriga legal: a habilitación para tratar os datos do alumnado é do centro e da administración, non de cada ferramenta que use un docente. Un modelo local, sen conexión, non envía nada fóra, pero os datos seguen suxeitos ás normas de seguridade do centro.

---

<!-- .slide: id="seudonimizar" class="statement" -->
## Cambiar o nome por un código non anonimiza

Mentres exista a táboa que o desfai, seguen sendo datos persoais (RXPD, considerando 26).

Notas:
Pseudonimizar é útil, porque reduce o risco, e o RXPD cítaa como medida de protección. Pero non saca os datos do Regulamento. Só a información anónima, a que non permite identificar ninguén con medios razoables, queda fóra.

---

<!-- .slide: id="que-identifica" class="table" -->
## O que identifica ademais do nome

| Que | Exemplos |
| --- | --- |
| Identificadores | Nome, sinatura, correo, usuario da aula virtual |
| Metadatos | Autor nas propiedades, comentarios, localización dunha foto |
| Cuasiidentificadores | Grupo, idade, localidade, club, o traballo dun familiar |
| Categorías especiais | Saúde, relixión, orixe étnica |
| Voz e cara | Audios e vídeos de exposicións |

---

<!-- .slide: id="singularizacion" class="statement" -->
## Sen nome tamén se identifica

«A única de 4.º B que xoga na selección galega» non necesita nome.

Notas:
O RXPD chámalle a isto singularización: illar unha persoa dentro dun grupo. Nunha clase de vinte, dous ou tres detalles abondan. E hai textos que non se poden anonimizar sen destruílos, como unha redacción autobiográfica: entón non é a vía 2.

---

<!-- .slide: id="demo-quitar-nombre" class="demo" -->
## Demo: quitar o nome non abonda

- Unha redacción inventada, nun procesador de textos e un *chatbot*.
- Fíxate no que non se ve ao abrir o ficheiro.

Notas:
**Demo (10 min)**. Word ou LibreOffice, e calquera *chatbot* nun chat temporal. Material: unha redacción inventada en `.docx`, coma a do apartado «Para practicar» da páxina, co nome na cabeceira, a autora nas propiedades e un comentario da alumna cun dato de saúde.

1. Abrir a redacción e pedirlle ao grupo que diga que datos ve: o nome da cabeceira.
2. Ensinar as propiedades do ficheiro (autora, «modificado por») e o comentario. En Word, coa interface en castelán: Archivo → Información → Comprobar si hay problemas → Inspeccionar documento.
3. En LibreOffice, activar «Eliminar información personal al guardar», gardar e volver abrir: o comentario segue aí, cun autor xenérico. Hai que borralo á parte.
4. Ler o texto en voz alta e pedirlle ao grupo que sinale os cuasiidentificadores e o dato de saúde.
5. Pegar só o texto xa limpo no chat, coa rúbrica, e pedir a valoración por criterios sen nota final.

**Resultado esperado:** o grupo descobre polo menos un dato que non vira (os metadatos ou o comentario), e a retroalimentación sobre a expresión sae igual de útil co texto limpo.
**Se falla:** facer o exercicio «Para practicar» da páxina, en voz alta.
**Mensaxe clave:** o máis seguro é copiar só o texto; o ficheiro leva máis do que se ve.

---

<!-- .slide: id="pasos-anonimizar" class="checklist" -->
## Antes de pedir axuda cun traballo

- [ ] Unha copia, e se abonda co texto, só o texto.
- [ ] Sen cabeceira, sinatura nin identificadores.
- [ ] Sen metadatos nin comentarios.
- [ ] Cuasiidentificadores reescritos, o mínimo.
- [ ] Sen categorías especiais.
- [ ] Fotos recortadas e sen localización.
- [ ] A táboa de códigos, fóra da ferramenta.

Notas:
E un paso que se esquece: nada de servizos en liña para anonimizar, porque para quitar os datos teñen que recibilos.

---

<!-- .slide: id="nota-docente" class="statement" -->
## A IA propón; a nota pómola ti

Unha cualificación que saíse só da ferramenta sería unha decisión automatizada (artigo 22 do RXPD).

Notas:
Ademais, os sistemas que avalían resultados de aprendizaxe son de alto risco para o Regulamento de IA. Detállao a páxina de normativa do bloque de ética.

---

<!-- .slide: id="demo-procedimiento" class="demo" -->
## Demo: a IA escribe a fórmula, non ve as notas

- Unha folla de cálculo con notas inventadas e calquera *chatbot*.
- Fíxate no que recibe a IA: tres filas falsas.

Notas:
**Demo (5 min)**. LibreOffice Calc ou Excel, e calquera *chatbot* nun chat temporal. Material: unha folla cuns vinte alumnos inventados e catro notas cada un.

1. Ensinar a folla completa e dicir que é a que nunca vai saír do equipo.
2. Pegar no chat o *prompt* da páxina: só as columnas e tres filas inventadas.
3. Copiar na folla as fórmulas que devolve e comprobar unha fila a man.

**Resultado esperado:** dúas fórmulas que funcionan sobre a folla real sen que a IA a vise.
**Se falla:** se a fórmula dá erro, pegar a mensaxe de erro no chat; se non hai rede, ensinar a fórmula xa preparada.
**Mensaxe clave:** pedir o procedemento en lugar do resultado é a vía máis segura, e a que máis se esquece.

---

<!-- .slide: id="prompt-procedimiento" class="prompt" -->
## As columnas e tres filas inventadas abondan

```text
Teño unha folla con estas columnas: alumno, proba_1, proba_2, proxecto, caderno.
Estas tres filas son inventadas, só para que vexas o formato: […]
Escribe a fórmula de LibreOffice Calc para a media ponderada (30 %, 30 %, 30 % e 10 %)
e outra que conte cantos alumnos teñen menos de 5 en cada proba.
```

Notas:
A versión completa, coas tres filas, está na páxina.

---

<!-- .slide: id="demo-plantilla" class="demo" -->
## Demo: un modelo de documento con ocos

- Un informe para as familias, con marcadores que se enchen en local.
- Fíxate en que a IA só achega a redacción.

Notas:
**Demo (5 min)**. Calquera *chatbot* nun chat temporal e un procesador de textos. Material: unha táboa inventada cos datos de cinco alumnos (nome, grupo, fortalezas, aspectos que mellorar, proposta).

1. Pedirlle ao chat un informe de titoría de primeira avaliación cos marcadores `[NOME]`, `[GRUPO]`, `[FORTALEZAS]`, `[A_MELLORAR]` e `[PROPOSTA]`.
2. Pegar o modelo no procesador de textos.
3. Encher un informe con buscar e substituír, ou todos coa combinación de correspondencia a partir da táboa.

**Resultado esperado:** un informe ben redactado con datos que non saíron do equipo.
**Se falla:** ensinar un modelo xa xerado e enchelo.
**Mensaxe clave:** a IA achega a redacción; os datos de cada alumno pómolos ti.

---

<!-- .slide: id="demo-examen" class="demo" -->
## Demo: un exame escrito a man

- A foto dun exame inventado, cuberto a man.
- Fíxate na cabeceira, na sinatura e na localización da foto.

Notas:
**Demo (5 min)**. Un móbil, o visor de fotos do ordenador e un *chatbot* que admita imaxes. Material: un exame inventado cuberto a man cun nome inventado, fotografado coa localización da cámara activada.

1. Ensinar nas propiedades da foto a localización que gardou a cámara.
2. Recortar a cabeceira e a sinatura, e compartir ou exportar a foto sen localización (no iPhone, Opciones → desactivar Ubicación ao compartir).
3. Subir a foto recortada ao chat e pedir que transcriba as respostas antes de valoralas.
4. Comparar a transcrición co orixinal: os erros de lectura vense aí, antes da corrección.

**Resultado esperado:** unha transcrición revisable e unha valoración por pregunta, sen nome, sinatura nin localización.
**Se falla:** ensinar a foto recortada e explicar os pasos.
**Mensaxe clave:** a foto leva máis do que se ve, e a transcrición compróbase antes de fiarse da corrección.

---

<!-- .slide: id="casos-anonimizables" class="table" -->
## Casos típicos e a súa vía

| Caso | Vía | Que facer |
| --- | --- | --- |
| Redacción ou traballo | 2 | Texto anonimizado e rúbrica |
| Exame a man | 2 | Foto recortada, sen localización |
| Notas dun grupo | 1 | A fórmula, cunha mostra inventada |
| Informes e familias | 1 | Modelo de documento con ocos |
| Necesidades específicas | 1 | A necesidade didáctica, non o diagnóstico |

Notas:
Para adaptar un material, «necesita frases curtas, vocabulario básico e unha idea por parágrafo» funciona igual de ben que nomear un trastorno, e non revela un dato de saúde. Na páxina están os oito casos, co código dos proxectos de FP.

---

<!-- .slide: id="sin-anonimizacion" class="bullets" -->
## Onde non hai anonimización posible

- **Gravacións**: a voz e a cara identifican; só ferramentas contratadas, ou transcrición no propio equipo.
- **Convivencia e expedientes**: os feitos identifican as persoas; só casos inventados.
- **Textos autobiográficos**: se ao limpalos non queda nada, non é a vía 2.

---

<!-- .slide: id="practica-fragmento" class="practice" -->
## Que quitarías?

1. Le o fragmento de redacción do apartado «Para practicar» da páxina.
2. Anota todo o que quitarías ou reescribirías para pedir retroalimentación sobre a expresión.
3. Compara a túa lista coa doutra persoa e despois coa solución.

10 minutos, en parellas.

Notas:
Na posta en común, buscar os tres tipos de dato: o de saúde (a diabete e o glicómetro), a singularización («a única de 4.º B…») e os cuasiidentificadores (Moaña, o equipo cadete feminino, o traballo do pai). Preguntar ao final que non se ve no fragmento: a cabeceira, as propiedades e os comentarios se chegou como ficheiro.
