from __future__ import annotations

import streamlit as st

from cli_demo import (
    AUDIENCE_LABELS,
    LANGUAGE_LABELS,
    MAX_INPUT_CHARS,
    STYLE_LABELS,
    RewriteError,
    rewrite_text,
)

PAGE_STYLES = """
<style>
:root {
  --paper: #f4efe4;
  --paper-deep: #e8dfcf;
  --ink: #182a2d;
  --muted: #637174;
  --coral: #e05a47;
  --teal: #1f6f78;
  --gold: #d6a84b;
  --line: rgba(24, 42, 45, 0.14);
}

[data-testid="stAppViewContainer"] {
  background:
    linear-gradient(90deg, transparent 0 7.4%, rgba(224, 90, 71, 0.24) 7.5%, transparent 7.62%),
    repeating-linear-gradient(0deg, transparent 0 31px, rgba(24, 42, 45, 0.045) 32px),
    var(--paper);
  color: var(--ink);
}

[data-testid="stHeader"] {
  background: transparent;
}

.block-container {
  max-width: 1180px;
  padding-top: 3.4rem;
  padding-bottom: 5rem;
}

.editorial-kicker {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .38rem .72rem;
  border: 1px solid var(--ink);
  border-radius: 999px;
  font-family: "Avenir Next", "PingFang SC", sans-serif;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  background: rgba(244, 239, 228, .72);
}

.editorial-kicker::before {
  content: "";
  width: .48rem;
  height: .48rem;
  border-radius: 50%;
  background: var(--coral);
  box-shadow: 0 0 0 3px rgba(224, 90, 71, .16);
}

h1, h2, h3 {
  font-family: "Iowan Old Style", "Songti SC", "Noto Serif CJK SC", Georgia, serif !important;
  color: var(--ink) !important;
}

h1 {
  max-width: 920px;
  font-size: clamp(3rem, 7vw, 6.8rem) !important;
  line-height: .91 !important;
  letter-spacing: -.055em !important;
  margin: 1.05rem 0 .7rem !important;
}

p, label, [data-testid="stCaptionContainer"] {
  font-family: "Avenir Next", "PingFang SC", "Noto Sans CJK SC", sans-serif;
}

.hero-copy {
  max-width: 720px;
  font-family: "Avenir Next", "PingFang SC", sans-serif;
  font-size: 1.08rem;
  line-height: 1.75;
  color: var(--muted);
  margin: 0 0 1.35rem;
}

.principles {
  display: flex;
  flex-wrap: wrap;
  gap: .65rem;
  margin: 0 0 2rem;
}

.principles span {
  padding: .42rem .72rem;
  border-left: 3px solid var(--gold);
  background: rgba(255, 255, 255, .42);
  font: 700 .72rem/1.2 "Avenir Next", "PingFang SC", sans-serif;
  letter-spacing: .04em;
}

[data-testid="stTextArea"] textarea,
div[data-baseweb="select"] > div {
  background: rgba(255, 253, 248, .82) !important;
  border: 1px solid rgba(24, 42, 45, .28) !important;
  border-radius: 2px !important;
  box-shadow: 3px 3px 0 rgba(24, 42, 45, .08) !important;
}

[data-testid="stTextArea"] textarea:focus,
div[data-baseweb="select"] > div:focus-within {
  border-color: var(--teal) !important;
  box-shadow: 3px 3px 0 rgba(31, 111, 120, .2) !important;
}

.stButton > button {
  min-height: 3.25rem;
  border: 1px solid var(--ink) !important;
  border-radius: 2px !important;
  background: var(--ink) !important;
  color: #fffaf0 !important;
  font: 750 .94rem/1 "Avenir Next", "PingFang SC", sans-serif !important;
  letter-spacing: .025em;
  box-shadow: 5px 5px 0 var(--coral) !important;
  transition: transform .16s ease, box-shadow .16s ease !important;
}

.stButton > button:hover {
  transform: translate(2px, 2px);
  box-shadow: 3px 3px 0 var(--coral) !important;
}

[data-testid="stVerticalBlockBorderWrapper"] {
  background: rgba(255, 253, 248, .78);
  border: 1px solid var(--ink) !important;
  border-radius: 2px !important;
  box-shadow: 5px 5px 0 var(--paper-deep);
  min-height: 270px;
}

[data-testid="stDataFrame"] {
  border: 1px solid var(--ink);
  box-shadow: 4px 4px 0 var(--paper-deep);
}

.result-rule {
  width: 74px;
  height: 5px;
  margin: 2.4rem 0 .8rem;
  background: linear-gradient(90deg, var(--coral) 0 68%, var(--gold) 68%);
}

.fine-print {
  margin-top: 2.7rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font: .75rem/1.6 "Avenir Next", "PingFang SC", sans-serif;
}

@media (max-width: 700px) {
  .block-container { padding-top: 2rem; }
  h1 { font-size: 3.2rem !important; }
  [data-testid="stVerticalBlockBorderWrapper"] { min-height: auto; }
}
</style>
"""


def build_comparison_rows(
    variants: list[dict[str, str | int]],
) -> list[dict[str, str | int]]:
    return [
        {
            "Version": str(variant["label"]),
            "Best for": str(variant["note"]),
            "Characters": int(variant["char_count"]),
        }
        for variant in variants
    ]


def main() -> None:
    st.set_page_config(page_title="Say It Better", page_icon="🗣️", layout="wide")
    st.markdown(PAGE_STYLES, unsafe_allow_html=True)
    st.markdown(
        '<div class="editorial-kicker">Bilingual rewriting desk · 双语表达台</div>',
        unsafe_allow_html=True,
    )
    st.title("嘴替工作室 · Say It Better")
    st.markdown(
        """
        <p class="hero-copy">
        把脑海里的大概意思，变成真正说得出口的话。选择语气、对象与语言，
        一次获得三个保留原意的版本。<br>
        Turn a rough thought into three clear, sendable versions—without losing your meaning.
        </p>
        <div class="principles">
          <span>01 · PRESERVE MEANING</span>
          <span>02 · CHOOSE THE VOICE</span>
          <span>03 · PICK YOUR VERSION</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    text = st.text_area(
        "你想表达什么？ · What do you want to say?",
        height=190,
        max_chars=MAX_INPUT_CHARS,
        placeholder="输入大概意思即可，不需要先组织好语言。\nA rough thought is enough—we'll shape the wording.",
    )

    style_column, audience_column, language_column = st.columns([1.15, 1, 0.85])
    with style_column:
        style = st.selectbox(
            "目标风格 · Target style",
            options=list(STYLE_LABELS),
            format_func=STYLE_LABELS.get,
        )
    with audience_column:
        audience = st.selectbox(
            "沟通对象 · Audience (optional)",
            options=list(AUDIENCE_LABELS),
            format_func=AUDIENCE_LABELS.get,
        )
    with language_column:
        language = st.selectbox(
            "输出语言 · Output language",
            options=list(LANGUAGE_LABELS),
            format_func=LANGUAGE_LABELS.get,
        )

    if st.button("帮我表达 · Help me say it", type="primary", use_container_width=True):
        try:
            with st.spinner("正在组织语言 · Rewriting..."):
                variants = rewrite_text(text, style, audience, language)
        except RewriteError as exc:
            st.error(str(exc))
        else:
            st.markdown('<div class="result-rule"></div>', unsafe_allow_html=True)
            st.subheader("三个候选版本 · Three options")
            columns = st.columns(3)
            for column, variant in zip(columns, variants, strict=True):
                with column:
                    with st.container(border=True):
                        st.markdown(f"### {variant['label']}")
                        st.caption(str(variant["note"]))
                        st.write(str(variant["text"]))

            st.subheader("快速比较 · Quick comparison")
            st.dataframe(
                build_comparison_rows(variants),
                hide_index=True,
                use_container_width=True,
                column_config={
                    "Version": st.column_config.TextColumn("Version · 版本"),
                    "Best for": st.column_config.TextColumn("Best for · 特点"),
                    "Characters": st.column_config.NumberColumn(
                        "Characters · 字符数", format="%d"
                    ),
                },
            )

    st.markdown(
        """
        <div class="fine-print">
        SHARP, NOT HARMFUL · 情绪可以尖锐，表达不越界。<br>
        Academic and career modes never invent citations, experience, achievements, or metrics.
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
