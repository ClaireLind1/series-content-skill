# From Dialogue Notes to WeChat Articles

An Agent Skill that turns English dialogue, expressions, and questions you note while watching a series into explanations and WeChat Official Account articles. The Pitt is the real case study featured here.

**[Open the full web demo →](https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html)** · [Skill instructions](skills/series-content-skill/SKILL.en.md) · [中文介绍](README.md)

## What it can do

- **Explain your notes:** Clarify the lines, expressions, or questions you selected, adding context, terminology, abbreviations, pronunciation, Chinese meaning, and examples. Unverified details are flagged.
- **Shape article content:** Organize explanations into themed series articles, or provide a glossary, outline, or editorial review.
- **Format for WeChat:** Generate Markdown and HTML with a “Copy formatted content” button, ready to paste into the WeChat article editor.

## Article preview

The showcase uses a responsive CSS Grid to display the latest series sample, Article 24, alongside this project-introduction article. It switches to a single column on mobile. Both articles can be scrolled in place or opened separately. The images below show Article 24’s cover and an illustration from the article.

<table>
  <tr>
    <td width="50%"><a href="https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html"><img src="assets/article-preview-24-cover.jpg" alt="Article 24 cover: Emergency communication and pain assessment"></a><br><sub>Article 24 · Emergency communication and pain assessment</sub></td>
    <td width="50%"><a href="https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html"><img src="assets/article-preview-24-terminology.jpg" alt="Article illustration: normal and sickle-shaped red blood cells"></a><br><sub>Illustration · Terminology in Chinese and English</sub></td>
  </tr>
</table>

- [Open the Grid article preview](https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html)
- [Open the project-introduction article](https://clairelind1.github.io/series-content-skill/examples/series-content-skill-intro.html)

## Published articles

- [Article 1 | Opening and conversational English](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484003&idx=1&sn=322c6f034dba8d2993a80e43d62d8ca4&scene=21#wechat_redirect)
- [Article 9 | Differential diagnosis and admission](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484137&idx=1&sn=adc7593300449d60e0ca8bd060d6fa24&scene=21#wechat_redirect)
- [Article 17 | Vomiting and accidental ingestion](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484211&idx=1&sn=ace509093aa2d55a8ba42343a0923f20&scene=21#wechat_redirect)

## From article to publication

Open the article HTML and click “Copy formatted content.” In the [WeChat Official Account platform](https://mp.weixin.qq.com/), create an article, paste the body, fill in the article details, preview, and publish.

## Download and install

### Option 1: Install from the command line

Copy and run the commands for your computer in a terminal (PowerShell on Windows). They download the project and install the Skill in Codex's user-level directory.

**Windows · PowerShell**

```powershell
git clone https://github.com/ClaireLind1/series-content-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\series-content-skill\skills\series-content-skill" "$env:USERPROFILE\.agents\skills\"
```

**macOS / Linux · Terminal**

```bash
git clone https://github.com/ClaireLind1/series-content-skill.git
mkdir -p ~/.agents/skills
cp -R series-content-skill/skills/series-content-skill ~/.agents/skills/
```

These commands install to Codex. For Claude Code or Cursor, replace `.agents` in the destination with `.claude` or `.cursor` (see the table below). Restart your Agent after installation; invoke the Skill in Codex with `$series-content-skill`.

### Option 2: Download the ZIP and install manually

1. Open the [GitHub project page](https://github.com/ClaireLind1/series-content-skill), click the green **Code** button, then choose **Download ZIP**.
2. Find the ZIP in your Downloads folder and extract it (double-click on macOS, or right-click and choose **Extract All** on Windows).
3. Open the extracted project folder and go to `skills` → `series-content-skill`. Confirm that `SKILL.md` is directly inside this folder.
4. Copy the entire `series-content-skill` folder to the user-level directory for your Agent in the table below. To make it available in only one project, use the project-level directory instead.
5. If a destination folder does not exist, create it. After copying, confirm the final path ends in `series-content-skill/SKILL.md`, then restart or reopen your Agent.

| Agent | User-level directory | Project-level directory |
|---|---|---|
| Codex | Windows: `%USERPROFILE%\.agents\skills\`<br>macOS/Linux: `~/.agents/skills/` | `<project>/.agents/skills/` |
| Claude Code | Windows: `%USERPROFILE%\.claude\skills\`<br>macOS/Linux: `~/.claude/skills/` | `<project>/.claude/skills/` |
| Cursor | Windows: `%USERPROFILE%\.cursor\skills\`<br>macOS/Linux: `~/.cursor/skills/` | `<project>/.cursor/skills/` |

**The installed folder should look like this:**

```text
skills/
└── series-content-skill/
    ├── SKILL.md
    ├── SKILL.en.md
    ├── agents/
    └── references/
```

Copy the `series-content-skill` folder inside `skills`, not the entire downloaded project folder. Do not add an extra nested folder with the same name. After restarting your Agent, invoke it in Codex by entering `$series-content-skill`. You can also mention `series-content-skill` in your request, for example: “Use it to turn these dialogue notes into an explained glossary.” Ask for a glossary, outline, review, or complete article.

The Skill works from the material you provide. Keep the full repository if you also want the The Pitt case study, sample article HTML, and builder scripts.

### Preview the web demo locally

From the extracted repository root, run `python -m http.server 8000` and open `http://localhost:8000/skills/series-content-skill/showcase.html`.

