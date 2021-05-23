from random import randrange
print("\nHey whassup!! \nThis is your \"Winning Number Game!\" \nAll the best \U0001F44D\n")
game_stage = "start"
attempt = 0
system_generated_random_number = randrange(10,99)
while(game_stage != "finish"):
    attempt += 1
    if (attempt == 1):
        user_input_number = int(input("\nEnter a number between 10 to 99: "))
    else:
        user_input_number = int(input("\nGuess again: "))
    if user_input_number == system_generated_random_number: # winner logic
        print("Congratulations you won!!")
        if attempt <= 10:
            game_stage = "finish"
            print("You are a pro!!! Be proud of yourself.")
            break
        else:
            print(f"You guessed it in {attempt} attempts. \n\nDo you wanna play again and improve the score?")
            play_again_to_improve_the_score = input("Enter Y to continue playing, or enter N to exit the game: ")
            if play_again_to_improve_the_score[0].lower() == "y":
                system_generated_random_number = randrange(10,99)
                game_stage = "restart"
                attempt = 0
                continue
            elif play_again_to_improve_the_score[0].lower() == "n":
                game_stage = "quit"
                break
            elif play_again_to_improve_the_score == "":
                print("You have entered an invalid input. \n Game closed.")
                game_stage = "quit"
                break
            else:
                print("You have entered an invalid input. \n Game closed.")
                break
    else: # try-again logic
        if (((user_input_number > system_generated_random_number) and (user_input_number < system_generated_random_number + 5)) 
        or 
        ((user_input_number < system_generated_random_number) and (user_input_number > (system_generated_random_number - 5)))):
            print("You are too close to win. Keep trying!\n")
        elif (user_input_number > system_generated_random_number):
            print("You are high. Try a low value number instead!\n")
        elif (user_input_number < system_generated_random_number):
            print("You are low. Try a high value number instead!\n")
