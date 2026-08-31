# Say It Better: 60–120 Second Video Demo Script

This script follows the course staff clarification:

- `cli_demo.py` is a standalone local terminal program for raw, text-only API
  output. It does not start Streamlit.
- The web app is shown once locally and once on Streamlit Community Cloud.
- This is an instructor-approved individual project, so no teammate handoff is
  shown.

Target length: about 105–115 seconds. The narration below is in English so it
can be read word for word. The operator notes are in Chinese and are not spoken.

## Before Recording

1. Rotate or confirm the Duke AI Gateway token, but never show it on screen.
2. Close `.env`, `.env.example`, the AI Dashboard, email, and terminal windows
   containing token history.
3. Turn off notifications and set browser zoom to 100%.
4. Open VS Code at the project root.
5. Prepare two terminals:
   - Terminal A: activated virtual environment, ready to run `python cli_demo.py`.
   - Terminal B: already running `python -m streamlit run app.py`.
6. Open two browser tabs:
   - Local app: `http://localhost:8501`
   - Live app: your verified `https://...streamlit.app` link
7. Wake up the live app and complete one practice request before recording.
8. Start macOS screen recording with `Shift + Command + 5`.

## Exact Timeline and Narration

### 0:00–0:10 — Introduce the project

**On screen:** Show the GitHub repository README, title, screenshot, and project
files for a few seconds.

**Say:**

> Hi, this is Say It Better, or 嘴替工作室. It is a bilingual rewriting
> assistant that turns a rough thought into three alternatives based on the
> selected style, audience, and output language. It uses Duke's AI Gateway.

### 0:10–0:38 — Run the standalone CLI

**On screen:** Switch to Terminal A and enter:

```bash
python cli_demo.py
```

Use this demonstration input:

```text
This conclusion doesn't make sense, and you haven't shown enough evidence.
```

Choose:

```text
8
5
2
```

These selections mean **Academic presentation**, **Professor**, and **English**.
Pause briefly on the three terminal results.

**Say:**

> First, `cli_demo.py` runs independently in the terminal. I enter a rough
> statement, choose academic presentation, professor, and English. The API
> returns three text-only versions: concise, natural, and complete. This script
> contains the reusable API function that the Streamlit app imports.

### 0:38–1:10 — Show Streamlit locally

**On screen:** Switch to `http://localhost:8501`. Enter:

```text
I did a lot of data analysis and helped the team make better decisions.
```

Select:

- Target style: **Résumé**
- Audience: **Recruiter or interviewer**
- Output language: **English**

Click **Help me say it**. Show the three result cards and the formatted
comparison table.

**Say:**

> Next, this is the Streamlit interface running locally. The same API function
> is imported into the web app. The user can enter text and choose a style,
> audience, and Chinese or English output. One request produces three different
> candidates, and the formatted comparison table is the required visual
> element.

### 1:10–1:42 — Prove the live deployment works

**On screen:** Switch to the `streamlit.app` tab. Enter:

```text
这个计划不太现实，时间安排也不合理。
```

Select:

- Target style: **Polite**
- Audience: **Manager**
- Output language: **Chinese**

Click **帮我表达 · Help me say it** and show the results.

**Say:**

> Finally, this is the public app on Streamlit Community Cloud. I will use a
> Chinese example with a polite style for a manager. The live deployment calls
> the same Duke AI Gateway and returns Chinese results without exposing the API
> token, which is stored only in Streamlit secrets.

### 1:42–1:52 — Close

**On screen:** Return to the top of the live app or GitHub README, where both
links are visible.

**Say:**

> The GitHub repository includes the source files, requirements, local and CLI
> instructions, tests, and the live app link. Thank you.

Stop the recording.

## If the API Is Slow During Recording

- Do not click the button repeatedly; one click is enough.
- Let the loading indicator appear, then continue when the results arrive.
- If the live app was sleeping, wake it before starting the recording.
- If a request fails, stop and restart the recording rather than showing a
  token or opening secret settings.

## What Must Be Visible

- CLI command and its three text-only results.
- Local Streamlit URL or clearly local browser tab.
- Text input, style, audience, and language selectors.
- Three candidate versions and the formatted comparison table.
- Public `streamlit.app` URL and a successful live request.
- GitHub README with local run, CLI run, Python version, screenshot, and live
  app link.

## What Must Never Be Visible

- The contents of `.env` or Streamlit Secrets.
- The Duke AI Dashboard token page.
- A real token in terminal history, VS Code search, clipboard history, or Git.
- Personal email, grades, messages, or unrelated browser tabs.
