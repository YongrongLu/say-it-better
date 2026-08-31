# Duke AI Gateway Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Route every Say It Better model request through Duke University's OpenAI-compatible AI Gateway.

**Architecture:** Keep `cli_demo.py` as the single API layer imported by the Streamlit app. Construct the standard OpenAI SDK client with Duke's token and base URL, while leaving prompt construction and response parsing unchanged.

**Tech Stack:** Python 3.11+, OpenAI Python SDK, python-dotenv, pytest, Streamlit

## Global Constraints

- Read the secret only from `LITELLM_TOKEN`.
- Use `https://litellm.oit.duke.edu/v1` as the fixed gateway URL.
- Default to `GPT 4.1`; allow `LITELLM_MODEL` to override it.
- Do not commit a real token.
- Preserve one API call returning exactly three normalized candidates.

---

### Task 1: Specify Duke Gateway Configuration

**Files:**
- Modify: `tests/test_cli_demo.py`
- Test: `tests/test_cli_demo.py`

- [ ] Update model tests to use `LITELLM_MODEL` and expect `GPT 4.1`.
- [ ] Update the missing-token test to require `LITELLM_TOKEN`.
- [ ] Add a client-construction test asserting Duke's token and base URL.
- [ ] Run the focused tests and observe failures caused by the old configuration.

### Task 2: Implement Duke Gateway Client Construction

**Files:**
- Modify: `cli_demo.py`
- Test: `tests/test_cli_demo.py`

- [ ] Set `DUKE_GATEWAY_URL = "https://litellm.oit.duke.edu/v1"`.
- [ ] Set `DEFAULT_MODEL = "GPT 4.1"` and read `LITELLM_MODEL`.
- [ ] Require `LITELLM_TOKEN` and pass it with the base URL to `OpenAI(...)`.
- [ ] Rename safe API errors to Duke AI Gateway.
- [ ] Run focused tests and commit the API migration.

### Task 3: Update Safe Configuration and Documentation

**Files:**
- Modify: `.env.example`
- Modify: `README.md`

- [ ] Document `LITELLM_TOKEN`, optional `LITELLM_MODEL`, and the Duke URL.
- [ ] Update local, Hugging Face, troubleshooting, and project-file guidance.
- [ ] Scan tracked code and docs for stale direct-OpenAI configuration.
- [ ] Commit documentation.

### Task 4: Full Verification and Push

**Files:**
- Verify: all tracked project files

- [ ] Run the complete pytest suite and Python compilation.
- [ ] Run whitespace, secret, ignore, and Git status checks.
- [ ] Push the isolated branch, merge it into `main`, and push `main`.
