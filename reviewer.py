# reviewer.py
import ollama

def review_iac_code(code_str, model="codellama"):
    prompt = (
        "You are an expert DevOps engineer. Review the following IaC code. "
        "Identify misconfigurations, security issues, and suggest improvements. "
        "Add inline comments where applicable.\n\n"
        f"{code_str}"
    )

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
