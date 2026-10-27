---
title: Ética e normativa
description: Criterios para decidir cando e como usar a IA no centro, separando o que obriga a lei do que é prudencia, cos nesgos, a privacidade, a autoría e o custo ambiental explicados desde como funciona a tecnoloxía.
derived_from:
  es/etica-legal/index.md: "e184defadf4e15cc389fc3ce453dc7f24d97e920"
---

## Que é lei e que é prudencia

Moitas listas do «que non se pode facer con IA» mesturan tres cousas de natureza moi distinta. Neste módulo cada criterio leva a súa orixe:

Obriga legal
: Esíxeo unha norma, e cítase o artigo. Non é opinable: cúmprese ou incúmprese.

Recomendación institucional
: Aconséllao unha guía oficial (da Comisión Europea, do Ministerio ou da Xunta), e cítase o documento. Non obriga por si mesma, pero reflicte o criterio de quen supervisa e convén coñecelo.

Boa práctica
: Propóno este curso, co seu razoamento. É discutible, e está ben discutilo.

Distinguilas evita dous erros frecuentes: tratar como prohibido o que só é prudente, ou como opcional o que é obrigatorio. Tamén permite ver onde unha prohibición non ten base legal nin técnica e queda en poñerlle portas ao campo. O que di cada norma desenvólvese en [Normativa](normativa.md), e a relación coa formación oficial da Xunta, no [anexo](anexo-formacion-xunta.md).

## Tres filtros antes de usar unha ferramenta

A formación da Xunta propón tres filtros, nesta orde:[^xunta-filtros]

1. **Pertinencia.** Achega algo á aprendizaxe ou ao meu traballo que non consiga igual de ben doutra forma? Se a resposta é non, non fai falla pasar aos demais.
2. **Ética.** Respecta as persoas afectadas: a súa autonomía, a súa privacidade, un trato xusto? As directrices da Comisión Europea para docentes, revisadas en 2026, concrétano en preguntas sobre supervisión humana, transparencia, inclusión, equidade, benestar, privacidade, solidez técnica e rendición de contas.[^directrices]
3. **Normativa.** Permíteo a lei? Protección de datos, Regulamento de IA e normas educativas.

A orde importa. Unha ferramenta perfectamente legal pode non ter sentido nunha tarefa, e unha que ten moito sentido pode ser ilegal con datos do alumnado.

## O residuo do pensamento

A formación da Xunta resume o risco pedagóxico central nunha cadea: unha tarefa **xerada con IA**, **realizada con IA** e **avaliada con IA** deixa o docente sen desenvolvemento profesional e o alumnado sen aprendizaxe. O que queda, di, é «o residuo do pensamento».[^xunta-residuo]

Non é só unha intuición. Nun ensaio controlado con case mil estudantes de matemáticas dun instituto de Turquía, os que practicaron cun asistente tipo ChatGPT sen restricións melloraron un 48 % nos exercicios de práctica, pero no exame posterior, xa sen asistente, sacaron un 17 % menos ca os que nunca o tiveron. Cun asistente configurado para dar pistas en lugar de solucións, ese efecto negativo desapareceu en boa parte.[^bastani] Un estudo con programadores apunta na mesma dirección: quen usa a IA para que lle explique aprende máis ca quen a usa para que lle dea o resultado (vese en [*Vibe coding*](../vibe-coding/index.md#en-los-ciclos-de-informática)).

**Boa práctica.** Deseña as tarefas para que o pensamento ocorra nalgún sitio visible: o proceso, a explicación oral, a versión corrixida, a decisión razoada. E se o alumnado vai usar un asistente, que sexa un configurado para guiar e non para resolver, como os [modos titor e os bots educativos](../bots-educativos/index.md).

## Nesgos

### De onde saen

Un modelo aprende as regularidades dos seus datos de adestramento, tamén as inxustas: se un grupo está pouco representado ou aparece asociado a certos estereotipos, o sistema reprodúceo. O mecanismo explícase en [Como funciona un modelo de linguaxe](../intro-ia/funcionamiento.md#sesgos-un-reflejo-de-los-datos). O importante para un docente é que o nesgo non se ve nunha resposta solta: aparece **ao medir o erro por grupos**.

### Dous casos medidos

O estudo *Gender Shades* avaliou en 2017 tres sistemas comerciais que clasificaban o xénero a partir dunha foto da cara. O erro variaba enormemente segundo o grupo:[^gender-shades]

![Gráfico de barras en tres paneis (Microsoft, Face++ e IBM). Nos tres, as mulleres de pel escura teñen con diferenza a maior porcentaxe de erros: 20,8 %, 34,5 % e 34,7 %. Os homes de pel clara, a menor: 0,0 %, 0,8 % e 0,3 %.](../../assets/etica-legal/gender-shades.svg)

| Sistema | Mulleres de pel escura | Homes de pel escura | Mulleres de pel clara | Homes de pel clara |
| --- | --- | --- | --- | --- |
| Microsoft | 20,8 % | 6,0 % | 1,7 % | 0,0 % |
| Face++ | 34,5 % | 0,7 % | 9,8 % | 0,8 % |
| IBM | 34,7 % | 12,0 % | 7,1 % | 0,3 % |

O segundo caso está máis preto da aula. Cinco sistemas de recoñecemento de voz (de Amazon, Apple, Google, IBM e Microsoft) transcribiron entrevistas con falantes dos Estados Unidos: equivocaban de media o 35 % das palabras dos falantes negros e o 19 % das dos brancos, tamén cando dicían exactamente as mesmas frases.[^koenecke] Se usas transcrición automática con alumnado de acentos, variedades ou linguas pouco representadas nos datos de adestramento, revisa o resultado antes de dalo por bo.

### Os nesgos de quen usa a ferramenta

A formación da Xunta insiste en algo que se esquece a miúdo: os humanos tamén temos nesgos, e os máis relevantes aquí son o de confirmación e a tendencia a fiarnos do que soa seguro.[^xunta-nesgos] Unha resposta ben redactada que coincide co que agardabamos é xusto a que menos revisamos. De aí sae o **exceso de confianza** que a propia formación inclúe entre os riscos.

**Boa práctica.** Revisa con máis coidado as respostas que confirman o que xa pensabas, e proba as ferramentas con casos de alumnado distinto antes de usalas cun grupo.

## Privacidade: a regra práctica

Os datos do alumnado pódeos tratar o centro para a súa función educativa, con medidas de seguridade e con deber de sixilo para o profesorado.[^loe] O que non cobre esa habilitación é copialos nunha ferramenta que a administración non contratou: o provedor non actúa por conta do centro, pode gardalos ou usalos para adestrar, e non hai contrato que o impida.

- **Obriga legal.** Non introducir datos persoais do alumnado (nomes, notas, informes, fotos, situacións familiares) en ferramentas que non estean contratadas ou autorizadas pola administración educativa. O detalle está en [Normativa](normativa.md#protección-de-datos).
- **Boa práctica.** Traballar con casos inventados ou anonimizados de verdade: non abonda con quitar o nome se a combinación de datos («a única alumna de 2.º con discapacidade auditiva») identifica a persoa.
- **Boa práctica.** Preferir sempre as contas que proporciona o centro, como se ve en [Bots educativos](../bots-educativos/index.md#lo-primero-con-qué-cuenta-entra-el-alumnado).

Unha demostración útil na clase: un modelo pequeno executado no propio ordenador, con programas gratuítos como Ollama ou LM Studio, funciona **sen conexión a internet**. Desconecta a rede e segue respondendo: é a proba visible de que o modelo non precisa enviar nada fóra. Son modelos menos capaces ca os dos *chatbots* comerciais, pero amosan que a cuestión da privacidade depende de **onde se executa** o modelo.

## Autoría e avaliación

**Os detectores de texto xerado por IA non son fiables.** OpenAI retirou o seu en xullo de 2023 «a causa de su bajo índice de precisión»: só identificaba o 26 % dos textos xerados por IA e marcaba como xerados o 9 % dos escritos por persoas.[^openai-clasificador] Un estudo con sete detectores atopou que clasificaban como xeradas por IA máis da metade das redaccións escritas por estudantes de inglés como lingua estranxeira, cunha taxa media de falsos positivos do 61 %: penalizan precisamente a quen escribe cun vocabulario máis sinxelo.[^liang]

- **Boa práctica.** Nunca sancionar polo resultado dun detector. Como moito, serve para iniciar unha conversa.
- **Boa práctica.** Reformular a avaliación, como pide a propia formación da Xunta:[^xunta-conclusiones] valorar o proceso, pedir explicacións orais, traballar na clase as partes clave, pedir as versións intermedias.
- **Recomendación institucional.** Pedirlle ao alumnado que declare como usou a IA e ensinarlle a citala. É unha das preguntas que as directrices europeas lles propoñen aos docentes.[^directrices]
- **Boa práctica.** Indicar nos teus materiais que partes se xeraron con IA. Ollo: o Regulamento de IA só obriga a etiquetar as ultrasuplantacións (*deepfakes*) e os textos publicados para informar o público sobre asuntos de interese público ([Normativa](normativa.md#transparencia)), non un material de clase normal.

As trampas de texto oculto nos enunciados, e por que non serven para avaliar, vense en [Técnicas avanzadas](../prompts/avanzado.md#trampas-de-texto-oculto-en-los-enunciados).

## Custo ambiental

As cifras públicas máis precisas son poucas e veñen dos propios provedores. Google mediu en 2025 que unha consulta de texto mediana a Gemini consumía 0,24 Wh e 0,26 ml de auga, algo menos que ver nove segundos de televisión; é a súa propia medición, e só para texto.[^google-energia] O problema é o agregado: segundo a Axencia Internacional da Enerxía, os centros de datos consumiron en 2024 arredor do 1,5 % da electricidade mundial (415 TWh), e prevé que esa cifra se duplique ata uns 945 TWh en 2030, coa IA como principal motor.[^iea]

**Boa práctica.** Proporcionalidade: usar a IA cando achega algo, non por defecto, e preferir a xeración de texto á de imaxe ou vídeo cando abonda.

## Oportunidades e riscos

A formación da Xunta enumera as oportunidades e os riscos da IA na educación, e recoñece que aínda faltan estudos sistemáticos e imparciais sobre os seus efectos.[^xunta-conclusiones] Esta é a correspondencia de cada risco co que se trata no curso:

| Risco | Que facer | Onde se trata |
| --- | --- | --- |
| Privacidade e protección de datos | Datos do alumnado só en ferramentas contratadas pola administración | [Privacidade](#privacidad-la-regla-práctica) e [Normativa](normativa.md#protección-de-datos) |
| Vixilancia | Nada de sistemas que infiran emocións no centro: está prohibido | [Normativa](normativa.md#prácticas-prohibidas) |
| Nesgos | Medir por grupos; revisar transcricións e clasificacións | [Nesgos](#sesgos) |
| Efecto filtro | Contrastar con fontes; pedir as fontes | [Chatbots](../chatbots/index.md#buscar-en-la-web-e-investigar-a-fondo) |
| Desconexión social | Que a IA non substitúa o traballo en grupo nin a titoría | [O residuo do pensamento](#el-residuo-del-pensamiento) |
| Efectos nas capacidades | Tarefas nas que o pensamento sexa visible | [O residuo do pensamento](#el-residuo-del-pensamiento) |
| Inexactitudes e exceso de confianza | Comprobar na fonte; desconfiar do que confirma o agardado | [Como funciona](../intro-ia/funcionamiento.md#alucinaciones-plausible-no-es-verdadero) |
| Dereitos de autor e plaxio | Avaliar o proceso; declarar o uso de IA | [Autoría e avaliación](#autoría-y-evaluación) |
| Comercialización da educación | Preferir ferramentas contratadas e recursos abertos | [Normativa](normativa.md#galicia) |
| Fenda dixital | Non esixir ferramentas de pago nin contas persoais | [Bots educativos](../bots-educativos/index.md) |
| Gasto enerxético | Proporcionalidade | [Custo ambiental](#coste-ambiental) |
| Manipulación e conflito de intereses | Alfabetización en IA do alumnado | [Co alumnado](#con-el-alumnado) |

## Para practicar

Colle as normas ou consignas sobre IA do teu centro, do teu departamento ou da túa programación, e etiqueta cada punto coa súa orixe: obriga legal, recomendación institucional ou boa práctica. Para cada obriga legal, busca o artigo en [Normativa](normativa.md); se non o atopas, probablemente non o sexa. E para cada prohibición sen base legal, pregúntate que risco tenta evitar e se hai unha forma mellor de evitalo.

## Co alumnado

A mellor protección do alumnado é entender como funcionan estas ferramentas: por que se equivocan, de onde saen os seus nesgos, que pasa co que escriben nelas. O Plan integral de benestar dixital da Xunta prevé incorporar aos currículos o uso responsable da IA e un programa de formación do alumnado en alfabetización mediática, verificación da información e IA (**recomendación institucional**).[^benestar] Moitos dos módulos deste curso serven directamente para iso: a [demostración da inxección de *prompts*](../navegadores-agenticos/index.md#una-demostración-segura), os casos de nesgo desta páxina ou a comparación de respostas en [Chatbots](../chatbots/index.md).

[^xunta-filtros]: Xunta de Galicia, presentación *Intelixencia artificial (Ética e normativa en materia de Educación)*, p. 12. O seu contido completo, comentado, está no [anexo](anexo-formacion-xunta.md).
[^directrices]: Comisión Europea, [*Guidelines on the ethical use of artificial intelligence and data in teaching and learning for educators*](https://data.europa.eu/doi/10.2766/7967834), edición revisada de 2026, apartado *Guiding questions for educators and school leaders*.
[^xunta-residuo]: Presentación da Xunta, pp. 16–19.
[^bastani]: Bastani et al., [*Generative AI without guardrails can harm learning: Evidence from high school mathematics*](https://doi.org/10.1073/pnas.2422633122), PNAS, 2025.
[^gender-shades]: Buolamwini e Gebru, [*Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification*](https://proceedings.mlr.press/v81/buolamwini18a.html), 2018, táboa 4. Gráfico propio cos seus datos.
[^koenecke]: Koenecke et al., [*Racial disparities in automated speech recognition*](https://doi.org/10.1073/pnas.1915768117), PNAS, 2020.
[^xunta-nesgos]: Presentación da Xunta, pp. 3–7 e 15.
[^loe]: Lei orgánica 2/2006, de educación, [disposición adicional vixésimo terceira](https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899#davigesimotercera).
[^openai-clasificador]: OpenAI, [*Nuevo clasificador de IA para detectar textos generados por IA*](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/), nota engadida o 20 de xullo de 2023.
[^liang]: Liang et al., [*GPT detectors are biased against non-native English writers*](https://arxiv.org/abs/2304.02819), Patterns, 2023.
[^xunta-conclusiones]: Presentación da Xunta, pp. 70–71.
[^google-energia]: Elsworth et al. (Google), [*Measuring the environmental impact of delivering AI at Google Scale*](https://arxiv.org/abs/2508.15734), agosto de 2025.
[^iea]: Axencia Internacional da Enerxía, [*Energy and AI*](https://www.iea.org/reports/energy-and-ai/executive-summary), 2025.
[^benestar]: Xunta de Galicia, [*Plan integral de benestar dixital de Galicia*](https://ficheiros-web.xunta.gal/plans/educacion-ciencia/plan-integral-benestar-dixital.pdf), 2026, actuacións 18 e 19.
