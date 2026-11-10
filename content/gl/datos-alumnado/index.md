---
title: Datos do alumnado
description: Como usar a IA para corrixir, analizar notas ou redactar informes sen expoñer datos do alumnado, que se pode facer cun traballo ao que lle cambias o nome por un código e que di a lei en cada caso típico.
derived_from:
  es/datos-alumnado/index.md: "545cc3bc432229ae80c063504f8a2ed617847940"
---

> [!NOTE]
> **Unha lectura docente, non asesoramento xurídico**
> Esta páxina aplica a casos típicos o que se explica en [Normativa](../etica-legal/normativa.md#protección-de-datos), co mesmo criterio que o resto do bloque: cada indicación di se é unha **obriga legal**, unha **recomendación institucional** ou unha **boa práctica**. Ante un caso concreto, a referencia é a persoa delegada de protección de datos da Consellería.

## A pregunta previa: necesita a IA os datos?

Tes vinte e cinco redaccións por corrixir e queres que a IA che axude coa retroalimentación. Podes pegalas nun *chatbot* se cambias cada nome por un código? A resposta depende menos do código que de dúas cousas: o que pode descubrir quen recibe o texto, que depende de como o limpes, e a ferramenta que uses, que decide a Consellería.

Antes de limpar nada convén preguntarse se a IA necesita ver o alumnado. Case nunca: na maioría das tarefas o que achega é redactar, estruturar ou calcular, e iso pódese pedir sen datos reais. Hai tres vías, da máis segura á menos:

| Que lle envías á IA | Pódese? |
| --- | --- |
| **1. Nada do alumnado.** A IA escribe o modelo de documento, a fórmula ou o procedemento, e ti aplícalo aos datos. Serve para informes, comunicacións ás familias, análise de notas e rúbricas | **Si** |
| **2. O traballo, sen nada que diga de quen é.** O nome cambiado por un código e o texto limpo de detalles que o delaten | **Sen aclarar.** Se está ben limpo, o risco para o alumno é mínimo, pero ninguén o autorizou, e o INTEF recomenda pedir permiso antes ([por que](#entonces-puedo-pegarlo-en-un-chatbot-con-mi-cuenta)) |
| **3. Datos persoais.** O nome, ou detalles que permiten saber de quen é | **Non**, agás en ferramentas que a administración educativa contratase ou autorizase. Hoxe non hai ningunha de IA xerativa |

A vía 3 é unha **obriga legal**: a habilitación para tratar os datos do alumnado é do centro e da administración, non de cada ferramenta que use un docente ([quen pode tratar os datos do alumnado](../etica-legal/normativa.md#quién-puede-tratar-los-datos-del-alumnado)). En Galicia, ademais, o protocolo de protección de datos da Consellería pídelles aos centros que usen só as ferramentas que ela proporciona e que non usen plataformas externas non autorizadas (**recomendación institucional**).[^protocolo] Entre elas non hai polo de agora ningunha de IA xerativa: o catálogo de sistemas homologados que prevé a Lei de educación dixital aínda non existe.

Un modelo executado no teu propio ordenador, sen conexión, non envía nada fóra ([a demostración](../etica-legal/index.md#privacidad-la-regla-práctica)): ningún terceiro recibe os datos. Pero seguen sendo datos do alumnado, e o protocolo pide non gardalos en dispositivos persoais do profesorado, porque a súa seguridade «non queda garantida pola Administración» (**recomendación institucional**).[^protocolo]

## A táboa de códigos, en catro preguntas

O procedemento habitual para a vía 2 é razoable: cambias o nome por un código (`R-07`), gardas á parte a táboa que di quen é cada código, pídeslle axuda á IA co traballo e, ao rematar, devólveslle a cada alumno a súa valoración. Suscita catro preguntas, e só unha está sen resolver.

### Podo gardar unha táboa que diga quen é cada código?

Si. Que ti saibas de quen é cada traballo non é ningún problema: es o seu profesor, e o centro pode tratar os datos do seu alumnado para avalialo.[^loe] A táboa gárdase co mesmo coidado que o caderno de notas: nunca na ferramenta de IA, e mellor no espazo do centro ou nun equipo do centro coa túa clave que nun dispositivo persoal (**recomendación institucional**).[^protocolo]

### Co código, o traballo xa é anónimo?

Depende de para quen. Para quen recibe o texto sen a táboa pode selo: se non ten outra forma razoable de descubrir de quen é, para el non é un dato de ninguén.[^srb] Para ti, non: seguen sendo datos do alumno, e a lei chámalle **pseudonimizar**, non anonimizar.[^rgpd] E non é só pola táboa: ti sabes de quen é o traballo, porque lle vas devolver a corrección. O detalle legal está en [Anonimizar e pseudonimizar](../etica-legal/normativa.md#anonimizar-y-seudonimizar).

### Entón, podo pegalo nun *chatbot* coa miña conta?

**Se o texto aínda delata o alumno, non** (**obriga legal**): sería enviar datos persoais a unha empresa que non ten contrato coa administración. O que pode delatalo, ademais do nome, está [na sección seguinte](#quitar-el-nombre-no-basta).

**Se está ben limpo, ninguén o aclarou.** O risco para o alumno é mínimo, porque quen recibe o texto non pode saber de quen é. O que falta é cobertura, por tres motivos:

- **Para ti seguen sendo datos do alumno, e envialos xa é tratalos.** Quen traballa para a Consellería trátaos seguindo as súas instrucións,[^rgpd] e o seu protocolo pide usar só as ferramentas que ela proporciona, sen dicir se iso inclúe un texto que xa non identifica ninguén (**recomendación institucional**).[^protocolo]
- **Para a Consellería, o alias non levanta as obrigas.** Nun caso parecido, o das plataformas externas para proxectos, o seu protocolo só as admite se dependen dun organismo público europeo e con autorización por escrito das familias (ou do alumno, se ten máis de 14 anos), e aínda así recomenda «contas con alias, é dicir, cos datos persoais “pseudonimizados” pero mantendo as obrigas e medidas contempladas na normativa de protección de datos».[^protocolo]
- **A orientación máis próxima pide permiso antes.** O INTEF pensa sobre todo no alumnado que usa unha ferramenta externa cun código, pero o seu criterio serve aquí: ese uso só cabe se non permite a reidentificación «en modo alguno», despois de que o centro consulte a delegación de protección de datos e co permiso da administración ou do centro. E descarta esas ferramentas para tratar «datos de carácter administrativo con efectos jurídicos», entre os que pon como exemplo a «evaluación de pruebas de conocimiento o aptitud» (**recomendación institucional**).[^intef]

En resumo: ningunha norma o prohibe de forma expresa, e ninguén o autorizou.

### Que fago mentres tanto?

O que segue é **boa práctica**:

- **Se che abonda coa vía 1, úsaa.** É a única sen dúbidas.
- **Se usas a vía 2, que sexa co texto ben limpo** ([como](#cómo-anonimizar-un-trabajo)), nun chat temporal e co adestramento desactivado, e nunca co que non se pode limpar: gravacións, convivencia, saúde.
- **Se o vas facer a miúdo, pide o visto e prace**: o centro pode preguntarllo á persoa delegada de protección de datos da Consellería, que é o que recomenda o INTEF.

## Quitar o nome non abonda

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
8. **Garda a táboa código → alumno fóra da ferramenta**, mellor no espazo do centro ou nun equipo do centro coa túa clave.
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

É o caso da vía 2 con máis reparos: un exame é unha proba de coñecemento, e o INTEF descarta as ferramentas externas para avalialas ([por que](#entonces-puedo-pegarlo-en-un-chatbot-con-mi-cuenta)). Se o fas, que a IA transcriba e sinale erros, e que a puntuación de cada pregunta a decidas ti.

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

[^rgpd]: Regulamento (UE) 2016/679, xeral de protección de datos ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807)), considerando 26 e artigos 4.2 (tratamento), 4.5 (pseudonimización) e 29 (tratamento baixo a autoridade do responsable).
[^loe]: Lei orgánica 2/2006, de educación, [disposición adicional vixésimo terceira](https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899#davigesimotercera).
[^srb]: Sentenza do Tribunal de Xustiza do 4 de setembro de 2025, *SEPD / JUR*, C-413/23 P, apartados 77 e 86 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62023CJ0413)).
[^nowak]: Sentenza do Tribunal de Xustiza do 20 de decembro de 2017, *Nowak*, C-434/16, apartados 37 e 62 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62016CJ0434)). Interpreta a Directiva 95/46, á que substituíu o RXPD cunha definición de dato persoal do mesmo alcance.
[^protocolo]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), setembro de 2022, apartados 12.1 (ferramentas da Consellería e plataformas externas), 14 (dispositivos persoais) e 21 (plataformas externas e equipos con clave persoal).
[^intef]: INTEF, [*Orientaciones sobre el uso de herramientas digitales en el ámbito educativo desde la perspectiva de la protección de datos*](https://intef.es/wp-content/uploads/2026/07/Orientaciones_sobre_el_uso_de_herramientas_digital.pdf), versión 3.0, xuño de 2026, advertencia 6 (p. 8) e puntos 4 e 9 do uso anonimizado ou pseudonimizado (pp. 11–12). É un documento orientativo do Ministerio de Educación, non unha norma.
[^protocolo-orientacion]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), setembro de 2022, apartado 22.3.
[^malentendidos]: AEPD e Supervisor Europeo de Protección de Datos, [*10 malentendidos relacionados con la anonimización*](https://www.edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_es.pdf_0.pdf), 2021, equívocos 1, 3 e 7.
[^word]: Microsoft, [*Quitar datos ocultos e información personal inspeccionando documentos, presentaciones o libros*](https://support.microsoft.com/es-es/office/quitar-datos-ocultos-e-informaci%C3%B3n-personal-inspeccionando-documentos-presentaciones-o-libros-356b7b5d-77af-44fe-a07f-9aa4d085966f), consultado o 5 de novembro de 2026.
[^libreoffice]: Axuda de LibreOffice, [*Opciones de seguridad y alertas*](https://help.libreoffice.org/latest/es/text/shared/optionen/securityoptionsdialog.html), consultada o 5 de novembro de 2026.
[^apple]: Apple, [*Gestionar los metadatos de ubicación en Fotos*](https://support.apple.com/es-es/guide/personal-safety/ips0d7a5df82/web), consultada o 5 de novembro de 2026.
