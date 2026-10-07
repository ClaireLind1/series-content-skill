---
name: series-content-skill
description: >-
  Turn user-selected English dialogue, expressions, viewing notes, or questions from a TV or film
  into contextual explanations, language-learning articles, and WeChat-ready HTML. Use for
  planning, terminology notes, drafting, reviewing, or requested learning extras.
---

# Series English Content Studio

## Purpose

Help users turn English material they selected while watching a series or film into clear,
context-rich Chinese learning content and, when requested, long-form articles for a WeChat Official
Account. Users choose what is worth organizing. Notes may be exact lines, approximate transcriptions,
expressions, words, or questions in any format. Never imply that the Skill watches episodes, discovers
unknown lines, or retrieves subtitles that were not provided.

Explain each selected item in context and add useful terminology, pronunciation, collocations, Chinese
explanations, or original teaching examples as appropriate. Create an outline or article only when
requested. Generate WeChat HTML with a “Copy formatted content” button when a suitable renderer is
available. Quizzes and answer keys are optional, never default deliverables.

## Repository example

This repository demonstrates the workflow with *The Pitt*, a medical drama. Its sample article,
medical terminology, data, and renderer are specific examples, not assumptions for other shows. For
other series, use the user's material and adapt the examples only as structural or visual references.

- `examples/pitt_t07_layout.py` — sample layout and Markdown/HTML helpers.
- `examples/pitt_ep1_17_data.py` and `examples/pitt_ep1_10_data.py` — sample content data.
- `examples/build-the-pitt-ep1-10-html.py` — sample article builder.
- `examples/the-pitt-ep1-terminology-9.html` — rendered article example.
- Root `AGENTS.md` — project rules for the sample assets.

## Modes

- **Plan:** return an angle, context to establish, outline, useful language, and verification items.
- **Explain:** organize the user's selected notes one by one; keep uncertain wording marked as such.
- **Draft:** arrange approved explanations for the requested audience and scope. Distinguish source
  dialogue, paraphrase, and original teaching examples.
- **Review:** check context, terms, translation, quotation status, flow, and series consistency.
- **Extras:** create only the quiz or answer explanation requested.

Do not turn planning, explanation, or proofreading into a full article unless requested.

## WeChat delivery

For HTML deliverables, tell the user to open the file, click “Copy formatted content,” sign in at
`https://mp.weixin.qq.com/`, create a new article, paste the body, fill in title/author/summary/cover
separately, preview, save as a draft, and publish when ready. Copying the body does not fill in metadata
or upload a cover. This workflow does not require an API or third-party layout plugin.

Read [the editorial workflow](references/editorial-workflow.en.md) when detailed guidance is needed.
For The Pitt samples, follow root `AGENTS.md`; for other shows, do not import show-specific facts or
content.

## Evidence and accuracy

1. Quote dialogue verbatim only when supplied by the user or verified from a reliable source. Label
   paraphrases and approximate transcriptions accurately; mark unresolved wording for verification.
2. Explain language in context and register. Add terminology and domain details when they help.
3. Verify specialized factual claims as needed. Medical explanations are educational context, not
   clinical guidance.
4. Never invent plot, dialogue, or facts to bridge gaps.
5. Preserve approved content during layout changes and report unresolved checks clearly.
6. Do not claim WeChat editor paste validation without testing it.

Deliver only what the user asked for: explanations, an outline, an article, WeChat HTML, review notes,
or requested derivatives. Add builders and content data when the project workflow needs them.
