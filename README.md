# iac-review-assistant
Infrastructure as Code Review Assistant using Ollama and Python


iac-review-assistant/
│
├── main.py                # Entry point
├── reviewer.py            # Ollama logic
├── prompts.py             # Prompt templates
├── test_data/
│   └── sample.tf          # Sample Terraform file
└── output/
    └── reviewed_sample.tf # Output with comments
🛠️ Goal:
Build a tool that:

Accepts Terraform/CloudFormation/CDK files.

Sends the code to Ollama (using a prompt template).

Gets back:

Misconfiguration insights

Security issues

Suggested improvements

Inline comments or review summary

🔧 Tech Stack:
Python

Ollama (local LLMs like llama3, mistral, codellama)

tkinter or argparse for file input (later maybe a web UI)

Optional: Git pre-commit hook integration
