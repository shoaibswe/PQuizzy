# Python Simple Quiz Game

questions = ("What is the capital of France?",
             "What is 2 + 2?",
             "What is the capital of Japan?",
             "What is the largest planet in our solar system?")
options = (("A. London", "B. Berlin", "C. Paris", "D. Madrid"),
           ("A. 3", "B. 4", "C. 5", "D. 6"),
           ("A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"),
           ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"))
answers = ("C", "B", "B", "B")
score = 0
total_questions = len(questions)
ques_number = 0

for question in questions:
    while True:
        print("\n" + question)
        for option in options[ques_number]:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer not in ('A', 'B', 'C', 'D'):
            print("Invalid option! Please choose A, B, C, or D.")
            print("Please try again.")
            continue

        if user_answer == answers[ques_number]:
            score += 1
            print("Correct!")
            break
        else:
            print("Wrong!")
            print("The correct answer is:", answers[ques_number])
            print("Please try again.")
            break
    
    ques_number += 1
print("\nYour correct answers are:", score, "out of", total_questions)
print("You got", int(score*100/total_questions), "percent score.")
