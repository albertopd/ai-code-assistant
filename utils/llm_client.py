from google import genai

from utils.prompt_templates import KNOWN_ERROR_PROMPT, UNKNOWN_ERROR_PROMPT


class LlmClient:
    def __init__(self, api_key: str, ai_model: str):
        # Initialize the GenAI client
        self.client = genai.Client(api_key=api_key)
        self.ai_model = ai_model

    def get_explanation(self, code: str, error: str) -> str:
        if not error.strip():
            prompt = UNKNOWN_ERROR_PROMPT.format(code=code)
        else:
            prompt = KNOWN_ERROR_PROMPT.format(code=code, error=error)

        # Generate content using the GenAI client
        response = self.client.models.generate_content(
            model=self.ai_model, contents=prompt
        )

        return response.text if response and response.text else "No explanation found."
