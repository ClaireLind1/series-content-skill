# 从台词清单，到公众号文章

一个把你记下的剧集英语台词、表达和疑问，整理成讲解内容与公众号文章的 Agent Skill。下面以《匹兹堡医护前线》（The Pitt）系列为实际案例。

**[打开完整网页演示 →](https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html)** · [查看 Skill 指令](skills/series-content-skill/SKILL.md) · [English](README.en.md)

## 它能帮你做什么

- **整理台词笔记：**逐条解释你选出的英文台词、词句或疑问，补充语境、术语、缩写、发音、中文释义和例句；无法确认的内容会标注待核实。
- **组织文章内容：**把逐条讲解整理成有主题和阅读顺序的系列文章；也可以只要词条清单、提纲或内容审校。
- **生成公众号排版：**输出 Markdown 和带「复制排版内容」按钮的 HTML，复制正文后即可粘贴到公众号图文编辑器。

## 公众号文章预览

这是实际文章 HTML 的渲染效果。点击图片可打开完整网页，滚动查看文章排版和系列案例。

[![公众号文章 HTML 实际排版预览](assets/article-preview.png)](https://clairelind1.github.io/series-content-skill/skills/series-content-skill/showcase.html)

## 已发布文章精选

- [第 1 篇｜开场与口语](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484003&idx=1&sn=322c6f034dba8d2993a80e43d62d8ca4&scene=21#wechat_redirect)
- [第 9 篇｜鉴别诊断与收治](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484137&idx=1&sn=adc7593300449d60e0ca8bd060d6fa24&scene=21#wechat_redirect)
- [第 17 篇｜呕吐与误食](https://mp.weixin.qq.com/s?__biz=Mzg2ODY0MDQ0MQ==&mid=2247484211&idx=1&sn=ace509093aa2d55a8ba42343a0923f20&scene=21#wechat_redirect)

## 从文章到发布

打开文章 HTML，点击「复制排版内容」；在[微信公众号后台](https://mp.weixin.qq.com/)新建图文并粘贴正文，填写标题等图文信息，预览确认后发布。

## 使用

将仓库中的 `skills/series-content-skill` 加载到支持 Agent Skills 的 AI 工具中。把自己记下的台词、表达或问题发给 AI，并说明希望整理成清单、提纲还是文章。

本地查看网页演示：在仓库根目录运行 `python -m http.server 8000`，打开 `http://localhost:8000/skills/series-content-skill/showcase.html`。
