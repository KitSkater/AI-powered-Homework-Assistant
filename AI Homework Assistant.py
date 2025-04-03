import sympy as sp
import nltk
import language_tool_python
import difflib
import ollama

nltk.download("punkt")
from nltk.tokenize import sent_tokenize

# Initialize tools
tool = language_tool_python.LanguageTool("en-US")

# Choose a high-quality local model (e.g., mistral, llama3)
OLLAMA_MODEL = "mistral"

def ask_ai(prompt):
    """Uses Ollama to generate AI-based responses."""
    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        return f"AI Error: {e}"

def solve_equation(equation):
    """Solves math equations step-by-step with LaTeX formatting."""
    try:
        x = sp.Symbol("x")
        expr = sp.sympify(equation)
        steps = sp.solve(expr, x, dict=True)
        latex_steps = sp.latex(steps)
        return f"Solution: {steps}\nLaTeX Format: {latex_steps}"
    except Exception as e:
        return f"Error solving equation: {e}"

def summarize_text(text, num_sentences=2):
    """Summarizes text using AI-powered processing."""
    return ask_ai(f"Summarize this in {num_sentences} sentences:\n{text}")

def check_grammar(text):
    """Checks grammar and provides corrections."""
    matches = tool.check(text)
    if matches:
        return f"Grammar Issues: {len(matches)} found.\nExample: {matches[0]}"
    return "No grammar issues found."

def plagiarism_check(student_text, reference_text):
    """Checks plagiarism by comparing texts."""
    similarity_ratio = difflib.SequenceMatcher(None, student_text, reference_text).ratio()
    return f"Plagiarism Score: {similarity_ratio * 100:.2f}%"

def main():
    while True:
        print("\n🔹 AI Homework Assistant 🔹")
        print("1️⃣ AI Homework Helper (Ask any question)")
        print("2️⃣ Solve Math Equation (Step-by-Step)")
        print("3️⃣ Summarize Text (AI-powered)")
        print("4️⃣ Check Grammar")
        print("5️⃣ Plagiarism Check")
        print("6️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            question = input("Ask your homework question: ")
            print(ask_ai(question))
        elif choice == "2":
            eq = input("Enter equation (use 'x' as variable, e.g., x**2 - 4): ")
            print(solve_equation(eq))
        elif choice == "3":
            text = input("Enter text to summarize: ")
            print(summarize_text(text))
        elif choice == "4":
            text = input("Enter text for grammar check: ")
            print(check_grammar(text))
        elif choice == "5":
            student_text = input("Enter student's text: ")
            reference_text = input("Enter reference text: ")
            print(plagiarism_check(student_text, reference_text))
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
