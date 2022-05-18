# step 1: prompt the question for users to enter the answer
# step 2: declare the score variable and asisgn it to 0 because the score is 0 before any questions are answered
# step 3: get the answer of the quiz, if the answer is correct, then add 1 to the score
# step 4: check if correct answer is 70% of the all the answer
# step 5: tell the user to level up if the correct answer is 70% or more


print("Welcome! Score 70% of the correct answers to level up!")
play = input("Are you ready to play? Enter yes to start! ").lower()
try:
    if play != "yes":
        quit()
    else:
        score = 0

        answer = input("Why Python language? Answer is: ").lower()
        if answer == "python is a popular programming language":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        answer = input("What is a variable? Answer is: ").lower()
        if answer == "a variable is containers for storing data values":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        answer = input("What does a list do? Answer is: ").lower()
        if answer == "a list is used to store multiple items in a single variable":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        answer = input("What is an array? Answer is: ").lower()
        if answer == "an arrays is used to store multiple values in one single variable":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        answer = input("What is an iterator? Answer is: ").lower()
        if answer == "an iterator is an object that contains a countable number of values":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    if score >= int(score*0.75):
        print("Congratulations! Your correct answer is ", score, "at least 70%. You are now leveled up!")
    else:
        print("Your correct answer is",score, "less than 70%, come back and try again!")
except:
    print("Enter a valid answer to play!")
    exit()
