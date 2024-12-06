# OpenO1 Chatbot

Welcome to **OpenO1**, a self-reasoning AI chatbot that breaks down complex queries into logical, step-by-step reasoning to deliver precise and insightful answers. This README explains the features, setup, and usage of OpenO1.

---

## 🚀 Features

1. **Step-by-Step Reasoning**: OpenO1 constructs logical reasoning steps to tackle queries systematically.
2. **Interactive Logging**: Every reasoning step is logged and available for review.
3. **Error-Resilient Design**: Handles issues gracefully for a smooth user experience.
4. **Final Answer Generation**: Leverages reasoning steps to craft clear and concise answers.

---

## 🛠️ Installation

To set up **OpenO1** locally, follow these steps:

\```bash
# Clone the repository
git clone https://github.com/your-username/OpenO1.git

# Navigate to the project directory
cd OpenO1

# Install the required dependencies
pip install -r requirements.txt
\```

---

## 💻 Usage

### Running OpenO1
1. **Start OpenO1**:
   \```bash
   python OpenO1.py
   \```
2. **Enter your query**: Type your question and let OpenO1 process it.
3. **Interactive Post-Query Options**:
   - Review the thought process.
   - Save the final answer.
   - Ask another question.
   - Exit the chatbot.

### Example Query
User query:
> How many 'r's are in the word 'strawberry'?

Output:
FINAL ANSWER: There are three 'r's in the word 'strawberry'.

---

## 📂 File Structure

- **`OpenO1.py`**: Main script to run the chatbot.
- **`thought_log.txt`**: Log file containing reasoning steps.
- **`final_answer.txt`**: File where the final answer can be saved.

---

## ⚙️ Configuration

- **Environment Variable**: Set your OpenAI API key as an environment variable:
  \```bash
  export OPENAI_API_KEY='your-api-key'
  \```

- **Default Model**: `gpt-4o-mini` (can be changed in the script).

---

## 🤝 Contribution Guidelines

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🧠 Acknowledgments

Special thanks to OpenAI for providing the technology powering OpenO1.

---

### Questions or Feedback?

Feel free to open an issue or contact the repository maintainer.

