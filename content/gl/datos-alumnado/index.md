---
title: Datos do alumnado
description: Como usar a IA para corrixir, analizar notas ou redactar informes sen expoñer datos do alumnado, cando abonda con anonimizar e que di a lei en cada caso típico.
derived_from:
  es/datos-alumnado/index.md: "a147d2a49a3a1df74e6fc3600ab19b9b95e8ab6a"
---

> [!NOTE]
> **Unha lectura docente, non asesoramento xurídico**
> Esta páxina aplica a casos típicos o que se explica en [Normativa](../etica-legal/normativa.md#protección-de-datos), co mesmo criterio que o resto do bloque: cada indicación di se é unha **obriga legal**, unha **recomendación institucional** ou unha **boa práctica**. Ante un caso concreto, a referencia é a persoa delegada de protección de datos da Consellería.

## A pregunta previa: necesita a IA os datos?

Antes de anonimizar nada convén preguntarse se a IA necesita ver o alumnado. Case nunca: na maioría das tarefas o que achega é redactar, estruturar ou calcular, e iso pódese pedir sen datos reais. Hai tres vías, e próbanse nesta orde:

1. **Sen datos do alumnado.** A IA escribe o modelo de documento, a fórmula ou o procedemento, e ti aplícalo aos datos no teu equipo. Serve para informes, comunicacións ás familias, análise de notas e rúbricas.
2. **Co traballo do alumno, anonimizado de verdade.** Cando o que fai falla é o contido (unha redacción, as respostas dun exame), envíase só ese contido, sen nada que permita saber de quen é. É máis difícil do que parece, como se ve na sección seguinte.
3. **Con datos persoais.** Só en ferramentas que a administración educativa contratase ou autorizase para ese uso (**obriga legal**; o porqué está en [quen pode tratar os datos do alumnado](../etica-legal/normativa.md#quién-puede-tratar-los-datos-del-alumnado)). En Galicia, ademais, o protocolo de protección de datos da Consellería pídelles aos centros que usen só as ferramentas que ela proporciona e que non usen plataformas externas non autorizadas (**recomendación institucional**).[^protocolo] Mentres non haxa entre elas unha ferramenta de IA para este uso (o catálogo de sistemas homologados que prevé a Lei de educación dixital aínda non existe), esta vía está pechada para a IA xerativa.

Un modelo executado no teu propio equipo, sen conexión, non envía nada fóra ([a demostración](../etica-legal/index.md#privacidad-la-regla-práctica)). Pero os datos seguen sendo datos do alumnado, suxeitos ás normas de seguridade e confidencialidade do centro.

## Quitar o nome non abonda

Cambiar o nome por un código (`R-07`) mentres gardas a lista que di quen é cada código é **pseudonimizar**, non anonimizar. Para o RXPD, os datos pseudonimizados «deben considerarse información sobre una persona física identificable»: seguen sendo datos persoais. Só a información anónima, a que non permite identificar ninguén cos medios que razoablemente poidan usar «el responsable del tratamiento o cualquier otra persona», queda fóra do Regulamento.[^rgpd] Pseudonimizar segue sendo útil, porque reduce o risco, e o RXPD cítaa como medida de protección, pero non saca os datos do Regulamento. O detalle está en [Anonimizar e pseudonimizar](../etica-legal/normativa.md#anonimizar-y-seudonimizar).

Tampouco abonda con mirar o nome, porque o traballo enteiro fala de quen o fixo. Para o Tribunal de Xustiza da UE, as respostas dun exame e as anotacións de quen o corrixe son datos persoais, e se o exame está escrito a man conteñen, ademais, «información sobre su escritura».[^nowak] Isto é o que pode identificar un alumno ou unha alumna nun traballo:

| Que | Exemplos |
| --- | --- |
| Identificadores directos | Nome, sinatura, foto, correo, usuario da aula virtual, número de lista |
| Metadatos do ficheiro | Autor e «modificado por» nas propiedades, comentarios, control de cambios, a localización dunha foto |
| Cuasiidentificadores | Grupo, idade, localidade, club, o traballo dun familiar: por separado non din nada, pero xuntos sinalan unha persoa |
| Categorías especiais | Saúde, relixión, orixe étnica, orientación sexual: aínda que non identifiquen, son os datos con máis protección |
| A voz e a cara | Audios e vídeos de exposicións orais |

Os cuasiidentificadores son os que máis se escapan. O RXPD conta a **singularización** entre os medios para identificar alguén:[^rgpd] illar unha persoa dentro dun grupo sen saber o seu nome. Nunha clase de vinte, «a única de 4.º B que xoga na selección galega» non necesita nome.

O que conta é o que pode deducir quen recibe o texto. O Tribunal de Xustiza precisou que, para quen recibe datos pseudonimizados sen a táboa que os desfai, poden non ser datos persoais, pero só se non pode atribuírllos razoablemente a ninguén ([Anonimizar e pseudonimizar](../etica-legal/normativa.md#anonimizar-y-seudonimizar)). Por iso a vía 2 esixe quitar todo o que permita recoñecer a persoa, non só o nome.

E hai textos que non se poden anonimizar sen destruílos: unha redacción autobiográfica chea de detalles persoais segue sendo recoñecible por moito que se quite. Entón non é a vía 2, e o que queda é a 1 ou a 3.

## Como anonimizar un traballo

1. **Traballa sobre unha copia**, nunca sobre o ficheiro que entregou o alumno.
2. **Se abonda co texto, cópiao e pégao no chat**: así non viaxa ningún metadato. Se tes que subir o ficheiro, límpao antes (paso 4).
3. **Quita a cabeceira, a sinatura e os identificadores**: nome, usuario, correo, número de lista.
4. **Limpa os metadatos e os comentarios.** As rutas están na interface en castelán:
   - En Word: Archivo → Información → Comprobar si hay problemas → Inspeccionar documento, e quita «Comentarios, revisiones, versiones y anotaciones» e «Propiedades del documento e información personal».[^word]
   - En LibreOffice, a opción «Eliminar información personal al guardar» (Herramientas → Opciones → LibreOffice → Seguridad → Opciones) quita os datos de autoría e substitúe o autor dos comentarios por un valor xenérico, pero **non borra os comentarios**: hai que eliminalos á parte.[^libreoffice]
5. **Reescribe os cuasiidentificadores** que non fagan falla para a tarefa: «o pavillón de Moaña» pasa a «o pavillón», e «a única de 4.º B que…» desaparece. Cambia o mínimo: se vas corrixir a expresión, o que corrixes ten que seguir aí.
6. **Quita as categorías especiais**: un diagnóstico, unha crenza, unha situación familiar.
7. **Nas fotos**, recorta a cabeceira e a sinatura, e fíxate na localización: a cámara do móbil pode gardar onde se fixo a foto. No iPhone pódese compartir sen ela (na folla de compartir, Opciones → desactivar Ubicación) ou impedir que a cámara a garde (Ajustes → Privacidad y seguridad → Localización → Cámara → Nunca).[^apple] En Android depende da app de cámara de cada fabricante. O máis seguro é fotografar os traballos coa localización da cámara desactivada.
8. **Garda a táboa código → alumno fóra da ferramenta**, no teu equipo ou no espazo do centro.
9. **Non uses un servizo en liña para anonimizar**: para quitar os datos, ese servizo ten que recibilos.

> [!IMPORTANT]
> **Anonimizar non sempre é posible**
> A AEPD e o Supervisor Europeo de Protección de Datos recollen dez malentendidos frecuentes sobre a anonimización (**recomendación institucional**).[^malentendidos] Tres afectan directamente a un docente. Pseudonimizar non é anonimizar. Os datos non sempre se poden anonimizar, entre outros casos cando «el número total de posibles individuos (“universo de sujetos”) es demasiado reducido», e un grupo-clase sono. E non se pode automatizar de todo: atopar os identificadores directos «es algo trivial», pero os indirectos «no siempre son obvios».

## Casos típicos

| Caso | Vía | Que facer |
| --- | --- | --- |
| Retroalimentación sobre unha redacción ou un traballo | 2 | Pegar o texto anonimizado coa rúbrica; a nota pómola ti |
| Corrixir un exame escrito a man | 2 | Foto recortada, sen cabeceira nin localización |
| Analizar as notas dun grupo | 1 | A IA escribe a fórmula a partir dunha mostra inventada |
| Informes e comunicacións ás familias | 1 | Modelo de documento con ocos que enches no teu equipo |
| Adaptar materiais para alumnado con necesidades específicas | 1 | Describir a necesidade didáctica, non o diagnóstico nin a persoa |
| Revisar o código dun proxecto de FP | 2 | Quitar autores, correos e nomes dos ficheiros |
| Exposicións orais gravadas | 3 | A voz e a cara identifican: só ferramentas contratadas, ou un modelo local |
| Convivencia e expedientes disciplinarios | 1 | Só casos inventados |

### Retroalimentación sobre unha redacción ou un traballo

Anonimiza o texto cos pasos anteriores e pégao xunto coa rúbrica. Pide a valoración por criterios, cunha cita do texto que a xustifique, e unha suxestión de mellora para o alumno:

```text
Es profesor de [materia] en [curso]. Pásoche unha redacción e a rúbrica coa que se avalía.
Para cada criterio, dime que nivel lle asignarías, cunha cita breve do texto que o xustifique,
e unha suxestión concreta de mellora dirixida ao alumno. Non poñas a nota final: decídoa eu.

[rúbrica]

[texto anonimizado]
```

**Obriga legal.** A IA propón e a nota decídela ti, revisando o traballo. Unha cualificación que saíse só da ferramenta sería unha decisión automatizada (artigo 22 do RXPD), e os sistemas que avalían resultados de aprendizaxe son de alto risco para o Regulamento de IA: explícao [Alto risco en educación](../etica-legal/normativa.md#alto-riesgo-en-educación).

### Corrixir un exame escrito a man

Os modelos que admiten imaxes len a letra manuscrita, aínda que convén comprobar a súa transcrición antes de fiarse da corrección. Antes de subila, recorta a cabeceira (nome, grupo, sinatura) e comproba a localización (paso 7). Se o exame ten preguntas persoais ou datos de saúde, non é a vía 2.

### Analizar as notas dun grupo

A IA non necesita as notas para escribir a fórmula: abóndalle coas columnas e unhas filas inventadas. Despois copias a fórmula na túa folla, que nunca sae do teu equipo.

```text
Teño unha folla de cálculo con estas columnas: alumno, proba_1, proba_2, proxecto, caderno.
Estas tres filas son inventadas, só para que vexas o formato:
Alumno A, 6.5, 7.0, 8.0, 9
Alumno B, 4.0, 5.5, 6.0, 5
Alumno C, 3.0, 4.5, 5.0, 5
Escribe a fórmula de LibreOffice Calc para a nota media ponderada (30 %, 30 %, 30 % e 10 %)
e outra que conte cantos alumnos teñen menos de 5 en cada proba.
```

É a vía máis segura e a que máis se esquece: pedir o **procedemento** en lugar do resultado. Funciona igual cunha macro, un script ou unha táboa dinámica.

### Informes e comunicacións ás familias

Pide o modelo de documento con marcadores (`[NOME]`, `[FORTALEZAS]`, `[A_MELLORAR]`) e éncheo no teu equipo, a man ou coa combinación de correspondencia do procesador de textos. A IA achega a redacción; os datos de cada alumno non saen do teu equipo.

### Adaptar materiais para alumnado con necesidades específicas

Describe a necesidade didáctica, non o diagnóstico nin a persoa: «adapta este texto para alguén que necesita frases curtas, vocabulario básico e unha idea por parágrafo» funciona igual de ben que nomear un trastorno, e non revela un dato de saúde. **Obriga legal**: os datos de saúde son unha [categoría especialmente protexida](../etica-legal/normativa.md#datos-especialmente-protegidos). E o expediente de orientación non se trata «en ningún caso» con ferramentas que non sexan da Consellería, segundo o seu protocolo (**recomendación institucional**).[^protocolo-orientacion]

### Revisar o código dun proxecto de FP

Un repositorio identifica o seu autor en varios sitios: o nome e o correo de cada *commit*, os comentarios de cabeceira dos ficheiros e, ás veces, as rutas (`/home/<usuario>/…`). Para pedir unha revisión, copia só os ficheiros que importan e limpa eses datos; non subas o repositorio enteiro.

### Exposicións orais gravadas

A voz e a cara identifican a persoa, e non hai forma razoable de anonimizalas. Unha gravación só pode ir a unha ferramenta contratada pola administración. Se o que necesitas é a transcrición, hai modelos de transcrición que funcionan no propio equipo, sen conexión.

### Convivencia e expedientes disciplinarios

Son os datos máis delicados do centro, e case nunca é posible anonimizalos: os feitos identifican as persoas. Se queres axuda para redactar, pide un modelo de escrito a partir dun caso inventado e adáptao ti.

## Para practicar

Este fragmento dunha redacción é inventado. Antes de ler a solución, anota todo o que quitarías ou cambiarías para pedir retroalimentación sobre a expresión escrita:

> O lugar máis importante para min é o pavillón municipal de Moaña, onde adestro co equipo cadete feminino de balonmán. Desde que me diagnosticaron diabete tipo 1 o ano pasado, a miña nai vén a todos os adestramentos co glicómetro. Este ano son a única de 4.º B que xoga na selección galega, e cando volvo das concentracións o pavillón é o sitio onde me sinto na casa, aínda que o meu pai, que traballa de noite na conserveira, non poida vir.

O que había que tocar:

- **A saúde**: «diagnosticaron diabete tipo 1» e o glicómetro. É unha categoría especial, e non fai falla para valorar a expresión.
- **A singularización**: «a única de 4.º B que xoga na selección galega».
- **Os cuasiidentificadores**: Moaña, o equipo cadete feminino e o traballo do pai. Xuntos, sinalan unha soa persoa.
- **O que non se ve no fragmento**: se chegou como ficheiro, a cabeceira, as propiedades e os comentarios.

Con todo iso quitado, a frase segue servindo para corrixir a expresión: «Cando volvo dos partidos fóra, o pavillón é o sitio onde me sinto na casa, aínda que alguén da miña familia non poida vir».

[^rgpd]: Regulamento (UE) 2016/679, xeral de protección de datos ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807)), considerando 26.
[^nowak]: Sentenza do Tribunal de Xustiza do 20 de decembro de 2017, *Nowak*, C-434/16, apartados 37 e 62 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62016CJ0434)). Interpreta a Directiva 95/46, á que substituíu o RXPD cunha definición de dato persoal do mesmo alcance.
[^protocolo]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), setembro de 2022, apartados 12.1 e 21.
[^protocolo-orientacion]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), setembro de 2022, apartado 22.3.
[^malentendidos]: AEPD e Supervisor Europeo de Protección de Datos, [*10 malentendidos relacionados con la anonimización*](https://www.edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_es.pdf_0.pdf), 2021, equívocos 1, 3 e 7.
[^word]: Microsoft, [*Quitar datos ocultos e información personal inspeccionando documentos, presentaciones o libros*](https://support.microsoft.com/es-es/office/quitar-datos-ocultos-e-informaci%C3%B3n-personal-inspeccionando-documentos-presentaciones-o-libros-356b7b5d-77af-44fe-a07f-9aa4d085966f), consultado o 5 de novembro de 2026.
[^libreoffice]: Axuda de LibreOffice, [*Opciones de seguridad y alertas*](https://help.libreoffice.org/latest/es/text/shared/optionen/securityoptionsdialog.html), consultada o 5 de novembro de 2026.
[^apple]: Apple, [*Gestionar los metadatos de ubicación en Fotos*](https://support.apple.com/es-es/guide/personal-safety/ips0d7a5df82/web), consultada o 5 de novembro de 2026.
