def main():
    print("Welcome to the Quiz Game!")

    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

    if difficulty == 'easy':
        questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": 1},
            {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": 2}
        ]
    elif difficulty == 'medium':
        questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": 1},
            {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": 2},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway"], "answer": 1}
        ]
    elif difficulty == 'hard':
        questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": 1},
            {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": 2},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway"], "answer": 1},
            {"question": "What is the square root of 144?", "options": ["11", "12", "13"], "answer": 2},
            {"question": "What is 9 multiplied by 9?", "options": ["72", "81", "90"], "answer": 2}
        ]
    else:
        print("Invalid difficulty level, defaulting to medium.")
        questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": 1},
            {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": 2},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway"], "answer": 1}
        ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")
        answer = input("Your answer (enter the number): ")
        if answer.isdigit():
            answer = int(answer)
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                correct_option = q['options'][q['answer'] - 1]
                print(f"Wrong! The correct answer was {q['answer']}. {correct_option}.")
        else:
            print("Invalid input! Please enter a number.")

    print(f"\nYour final score is {score}/{len(questions)}")


if __name__ == "__main__":
    main()
