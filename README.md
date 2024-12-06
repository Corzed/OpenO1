# OpenO1

Welcome to **OpenO1**, an open-source self-reasoning AI chatbot (not $200 per month :O) that breaks down complex queries into logical, step-by-step reasoning to deliver precise and insightful answers.

---

## 🚀 Features

1. **Step-by-Step Reasoning**: OpenO1 constructs logical reasoning steps to tackle queries systematically.
2. **Interactive Logging**: Every reasoning step is logged and available for review.
4. **Final Answer Generation**: The final result is generated with the Reasoning file as context to the request.

---

## 🛠️ Installation

To set up **OpenO1** locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-username/OpenO1.git

# Navigate to the project directory
cd OpenO1

# Install the required dependencies
pip install -r requirements.txt
```

---

## 💻 Usage

### Running OpenO1
1. **Start OpenO1**:
   ```bash
   python OpenO1.py
   ```
2. **Enter your query**: Type your question and let OpenO1 process it.
3. **Interactive Post-Query Options**:
   - Review the thought process.
   - Save the final answer.
   - Ask another question.
   - Exit the chatbot.

### Example Query:
Prompt:
```markdown
How many 'r's are in the word 'strawberry'?
```

Reasoning:
```markdown
Step 1:
To determine how many 'r's are in the word 'strawberry', the first step is to analyze the spelling of the word itself. 

1. **Identify the letters in 'strawberry'**:  
   The word 'strawberry' consists of the following letters: s, t, r, a, w, b, e, r, r, y.

Next, I will count the occurrences of the letter 'r' in this list.

**DECISION: CONTINUE**: The next step is to count how many times the letter 'r' appears in the word 'strawberry'.

Step 2:
Now, I will count the occurrences of the letter 'r' in the word 'strawberry':

2. **Count the 'r's**:  
   In the spelling: s, t, **r**, a, w, b, **e**, **r**, **r**, y, we can identify the positions of the 'r's:
   - The first 'r' appears after 't' in the third position.
   - The second 'r' appears after 'e' in the seventh position.
   - The third 'r' appears after the second 'r' in the eighth position.

Now, let's tally them up. 

**DECISION: STOP**: The counting process has concluded, and we have identified that there are a total of **three 'r's** in the word 'strawberry'.
```

Output:
```markdown
There are three 'r's in the word 'strawberry'.
```

---

## 📂 File Structure

- **`OpenO1.py`**: Main script to run the chatbot.
- **`thought_log.txt`**: Log file containing reasoning steps.
- **`final_answer.txt`**: File where the final answer can be saved.

---

## ⚙️ Configuration

- **Environment Variable**: Set your OpenAI API key as an environment variable:
  ```bash
  export OPENAI_API_KEY='your-api-key'
  ```

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

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

---

## 🧠 Acknowledgments

Special thanks to OpenAI for providing the technology powering OpenO1.

---

### Questions or Feedback?

Feel free to open an issue or contact the repository maintainer.

