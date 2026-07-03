# Function to generate a World Cup question
def generate_question(question_number):

    question_1 = "In what year was the first FIFA World Cup held?"
    answer_1 = 1930

    question_2 = "In what year did South Africa host the FIFA World Cup?"
    answer_2 = 2010

    question_3 = "In what year did England win the FIFA World Cup?"
    answer_3 = 1966

    question_4 = "In what year did Russia host the FIFA World Cup?"
    answer_4 = 2018

    question_5 = "In what year did Brazil last win the FIFA World Cup?"
    answer_5 = 2002

    if question_number == 0:
        return question_1, answer_1

    elif question_number == 1:
        return question_2, answer_2

    elif question_number == 2:
        return question_3, answer_3

    elif question_number == 3:
        return question_4, answer_4

    else:
        return question_5, answer_5


# Function to display the final score
def display_final_score(score):

    print()

    if score < 2:
        print(f"⚽ You might want to work on your World Cup knowledge. ⚽ You scored {score} out of 5.⚽")

    elif score < 5:
        print(f"⚽ You're a World Cup fan! ⚽ You scored {score} out of 5.⚽")

    else:
        print(f"🏆 You know your stuff! Well Done! 🏆 You scored {score} out of 5.🏆")


# Main program
print("Years of the World Cup Quiz")

# Stores the users score
score = 0

for question_number in range(5):

    question, answer = generate_question(question_number)

    print()
    print("Question", question_number + 1, "of 5")
    print(question)

    user_answer = int(input("Your answer: "))

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong. The correct answer was:", answer)

display_final_score(score)
