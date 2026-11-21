---
title: How a language model works
description: What a language model does inside and why that explains both its successes and its errors.
derived_from:
  es/intro-ia/funcionamiento.md: "d5ed5b86bc9b4aa1da5f1ed540eecf35524dde68"
---

## Predicting the next word

A language model does, in essence, the same as a phone keyboard when it suggests the next word: **it calculates what is most likely to come next**, given all the text before it. Then it adds that word to the text and repeats the process, word by word, until the answer is complete.

The difference from the keyboard is one of scale. The model has been trained on an enormous amount of text (books, websites, articles, code) and has billions of parameters, so its predictions take into account whole paragraphs, the tone, the structure of a document or what was said twenty messages earlier.

An analogy: someone who has read thousands of recipes can guess that “add salt and…” is usually followed by “pepper”, without that guaranteeing that a particular recipe includes it. The model does something similar with every kind of text, on an immensely larger scale.

> [!IMPORTANT]
> **The idea that explains almost everything**
> A language model does not consult a database of facts or check what it says: it generates the **most plausible** continuation according to the patterns it learned. Almost always, what is plausible coincides with what is correct; when it does not, the error comes out as fluently as a correct answer.

## Tokens and context window

The model does not actually work with words but with **tokens**: pieces of text that can be a short word, part of a long word or a punctuation mark. In Spanish, for example, a word often takes up more than one token.

The **context window** is the maximum number of tokens the model can take into account at once: your instructions, the whole conversation, attached documents and the answer itself. Whatever falls outside the window does not exist for the model. That is why, in very long conversations or with huge documents, the model may “forget” instructions from the beginning or overlook parts of a file. The size of the window varies widely between models and plans; the current figures are in [Chatbots](../chatbots/index.md).

## From base model to assistant

A chatbot like today’s is built in two main phases:

1. **Pre-training.** The model learns to predict the next token over a massive amount of text. The result, the *base model*, can continue texts of any kind, but does not follow instructions: if you write it a question, it may continue with another question.
2. **Post-training.** With examples of well-handled conversations and with human ratings of which answer is better (so-called *reinforcement learning from human feedback*), the model learns to behave like an assistant: following instructions, answering in a useful format, refusing certain requests.

This second phase explains traits that are sometimes attributed to a “personality”: the helpful tone, the tendency to agree with you or the safety warnings. They are behaviours learned during post-training.

## Why it does not always give the same answer

At each step the model does not calculate a single word, but a **probability distribution** over all possible words. The chatbot chooses among the most likely ones with a controlled element of chance. That is why the same question can give different answers, and why it is worth **regenerating** an answer or making the same request in a new chat when the result matters.

The fact that the input text shapes the probabilities also explains why prompt design works: it is not a trick, it is giving the model the context that shifts its predictions towards what you want. This is covered in [Prompt design](../prompts/index.md).

## Hallucinations: plausible is not true

A **hallucination** is a fluent, confident answer that is false: an invented figure, a quotation that does not exist, a bibliographic reference with plausible but imaginary authors and title.

It is not a one-off fault that will be fixed in the next version, but a consequence of how these models are trained. Their objective is to produce plausible text, and both training and the usual evaluations reward guessing an answer more than admitting “I don’t know”.[^kalai] Today’s models make considerably fewer mistakes than those of two years ago, especially when they search the web, but the risk does not go away.

> [!WARNING]
> **Practical implication**
> Every figure, quotation, reference or regulation that a model generates is checked at the source before it is used in class or in an official document.

> [!TIP]
> **Try it**
> In a temporary chat, and without web search if your chatbot lets you turn it off, ask for three academic references on a very specific topic in your subject and look up each title in an academic search engine. Then repeat the request with search turned on and open the sources it cites. It is common to find a plausible reference that does not exist, or one with the authors, year or journal changed.

## What it knows and what it searches for

The model learns up to a **cutoff date**: what happened afterwards is not in its parameters. Today’s chatbots make up for that limitation by **searching the web** and citing the pages they use. That greatly improves how up to date they are and makes checking possible, but it brings another risk: the model may choose unreliable sources or summarise them badly.

Nor is it accurate to say that the model “memorises nothing”. It learns general patterns, but it can also reproduce fragments of its training data word for word, especially texts that appear many times.[^carlini] This is one of the reasons for the copyright disputes and for the recommendation not to enter personal data into these tools ([Ethics and law](../etica-legal/index.md#privacy-the-practical-rule)).

## Reasoning models

Since 2024 there have been models trained to **generate intermediate reasoning before answering**: they break the problem down, try different paths and review steps. They are trained above all on problems whose answer can be checked (mathematics, programming, logic), and on that kind of task they improve a great deal, at the cost of taking longer and costing more.

Today most chatbots decide by themselves how much to reason depending on the question, or let you turn reasoning on with an option. Two important caveats:

- The reasoning is still text generated by the same mechanism: it improves the results, but it does not turn the model into an infallible logical deduction system.
- The reasoning that the chatbot shows does not always reflect what actually determined the answer: the developers themselves have documented cases in which the model used a hint that it does not mention in its reasoning.[^chen]

## Biases: a reflection of the data

If, in the training texts, certain professions are associated more with one gender, or certain groups are described with different adjectives, the model learns those associations, because that is exactly what it does: extract the regularities in its data. Biases are not a “decision” of the model, but a statistical reflection of the texts it was trained on, of how they were selected and of how post-training was done.

The word “bias” is used in two senses that are best kept apart. In statistics, a bias is a systematic error: an estimate that deviates from the true value always in the same direction. In the sense of fairness, it is an error or a treatment that differs systematically by group. A model can reproduce its data with complete fidelity and still give unfair results, if that data reflects an unequal world: it does exactly what it was trained to do. That is why “Is AI sexist?” is a misleading question. The useful one is at which stage the bias entered (the data, what was chosen to be measured, how it was evaluated, what it is used for) and who made that decision.

Correcting biases is not trivial either: the corrections introduce their own imbalances. The stages, the documented cases and how to detect a bias by measuring the error by group are covered in [Ethics and law](../etica-legal/index.md#bias).

## Going further

<details>
<summary>The transformer architecture and attention</summary>

Today’s language models use the transformer architecture.[^vaswani] Its central piece, **attention**, lets the model weigh the relevance of all the previous tokens as it processes each token: when it reads “it” in “I left the book on the table and opened it”, attention links “it” with “book”. Because these calculations can be done in parallel, the architecture makes very good use of GPUs, and that made it possible to train huge models.

</details>

<details>
<summary>How the model represents words</summary>

Each token is turned into a vector of thousands of numbers (an embedding). During training, tokens that appear in similar contexts end up with nearby vectors, so that the model works with approximate relations of meaning (“king” lies close to “queen” and to “monarch”). The model’s layers transform those vectors, taking the context into account, until they produce the probability distribution of the next token.

</details>

<details>
<summary>From base model to assistant, in more detail</summary>

The work that popularised tuning with human ratings, the basis of ChatGPT, is that of Ouyang et al. (2022).[^ouyang] Today post-training combines several techniques: examples written by people, comparisons between answers, explicit rules that the model itself uses to evaluate itself and, in reasoning models, reinforcement learning with verifiable problems.

</details>

[^kalai]: Kalai, A. T. et al. (2025). [*Why Language Models Hallucinate*](https://arxiv.org/abs/2509.04664).
[^carlini]: Carlini, N. et al. (2021). [*Extracting Training Data from Large Language Models*](https://arxiv.org/abs/2012.07805).
[^chen]: Chen, Y. et al. (2025). [*Reasoning Models Don’t Always Say What They Think*](https://arxiv.org/abs/2505.05410).
[^vaswani]: Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762).
[^ouyang]: Ouyang, L. et al. (2022). [*Training language models to follow instructions with human feedback*](https://arxiv.org/abs/2203.02155).
