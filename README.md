# 从看剧笔记，到公众号文章

一个把你记下的剧集英语台词、表达和疑问，整理成讲解内容与公众号文章的 Agent Skill。下面以《匹兹堡医护前线》（The Pitt）系列为实际案例。

**[打开完整网页演示 →](https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html)** · [查看给 AI 加载的 Skill 指令](skills/series-content-skill/SKILL.md) · [English](README.en.md)

## 它能帮你做什么

- **整理台词笔记：** 逐条解释你选出的英文台词、词句或疑问，补充语境、术语、缩写、发音、中文释义和例句；无法确认的内容会标注待核实。
- **组织文章内容：** 把逐条讲解整理成有主题和阅读顺序的系列文章；也可以只要词条清单、提纲或内容审校。
- **生成公众号排版：** 输出 Markdown 和带「复制排版内容」按钮的 HTML，复制正文后即可粘贴到公众号图文编辑器。

## 公众号文章预览

展示页使用响应式 Grid 并排展示第 24 篇《急诊沟通与疼痛评估》和本项目推广文章。桌面端并排浏览，手机端自动切换为单列；每篇都可以在框内滚动预览，也可以单独打开。下面两张图展示第 24 篇的文章封面与文中术语配图。

<table>
  <tr>
    <td width="50%"><a href="https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html"><img src="assets/article-preview-24-cover.jpg" alt="第 24 篇公众号文章封面：急诊沟通与疼痛评估"></a><br><sub>第 24 篇 · 急诊沟通与疼痛评估</sub></td>
    <td width="50%"><a href="https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html"><img src="assets/article-preview-24-terminology.jpg" alt="第 24 篇医学英语配图：正常红细胞与镰状红细胞"></a><br><sub>文中配图 · 中英文术语说明</sub></td>
  </tr>
</table>

- [打开 Grid 文章预览页](https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html)
- [单独预览项目推广文章](https://clairelind1.github.io/series-content-skill/examples/series-content-skill-intro.html)

## 已发布文章精选

- [第 1 篇｜开场与口语](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484003&idx=1&sn=322c6f034dba8d2993a80e43d62d8ca4&scene=21#wechat_redirect)
- [第 9 篇｜鉴别诊断与收治](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484137&idx=1&sn=adc7593300449d60e0ca8bd060d6fa24&scene=21#wechat_redirect)
- [第 17 篇｜呕吐与误食](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484211&idx=1&sn=ace509093aa2d55a8ba42343a0923f20&scene=21#wechat_redirect)

## 从文章到发布

打开文章 HTML，点击「复制排版内容」；在[微信公众号后台](https://mp.weixin.qq.com/)新建图文并粘贴正文，填写标题等图文信息，预览确认后发布。

## 下载与安装

### 方式一：用命令行安装

复制下面适合你电脑的命令，在终端（Windows 用 PowerShell）中运行。命令会下载项目，并把 Skill 安装到 Codex 的用户级目录。

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

以上命令安装到 Codex。若使用 Claude Code 或 Cursor，把目标目录中的 `.agents` 分别改为 `.claude` 或 `.cursor`（路径见下表）。安装后重启 Agent；Codex 可输入 `$series-content-skill` 调用。

### 方式二：下载 ZIP，手动安装

1. 打开 [GitHub 项目页](https://github.com/ClaireLind1/series-content-skill)，点击绿色 **Code** 按钮，再点 **Download ZIP**。
2. 下载完成后，在电脑「下载」文件夹里找到 ZIP，右键选择「全部解压」（macOS 可双击解压）。
3. 打开解压后的项目文件夹，依次进入 `skills` → `series-content-skill`。确认 `SKILL.md` 就在这个文件夹里面。
4. 复制整个 `series-content-skill` 文件夹，粘贴到下表中 Agent 的「用户级目录」。只想在某个项目使用时，则放到「项目级目录」。
5. 如果目标目录还不存在，就按表格路径逐层新建；粘贴后确认最终路径以 `series-content-skill/SKILL.md` 结尾，再重启或重新打开 Agent。

| Agent | 用户级安装目录 | 项目级安装目录 |
|---|---|---|
| Codex | Windows：`%USERPROFILE%\.agents\skills\`<br>macOS/Linux：`~/.agents/skills/` | `<项目>/.agents/skills/` |
| Claude Code | Windows：`%USERPROFILE%\.claude\skills\`<br>macOS/Linux：`~/.claude/skills/` | `<项目>/.claude/skills/` |
| Cursor | Windows：`%USERPROFILE%\.cursor\skills\`<br>macOS/Linux：`~/.cursor/skills/` | `<项目>/.cursor/skills/` |

**文件夹结构应当是：**

```text
skills/
└── series-content-skill/
    ├── SKILL.md
    ├── SKILL.en.md
    ├── agents/
    └── references/
```

注意：复制 `skills` 里面的 `series-content-skill` 文件夹，不是整个下载的项目文件夹；不要多套一层同名文件夹。重启 Agent 后，Codex 可输入 `$series-content-skill` 调用。也可以在请求里提到 `series-content-skill`，例如：「用它整理这些英文台词，输出逐条讲解清单。」你可以要求它只做词条清单、提纲、审校或完整文章。

单独安装 Skill 文件夹即可处理你提供的材料。若还要查看 The Pitt 案例、文章 HTML 和生成脚本，请保留整个下载的项目文件夹。

### 本地查看网页演示

在解压后的仓库根目录运行 `python -m http.server 8000`，再打开 `http://localhost:8000/skills/series-content-skill/showcase.html`。


