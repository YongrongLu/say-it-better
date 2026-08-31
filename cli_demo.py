from __future__ import annotations

MAX_INPUT_CHARS = 2_000

STYLE_LABELS = {
    "angry": "愤怒 / Angry",
    "sarcastic": "讽刺 / Sarcastic",
    "passive_aggressive": "阴阳怪气 / Passive-aggressive",
    "polite": "礼貌 / Polite",
    "warm": "温和 / Warm",
    "direct": "直接 / Direct",
    "formal": "正式 / Formal",
    "academic_presentation": "学术汇报 / Academic presentation",
    "resume": "简历 / Résumé",
    "job_interview": "工作面试 / Job interview",
}

AUDIENCE_LABELS = {
    "general": "通用 / General",
    "friend": "朋友 / Friend",
    "colleague": "同事 / Colleague",
    "manager": "上级 / Manager",
    "professor": "教授 / Professor",
    "recruiter_interviewer": "招聘者或面试官 / Recruiter or interviewer",
}

LANGUAGE_LABELS = {
    "zh": "中文 / Chinese",
    "en": "英文 / English",
}


class RewriteError(Exception):
    """A safe, user-facing rewrite failure."""


def validate_input(text: str, style: str, audience: str, language: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise RewriteError("Enter the meaning you want rewritten.")
    if len(cleaned) > MAX_INPUT_CHARS:
        raise RewriteError("Keep the input at or below 2,000 characters.")
    if style not in STYLE_LABELS:
        raise RewriteError("Choose a supported target style.")
    if audience not in AUDIENCE_LABELS:
        raise RewriteError("Choose a supported audience.")
    if language not in LANGUAGE_LABELS:
        raise RewriteError("Choose Chinese or English as the output language.")
    return cleaned
