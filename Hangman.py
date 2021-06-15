# importing the random and time module
import random
import time

# Initial steps to invite in the game:
print("\nWelcome to the hangman game by Anurag Deshmukh\n")
name = input("Enter your name: ")
print("Hello " + name + "!Best Of Luck!")
time.sleep(2)
print("The game is about the to start!\nLets play Hangman")
time.sleep(3)


# define the main function
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = " "


# Develop a loop to execute the game again:
# a loop to re-execute the game when the first roung ends

def play_loop():
    global play_game
    play_game = input("Do u want to play game again? y = yes,n= no\n")
    while play_game not in["y","n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("thanks for playing! we expect u back again!")
        exit()


# initalize conditions for hangmangame:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the hangman word: " + display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("invalid input, try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("try another letter \n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print(" _____  \n"
                  " |      \n"
                  "  |      \n"
                  "  |      \n"
                  " |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("wrong guess. " + str(limit - count) + "guesses remaning\n")
        elif count == 2:
            time.sleep(1)
            print("  ____ \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |        \n"
                  "  |        \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("wrong guess. " + str(limit - count) + "guesses remaning\n")
        elif count == 3:
            time.sleep(1)
            print(" ____ \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |        \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("rong guess. " + str(limit - count) + "guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print(" ____ \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |      0  \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("wrong guess. " + str(limit - count) + "guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print(" ____ \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |      | \n"
                  "  |      0  \n"
                  "  |     /|\ \n"
                  "  |     /|\ \n"
                  "__|__\n")
            print("wrong guess.u r hanged!!!\n")
            print("the word was: " + already_guessed, word)
            play_loop()

        elif count != limit:
            hangman()

main()


hangman()
