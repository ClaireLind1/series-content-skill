# -*- coding: utf-8 -*-
"""Shared T07 layout for The Pitt WeChat series (from article 9 onward)."""
from __future__ import annotations

import re

FONT = (
    "-apple-system, BlinkMacSystemFont, 'PingFang SC', "
    "'Helvetica Neue', 'Microsoft YaHei', sans-serif"
)

BRAND_GREEN = "#8A9470"

THEMES = {
    "sage": {
        "accent": "#8A9470",
        "tip_bg": "#E8EDD8",
        "tip_border": "#9FA882",
        "tip_strong": "#8A9470",
        "tip_text": "#383838",
        "figure_bg": "#F4F6EE",
    },
    "blue": {
        "accent": "#738291",
        "tip_bg": "#EEF1F4",
        "tip_border": "#8A9AA8",
        "tip_strong": "#738291",
        "tip_text": "#2F3840",
        "figure_bg": "#F4F6F8",
    },
    "dust": {
        "accent": "#A89090",
        "tip_bg": "#F0E4E4",
        "tip_border": "#B8A0A0",
        "tip_strong": "#A89090",
        "tip_text": "#383838",
        "figure_bg": "#F8F3F3",
    },
    "lavender": {
        "accent": "#9890AD",
        "tip_bg": "#E4DFEC",
        "tip_border": "#B0A8C4",
        "tip_strong": "#9890AD",
        "tip_text": "#383838",
        "figure_bg": "#F7F4FB",
    },
}

SECTION_THEME_ORDER = ("sage", "blue", "dust", "lavender")

COPY_SCRIPT = """
<script>
function wechatSafeHtml(html) {
  html = html.replace(/<!--[\\s\\S]*?-->/g, '');
  html = html.replace(/>\\s+</g, '><');
  html = html.replace(/<p\\b/gi, '<section');
  html = html.replace(/<\\/p>/gi, '</section>');
  return html;
}
function copyContent() {
  var target = document.getElementById('copy-target');
  var tail = document.getElementById('copy-target-tail');
  var html = wechatSafeHtml(target.innerHTML + (tail ? tail.innerHTML : ''));
  var holder = document.createElement('div');
  holder.innerHTML = html;
  var plain = holder.innerText.replace(/\\n{2,}/g, '\\n');
  if (navigator.clipboard && window.ClipboardItem) {
    var blob = new Blob([html], { type: 'text/html' });
    var plainBlob = new Blob([plain], { type: 'text/plain' });
    navigator.clipboard.write([new ClipboardItem({ 'text/html': blob, 'text/plain': plainBlob })])
      .then(function () { alert('已复制，可粘贴到公众号编辑器'); })
      .catch(function () { fallbackCopy(holder); });
  } else {
    fallbackCopy(holder);
  }
}
function fallbackCopy(el) {
  var range = document.createRange();
  range.selectNodeContents(el);
  var sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  try { document.execCommand('copy'); alert('已复制'); } catch (e) { alert('复制失败，请手动选择'); }
  sel.removeAllRanges();
}
</script>
"""


def tip_box(tips: list[str], theme: dict) -> str:
    if not tips:
        return ""
    o_count = sum(1 for t in tips if t.startswith("○"))
    has_extra = any(not t.startswith("○") for t in tips)
    if o_count == 1 and not has_extra:
        t = tips[0]
        return (
            f'<p style="margin:10px 0 0;font-size:14px;line-height:1.75;'
            f'color:{theme["tip_text"]};text-align:left;">'
            f'<span style="display:inline-block;padding:3px 10px;border-radius:980px;'
            f'background:{theme["tip_bg"]};background-color:{theme["tip_bg"]};'
            f'border:1px solid {theme["tip_border"]};">{t}</span></p>'
        )
    lines = []
    for i, t in enumerate(tips):
        last = i == len(tips) - 1
        is_header = t.startswith("<strong")
        if is_header and i > 0:
            margin = "10px 0 0" if last else "10px 0 4px"
        else:
            margin = "0" if last else "0 0 4px"
        nested = not t.startswith("○") and not t.startswith("<strong")
        pad = "padding-left:1.25em;" if nested else ""
        lines.append(
            f'<p style="margin:{margin};{pad}font-size:14px;line-height:1.75;'
            f'color:{theme["tip_text"]};text-align:left;">{t}</p>'
        )
    return (
        f'<section style="margin:0;padding:12px 14px;border-radius:12px;'
        f'border:1px solid {theme["tip_border"]};background:{theme["tip_bg"]};'
        f'background-color:{theme["tip_bg"]};">'
        + "".join(lines)
        + "</section>"
    )


def figure_box(fig: dict, theme: dict, has_after: bool) -> str:
    caption = fig.get("caption", "")
    sub = fig.get("sub", "")
    inner = caption
    if sub:
        inner += f"<br>{sub}"
    margin = "0 0 10px" if has_after else "0"
    return (
        f'<section style="margin:{margin};padding:48px 14px;border-radius:12px;'
        f'border:1px dashed {theme["tip_border"]};background:{theme["figure_bg"]};'
        f'background-color:{theme["figure_bg"]};">'
        f'<p style="margin:0;font-size:13px;line-height:1.7;color:{theme["accent"]};text-align:center;">{inner}</p>'
        f"</section>"
    )


def as_list(val) -> list:
    if not val:
        return []
    if isinstance(val, list):
        return val
    return [val]


def _split_example(ex: str) -> tuple[str, str]:
    m = re.match(r"<em>(.*?)</em>\s*(.*)$", ex, flags=re.DOTALL)
    if m:
        return m.group(1), m.group(2)
    return ex, ""


def merge_examples(examples: list[str]) -> list[str]:
    if len(examples) < 3:
        return examples
    merged: list[str] = []
    i = 0
    while i < len(examples):
        if i + 1 < len(examples):
            en1, zh1 = _split_example(examples[i])
            en2, zh2 = _split_example(examples[i + 1])
            merged.append(f"<em>{en1} — {en2}</em><br>{zh1}——{zh2}")
            i += 2
        else:
            merged.append(examples[i])
            i += 1
    return merged


def entry_html(idx: int, e: dict, theme: dict, is_first: bool, is_last: bool) -> str:
    accent = theme["accent"]
    top_margin = "16px 0 14px" if is_first else "0 0 14px"
    pad = "0" if is_last else "0 0 14px"
    border = "" if is_last else "border-bottom:1px solid #E5E5EA;"
    bodies = as_list(e.get("bodies") or e.get("body"))
    examples = merge_examples(as_list(e.get("examples") or e.get("example")))
    after = as_list(e.get("after"))
    sources = as_list(e.get("sources"))
    figure = e.get("figure")
    more_after_example = bool(
        e.get("dialogue") or e.get("tips") or after or sources or len(examples) > 1
    )
    more_after_body = bool(examples or e.get("dialogue") or after or sources or e.get("tips") or figure)

    parts = [
        f'<section style="margin:{top_margin};padding:{pad};{border}">',
        f'<p style="margin:0 0 8px;font-size:18px;font-weight:700;line-height:1.45;color:#383838;">'
        f'<span style="font-size:18px;font-weight:700;color:{accent};">{idx}. </span>'
        f'{e["title"]}</p>',
    ]
    if e.get("phonetic"):
        parts.append(
            f'<p style="margin:0 0 6px;font-size:13px;line-height:1.6;color:#888888;text-align:left;">{e["phonetic"]}</p>'
        )
    for i, b in enumerate(bodies):
        last_body = i == len(bodies) - 1
        margin = "0 0 8px" if (not last_body or more_after_body) else "0"
        parts.append(
            f'<p style="margin:{margin};font-size:14px;line-height:1.7;color:#666666;text-align:left;">{b}</p>'
        )
    if figure:
        has_after = bool(examples or after or e.get("dialogue") or e.get("tips"))
        parts.append(figure_box(figure, theme, has_after))
    for i, ex in enumerate(examples):
        last_ex = i == len(examples) - 1
        if last_ex and not more_after_example:
            margin = "0"
        else:
            margin = "0 0 8px" if (not last_ex or after) else "0 0 10px"
            if last_ex and e.get("dialogue") and not after:
                margin = "0 0 10px"
            if last_ex and e.get("tips") and not after and not e.get("dialogue"):
                margin = "0 0 10px"
        parts.append(
            f'<p style="margin:{margin};font-size:15px;line-height:1.85;color:#383838;text-align:left;">{ex}</p>'
        )
    for i, line in enumerate(after):
        last_a = i == len(after) - 1
        margin = "0 0 10px" if last_a and (e.get("dialogue") or e.get("tips")) else ("0" if last_a else "0 0 4px")
        if last_a and not e.get("dialogue") and not e.get("tips"):
            margin = "0"
        parts.append(
            f'<p style="margin:{margin};font-size:14px;line-height:1.75;color:#383838;text-align:left;">{line}</p>'
        )
    if e.get("dialogue"):
        d = e["dialogue"]
        d_margin = "0 0 10px" if e.get("tips") else "0"
        parts.append(
            f'<section style="margin:{d_margin};padding:12px 14px;border-radius:12px;'
            f'border:1px solid {theme["tip_border"]};background:{theme["tip_bg"]};'
            f'background-color:{theme["tip_bg"]};">'
            f'<p style="margin:0 0 6px;font-size:13px;letter-spacing:1px;color:{accent};">剧中对话</p>'
            + "".join(
                f'<p style="margin:0 0 4px;font-size:15px;line-height:1.75;color:#383838;text-align:left;">{line}</p>'
                for line in d["lines"]
            )
            + f'<p style="margin:0;font-size:14px;line-height:1.75;color:#383838;text-align:left;">{d["zh"]}</p>'
            + "</section>"
        )
    if e.get("tips"):
        parts.append(tip_box(e["tips"], theme))
    if sources:
        for i, line in enumerate(sources):
            last_s = i == len(sources) - 1
            margin = "10px 0 0" if i == 0 and last_s else (
                "10px 0 4px" if i == 0 else ("0" if last_s else "0 0 4px")
            )
            parts.append(
                f'<p style="margin:{margin};font-size:13px;line-height:1.7;color:#888888;text-align:left;">{line}</p>'
            )
    parts.append("</section>")
    return "\n      ".join(parts)


def section_html(label: str, title: str, theme_key: str, entries: list[dict]) -> str:
    theme = THEMES[theme_key]
    accent = theme["accent"]
    body = []
    for i, e in enumerate(entries):
        body.append(
            entry_html(
                i + 1,
                e,
                theme,
                is_first=(i == 0),
                is_last=(i == len(entries) - 1),
            )
        )
    return f"""
<!-- {title} -->
<section style="margin:0;padding:12px 16px 8px;font-family:{FONT};background:#E8E4DE;background-color:#E8E4DE;">
  <section style="margin:0;padding:28px 22px 24px;border-radius:12px;border:1px solid #D1D1D6;background:#FAFAFA;background-color:#FAFAFA;">
    <section style="margin:0 0 6px;">
      <p style="margin:0 0 6px;font-size:12px;letter-spacing:1px;color:{accent};">{label} · 共 {len(entries)} 条</p>
      <p style="margin:0;font-size:22px;font-weight:700;line-height:1.38;color:#383838;padding-bottom:10px;border-bottom:2px solid {accent};">{title}</p>
    </section>
    <section style="margin:0;">
      {"".join(body)}
    </section>
  </section>
</section>
"""


def to_md(s: str) -> str:
    s = s.replace("<br>", "\n").replace("<br/>", "\n")
    s = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', r"[\2](\1)", s)
    s = re.sub(r"<strong[^>]*>", "**", s)
    s = s.replace("</strong>", "**")
    s = re.sub(r"<em>", "*", s)
    s = s.replace("</em>", "*")
    s = re.sub(r"<[^>]+>", "", s)
    return s


def entry_md(idx: int, e: dict) -> str:
    lines = [f"#### {idx}. {e['title']}", ""]
    if e.get("phonetic"):
        lines += [to_md(e["phonetic"]), ""]
    for b in as_list(e.get("bodies") or e.get("body")):
        lines += [to_md(b), ""]
    if e.get("figure"):
        fig = e["figure"]
        lines.append(f"**{to_md(fig.get('caption', ''))}**")
        if fig.get("sub"):
            lines.append(to_md(fig["sub"]))
        lines.append("")
    for ex in as_list(e.get("examples") or e.get("example")):
        lines += [to_md(ex), ""]
    for a in as_list(e.get("after")):
        lines.append(to_md(a))
    if e.get("after"):
        lines.append("")
    if e.get("dialogue"):
        d = e["dialogue"]
        for line in d["lines"]:
            lines.append(to_md(line))
        lines += [to_md(d["zh"]), ""]
    if e.get("tips"):
        for t in e["tips"]:
            md = to_md(t)
            if not t.startswith("○") and not t.startswith("<strong"):
                lines.append("  " + md)
            else:
                lines.append(md)
        lines.append("")
    if e.get("sources"):
        for s in as_list(e["sources"]):
            lines.append(to_md(s))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def structure_line(blocks: list[tuple[str, list]]) -> str:
    bits = []
    for title, entries in blocks:
        name = title.split("、", 1)[-1] if "、" in title else title
        bits.append(f"{name} {len(entries)} 条")
    return "本篇共四块：" + " / ".join(bits) + "。"


def opening_html(series_line: str, h1: str, preface_paras: list[str] | None = None) -> str:
    preface_block = ""
    h1_margin = "0"
    if preface_paras:
        h1_margin = "0 0 16px"
        paras = []
        for i, p in enumerate(preface_paras):
            margin = "0" if i == len(preface_paras) - 1 else "0 0 12px"
            paras.append(
                f'<p style="margin:{margin};font-size:15px;line-height:1.9;color:#383838;text-align:left;">{p}</p>'
            )
        preface_block = (
            f'<section style="margin:0;padding:16px;border-radius:12px;'
            f'background:#F4ECD7;background-color:#F4ECD7;border:1px solid #D9CEB0;'
            f'border-top:3px solid {BRAND_GREEN};">'
            f'<p style="margin:0 0 10px;font-size:14px;letter-spacing:1px;color:#6E6248;">前言</p>'
            f'{"".join(paras)}</section>'
        )
    return f"""
<!-- 开篇 -->
<section style="margin:0;padding:20px 16px 8px;font-family:{FONT};background:#E8E4DE;background-color:#E8E4DE;">
  <section style="margin:0;padding:28px 22px 24px;border-radius:12px;border:1px solid #D1D1D6;background:#FAFAFA;background-color:#FAFAFA;">
    <p style="margin:0 0 8px;font-size:12px;letter-spacing:1px;color:#888888;">{series_line}</p>
    <p style="margin:{h1_margin};font-size:22px;font-weight:700;line-height:1.4;color:#383838;">{h1}</p>
    {preface_block}
  </section>
</section>
"""


def quiz_html(question: str, options: list[str], footer: str, wrap_id: str = "") -> str:
    opt_ps = []
    for i, opt in enumerate(options):
        margin = "0 0 12px" if i == len(options) - 1 else "0 0 4px"
        opt_ps.append(
            f'<p style="margin:{margin};font-size:15px;line-height:1.85;color:#383838;text-align:left;">{opt}</p>'
        )
    id_attr = f' id="{wrap_id}"' if wrap_id else ""
    return f"""
<!-- 小测试 -->
<section{id_attr} style="margin:0;padding:12px 16px 8px;font-family:{FONT};background:#E8E4DE;background-color:#E8E4DE;">
  <section style="margin:0;padding:28px 22px 24px;border-radius:12px;border:1px solid #D1D1D6;background:#FAFAFA;background-color:#FAFAFA;">
    <section style="margin:0;padding:18px 16px;border-radius:12px;background:#EEF1F4;background-color:#EEF1F4;border:1px solid #8A9AA8;border-top:3px solid {BRAND_GREEN};">
      <p style="margin:0 0 10px;font-size:14px;letter-spacing:1px;color:#738291;">小测试</p>
      <p style="margin:0 0 12px;font-size:15px;line-height:1.9;color:#383838;text-align:left;">{question}</p>
      {"".join(opt_ps)}
      <p style="margin:0;font-size:14px;line-height:1.7;color:#666666;text-align:left;">{footer}</p>
    </section>
  </section>
</section>
"""


def closing_html(body: str, signoff: str = "下篇文章见~") -> str:
    if body and signoff:
        text = (
            f'<p style="margin:0 0 12px;font-size:15px;line-height:1.9;color:#383838;text-align:left;">{body}</p>'
            f'<p style="margin:0;font-size:15px;line-height:1.9;color:#383838;text-align:center;">{signoff}</p>'
        )
    elif signoff:
        text = (
            f'<p style="margin:0;font-size:15px;line-height:1.9;color:#383838;text-align:center;">{signoff}</p>'
        )
    else:
        text = (
            f'<p style="margin:0;font-size:15px;line-height:1.9;color:#383838;text-align:left;">{body}</p>'
        )
    return f"""
<!-- 收束 -->
<section style="margin:0;padding:12px 16px 8px;font-family:{FONT};background:#E8E4DE;background-color:#E8E4DE;">
  <section style="margin:0;padding:28px 22px 24px;border-radius:12px;border:1px solid #D1D1D6;background:#FAFAFA;background-color:#FAFAFA;">
    <section style="margin:0;padding:18px 16px;border-radius:12px;background:#F4ECD7;background-color:#F4ECD7;border:1px solid #D9CEB0;border-top:3px solid {BRAND_GREEN};">
      {text}
    </section>
  </section>
</section>
"""


def about_html(line: str) -> str:
    return f"""
<!-- T99 -->
<section style="margin:0;padding:12px 16px 28px;font-family:{FONT};background:#E8E4DE;background-color:#E8E4DE;">
  <section style="margin:0;padding:16px 20px;border-radius:12px;border:1px solid #D1D1D6;background:#EEEEEE;background-color:#EEEEEE;">
    <section style="margin:0 0 10px;height:1px;background:#CCCCCC;"></section>
    <p style="margin:0 0 8px;font-size:12px;letter-spacing:1px;color:#666666;">关于本篇</p>
    <p style="margin:0 0 4px;font-size:13px;line-height:1.7;color:#383838;">{line}</p>
    <p style="margin:0;font-size:13px;line-height:1.7;color:#666666;text-align:right;">关注账号，获取更多内容~</p>
  </section>
</section>
"""


def article_tail(about_line: str) -> str:
    return about_html(about_line)


def html_document(
    page_title: str,
    toolbar_note: str,
    inner: str,
    extra_html: str = "",
    inner_after: str = "",
) -> str:
    tail_block = (
        f'  <div id="copy-target-tail">\n{inner_after}\n  </div>\n' if inner_after else ""
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <style>
    body {{ margin: 0; padding: 24px 16px 48px; background: #E8E4DE; font-family: {FONT}; }}
    .page {{ max-width: 680px; margin: 0 auto; }}
    .toolbar {{ text-align: center; margin-bottom: 20px; }}
    .toolbar button {{ background: #5C5348; color: #FAF6EC; border: none; border-radius: 980px; padding: 12px 28px; font-size: 15px; cursor: pointer; font-family: inherit; }}
    .toolbar p {{ font-size: 13px; color: #6B6560; margin-top: 10px; line-height: 1.6; }}
  </style>
</head>
<body>
<div class="page">
  <div class="toolbar">
    <button type="button" onclick="copyContent()">复制排版内容</button>
    <p>{toolbar_note}</p>
  </div>
  <div id="copy-target">
{inner}
  </div>
  {extra_html}
{tail_block}</div>
{COPY_SCRIPT}
</body>
</html>
"""
