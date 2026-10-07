---
name: series-content-skill
description: >-
  Turn user-selected English dialogue, expressions, viewing notes, or questions from a TV or film
  into contextual explanations, language-learning articles, and WeChat-ready HTML. Use for
  planning, terminology notes, drafting, reviewing, or requested learning extras.
---

# Series English Content Studio

## Purpose

Help the user turn English material they selected while watching a series or film into clear,
context-rich Chinese learning content and, when requested, a long-form article for a WeChat Official
Account. The user decides what is worth organizing. Notes may be exact lines, approximate
transcriptions, expressions, words, or questions; any format is acceptable. Do not imply that this
Skill watches episodes, finds the user's unknown lines, or retrieves unprovided subtitles.

For each selected item, explain its meaning in context and add useful terminology, pronunciation,
collocations, Chinese explanations, or original teaching examples as appropriate. Organize reviewed
material into an outline or article only when requested. Generate WeChat HTML with a “Copy formatted
content” button when the project includes a suitable renderer. Quizzes and answer keys are optional
extras, never default deliverables.

## This repository's example

The repository demonstrates the workflow with *The Pitt*, a medical drama. Its sample article,
medical terminology, data, and renderer are examples for that series; do not reuse them as facts or
assume another show is medical. For a different series, work from the user's material and adapt the
examples only as a structural or visual reference.

Useful files in this repository:

- `examples/pitt_t07_layout.py` — The Pitt sample's article layout and Markdown/HTML helpers.
- `examples/pitt_ep1_17_data.py` and `examples/pitt_ep1_10_data.py` — sample article data.
- `examples/build-the-pitt-ep1-10-html.py` — sample article builder.
- `examples/the-pitt-ep1-terminology-9.html` — rendered article example.
- Root `AGENTS.md` — project rules, including boundaries for using the sample assets.

## Modes

- **Plan:** return a topic angle, context to establish, outline, useful language to explain, and items
  needing verification. Do not expand a plan into a full article unless asked.
- **Explain selected material:** handle the user's chosen notes one by one. Keep approximate wording
  marked as uncertain; do not silently convert it into a verified quote.
- **Draft or continue an article:** organize the approved explanations around a clear theme and the
  requested audience. Keep source dialogue, paraphrase, and original teaching examples distinct.
- **Review:** check context, terms, translation, quotations, flow, and series consistency. Preserve
  structure and wording when the user asks only for proofreading.
- **Make extras:** create only the quiz or answer explanation the user requested.

## WeChat delivery

When the output includes article HTML, explain this workflow:

1. Open the HTML and click “Copy formatted content.”
2. Sign in at `https://mp.weixin.qq.com/`.
3. Create a new article and paste into the body editor.
4. Fill in the title, author, summary, and cover separately.
5. Preview, save as a draft, and publish from the Official Account backend when ready.

Copying the body does not fill in article metadata or upload a cover. Do not ask the user to configure
an API, developer key, or third-party layout plugin for this copy-and-paste workflow.

Read [the editorial workflow](references/editorial-workflow.md) for detailed guidance. When working
on The Pitt samples in this repository, follow root `AGENTS.md`; for other shows, use its constraints
only where they are genuinely general and never import show-specific facts or content.

## Evidence and accuracy

1. Use only user-provided or reliably verified dialogue as a verbatim quote. Label paraphrases and
   approximate transcriptions accurately; mark unresolved wording “待核实”.
2. Explain expressions in their scene and register. Add terminology and domain context only when it
   helps the learner.
3. Verify factual claims in specialized domains against reliable sources when needed. Medical
   explanations are educational context, not clinical guidance.
4. Do not invent plot, dialogue, or facts to bridge gaps.
5. Protect approved content when editing layout. State unresolved checks and delivery status clearly.
6. Do not claim WeChat editor paste validation without actually testing the paste.

## Typical deliverables

Depending on the user's request: a selected-expression list with explanations; an outline; an article
in Markdown; WeChat-ready HTML; a review with verification notes; or requested derivative material.
For a complete article, include a scene-setting opening, organized explanations, useful examples, and
an ending appropriate to the user's series. Include a regenerable builder and content data only when
the project workflow calls for them.
