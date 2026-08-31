# Say It Better / 嘴替工作室

Say It Better turns a rough meaning into three concise, natural, and complete
versions for a selected style, audience, and Chinese or English output.

“嘴替工作室”把尚未组织好的意思，转换成简洁、自然和完整三个候选版本，
并根据用户选择的表达风格、沟通对象和输出语言调整措辞。

![Say It Better application](assets/app-demo.png)

## Live App

- [GitHub repository](https://github.com/YongrongLu/say-it-better)
- Streamlit Community Cloud link: add the verified `https://...streamlit.app`
  URL here after deployment.

The course staff approved Streamlit Community Cloud for this challenge after
Hugging Face removed its free native Streamlit SDK. This repository is the
source used by the deployed app.

## Features

- Ten emotional, everyday, professional, academic, and career styles.
- Six optional audience choices, including colleagues, professors, and interviewers.
- Chinese or English output regardless of the input language.
- Three meaning-preserving alternatives from one Duke AI Gateway request.
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

Create a token in the Duke AI Dashboard, then open `.env` and replace the
example value with that token:

```text
LITELLM_TOKEN=replace_with_your_duke_gateway_token
LITELLM_MODEL=gpt-5.6-sol
```

The app uses Duke's OpenAI-compatible endpoint at
`https://litellm.oit.duke.edu/v1`. `LITELLM_MODEL` is optional; when omitted,
the app uses `GPT 4.1`. Never commit `.env` or share a real token.

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

Automated tests use mocked gateway responses and do not spend API credits:

```bash
python -m pytest -v
```

## Streamlit Community Cloud

Deploy `app.py` from the `main` branch of this GitHub repository. In the
deployment form's **Advanced settings**, keep Python 3.12 and add these root-level
secrets in TOML format:

```toml
LITELLM_TOKEN = "paste_your_real_duke_gateway_token_here"
LITELLM_MODEL = "gpt-5.6-sol"
```

Never put the real token in this README, `.env.example`, source code, or Git
history. Streamlit exposes root-level secrets as environment variables, so the
same API layer works locally and in Community Cloud.

For the complete click-by-click workflow, see
[`docs/STREAMLIT_DEPLOYMENT_AND_SUBMISSION_GUIDE.md`](docs/STREAMLIT_DEPLOYMENT_AND_SUBMISSION_GUIDE.md).
For the 60–120 second recording script, see
[`docs/VIDEO_DEMO_SCRIPT.md`](docs/VIDEO_DEMO_SCRIPT.md).

## Safety and Privacy

- Do not enter secrets or highly sensitive personal information.
- Emotional rewrites may be sharp, but the app avoids threats, hate,
  discrimination, and severe personal abuse.
- Academic and career modes do not invent citations, experience, achievements,
  skills, or metrics.
- The user's core meaning is preserved across all three versions.

## Troubleshooting

- **Missing token:** Confirm `.env` locally or `LITELLM_TOKEN` in Streamlit
  Community Cloud secrets.
- **Unauthorized token:** Verify that the Duke Gateway token is active and copied correctly.
- **Rate or usage limit:** Check the Duke AI Dashboard and retry later.
- **Timeout or connection failure:** Check the network and retry.
- **Unreadable response:** Generate again; the model response did not match the
  expected three-version structure.

## Project Files

- `cli_demo.py`: validation, prompt, Duke Gateway call, response parsing, errors, and CLI.
- `app.py`: Streamlit interface, result cards, and comparison table.
- `tests/`: mocked API, CLI, validation, parsing, and Streamlit smoke tests.
- `requirements.txt`: Python dependencies.
- `.env.example`: safe configuration names without a real secret.
