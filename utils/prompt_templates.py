"""
Prompt templates for the Language Model (LLM) requests.
These templates are used to instruct the LLM on how to generate explanations for code errors.
"""

# Prompt for when an error message is known and provided
KNOWN_ERROR_PROMPT = """
You are a teaching assistant. Given a code snippet and its error, explain:

What the error means.
Why it happened?
How to fix it conceptually? (**IMPORTANT! DO NOT provide code fixes or examples**)

Code:
{code}

Error:
{error}
"""

# Prompt for when no error message is provided; the LLM should infer the error
UNKNOWN_ERROR_PROMPT = """
You are a teaching assistant. Given a code snippet, look for an error and if found, explain:

What the error means.
Why it happened?
How to fix it conceptually? (**IMPORTANT! DO NOT provide code fixes or examples**)

Code:
{code}
"""
