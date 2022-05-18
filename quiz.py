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
        level = score*0.75
        answer = input("Why Python language? Answer is: A. Python is a popular programming language; B. Python is not a popular programming language; C. Python is a snake. ").lower()
        if answer == "a" and answer !="":
            score += 1
        else:
            print("Incorrect!")

        answer = input("What is a variable? Answer is: A. A variable is a container for storing data values; B. A variable is not a container for storing data values. ").lower()
        if answer == "a" and answer !="":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        answer = input("What does a list do? Answer is: A. A list is used to store multiple items in a single variable; B. A list is not used to store multiple items in a single variable. " ).lower()
        if answer == "a" and answer !="":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        answer = input("What is an array? Answer is: A. An arrays is not used to store multiple values in one single variable; B. An arrays is used to store multiple values in one single variable. " ).lower()
        if answer == "b" and answer !="":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        answer = input("What is an iterator? Answer is: A. An iterator is an object that contains a countable number of values; B. An iterator is an object that contains a countable number of values. " ).lower()
        if answer == "b" and answer !="":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    if level >= int(score):
        print("Congratulations! Your correct answer is ", score, ", at least 70%. You are now leveled up!")
    else:
        print("Your correct answer is",score, "less than 70%, come back and try again!")
except:
    print("Enter a valid answer to play!")
    exit()
