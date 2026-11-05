---
title: Datos do alumnado
description: Como usar a IA para corrixir, analizar notas ou redactar informes sen expoñer datos do alumnado, cando abonda con anonimizar e que di a lei en cada caso típico.
derived_from:
  es/datos-alumnado/index.md: "09bee5b7d030916665d1f922e82b34664bd31f81"
---

> [!NOTE]
> **Unha lectura docente, non asesoramento xurídico**
> Esta páxina aplica a casos típicos o que se explica en [Normativa](../etica-legal/normativa.md#protección-de-datos), co mesmo criterio que o resto do bloque: cada indicación di se é unha **obriga legal**, unha **recomendación institucional** ou unha **boa práctica**. Ante un caso concreto, a referencia é a persoa delegada de protección de datos da Consellería.

## A pregunta previa: necesita a IA os datos?

Antes de anonimizar nada convén preguntarse se a IA necesita ver o alumnado. Case nunca: na maioría das tarefas o que achega é redactar, estruturar ou calcular, e iso pódese pedir sen datos reais. Hai tres vías, e próbanse nesta orde:

1. **Sen datos do alumnado.** A IA escribe o modelo de documento, a fórmula ou o procedemento, e ti aplícalo aos datos no teu equipo. Serve para informes, comunicacións ás familias, análise de notas e rúbricas.
2. **Co traballo, sen nada que diga de quen é.** Cando o que fai falla é o contido (unha redacción, as respostas dun exame), envíase só ese contido. Ti podes seguir sabendo de quen é, cunha táboa de códigos; quen o recibe non debe poder sabelo. É máis difícil do que parece, como se ve [na sección seguinte](#quitar-el-nombre-no-basta).
3. **Con datos persoais.** Só en ferramentas que a administración educativa contratase ou autorizase para ese uso (**obriga legal**; o porqué está en [quen pode tratar os datos do alumnado](../etica-legal/normativa.md#quién-puede-tratar-los-datos-del-alumnado)). En Galicia, ademais, o protocolo de protección de datos da Consellería pídelles aos centros que usen só as ferramentas que ela proporciona e que non usen plataformas externas non autorizadas (**recomendación institucional**).[^protocolo] Mentres non haxa entre elas unha ferramenta de IA para este uso (o catálogo de sistemas homologados que prevé a Lei de educación dixital aínda non existe), esta vía está pechada para a IA xerativa.

Un modelo executado no teu propio equipo, sen conexión, non envía nada fóra ([a demostración](../etica-legal/index.md#privacidad-la-regla-práctica)). Pero os datos seguen sendo datos do alumnado, suxeitos ás normas de seguridade e confidencialidade do centro.

## Quitar o nome non abonda

O procedemento habitual é razoable: cambias o nome por un código (`R-07`), gardas no teu equipo a táboa que di quen é cada código, pídeslle axuda á IA co traballo e, ao rematar, devólveslle a cada alumno a súa valoración. Que ti saibas de quen é cada traballo non é ningún problema: es o seu profesor, e o centro pode tratar os datos do seu alumnado para avalialo.[^loe] O que importa é que **non poida sabelo quen recibe o texto**. Se non ten a táboa nin outra forma razoable de descubrilo, para el non é un dato de ninguén.[^srb]

Para ti, pola contra, coa táboa seguen sendo datos do alumno: a lei chámalle **pseudonimizar**, non anonimizar.[^rgpd] Iso non cambia o que podes facer, pero explica por que a táboa se garda co mesmo coidado que o caderno de notas. O detalle legal está en [Anonimizar e pseudonimizar](../etica-legal/normativa.md#anonimizar-y-seudonimizar).

O código é só o primeiro paso, porque o nome non é o único que di de quen é un traballo: o ficheiro leva o autor e os comentarios, e ás veces abonda co propio texto. As respostas dun exame e o que anota quen o corrixe tamén son datos do alumno, e a letra a man identifícao.[^nowak] Isto é o que pode identificar un alumno ou unha alumna nun traballo:

| Que | Exemplos |
| --- | --- |
| Identificadores directos | Nome, sinatura, foto, correo, usuario da aula virtual, número de lista |
| Metadatos do ficheiro | Autor e «modificado por» nas propiedades, comentarios, control de cambios, a localización dunha foto |
| Cuasiidentificadores | Grupo, idade, localidade, club, o traballo dun familiar: por separado non din nada, pero xuntos sinalan unha persoa |
| Categorías especiais | Saúde, relixión, orixe étnica, orientación sexual: aínda que non identifiquen, son os datos con máis protección |
| A voz e a cara | Audios e vídeos de exposicións orais |

Os cuasiidentificadores son os que máis se escapan: dous ou tres detalles abondan para illar unha persoa dentro dun grupo sen saber o seu nome, e a lei cóntao como unha forma de identificala (chámalle **singularización**).[^rgpd] Nunha clase de vinte, «a única de 4.º B que xoga na selección galega» non necesita nome.

E hai textos que non se poden limpar sen destruílos: unha redacción autobiográfica chea de detalles persoais segue sendo recoñecible por moito que se quite. Entón non é a vía 2, e o que queda é a 1 ou a 3.

> [!NOTE]
> **Unha dúbida que aínda ninguén resolveu**
> O protocolo da Consellería pide usar cos datos do alumnado só as ferramentas que ela proporciona (**recomendación institucional**).[^protocolo] Non aclara se iso inclúe un traballo xa limpo, do que só ti sabes o autor: o que sae non identifica ninguén, pero quen o envía es ti, e para ti segue sendo o traballo dun alumno. Se o limpaches ben, o risco para o alumno é mínimo. Se o vas facer a miúdo e queres certeza, pregúntalle á persoa delegada de protección de datos da Consellería.

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
10. **Desactiva que as túas conversas se usen para adestrar modelos** (**boa práctica**). Onde se fai en cada *chatbot* está en [Chatbots](../chatbots/index.md#que-tus-conversaciones-entrenen-modelos).

> [!IMPORTANT]
> **Anonimizar non sempre é posible**
> A AEPD e o Supervisor Europeo de Protección de Datos resúmeno en tres ideas que afectan a calquera docente (**recomendación institucional**).[^malentendidos] Cambiar o nome non é anonimizar. Nun grupo pequeno, como unha clase, poucos detalles abondan para que quen o coñece saiba de quen se fala. E non se pode deixar en mans dun programa: os nomes atópanse sós, pero os detalles indirectos non sempre son obvios.

## Casos típicos

| Caso | Vía | Que facer |
| --- | --- | --- |
| Retroalimentación sobre unha redacción ou un traballo | 2 | Pegar o texto anonimizado coa rúbrica; a nota pómola ti |
| Corrixir un exame escrito a man | 2 | Foto recortada, sen cabeceira nin localización |
| Analizar as notas dun grupo | 1 | A IA escribe a fórmula a partir dunha mostra inventada |
| Informes e comunicacións ás familias | 1 | Modelo de documento con ocos que enches no teu equipo |
| Adaptar materiais para alumnado con necesidades específicas | 1 | Describir a necesidade didáctica, non o diagnóstico nin a persoa |
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

[^rgpd]: Regulamento (UE) 2016/679, xeral de protección de datos ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807)), considerando 26 e artigo 4.5.
[^loe]: Lei orgánica 2/2006, de educación, [disposición adicional vixésimo terceira](https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899#davigesimotercera).
[^srb]: Sentenza do Tribunal de Xustiza do 4 de setembro de 2025, *SEPD / JUR*, C-413/23 P, apartados 77 e 86 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62023CJ0413)).
[^nowak]: Sentenza do Tribunal de Xustiza do 20 de decembro de 2017, *Nowak*, C-434/16, apartados 37 e 62 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62016CJ0434)). Interpreta a Directiva 95/46, á que substituíu o RXPD cunha definición de dato persoal do mesmo alcance.
[^protocolo]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), setembro de 2022, apartados 12.1 e 21.
[^protocolo-orientacion]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), setembro de 2022, apartado 22.3.
[^malentendidos]: AEPD e Supervisor Europeo de Protección de Datos, [*10 malentendidos relacionados con la anonimización*](https://www.edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_es.pdf_0.pdf), 2021, equívocos 1, 3 e 7.
[^word]: Microsoft, [*Quitar datos ocultos e información personal inspeccionando documentos, presentaciones o libros*](https://support.microsoft.com/es-es/office/quitar-datos-ocultos-e-informaci%C3%B3n-personal-inspeccionando-documentos-presentaciones-o-libros-356b7b5d-77af-44fe-a07f-9aa4d085966f), consultado o 5 de novembro de 2026.
[^libreoffice]: Axuda de LibreOffice, [*Opciones de seguridad y alertas*](https://help.libreoffice.org/latest/es/text/shared/optionen/securityoptionsdialog.html), consultada o 5 de novembro de 2026.
[^apple]: Apple, [*Gestionar los metadatos de ubicación en Fotos*](https://support.apple.com/es-es/guide/personal-safety/ips0d7a5df82/web), consultada o 5 de novembro de 2026.
