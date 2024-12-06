import os
import openai
from datetime import datetime

# Ensure the OpenAI API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

# File for logging the thought process
LOG_FILE = "thought_log.txt"


def log_thought(step_number, thought):
    """
    Logs the reasoning step to a .txt file with structured metadata.
    """
    with open(LOG_FILE, "a") as log:
        log.write(f"Step {step_number} - {datetime.now().isoformat()}:\n{thought}\n\n")


def clear_log():
    """Clears the thought log file."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)


def display_ui(query, thoughts, final_answer=None):
    """
    Clean and interactive UI for displaying the thought process and final answer.
    """
    print("\n" + "=" * 60)
    print(f"USER QUERY: {query}")
    print("=" * 60)
    print("THOUGHT PROCESS:")
    for i, thought in enumerate(thoughts, start=1):
        print(f"\n[Step {i}]")
        print(thought)
    print("\n" + "=" * 60)
    if final_answer:
        print(f"FINAL ANSWER:\n{final_answer}")
    print("=" * 60)



def generate_response(messages, model="gpt-4o-mini", temperature=0.7):
    """
    Sends a prompt to the OpenAI API and retrieves the response.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during API call: {e}")
        return None


def generate_final_answer(thoughts, query, model="gpt-4o-mini", temperature=0.7):
    """
    Generates the final answer using a separate model with the accumulated thoughts as context.
    """
    # Combine thoughts into a single context
    context = "\n".join([f"Step {i}: {thought}" for i, thought in enumerate(thoughts, start=1)])
    prompt = (
        "You are an advanced AI assistant tasked with providing a final answer based on the following thought process:\n\n"
        f"{context}\n\n"
        "Given this reasoning, provide a clear and concise final answer to the user's query:\n"
        f"USER QUERY: {query}"
    )

    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a concise and accurate AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during final answer generation: {e}")
        return "An error occurred while generating the final answer."


def self_reasoning_chatbot(query, model="gpt-4o-mini", temperature=0.7, max_iterations=10):
    """
    Self-reasoning AI chatbot:
    - Iteratively generates reasoning steps.
    - Logs each step and displays it in real-time.
    - Uses a separate model for generating the final answer.
    """
    # Initial system instructions
    system_message = {
        "role": "system",
        "content": (
            """You are a self-reasoning AI assistant tasked with assisting the main AI in producing accurate, well-structured, and thoughtful results for the user. Your role is **not** to provide the final answer but to build a logical, step-by-step reasoning process to guide the main assistant toward the best outcome. Follow this protocol strictly:

1. **Break the query into clear, intermediate steps.**  
   Each step should build on the previous one to explore the query logically and systematically.

2. **Do not include multiple reasoning steps in one output.**  
   - Each output should represent a **single, well-defined step** that focuses on one aspect of the reasoning process at a time.  
   - At the end of each step, explicitly decide whether to:  
     - **DECISION: CONTINUE**: If further reasoning is required, specify what aspect you will address in the next step.  
     - **DECISION: STOP**: If the reasoning process has concluded or sufficient context has been generated, signal the end of the thought process.

3. **Use at least 3 steps.**  
   - Ensure a thorough exploration of the query, unless the reasoning chain naturally concludes earlier.  
   - Spreading steps out ensures clarity, avoids rushing conclusions, and allows refinement between steps.

4. **Avoid overloading a single step with multiple actions.**  
   - Focus on **one idea, concept, or action** per step to maintain clarity and precision.  
   - Avoid condensing or summarizing multiple steps in a single output.

5. **Ultimate Goal.**  
   - Your role is to build a structured reasoning chain for the main AI assistant to use to output a perfect output.

---

### Key Objectives:
- **Clarity**: Break down the reasoning into simple, digestible parts.  
- **Thoroughness**: Ensure each step explores its assigned task fully before moving to the next.  
- **Focus**: Keep each step concise and limited to a single thought or action.  

Your ultimate goal is to create a reasoning process that is **logical, concise, and easy to follow**. This ensures the main assistant can provide the best possible result for the user."""
        )
    }

    # Initialize conversation state
    user_message = {"role": "user", "content": query}
    messages = [system_message, user_message]

    thoughts = []  # List to store reasoning steps
    final_answer = None

    print("\nThinking... Please wait.\n")
    for step in range(1, max_iterations + 1):
        response = generate_response(messages, model, temperature)

        if not response:
            print("Failed to retrieve response. Please try again later.")
            break

        # Log the response
        log_thought(step, response)
        thoughts.append(response)

        # Display real-time progress
        print(f"[Step {step}] {response}\n")

        # Check for STOP decision
        if "DECISION: STOP" in response.upper():
            break

        # Append the reasoning step back with clear instructions to continue
        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": "Continue reasoning based on the previous step."})

    # Use a new model for the final answer
    if thoughts:
        print("\nGenerating final answer based on thought process...\n")
        final_answer = generate_final_answer(thoughts, query, model="gpt-4o-mini", temperature=0.7)

    # Display the final result in the UI
    display_ui(query, thoughts, final_answer)
    return final_answer




def main():
    """
    Main function to run the chatbot in a loop for continuous user interaction.
    """
    print("Welcome to the Enhanced Self-Reasoning AI Chatbot!")
    print("Type 'exit' to quit the program.")
    while True:
        query = input("\nEnter your query: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        # Clear the thought log before starting a new query
        clear_log()

        # Run the self-reasoning chatbot
        final_answer = self_reasoning_chatbot(query)

        # Post-query options
        print("\nWhat would you like to do next?")
        print("1. Review the thought process")
        print("2. Save the final answer")
        print("3. Ask another question")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            with open(LOG_FILE, "r") as log:
                print("\nThought Log:")
                print(log.read())
        elif choice == "2":
            with open("final_answer.txt", "w") as f:
                f.write(final_answer)
            print("Final answer saved to 'final_answer.txt'.")
        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
