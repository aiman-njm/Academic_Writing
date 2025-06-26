import os
import json
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

SUPPORTED_MODULES = [
    "Writing Structure",
    "Grammar Rules",
    "Referencing",
    "Cohesion and Coherence",
    "Critical Thinking",
]


def analyze_text(text: str) -> dict:
    """Send text to GPT-4o and return structured feedback as dict."""
    system_prompt = (
        "You are an academic writing assistant. "
        "When given a student's writing, provide structured feedback in JSON "
        "with the following keys: grammar_issues, structure_issues, "
        "overall_comment, recommended_modules. The recommended_modules value "
        "should be an array containing at most three items chosen from the "
        "following list: Writing Structure, Grammar Rules, Referencing, "
        "Cohesion and Coherence, Critical Thinking."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
    )

    content = response["choices"][0]["message"]["content"]
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # In case the model returns non-JSON, wrap it
        data = {
            "grammar_issues": "",
            "structure_issues": "",
            "overall_comment": content,
            "recommended_modules": [],
        }
    # Ensure recommended modules are valid and max 3
    recs = [m for m in data.get("recommended_modules", []) if m in SUPPORTED_MODULES]
    data["recommended_modules"] = recs[:3]
    return {
        "grammar_issues": data.get("grammar_issues", ""),
        "structure_issues": data.get("structure_issues", ""),
        "overall_comment": data.get("overall_comment", ""),
        "recommended_modules": data.get("recommended_modules", []),
    }
