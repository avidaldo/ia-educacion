---
derived_from:
  es/vibe-coding/slides.md: "79762e1ed736a5a5a713ef0e83fa0f38b890841b"
---

<!-- .slide: id="olvidar-codigo" class="statement" -->
## *Vibe coding*: pedir, aceptalo todo e esquecer que o código existe

Karpathy, febreiro de 2025: «para proxectos de fin de semana de usar e tirar».

---

<!-- .slide: id="vibe-o-programar" class="comparison" -->
## Non todo o que se programa con IA é *vibe coding*

### *Vibe coding*
Aceptas o que propón sen lelo e pégaslle os erros ata que funciona.

### Programar con IA
Revisas o código, próbalo e saberías explicar como funciona.

Notas:
A distinción é de Simon Willison. Importa porque o *vibe coding* é perfecto para un prototipo e arriscado para calquera cousa que manexe datos ou da que dependan outras persoas.

---

<!-- .slide: id="niveles" class="table dense" -->
## Tres niveis de ferramentas

| Nivel | Exemplos | Que obtés |
| --- | --- | --- |
| Chat con vista previa | Canvas, Artifacts, Sites | Unha páxina ou unha aplicación lixeira |
| Xeradores de aplicacións | Google AI Studio, Lovable | Unha aplicación completa, publicada |
| Axentes de programación | Claude Code, Codex, Copilot | Traballo sobre os ficheiros dun proxecto |

Notas:
Claude Code está incluído en todos os plans de pago de Claude; Codex, en todos os de ChatGPT, tamén o gratuíto con límites. GitHub ofrece Copilot Pro de balde aos docentes verificados en GitHub Education.

---

<!-- .slide: id="metodo" class="fragments" -->
## Un método: especificar, empezar pequeno, probar

- Primeiro a especificación, e un plan antes do código.
- O mínimo que funcione; despois, un cambio cada vez.
- Próbaa como o faría o alumnado.
- Garda versións para poder volver atrás.
- Describe os fallos: que fixeches, que esperabas, que pasou.
- Pide que che explique as partes delicadas.

---

<!-- .slide: id="especificacion" class="prompt dense" -->
## Unha especificación antes do código

```text
Quero unha aplicación web para que o meu alumnado de 3.º de ESO practique
a formulación inorgánica. Antes de escribir código, faime as preguntas
que precises e proponme un plan de pantallas e funcións.
Requisitos: sen rexistro; non recolle nin envía datos; o progreso gárdase
só no navegador; tres niveis, con pista e corrección explicada;
usable no móbil e co teclado; sen servizos externos.
```

Notas:
A versión completa está na páxina.

---

<!-- .slide: id="demo-app" class="demo" -->
## Da especificación a unha aplicación que funciona

Preguntas antes do código e un cambio cada vez.

Notas:
**Demo (10 min)**. Google AI Studio (modo Build) ou Lovable, cunha conta de probas.

1. Pegar a especificación da páxina e responder ás preguntas.
2. Revisar o plan antes de que escriba código.
3. Probar a primeira versión con respostas equivocadas e no móbil.
4. Pedir un cambio concreto e volver á versión anterior desde o historial.

**Resultado esperado:** unha aplicación que funciona sen rexistro nin datos fóra do navegador.
**Se falla:** ensinar o historial de versións e a volta atrás, que é o que máis se usa.
**Mensaxe clave:** a especificación e as versións importan máis ca o *prompt* perfecto.

---

<!-- .slide: id="limite" class="statement" -->
## O que se gaña en rapidez pérdese en control se ninguén entende o código

---

<!-- .slide: id="riesgos" class="cards" -->
## Catro riscos concretos

### Seguridade
Bases de datos abertas a calquera, como en aplicacións de Lovable en 2025.

### Paquetes inventados
Polo menos un 5 % das bibliotecas suxeridas non existen.

### Claves e custos
O consumo de quen use a aplicación págalo ti.

### Mantemento
Se non entendes o código, cada cambio é unha lotaría.

Notas:
Os paquetes inventados, segundo un estudo de USENIX Security 2025 sobre 576.000 fragmentos de código de 16 modelos: un 5,2 % nos comerciais e un 21,7 % nos abertos. Un atacante pode rexistrar eses nomes con código malicioso.

---

<!-- .slide: id="gemini-menores" class="statement" -->
## Unha aplicación con Gemini dentro non se lle pode dar a menores de idade

Prohíbeno as condicións da súa API; unha aplicación sen chamadas a ningún modelo é outra cousa.

Notas:
As condicións esixen ademais os servizos de pago para ofrecer a aplicación a usuarios do Espazo Económico Europeo.

---

<!-- .slide: id="adelante" class="table" -->
## Onde está o límite

| Adiante | Mellor non, sen revisión do código |
| --- | --- |
| Prototipos e demostracións | Rexistro de usuarios |
| Ferramentas persoais | Datos do alumnado |
| Nada gardado fóra do navegador | API de pago |
| Material que se pode refacer | Ferramentas das que dependen outros |

Notas:
Para o que manexe datos do alumnado xa existen as ferramentas do centro, como a aula virtual.

---

<!-- .slide: id="ciclos" class="section" -->
## Nos ciclos de informática

---

<!-- .slide: id="estudio" class="big-number" -->
## Programar con IA pode frear a aprendizaxe

**17 %** menos nun cuestionario sobre os conceptos que acababan de usar.

Anthropic, xaneiro de 2026: ensaio controlado con 52 programadores.

Notas:
Aprendían unha biblioteca de Python nova. A maior diferenza, nas preguntas de depuración, e non foron significativamente máis rápidos. É un único estudo, dunha empresa do sector e sobre unha tarefa concreta.

---

<!-- .slide: id="explicaciones" class="statement" -->
## Quen pedía explicacións obtivo mellores resultados ca quen só pedía código

---

<!-- .slide: id="aula" -->
## Na aula

- Usar o axente para entender: explicacións, alternativas, erros sinalados.
- Predicir antes de executar.
- Depurar sen axuda unha parte do traballo.
- Defender o código: non se entrega o que non sabes explicar.

---

<!-- .slide: id="practica-especificacion" class="practice" -->
## A túa especificación

1. Pensa unha aplicación para a túa materia que non garde datos.
2. Escribe a súa especificación co modelo do exemplo.
3. Pídelle ao *chatbot* preguntas e un plan, aínda sen código.
4. Revisa o plan: que garda, que envía fóra.

**15 minutos.** Produto: unha especificación lista para construír.

Notas:
Por parellas. Ao final, dúas parellas len a súa especificación e o grupo busca que datos gardaría a aplicación sen que o pedisen.
