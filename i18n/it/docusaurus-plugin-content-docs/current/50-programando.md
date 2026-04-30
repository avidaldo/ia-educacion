# Creare applicazioni senza saper programmare

##VibeCoding

**Vibe coding** è un termine coniato da [Andrej Karpathy](https://twitter.com/karpathy) nel febbraio 2025 per descrivere un nuovo modo di programmare in cui l'intelligenza artificiale genera il codice e l'essere umano lo guida attraverso istruzioni in linguaggio naturale.

> "Il nuovo linguaggio di programmazione più in voga è l'inglese" — Andrej Karpathy

### Come funziona?

1. **Descrivi** ciò che desideri in linguaggio naturale
2. L'IA **genera** il codice
3. **Corri** e osserva il risultato
4. **Itera** con le correzioni fino a ottenere ciò che desideri

### Strumenti per la codifica delle vibrazioni

| Strumento | Descrizione |
|-------------|-------------|
| **Artefatti di Claude** | Crea applicazioni web e ospitale automaticamente |
| **ChatGPT Canvas** | Area di lavoro con modifica ed esecuzione del codice |
| **Gemelli** | Genera codice con possibilità di esportare |
| **Cursore/Copilota GitHub** | Editor di codice con AI integrata |

### Vantaggi
- ✅Non è necessario saper programmare per creare semplici applicazioni
- ✅Prototipazione molto veloce
- ✅ Ideale per piccoli strumenti didattici

### Limitazioni
- ⚠️ Il codice potrebbe presentare errori o vulnerabilità
- ⚠️ Difficile da mantenere se non si capisce il codice
- ⚠️ Meglio per i prototipi che per la produzione

---

## Dal Vibe Coding agli agenti (automazione con criteri)

La codifica delle vibrazioni viene spesso descritta come "iterazione in base alla sensazione" finché qualcosa non funziona. Questo è utile per i prototipi, ma non appena si desidera **affidabilità**, è una buona idea passare dalla “chat” a un **flusso di tipo agente**.

### Cos'è un agente (in pratica)

Un agente non è “un’intelligenza artificiale più intelligente”, ma un sistema che:

- persegue un **obiettivo** (con criteri di accettazione),
- mantiene lo **stato** (cosa è stato provato, cosa ha fallito, cosa rimane),
- puoi utilizzare **strumenti** (test, linter, ricerca, convertitori di formato, ecc.),
- esegue un ciclo controllato e **si ferma** quando l'obiettivo viene raggiunto.

Se vuoi vedere modelli finalizzati alla didattica, ecco degli esempi pronti da riutilizzare:

- [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)
- [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### Modelli che funzionano (e come ordinarli)

**1) Pianificatore/Esecutore (pianificare → eseguire → convalidare)**

- Richiedi un piano breve (3-7 passaggi), quindi eseguilo passo dopo passo con convalida.
- Definire una “Definizione di Fatto”: quali test superare, quali file modificare, quale formato consegnare.

**2) Ciclo di critica (bozza → critica → versione finale)**

- Utile per: rubriche, attività, banche di domande, testi esplicativi.
- Limitare i turni (1–2) e definire i criteri (chiarezza, privacy, verificabilità).

**3) Utilizzo dello strumento/ReAct (Azione → Osservazione → Regolazione)**

- Utile per: ricerca con fonti, verifica, estrazione e riformattazione.
- Chiedere “azioni e osservazioni” (cosa hai fatto e cosa hai ottenuto). Evita di chiedere di “pensare passo dopo passo”.

**4) Multi-agente (ruoli: progettazione → valutazione → modifica)**

- Utile quando si desidera separare creatività, revisione critica e editing finale.
- Definire ruoli e un ordine rigoroso per ridurre i pregiudizi di autoconferma.

### Suggerimenti più utili quando si programma con l'intelligenza artificiale

Quando si utilizza Copilot/Cursor/Canvas/Artifacts, questi requisiti in genere migliorano notevolmente la qualità:

- Ingressi/uscite come contratto: “basta restituire il codice”, “intestazioni fisse”, “tabella con X colonne”.
- Criterio di arresto: “per quando X passa / quando non ci sono avvisi / quando compila”.
- Restrizioni: “non aggiungere dipendenze”, “non inventare dati”, “non utilizzare dati personali”.

Per la base dei prompt (formattazione, delimitatori, verifica), vedere: [/docs/prompt](/docs/prompt)

---

## Spazi di lavoro nei chatbot

### Artefatti di Claude

[Claude Artifacts](https://claude.ai/artifacts) ti consente di creare e pubblicare applicazioni web direttamente dalla chat.

**Guida rapida**:
1. Visita [Claude.ai](https://claude.ai/) e accedi con il tuo account
2. Descrivi l'applicazione di cui hai bisogno
3. Claude lo crea automaticamente e ti fornisce un collegamento da condividere
4. Il codice è ospitato su server Anthropic

:::note[Artículo interesante]
[Come creare mini-applicazioni educative con Claude](https://educacion.bilateria.org/como-crear-aplicaciones-educativas-con-claude)
:::

**Esempi di uso didattico**:
- Calcolatrici interattive
- Quiz e giochi educativi
- Visualizzazioni concettuali
- Simulatori semplici

### ChatGPT Canvas

[Canvas](https://openai.com/index/introducing-canvas/) è lo spazio di lavoro di ChatGPT per progetti più elaborati.

**Caratteristiche**:
- Pannello chat + editor integrato
- **Modifica in linea**: seleziona il codice e richiedi modifiche specifiche
- **Esecuzione Python**: esegue direttamente il codice
- **Controllo della versione**: annulla modifiche, ripristina versioni
- **Strumenti di codice**: debug, commenti, refactoring, traduzione in altre lingue

**Come attivarlo**:
- Automaticamente quando rileva il codice lungo
- Digitando manualmente "usa tela" o "apri tela"

### Gemelli

Gemini può anche generare codice e applicazioni, sebbene con capacità di hosting meno dirette. Tuttavia consente:
- Genera codice in più lingue
- Collaborare alla redazione
- Esporta per l'utilizzo su altri siti

---

## Integra le applicazioni in Moodle

Per inserire un'applicazione (come un Claude Artifact) in Moodle:

### Utilizzando l'URL dell'app

È possibile utilizzare l'URL (collegamento Claude Artifacts) per inserirlo direttamente in Moodle con una risorsa di tipo "URL".

### Utilizzando un iframe

1. Ottieni il collegamento all'app
2. Nel tuo corso Moodle, attiva la modalità di modifica
3. Aggiungi una risorsa o un'attività di tipo "Pagina" o "Etichetta"
4. Fare clic sull'icona del codice HTML `<>`
5. Incolla un codice iframe:
   ```html
   <iframe src="https://tu-enlace-de-aplicacion" width="100%" height="600px" frameborder="0"></iframe>
   ```
6. Salva le modifiche

### Creazione di pagine HTML

Qualsiasi chatbot può creare facilmente pagine HTML con il semplice tocco di un prompt. Quindi puoi:
- Scarica la pagina e incolla il codice in una risorsa "Pagina" di Moodle
- Utilizza una risorsa "Etichetta" da visualizzare direttamente sulla pagina del corso

---

## Risorse correlate

- [Test per Moodle](./41-casos-uso/01-tests-moodle.mdx) - Generazione di domande importabili
- [Procedure guidate personalizzate](./31-ejemplos/09-asistente-personalizado.mdx) - Crea GPT e gemme
