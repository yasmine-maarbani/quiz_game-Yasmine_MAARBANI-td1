def main():
    print("Welcome to the Quiz Game!")
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
        {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": "4"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway"],
         "answer": "Shakespeare"}
    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")
        answer = input("Your answer: ")
        if answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score is {score}/{len(questions)}")


if __name__ == "__main__":
    main()