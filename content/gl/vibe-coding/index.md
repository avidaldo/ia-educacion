---
title: Vibe coding
description: Crear aplicacións a base de prompts, que ferramentas hai para cada nivel, un método que funciona e onde está o límite entre un prototipo e algo que pode usar o alumnado.
derived_from:
  es/vibe-coding/index.md: "57c7b2101781e8498e4bbdce4bbb5f3b92ce3530"
---

## Que é

Andrej Karpathy, que formou parte do equipo fundador de OpenAI, creou o termo en febreiro de 2025 para describir unha forma de programar na que «te entregas ás sensacións» e «esqueces que o código existe»: pides cambios en linguaxe natural, aceptas todo o que propón a IA sen lelo e, cando algo falla, pégaslle a mensaxe de erro ata que funciona.[^karpathy] El mesmo presentábao como algo para «proxectos de fin de semana de usar e tirar». O termo estendeuse tanto que o dicionario Collins o escolleu palabra do ano 2025.[^collins]

Convén distinguilo de programar coa axuda da IA. Simon Willison explícao así: se revisas o código que escribe o modelo, o probas a fondo e saberías explicarlle a outra persoa como funciona, iso xa non é *vibe coding*; é desenvolvemento de software, e que te axudase un modelo é o de menos.[^willison] A distinción importa porque o *vibe coding* é perfecto para un prototipo ou unha ferramenta persoal e arriscado para calquera cousa que manexe datos ou da que dependan outras persoas.

Respecto a [Webs educativas](../webs-educativas/index.md), a diferenza é de tamaño: alí trátase dunha páxina nun único ficheiro; aquí, dunha **aplicación**, con varias pantallas, datos que se gardan, usuarios ou un servidor.

## Tres niveis de ferramentas

| Nivel | Exemplos | Que obtés | Para quen |
| --- | --- | --- | --- |
| Chat con vista previa | Canvas en Gemini e ChatGPT, Artifacts en Claude, Sites en ChatGPT | Unha páxina ou unha aplicación lixeira dentro do *chatbot* | Calquera; é o punto de partida de [Webs educativas](../webs-educativas/index.md) |
| Xeradores de aplicacións | [Google AI Studio](https://aistudio.google.com) (modo Build), [Lovable](https://lovable.dev) | Unha aplicación completa (interface, servidor, base de datos, inicio de sesión) publicada nun enderezo propio | Sen instalar nada; plans gratuítos con límites |
| Axentes de programación | Claude Code, Codex, GitHub Copilot, Gemini CLI | Un axente que traballa sobre os ficheiros dun proxecto: le e modifica o código, executa o programa e as probas, e corrixe o que falla | Quen xa programa ou está aprendendo, como nos ciclos de informática |

Algúns datos útiles para o último nivel: Claude Code está incluído en todos os plans de pago de Claude, Codex en todos os de ChatGPT (tamén no gratuíto, con límites) e GitHub ofrece Copilot Pro de balde aos docentes verificados en GitHub Education.[^planes]

## Un método que funciona

1. **Primeiro, a especificación.** Antes de pedir código, describe que fai a aplicación, quen a usa, en que dispositivos e que datos garda (idealmente, ningún). Pídelle ao *chatbot* que che faga preguntas ata telo claro, como no [*metaprompting*](../prompts/index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt), e que che propoña un plan antes de escribir nada.
2. **O mínimo que funcione.** Unha primeira versión cunha soa función. Despois, un cambio cada vez.
3. **Próbaa ti**, como o faría o alumnado: co móbil, con respostas equivocadas, premendo onde non toca.
4. **Garda versións.** Todas estas ferramentas teñen historial ou conéctanse a GitHub: cando un cambio o estraga todo, vólvese atrás en lugar de pedir arranxos enriba de arranxos.
5. **Describe os fallos con precisión**: que fixeches, que esperabas e que pasou, mellor que pegar só o erro.
6. **Pide explicacións das partes delicadas**: onde se gardan os datos, que se envía fóra, que pasa se alguén escribe algo inesperado.

Un exemplo de especificación:

```text
Quero unha aplicación web para que o meu alumnado de 3.º de ESO practique
a formulación inorgánica. Antes de escribir código, faime as preguntas
que precises e proponme un plan de pantallas e funcións.

Requisitos:
- Sen rexistro nin inicio de sesión. Non recolle nin envía ningún dato.
- O progreso gárdase só no navegador do alumno.
- Tres niveis de dificultade; en cada pregunta, unha pista e a corrección explicada.
- Funciona no móbil e é manexable co teclado.
- Sen servizos externos: nada de analíticas, fontes nin bibliotecas doutras webs.
```

## Onde está o límite

O que se gaña en rapidez pérdese en control cando ninguén entende o código. Estes son os riscos concretos:

Seguridade dos datos
: En 2025 rexistrouse unha vulnerabilidade en aplicacións xeradas con Lovable: unhas regras de acceso insuficientes na base de datos permitían a calquera ler ou modificar as súas táboas sen identificarse. Lovable cuestionouna co argumento de que a seguridade de cada aplicación é responsabilidade de quen a crea.[^lovable] Esa é xustamente a cuestión: se unha aplicación garda datos e ten usuarios, alguén ten que entender como está protexida.

Paquetes inventados
: Os modelos recomendan ás veces bibliotecas que non existen. Un estudo presentado en USENIX Security 2025 analizou 576.000 fragmentos de código de 16 modelos: polo menos un 5,2 % dos paquetes suxeridos polos modelos comerciais, e un 21,7 % nos abertos, eran inventados.[^paquetes] Un atacante pode rexistrar eses nomes con código malicioso, e quen non revisa o que instala descárgao.

Claves e custos
: Unha aplicación que usa un modelo de linguaxe precisa unha clave de acceso á súa API, que non debe quedar á vista no código do navegador, e cada uso ten un custo. As plataformas actuais adoitan gardar a clave no servidor, pero o consumo de quen use a aplicación págalo ti.

Condicións de uso
: As da API de Gemini, que usan as aplicacións de Google AI Studio, esixen 18 anos, prohíben usala en aplicacións dirixidas a menores de 18 anos ou que probablemente usen menores, e obrigan a usar os servizos de pago para ofrecer unha aplicación a usuarios do Espazo Económico Europeo.[^gemini-api] Unha aplicación con IA dentro feita en AI Studio non se lle pode dar, polo tanto, a alumnado menor de idade. Unha aplicación sen chamadas a ningún modelo, como a do exemplo, é outra cousa: é código coma calquera outro.

Mantemento
: Se non entendes o código, cada cambio é unha lotaría. E as ferramentas cambian: o que hoxe se fai nunha plataforma pode non existir o curso que vén.

| Adiante | Mellor non, agás que alguén revise o código |
| --- | --- |
| Prototipos e demostracións para a clase | Aplicacións con rexistro de usuarios |
| Ferramentas persoais (un xerador de rúbricas, un conversor de formatos) | Aplicacións que gardan datos do alumnado |
| Aplicacións que non gardan nada fóra do navegador | Aplicacións que usan API de pago co diñeiro de alguén |
| Material que se pode tirar e refacer | Ferramentas das que van depender outros docentes |

Para todo o que manexe datos do alumnado xa existen ferramentas do centro, como a aula virtual, coa súa protección de datos resolta.

## Nos ciclos de informática

Para quen aprende a programar, o risco non é só a calidade do código senón **deixar de aprender**. Nun ensaio controlado publicado por Anthropic en xaneiro de 2026, 52 programadores aprenderon unha biblioteca de Python nova: os que usaron un asistente de IA sacaron un 17 % menos nun cuestionario sobre os conceptos que acababan de usar, e a maior diferenza estivo nas preguntas de depuración. Non foron significativamente máis rápidos. Pero non todos os que usaron IA aprenderon menos: os que lle pedían explicacións e lle facían preguntas conceptuais obtiveron mellores resultados que os que só lle pedían código.[^anthropic-aprendizaje] É un único estudo, feito por unha empresa do sector e sobre unha tarefa concreta, pero apunta nunha dirección clara.

Algunhas ideas para a aula:

- **Usar o axente para entender, non só para producir**: pedirlle que explique, que propoña alternativas e que sinale erros en lugar de corrixilos.
- **Predicir antes de executar**: que fará este código e por que.
- **Depurar sen axuda unha parte do traballo**, que é xusto o que máis se resente.
- **Defender o código** oralmente ou modificándoo en directo. A regra de Willison serve como criterio de avaliación: non se entrega código que non saibas explicar.[^willison]

[^karpathy]: A mensaxe orixinal de Karpathy, de febreiro de 2025, está citada completa no artigo de Simon Willison da nota seguinte.
[^collins]: Collins, [*Word of the Year 2025*](https://www.collinsdictionary.com/woty).
[^willison]: Simon Willison, [*Not all AI-assisted programming is vibe coding (but vibe coding rocks)*](https://simonwillison.net/2025/Mar/19/vibe-coding/), 19 de marzo de 2025.
[^planes]: Segundo as páxinas de [prezos de Claude](https://claude.com/pricing), [prezos de Codex](https://developers.openai.com/codex/pricing) e [GitHub Copilot para docentes](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers), consultadas o 22 de outubro de 2026.
[^lovable]: [CVE-2025-48757](https://www.cve.org/CVERecord?id=CVE-2025-48757), publicada o 30 de maio de 2025, coa nota de que o provedor a cuestiona.
[^paquetes]: Spracklen et al., [*We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*](https://arxiv.org/abs/2406.10279), USENIX Security 2025.
[^gemini-api]: Google, [*Gemini API Additional Terms of Service*](https://ai.google.dev/gemini-api/terms), apartados *Age Requirements* e *Use Restrictions*, consultados o 22 de outubro de 2026.
[^anthropic-aprendizaje]: Anthropic, [*How AI assistance impacts the formation of coding skills*](https://www.anthropic.com/research/AI-assistance-coding-skills), 29 de xaneiro de 2026.
