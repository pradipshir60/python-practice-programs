n=18
number_of_guesses=1
print("Number of gueses is limited to only 9 times :")
while(number_of_guesses<=9):
    guess_number=int(input("Guess the no:\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("You have enter grater no please input smaller number.\n")
    else:
        print("You Won")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no.of guesses left")
    number_of_guesses = number_of_guesses+1

    if(number_of_guesses>9):
        print("Game Over")   