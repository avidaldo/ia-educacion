---
title: Como funciona un modelo de linguaxe
description: Que fai por dentro un modelo de linguaxe e por que iso explica tanto os seus acertos coma os seus erros.
derived_from:
  es/intro-ia/funcionamiento.md: "85900217673a2a2f9c7585cce76fe1c774c77bc3"
---

## Predicir a seguinte palabra

Un modelo de linguaxe fai, en esencia, o mesmo que o teclado do móbil cando suxire a seguinte palabra: **calcula que é máis probable que veña a continuación**, dado todo o texto anterior. Despois engade esa palabra ao texto e repite o proceso, palabra a palabra, ata completar a resposta.

A diferenza co teclado é de escala. O modelo adestrouse cunha cantidade enorme de texto (libros, webs, artigos, código) e ten miles de millóns de parámetros, de modo que as súas predicións teñen en conta parágrafos enteiros, o ton, a estrutura dun documento ou o que se dixo vinte mensaxes antes.

Unha analoxía: alguén que lese miles de receitas pode adiviñar que despois de «engadir sal e…» adoita vir «pementa», sen que iso garanta que a receita concreta a leve. O modelo fai algo parecido con todo tipo de textos, a unha escala inmensamente maior.

> [!IMPORTANT]
> **A idea que o explica case todo**
> Un modelo de linguaxe non consulta unha base de datos de feitos nin comproba o que di: xera a continuación **máis plausible** segundo as regularidades que aprendeu. Case sempre o plausible coincide co correcto; cando non coincide, o erro preséntase coa mesma fluidez ca un acerto.

## *Tokens* e xanela de contexto

En realidade o modelo non traballa con palabras, senón con ***tokens***: fragmentos de texto que poden ser unha palabra curta, parte dunha palabra longa ou un signo de puntuación. En galego, unha palabra ocupa a miúdo máis dun *token*.

A **xanela de contexto** é a cantidade máxima de *tokens* que o modelo pode ter en conta á vez: as túas instrucións, toda a conversa, os documentos adxuntos e a propia resposta. O que queda fóra da xanela non existe para o modelo. Por iso, en conversas moi longas ou con documentos enormes, o modelo pode «esquecer» instrucións do principio ou pasar por alto partes dun ficheiro. O tamaño da xanela varía moito entre modelos e plans; as cifras actuais están en [Chatbots](../chatbots/index.md).

## Do modelo base ao asistente

Un *chatbot* como os actuais constrúese en dúas grandes fases:

1. **Preadestramento.** O modelo aprende a predicir o seguinte *token* sobre unha cantidade masiva de texto. O resultado, o *modelo base*, sabe continuar textos de calquera tipo, pero non segue instrucións: se lle escribes unha pregunta, pode continuar con outra pregunta.
2. **Axuste posterior.** Con exemplos de conversas ben resoltas e con valoracións humanas de que resposta é mellor (a chamada *aprendizaxe por reforzo con retroalimentación humana*), o modelo aprende a comportarse como un asistente: seguir instrucións, responder cun formato útil, negarse a certas peticións.

Esta segunda fase explica trazos que ás veces se atribúen a unha «personalidade»: o ton servizal, a tendencia a darche a razón ou os avisos de seguridade. Son comportamentos aprendidos durante o axuste.

## Por que non responde sempre o mesmo

En cada paso o modelo non calcula unha única palabra, senón unha **distribución de probabilidades** sobre todas as posibles. O *chatbot* escolle entre as máis probables cun compoñente de azar controlado. Por iso a mesma pregunta pode dar respostas distintas, e por iso paga a pena **rexenerar** unha resposta ou facer a mesma petición nun chat novo cando o resultado importa.

Que o texto de entrada condicione as probabilidades explica tamén por que funciona o deseño de *prompts*: non é un truco, é darlle ao modelo o contexto que despraza as súas predicións cara ao que queres. Vese en [Deseño de prompts](../prompts/index.md).

## Alucinacións: plausible non é verdadeiro

Chámase **alucinación** a unha resposta fluída e segura que é falsa: un dato inventado, unha cita que non existe, unha referencia bibliográfica con autores e título verosímiles pero imaxinarios.

Non é un fallo puntual que se vaia corrixir na próxima versión, senón unha consecuencia de como se adestran estes modelos. O seu obxectivo é producir texto plausible, e tanto o adestramento coma as avaliacións habituais premian máis arriscar unha resposta ca recoñecer «non o sei».[^kalai] Os modelos actuais equivócanse bastante menos ca os de hai dous anos, sobre todo cando buscan na web, pero o risco non desaparece.

> [!WARNING]
> **Implicación práctica**
> Toda cifra, cita, referencia ou norma que xere un modelo compróbase na fonte antes de usala na clase ou nun documento oficial.

> [!TIP]
> **Próbao**
> Nun chat temporal, e sen busca web se o teu *chatbot* permite desactivala, pide tres referencias académicas sobre un tema moi concreto da túa materia e busca cada título nun buscador académico. Despois repite a petición coa busca activada e abre as fontes que cite. É habitual atopar algunha referencia verosímil que non existe, ou con autores, ano ou revista cambiados.

## O que sabe e o que busca

O modelo aprende ata unha **data de corte**: o que pasou despois non está nos seus parámetros. Os *chatbots* actuais compensan esa limitación **buscando na web** e citando as páxinas que usan. Iso mellora moito a actualidade e permite verificar, pero introduce outro risco: o modelo pode escoller fontes pouco fiables ou resumilas mal.

Tampouco é exacto dicir que o modelo «non memoriza nada». Aprende regularidades xerais, pero tamén pode reproducir de forma literal fragmentos dos seus datos de adestramento, sobre todo textos que aparecen moitas veces.[^carlini] É unha das razóns dos conflitos sobre dereitos de autor e da recomendación de non introducir datos persoais nestas ferramentas, que se tratan no módulo de ética.<!-- TODO: enlazar ../etica-legal/index.md cuando exista -->

## Modelos que razoan

Desde 2024 existen modelos adestrados para **xerar un razoamento intermedio antes de responder**: descompoñen o problema, proban camiños e revisan pasos. Adéstranse sobre todo con problemas cuxa resposta se pode comprobar (matemáticas, programación, lóxica), e nese tipo de tarefas melloran moito, a cambio de tardar máis e gastar máis.

Hoxe a maioría dos *chatbots* deciden por si mesmos canto razoar segundo a pregunta, ou permiten activalo cunha opción. Dous matices importantes:

- O razoamento segue a ser texto xerado polo mesmo mecanismo: mellora os resultados, pero non converte o modelo nun sistema de dedución lóxica infalible.
- O razoamento que mostra o *chatbot* non sempre reflicte o que de verdade determinou a resposta: os propios desenvolvedores documentaron casos en que o modelo usou unha pista que non menciona no seu razoamento.[^chen]

## Nesgos: un reflexo dos datos

Se nos textos de adestramento certas profesións se asocian máis a un xénero, ou certos grupos se describen con outros adxectivos, o modelo aprende esas asociacións, porque iso é exactamente o que fai: extraer as regularidades dos seus datos. Os nesgos non son unha «decisión» do modelo, senón un reflexo estatístico dos textos cos que se adestrou, de como se seleccionaron e de como se fixo o axuste posterior.

Corrixilos tampouco é trivial: as correccións introducen os seus propios desequilibrios. Os tipos de nesgo e os casos documentados trátanse no módulo de ética.<!-- TODO: enlazar ../etica-legal/index.md cuando exista -->

## Para saber máis

<details>
<summary>A arquitectura <em>transformer</em> e a atención</summary>

Os modelos de linguaxe actuais usan a arquitectura *transformer*.[^vaswani] A súa peza central, a **atención**, permite que ao procesar cada *token* o modelo pondere a relevancia de todos os anteriores: ao chegar a «abrino» en «deixei o libro na mesa e abrino», a atención relaciona o pronome con «libro». Como estes cálculos se poden facer en paralelo, a arquitectura aproveita moi ben as GPU, e iso fixo posible adestrar modelos enormes.

</details>

<details>
<summary>Como representa o modelo as palabras</summary>

Cada *token* convértese nun vector de miles de números (un *embedding*). Durante o adestramento, os *tokens* que aparecen en contextos parecidos acaban con vectores próximos, de modo que o modelo traballa con relacións de significado aproximadas («rei» queda preto de «raíña» e de «monarca»). As capas do modelo transforman eses vectores tendo en conta o contexto ata producir a distribución de probabilidade do seguinte *token*.

</details>

<details>
<summary>Do modelo base ao asistente, con máis detalle</summary>

O traballo que popularizou o axuste con valoracións humanas, base de ChatGPT, é o de Ouyang et al. (2022).[^ouyang] Hoxe o axuste combina varias técnicas: exemplos escritos por persoas, comparacións entre respostas, regras explícitas que o propio modelo usa para avaliarse e, nos modelos que razoan, aprendizaxe por reforzo con problemas verificables.

</details>

[^kalai]: Kalai, A. T. et al. (2025). [*Why Language Models Hallucinate*](https://arxiv.org/abs/2509.04664).
[^carlini]: Carlini, N. et al. (2021). [*Extracting Training Data from Large Language Models*](https://arxiv.org/abs/2012.07805).
[^chen]: Chen, Y. et al. (2025). [*Reasoning Models Don't Always Say What They Think*](https://arxiv.org/abs/2505.05410).
[^vaswani]: Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762).
[^ouyang]: Ouyang, L. et al. (2022). [*Training language models to follow instructions with human feedback*](https://arxiv.org/abs/2203.02155).
