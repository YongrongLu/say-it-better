---
title: Say It Better
emoji: 🗣️
colorFrom: yellow
colorTo: red
sdk: streamlit
app_file: app.py
pinned: false
---

# Say It Better / 嘴替工作室

Say It Better turns a rough meaning into three concise, natural, and complete
versions for a selected style, audience, and Chinese or English output.

“嘴替工作室”把尚未组织好的意思，转换成简洁、自然和完整三个候选版本，
并根据用户选择的表达风格、沟通对象和输出语言调整措辞。

![Say It Better application](assets/app-demo.png)

## Live App

The public GitHub and Hugging Face links will be added after the verified deployment.

## Features

- Ten emotional, everyday, professional, academic, and career styles.
- Six optional audience choices, including colleagues, professors, and interviewers.
- Chinese or English output regardless of the input language.
- Three meaning-preserving alternatives from one OpenAI Responses API request.
- A standalone CLI and a polished Streamlit interface using the same API function.
- Friendly validation, configuration, network, rate-limit, and API errors.

## Python Version

Python 3.11 or newer. Development tests also run on Python 3.13.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Open `.env` and replace the example API key with an active key:

```text
OPENAI_API_KEY=replace_with_your_key
OPENAI_MODEL=gpt-5.6-luna
```

Never commit `.env` or share a real API key.

Start the application:

```bash
streamlit run app.py
```

## Run the CLI

```bash
python cli_demo.py
```

Enter the meaning, then choose a target style, audience, and output language from
the numbered menus. The CLI prints the same three candidates as the web app.

## Test

Automated tests use mocked OpenAI responses and do not spend API credits:

```bash
python -m pytest -v
```

## Hugging Face Spaces

Create an `OPENAI_API_KEY` Space Secret. Do not add it as a public Variable.
`OPENAI_MODEL` is optional; without it, the app uses `gpt-5.6-luna`.
The Space repository must contain the same files and README as GitHub.

## Safety and Privacy

- Do not enter secrets or highly sensitive personal information.
- Emotional rewrites may be sharp, but the app avoids threats, hate,
  discrimination, and severe personal abuse.
- Academic and career modes do not invent citations, experience, achievements,
  skills, or metrics.
- The user's core meaning is preserved across all three versions.

## Troubleshooting

- **Missing key:** Confirm `.env` locally or `OPENAI_API_KEY` in Space Secrets.
- **Unauthorized key:** Verify that the key is active and copied correctly.
- **Rate or usage limit:** Check OpenAI usage and retry later.
- **Timeout or connection failure:** Check the network and retry.
- **Unreadable response:** Generate again; the model response did not match the
  expected three-version structure.

## Project Files

- `cli_demo.py`: validation, prompt, OpenAI call, response parsing, errors, and CLI.
- `app.py`: Streamlit interface, result cards, and comparison table.
- `tests/`: mocked API, CLI, validation, parsing, and Streamlit smoke tests.
- `requirements.txt`: Python dependencies.
- `.env.example`: safe configuration names without a real secret.
