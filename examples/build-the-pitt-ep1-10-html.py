# -*- coding: utf-8 -*-
"""Build the-pitt-ep1-terminology-10.html (T07 layout from pitt_t07_layout)."""
from pathlib import Path

from pitt_ep1_10_data import sec1, sec2, sec3, sec4
from pitt_t07_layout import (
    SECTION_THEME_ORDER,
    article_tail,
    closing_html,
    entry_md,
    html_document,
    opening_html,
    quiz_html,
    section_html,
    structure_line,
)

OUT = Path(__file__).with_name("the-pitt-ep1-terminology-10.html")
MD_OUT = Path(__file__).with_name("the-pitt-ep1-terminology-10.md")

H1 = "《匹兹堡医护前线》第一集｜医学英语：高钾透析与轮岗"
SERIES = "The Pitt 第一集 · 系列第 10 篇"
BLOCKS = [
    ("一、轮转口语", sec1),
    ("二、化验与临时降钾", sec2),
    ("三、透析置管", sec3),
    ("四、醒后交代", sec4),
]
CLOSING = (
    "如果你也在追这部剧，或正在学医学英语 / 医学口译，欢迎转发给一起追剧、一起备考的小伙伴。"
    "觉得有用的话，点个「在看」支持一下～"
)
QUIZ_FOOTER = "欢迎在评论区留下你的选项（A / B / C / D）。正确答案将于评论区置顶公布。"


def build_md() -> str:
    parts = [
        f"# {H1}",
        "",
        SERIES,
        "",
        "## 前言",
        "",
        "上一场那个铁人三项后骤停的年轻人，化验数字出来了。血钾 7.8（正常大概 3.5 到 5.0），肌酐 5.6：钾高到能再停跳，肾也已经伤了。",
        "",
        "急诊先打胰岛素和葡萄糖，让钾暂时躲进细胞里，人先稳住；要真正把多余的钾清掉，还得做透析。同一段里，住院医还在拿轮转打赌。",
        "",
        structure_line(BLOCKS),
        "",
        "/",
        "",
    ]
    for title, entries in BLOCKS:
        parts.append(f"## {title}（{len(entries)}）")
        parts.append("")
        for i, e in enumerate(entries, 1):
            parts.append(f"{i}. {e['title']}  ")
        parts.append("")
        parts.append("/")
        parts.append("")
    parts += ["## 词条详解", ""]
    for title, entries in BLOCKS:
        parts.append(f"### {title}")
        parts.append("")
        for i, e in enumerate(entries, 1):
            parts.append(entry_md(i, e))
            parts.append("")
        parts.append("/")
        parts.append("")
    parts += [
        "## 小测试",
        "",
        "剧中 **creatinine** 是什么？",
        "",
        "A. 肌酐  ",
        "B. 肌酸  ",
        "C. 肌红蛋白  ",
        "D. 肌钙蛋白",
        "",
        QUIZ_FOOTER,
        "",
        "/",
        "",
        "## 收束",
        "",
        CLOSING,
        "",
        "下篇文章见~",
        "",
        "---",
        "",
        "关于本篇  ",
        f"{SERIES} · 医学英语 · 高钾透析与轮岗  ",
        "关注账号，获取更多内容~",
        "",
        "这篇文章对你有帮助吗？ 有的 / 没有",
        "",
    ]
    return "\n".join(parts)


def build() -> str:
    preface = [
        "上一场那个铁人三项后骤停的年轻人，化验数字出来了。血钾 7.8（正常大概 3.5 到 5.0），肌酐 5.6：钾高到能再停跳，肾也已经伤了。",
        "急诊先打胰岛素和葡萄糖，让钾暂时躲进细胞里，人先稳住；要真正把多余的钾清掉，还得做透析。同一段里，住院医还在拿轮转打赌。",
        structure_line(BLOCKS),
    ]
    inner = opening_html(SERIES, H1, preface)
    for (title, entries), theme in zip(BLOCKS, SECTION_THEME_ORDER):
        inner += section_html("医学口译", title, theme, entries)
    inner += quiz_html(
        "剧中 <strong>creatinine</strong> 是什么？",
        ["A. 肌酐", "B. 肌酸", "C. 肌红蛋白", "D. 肌钙蛋白"],
        QUIZ_FOOTER,
    )
    inner += closing_html(CLOSING)
    inner += article_tail(f"《匹兹堡医护前线》{SERIES} · 医学英语 · 高钾透析与轮岗")
    return html_document(
        H1,
        "T07 · 与系列同模版 · 医学英语 · 高钾透析与轮岗（第十篇）",
        inner,
    )


def main() -> None:
    html = build()
    OUT.write_text(html, encoding="utf-8")
    MD_OUT.write_text(build_md(), encoding="utf-8")
    print(f"wrote {OUT} ({len(html)} chars)")
    print(f"wrote {MD_OUT}")
    n = sum(len(e) for _, e in BLOCKS)
    print("entries: " + "+".join(str(len(e)) for _, e in BLOCKS) + f"={n}")


if __name__ == "__main__":
    main()
