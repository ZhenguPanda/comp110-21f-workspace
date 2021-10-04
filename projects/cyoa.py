"""I will create a small game where the user guesses a number."""

__author__ = "730401590"


import random
random_number = random.randint(1, 30)
x = 0
guesses = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001F923"
grinning: str = "\U0001f600"
points: int = 0 


def main() -> None:  
    """Should define to None and call points.""" 
    global points
    points = 0
    greet()
    option = int(input("Are you ready to start? 1. Yes 2. No 3. Can you explain the instructions?"))
    if option == 1:
        print("Now, let's begin!", grinning)
        guess_game()
        print(f'You guessed {int(points)} times, {player}.')
    if option == 2:
        print(f'Goodbye, {player}.')
    else:
        if option == 3:
            print("This is a guessing numbers game. You will guess until you get it correct?")
            option2 = int(input("Are you ready now? 1. Yes 2. No"))
            if option2 == 1:
                print("Now, let's begin!")
            else:
                print(f'Goodbye, {player}.')
    

def greet() -> None:  
    """Greets the player."""
    player = str(input("What is your name? "))
    print(f'Welcome, {player}.')


def guess_game() -> None:
    """Starts the game."""
    global points
    number = int(input("I am guessing a number between 1 and 30. Can you guess it? "))
    while number != random_number:
        if number > 30:
            print("The number should be lower than 30! Try again.", NAMED_CONSTANT)
            points += 1
            number = int(input("Guess another number: "))
        if number < 1:
            print("The number should be bigger than 1!")
            points += 1
            number = int(input("Guess another number: "))
        if number < random_number:
            print("Too low! Try again.")
            points += 1
            number = int(input("Guess another number: "))
        if number > random_number:
            print("Too high! Try again.")
            points += 1
            number = int(input("Guess another number: "))
    else:
        print(f'Congrats {player}!')
        points += 1
        

if __name__ == "__main__":
    main()