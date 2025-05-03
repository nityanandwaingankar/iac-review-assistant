

# 🛠️ IaC Review Assistant

**Infrastructure as Code Review Assistant using Ollama and Python**

A CLI-based tool that reviews Infrastructure-as-Code (IaC) files like **Terraform**, **CloudFormation**, and **CDK**, providing:
- ⚠️ Misconfiguration insights
- 🔐 Security issue detection
- 💡 Suggested improvements
- 💬 Inline comments or code review summaries

Powered by local LLMs using **Ollama** (supports `llama3`, `mistral`, `codellama`, etc.).

---
```markdown
## 📁 Project Structure


iac-review-assistant/
├── main.py            # Entry point
├── reviewer.py        # Ollama logic
├── prompts.py         # Prompt templates
├── test_data/
│   └── sample.tf      # Sample Terraform file
└── output/
    └── reviewed_spl.tf # Output with inline comments

```


## 🎯 Project Goals

- ✅ Accept Terraform / CloudFormation / CDK code files
- ✅ Analyze them using local LLMs (via Ollama)
- ✅ Return human-readable feedback:
  - Misconfigurations
  - Security best practices
  - Suggestions for improvement
  - Inline code comments

---

## 🧰 Tech Stack

- **Python**
- **Ollama** (Local LLMs)
- `argparse` (CLI input, upgradeable to `tkinter` or web UI)
- Optional: Git pre-commit hook integration

---

## 🚀 Getting Started

1. **Install Ollama**  
   Follow instructions from: [https://ollama.com](https://ollama.com)

2. **Pull a model (e.g., Code LLaMA):**
   ```bash
   ollama pull codellama

3. **Clone and run:**

   ```bash
   git clone https://github.com/your-username/iac-review-assistant.git
   cd iac-review-assistant
   python main.py
   #```

4. **Edit `test_data/sample.tf`** or use your own IaC file.

---

## 📦 Future Features

* [ ] Auto-detect IaC file type (Terraform / CloudFormation / CDK)
* [ ] Web UI (using Streamlit or Flask)
* [ ] Git pre-commit hook support
* [ ] Summarized PDF/HTML reports
* [ ] Integration with GitHub/GitLab APIs

---

## 📄 License

MIT License

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or PRs.

---

## 💡 Inspiration

This project combines DevOps, security best practices, and AI to help engineers catch issues early in their infrastructure code using **local LLMs**.



