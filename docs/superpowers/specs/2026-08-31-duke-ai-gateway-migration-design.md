# Duke AI Gateway Migration Design

## Goal

Move Say It Better from direct OpenAI authentication to Duke University's
OpenAI-compatible AI Gateway while keeping the Streamlit and CLI behavior
unchanged.

## Configuration

- Read the secret from `LITELLM_TOKEN`.
- Send requests to `https://litellm.oit.duke.edu/v1`.
- Use `GPT 4.1` by default.
- Allow an optional `LITELLM_MODEL` override for models enabled on the user's
  Duke account.
- Never store a real token in the repository; local secrets belong in `.env`
  and deployed secrets belong in Hugging Face Space Secrets.

## Request Flow

`app.py` continues to import the rewrite function from `cli_demo.py`.
`cli_demo.py` builds the same prompt and makes one
`client.responses.create(...)` call. The OpenAI SDK client receives Duke's
token as `api_key` and the Gateway URL as `base_url`. The existing JSON parsing,
three candidate variants, validation, and safe error messages remain intact.

## User-Facing Changes

- Missing-credential messages name `LITELLM_TOKEN`.
- `.env.example` and README instructions use Duke Gateway settings.
- Hugging Face deployment instructions create a `LITELLM_TOKEN` secret and an
  optional `LITELLM_MODEL` variable.

## Testing

Tests first assert the new default model, environment variable names, and
OpenAI client construction parameters. After observing the expected failures,
the implementation changes minimally. The full test suite, compilation, secret
scan, and Git checks must pass before the change is pushed.
