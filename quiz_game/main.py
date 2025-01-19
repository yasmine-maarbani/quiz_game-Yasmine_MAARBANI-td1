import time

def main():
    print("Welcome to the Quiz Game!")
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": 1},
        {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": 2},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway"], "answer": 1}
    ]

    score = 0
    total_time = 0  # To track the total time taken

    for q in questions:
        print("\n" + q["question"])
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")
        
        # Start timing
        start_time = time.time()

        answer = input("Your answer (enter the number): ")

        # Stop timing
        end_time = time.time()

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

        # Calculate time taken for this question
        time_taken = end_time - start_time
        total_time += time_taken
        print(f"Time taken for this question: {time_taken:.2f} seconds")

    print(f"\nYour final score is {score}/{len(questions)}")
    print(f"Total time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
