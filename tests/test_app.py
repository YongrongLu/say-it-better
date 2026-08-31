from pathlib import Path

from streamlit.testing.v1 import AppTest

from app import build_comparison_rows


def sample_variants():
    return [
        {
            "kind": "concise",
            "label": "简洁版",
            "text": "版本一",
            "note": "简短",
            "char_count": 3,
        },
        {
            "kind": "natural",
            "label": "自然版",
            "text": "版本二",
            "note": "自然",
            "char_count": 3,
        },
        {
            "kind": "complete",
            "label": "完整版",
            "text": "版本三",
            "note": "完整",
            "char_count": 3,
        },
    ]


def test_build_comparison_rows_keeps_display_fields_only():
    assert build_comparison_rows(sample_variants()) == [
        {"Version": "简洁版", "Best for": "简短", "Characters": 3},
        {"Version": "自然版", "Best for": "自然", "Characters": 3},
        {"Version": "完整版", "Best for": "完整", "Characters": 3},
    ]


def test_streamlit_page_has_required_inputs_and_action():
    app_path = Path(__file__).parents[1] / "app.py"
    app = AppTest.from_file(app_path).run()
    assert not app.exception
    assert app.title[0].value == "嘴替工作室 · Say It Better"
    assert len(app.text_area) == 1
    assert len(app.selectbox) == 3
    assert app.button[0].label == "帮我表达 · Help me say it"
