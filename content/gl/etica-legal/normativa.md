---
title: Normativa
description: O que din o RXPD, a LOPDGDD, a LOE, o Regulamento de IA e as normas galegas sobre o uso da IA nun centro educativo, co seu calendario de aplicación e o que aínda está en tramitación.
derived_from:
  es/etica-legal/normativa.md: "7b64fe9222865dcc5465019dd14c0b2292d5f976"
---

> [!NOTE]
> **Unha lectura docente da normativa**
> Esta páxina explica as normas desde o traballo dun docente e cita os seus artigos para que poidas comprobalos. Non é asesoramento xurídico: ante un caso concreto, a referencia é a persoa delegada de protección de datos da Consellería, que todas as administracións públicas teñen que designar. Situación revisada o 27 de outubro de 2026.

## Como se ordenan as normas

Un **regulamento europeo** é obrigatorio e directamente aplicable en todos os Estados, sen que faga falla unha lei nacional que o traspoña; unha **directiva**, en cambio, fixa obxectivos que cada Estado incorpora coa súa propia lei. Pero «directamente aplicable» non significa «aplicable desde que se publica»: cada regulamento fixa a súa data de entrada en vigor e os seus prazos de aplicación. O Regulamento de IA, por exemplo, publicouse en xullo de 2024, entrou en vigor o 1 de agosto de 2024 e aplícase por fases ata 2028 ([calendario](#calendario)).

Por debaixo están as normas españolas (leis orgánicas como a LOPDGDD ou a LOE, reais decretos) e as galegas. E fóra desa xerarquía, as **guías e recomendacións** (da Comisión Europea, do INTEF, da Xunta), que orientan pero non obrigan.

## Protección de datos

As normas son o Regulamento xeral de protección de datos (RXPD), que é europeo, e a Lei orgánica de protección de datos (LOPDGDD), que o completa en España. Con elas, a Lei orgánica de educación (LOE) regula os datos do alumnado.

### Que é un dato persoal

O RXPD defíneo de forma moi ampla: «toda información sobre una persona física identificada o identificable», e é identificable quen pode ser identificado «directa o indirectamente», por exemplo mediante «uno o varios elementos propios de la identidad física, fisiológica, genética, psíquica, económica, cultural o social».[^rgpd] Unha nota, un comentario sobre a conduta ou unha descrición que permite saber de quen se fala son datos persoais, aínda que non apareza o nome.

### Quen pode tratar os datos do alumnado

A LOE habilita os centros: «podrán recabar los datos personales de su alumnado que sean necesarios para el ejercicio de su función educativa», e engade dúas condicións que importan aquí:[^loe]

- «se aplicarán normas técnicas y organizativas que garanticen su seguridad y confidencialidad»;
- o profesorado que acceda a eses datos «quedará sujeto al deber de sigilo».

Esa habilitación é do centro e da administración educativa, non de cada ferramenta que use un docente. Cando un terceiro trata datos por conta do centro, o RXPD esixe que sexa un **encargado do tratamento** elixido entre quen ofreza «garantías suficientes», cun contrato que o regule.[^rgpd] Un *chatbot* con conta persoal non é iso: por iso os datos do alumnado só van a ferramentas que a administración contratou ou autorizou. E aínda nelas, só os imprescindibles: os datos han de ser «limitados a lo necesario en relación con los fines» (minimización).[^rgpd]

### Datos especialmente protexidos

Algunhas categorías teñen unha protección reforzada: o RXPD prohibe en principio tratar datos que revelen a orixe étnica, as conviccións relixiosas, a saúde ou a orientación sexual, entre outros, agás nos supostos que enumera.[^rgpd] Un informe de necesidades educativas, un diagnóstico ou unha adaptación por motivos de saúde entran aquí: son os últimos datos que deberían acabar nunha ferramenta de IA.

### A idade do alumnado

En España, un menor pode consentir por si mesmo o tratamento dos seus datos «cuando sea mayor de catorce años»; por debaixo fai falla o consentimento de quen exerce a patria potestade ou a titoría.[^lopdgdd] O RXPD fixa 16 anos para os servizos en liña ofrecidos directamente a menores e permite a cada Estado baixala ata 13; España escolleu 14.[^rgpd]

Isto pode cambiar. O proxecto de lei orgánica de protección das persoas menores de idade nas contornas dixitais, en tramitación no Congreso en outubro de 2026, eleva esa idade a dezaseis anos no texto que presentou o Goberno.[^menores]

### Decisións automatizadas e avaliacións de impacto

Toda persoa ten dereito «a no ser objeto de una decisión basada únicamente en el tratamiento automatizado, incluida la elaboración de perfiles, que produzca efectos jurídicos en él o le afecte significativamente de modo similar».[^rgpd] Unha cualificación, unha sanción ou unha decisión de promoción non poden saír só dunha ferramenta.

E cando unha administración quere usar unha tecnoloxía nova con datos que supoñen un alto risco, antes ten que facer unha **avaliación de impacto relativa á protección de datos**.[^rgpd] É responsabilidade da administración que implanta a ferramenta, non do docente que a usa, pero explica por que un centro non debería adoptar pola súa conta unha plataforma de IA con datos do alumnado.

## Regulamento de IA

A súa lóxica é graduar as obrigas segundo o risco: unhas poucas prácticas están prohibidas, certos usos son de alto risco e cargan con obrigas estritas, algúns sistemas teñen obrigas de transparencia, e o resto, que é a maioría dos usos, non ten obrigas específicas. Á parte, os modelos de uso xeral, como os que hai detrás dos *chatbots*, teñen as súas propias obrigas, que recaen en quen os desenvolve.

### Calendario

O Regulamento (UE) 2024/1689, coñecido como RIA ou *AI Act*, aplícase por fases. En xullo de 2026 modificouno o Regulamento (UE) 2026/1744, o chamado *Digital Omnibus*, que atrasou as obrigas dos sistemas de alto risco e engadiu novas prohibicións.[^ria] [^omnibus]

| Desde | Que se aplica | Relevancia nun centro |
| --- | --- | --- |
| 1 de agosto de 2024 | Entrada en vigor | Ningunha obriga aínda |
| 2 de febreiro de 2025 | Disposicións xerais, alfabetización e prácticas prohibidas | Prohibido inferir emocións en centros educativos |
| 2 de agosto de 2025 | Modelos de uso xeral, gobernanza e sancións | Obrigas para os provedores dos modelos |
| 2 de agosto de 2026 | Aplicación xeral, incluídas as obrigas de transparencia | Avisar de que se fala cunha IA; etiquetar ultrasuplantacións |
| 2 de decembro de 2026 | Novas prohibicións do *Omnibus* | Prohibidos os sistemas para xerar imaxes íntimas sen consentimento |
| 2 de decembro de 2027 | Sistemas de alto risco do anexo III, entre eles os educativos | Obrigas para quen implante sistemas que avalían ou admiten alumnado |
| 2 de agosto de 2028 | Sistemas de alto risco integrados en produtos (anexo I) | Pouca |

As datas de alto risco eran o 2 de agosto de 2026 e 2027. Moitas guías publicadas antes de xullo de 2026, incluídas as directrices europeas para docentes, aínda dan as datas antigas.

### Quen é quen

O Regulamento reparte as obrigas entre o **provedor**, quen desenvolve o sistema e o comercializa, e o **responsable do despregamento**, que é quen o usa «bajo su propia autoridad, salvo cuando su uso se enmarque en una actividad personal de carácter no profesional».[^ria] Nun centro público, cando a Consellería implanta unha ferramenta, o responsable do despregamento é a administración, e o docente úsaa por conta dela. O que faga un docente pola súa conta para o seu traballo queda nunha zona menos clara, e é outro motivo para usar as ferramentas que proporciona a administración.

### Alfabetización

O artigo 4 obrigaba inicialmente a provedores e responsables do despregamento a «garantizar que, en la mayor medida posible», o seu persoal tivese «un nivel suficiente de alfabetización en materia de IA». Desde o 27 de xullo de 2026, tras o *Omnibus*, a obriga é máis suave: deben adoptar «medidas para apoyar la promoción de la alfabetización en materia de IA» do seu persoal, e o texto aclara que non lles esixe garantir «un nivel específico» de ninguén. A Comisión e os Estados deben apoiar ese esforzo.[^omnibus]

En Galicia, ademais, a lei de IA obriga a administración a velar porque o persoal que intervén no ciclo de vida destes sistemas manteña «as capacidades precisas para que poida garantir un debido uso destes».[^lei-ia]

### Prácticas prohibidas

A máis relevante en educación é a do artigo 5.1.f: o uso de sistemas de IA «para inferir las emociones de una persona física en los lugares de trabajo y en los centros educativos», agás por motivos médicos ou de seguridade. Está prohibida desde o 2 de febreiro de 2025.[^ria] As directrices da Comisión concrétano con exemplos:[^directrices]

- Unha aplicación para aprender idiomas con recoñecemento de emocións non está prohibida se se usa fóra do centro; se o centro obriga o alumnado a usala, si o está.
- Un sistema de supervisión de exames en liña que segue a mirada para detectar material non autorizado non está prohibido; se ademais detecta nerviosismo ou ansiedade, si.
- Usar o recoñecemento de emocións para inferir o interese ou a atención do alumnado está prohibido.

O resto da lista (manipulación subliminar, explotación de vulnerabilidades, puntuación social, bases de datos de recoñecemento facial, categorización biométrica para deducir datos sensibles, identificación biométrica en tempo real en espazos públicos con fins policiais) afecta pouco ao traballo dun centro.

Desde o 2 de decembro de 2026 engádense dúas prohibicións con consecuencias directas para a convivencia escolar: os sistemas que xeren imaxes, vídeos ou audios realistas «de las partes íntimas de una persona física identificable» ou dunha persoa identificable en actividades sexualmente explícitas sen o seu consentimento, e os que xeren material de abuso sexual infantil.[^omnibus] Afecta ás aplicacións de «espidos» falsos, cuxo uso entre estudantes é un risco para a convivencia.

### Alto risco en educación

O anexo III considera de alto risco catro usos en educación e formación profesional:[^ria]

- a) determinar o acceso ou a admisión aos centros, ou distribuír o alumnado entre eles;
- b) avaliar os resultados da aprendizaxe, tamén cando se usan para orientar o proceso de aprendizaxe;
- c) avaliar o nivel de educación axeitado que recibirá unha persoa ou ao que poderá acceder;
- d) vixiar e detectar comportamentos prohibidos durante os exames.

Non todo sistema que toque eses ámbitos é de alto risco. Segundo o artigo 6.3, non o é cando non inflúe substancialmente na decisión: se fai unha tarefa de procedemento limitada, mellora o resultado dunha actividade humana xa feita, detecta desviacións en pautas de decisión sen substituír a valoración humana, ou fai unha tarefa preparatoria. Pero sempre o é cando elabora perfís de persoas.[^ria]

As obrigas correspondentes aplícanse desde o 2 de decembro de 2027. Para a administración que implante un destes sistemas inclúen encargar a supervisión humana «a personas físicas que tengan la competencia, la formación y la autoridad necesarias» e, por ser un organismo público, facer unha avaliación de impacto sobre os dereitos fundamentais antes de despregalo.[^ria]

Queda unha cuestión aberta: o artigo 25.1.c converte en provedor dun sistema de alto risco a quen «modifique la finalidad prevista de un sistema de IA, incluido un sistema de IA de uso general», de xeito que pase a ser de alto risco.[^ria] Como se aplica a un docente que usa un *chatbot* xeral para poñer notas non está resolto no texto. É un argumento máis, xunto ao artigo 22 do RXPD, para que a IA non decida a cualificación.

### Transparencia

Desde o 2 de agosto de 2026, os provedores deben avisar as persoas de que interactúan cun sistema de IA e marcar o contido sintético para que sexa detectable. Quen use un sistema para xerar ultrasuplantacións (*deepfakes*) debe facer público que se xeraron artificialmente, e quen publique textos xerados por IA «con el fin de informar al público sobre asuntos de interés público» debe indicalo, agás que tivesen revisión humana e alguén asuma a responsabilidade editorial.[^ria] Un material de clase normal non entra neses supostos: etiquetalo é unha boa práctica, non unha obriga.

### Quen supervisa

En España, a Axencia Española de Supervisión da Intelixencia Artificial (AESIA), con sede na Coruña, ten funcións de «supervisión, el asesoramiento, la concienciación y la formación» e de «inspección, comprobación, sanción».[^aesia] O relativo aos datos persoais segue sendo competencia da Axencia Española de Protección de Datos.

## Galicia

### A lei galega de IA

A Lei 2/2025, para o desenvolvemento e o impulso da intelixencia artificial en Galicia, aplícase á administración autonómica e ao seu sector público, e polo tanto á Consellería de Educación e aos sistemas de IA que implante.[^lei-ia] O seu artigo 12 establece unha **reserva de humanidade**: cando un sistema de IA sirva de apoio a un acto ou decisión administrativa, «en ningún caso tales actuacións nas que se empreguen sistemas de intelixencia artificial constituirán de seu decisións ou actos administrativos sen validación pola persoa titular do órgano competente». A lei foi modificada pola Lei 5/2025, que cambiou entre outros o seu obxecto e as súas definicións, pero non os artigos citados aquí.[^lei-5]

### O que está en marcha

- **Estratexia galega de intelixencia artificial 2030 (EGIA).** A súa medida 4 prevé incorporar a IA a todas as etapas educativas, un grupo de persoas expertas que deseñe a folla de ruta e un programa específico de formación do profesorado.[^xunta-egia]
- **Plan integral de benestar dixital** (xaneiro de 2026). Prevé incorporar aos currículos o uso responsable da IA, un programa de formación do alumnado en IA e a publicación dunha guía de *Orientacións para o uso e a integración da IA no ámbito educativo*.[^benestar]
- **Lei de educación dixital de Galicia.** O proxecto (expediente 12/PL-000015) está no Parlamento desde xullo de 2026, coa previsión de entrar en vigor en 2027.[^xunta-lei] Segundo a Xunta, dedicará un capítulo aos usos permitidos e prohibidos da IA no ensino.[^xunta-ia] O máis relevante para o profesorado: **só se poderán usar sistemas de IA homologados e autorizados pola Consellería**, que publicará un catálogo. Ademais, prohibiranse as decisións académicas, organizativas e administrativas baseadas unicamente en resultados de IA, os sistemas de control automatizado do comportamento, a atención ou o rendemento, o uso da IA para predicir ou identificar condicións como o TEA ou o TDAH, e o recoñecemento facial. É un texto en tramitación: pode cambiar, e convén seguir a súa aprobación.
- **EdugalIA.** Proxecto da Consellería para reducir o abandono escolar temperán mediante a análise de datos con IA, que a formación da Xunta presenta como a integración en «unha única plataforma» dos datos que hoxe están dispersos.[^xunta-edugalia] Unha plataforma así está en tensión co principio de minimización e, se elabora perfís do alumnado, necesita unha avaliación de impacto previa e non pode tomar por si soa decisións que lles afecten significativamente.

[^rgpd]: Regulamento (UE) 2016/679, xeral de protección de datos ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807)): artigos 4.1 (dato persoal), 5.1.c (minimización), 8.1 (consentimento de menores en servizos en liña), 9.1 (categorías especiais), 22.1 (decisións automatizadas), 28.1 (encargado do tratamento), 35.1 (avaliación de impacto) e 37.1.a (delegado de protección de datos das autoridades públicas).
[^loe]: Lei orgánica 2/2006, de educación, [disposición adicional vixésimo terceira](https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899#davigesimotercera).
[^lopdgdd]: Lei orgánica 3/2018, de protección de datos persoais e garantía dos dereitos dixitais, [artigo 7](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673#a7).
[^menores]: Proxecto de lei orgánica para a protección das persoas menores de idade nas contornas dixitais, [BOCG, Congreso, serie A, núm. 52-1](https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-52-1.PDF), 11 de abril de 2025, disposición derradeira sexta.
[^ria]: Regulamento (UE) 2024/1689, de intelixencia artificial ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-81079)): artigos 3.4 (responsable do despregamento), 5.1.f, 6.3, 25.1.c, 26.2, 27, 50 e 113, e anexo III, punto 3.
[^omnibus]: Regulamento (UE) 2026/1744, do 8 de xullo de 2026 ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2026-81147)): novo artigo 4; artigo 5.1, letras b bis e b ter; artigo 113.
[^lei-ia]: [Lei 2/2025, do 2 de abril](https://www.xunta.gal/dog/Publicados/2025/20250404/AnuncioC3B0-030425-0001_gl.html), para o desenvolvemento e o impulso da intelixencia artificial en Galicia, artigos 3, 12 e 19.
[^lei-5]: [Lei 5/2025, do 23 de decembro](https://www.xunta.gal/dog/Publicados/2025/20251231/AnuncioC3B0-231225-0002_gl.html), de medidas fiscais e administrativas, artigo 48.
[^directrices]: Comisión Europea, [*Guidelines on the ethical use of artificial intelligence and data in teaching and learning for educators*](https://data.europa.eu/doi/10.2766/7967834), 2026, táboa 1, con exemplos das directrices da Comisión sobre prácticas prohibidas. Tradución propia.
[^aesia]: Real decreto 729/2023, Estatuto da AESIA, [artigo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2023-18911).
[^benestar]: Xunta de Galicia, [*Plan integral de benestar dixital de Galicia*](https://ficheiros-web.xunta.gal/plans/educacion-ciencia/plan-integral-benestar-dixital.pdf), actuacións 18, 19 e 28.
[^xunta-lei]: Xunta de Galicia, [nota de prensa do 29 de xuño de 2026](https://www.xunta.gal/notas-de-prensa/-/nova/026191/rueda-anuncia-aprobacion-anteproxecto-lei-educacion-dixital-unha-norma-pioneira); Parlamento de Galicia, [ficha do proxecto 12/PL-000015](https://www.parlamentodegalicia.es/ParticipacionCidada/LexislaConNos/3482/proxecto-de-lei-de-educacion-dixital-de-galicia.-12pl-000015).
[^xunta-ia]: Xunta de Galicia, [nota de prensa do 11 de abril de 2026](https://www.xunta.gal/es/notas-de-prensa/-/nova/023351/galicia-autorizara-uso-educacion-para-deteccion-temprana-dificultades-aprendizaje).
[^xunta-egia]: Presentación da Xunta *Intelixencia artificial (Ética e normativa en materia de Educación)*, p. 40.
[^xunta-edugalia]: Presentación da Xunta *Intelixencia artificial (Ética e normativa en materia de Educación)*, pp. 64–68, comentada no [anexo](anexo-formacion-xunta.md).
