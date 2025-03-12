import random
user_name = str(input("Firstly Enter your name :"))
print(f"We Welcome you  Mr {user_name}! Get ready to test your luck in the Number Guessing Game!")
print("Sir you have five attempt in which you have to guess the number between 50 to 100.")


number_to_guess = random.randrange(50 , 100)
chances = 5
guess_counter = 0 

while guess_counter < chances: 
    guess_counter += 1
    my_guess = int(input("Enter your number:"))
    if my_guess == number_to_guess:
        print(f"Congratulations! The number was {number_to_guess}. You have found it right!! in the {guess_counter} attempt!")
        break
    elif my_guess > number_to_guess:
        print(f"The number you have guess is too high! Try Again")
    elif my_guess < number_to_guess:
        print(f"The number you have guess is too Low! Try Again")
    if guess_counter == chances and my_guess != number_to_guess:
        print(f"Oops! you have used all attempts!The number was {number_to_guess}  better luck next time" )

    
    
