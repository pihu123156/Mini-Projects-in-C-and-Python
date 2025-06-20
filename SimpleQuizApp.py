import json

def load_questions(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(" Quiz file not found!")
        return []
    except json.JSONDecodeError:
        print(" Error reading JSON.")
        return []

def run_quiz(questions):
    score = 0
    print("\n Welcome to the Quiz!\n")
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer was: {q['answer']}\n")
    return score

def main():
    questions = load_questions("questions.json")
    if not questions:
        return

    total = len(questions)
    score = run_quiz(questions)
    print(f" Quiz finished! You scored {score} out of {total}.")


if __name__ == "__main__":
    main()
