print("Welcome to this quiz!")

# Asks the user to play or quit
play = input("Would you like to play? Enter Yes to play and no to quit. ").lower() 

try:
    if play == "no":
        exit()
    
    if play == "yes":
        print("Alright, hang tight!")
        while True:
            answer = input("What is CPU stand for? ").lower()
            if answer == "central processing unit":
                print("Way to go!")
                break
            else:
                print("Wrong, try again!")
except:
    print("Please enter y to play!")
    exit()



    

