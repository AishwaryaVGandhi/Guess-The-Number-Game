import random

easy_level_attempts = 10
medium_level_attempts = 7
hard_level_attempts = 5

def set_difficulty(level):
    if level == "easy":
        return easy_level_attempts
    elif level == "medium":
        return medium_level_attempts
    elif level == "hard":
        return hard_level_attempts
    else:
        return

def check_answer(guess, answer, attempts):
    if guess < answer:
        print("Your guess is too low.")
        return attempts - 1
    elif guess > answer:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"\nYour guess is correct. The answer is {answer}. You won !!")
        return 0

def game():
    print("Guess The Number Game !!\n")
    
    print("Let me think a number between 1 to 100.")
    answer = random.randint(1, 100)
    
    level = input("Choose the level of difficulty : 'EASY', 'MEDIUM' or 'HARD' : ").lower()
    attempts = set_difficulty(level)
    if attempts is None:
        print("Wrong Difficulty Level !!")
        return
    
    guess = 0
    while guess != answer:
        print(f"\nYou have {attempts} attempts remaining !!")
        guess = int(input("Make a guess : "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print(f"\nYou are out of guesses. The correct answer is {answer}. You Lost !!")
            return
        elif guess != answer:
            print("Guess Again !!")
        

game()
