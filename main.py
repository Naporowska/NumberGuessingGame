import random

game_over = False

print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

random_number = random.randint(1, 101)

while not game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == random_number:
        print("You win.")
        game_over = True
    elif attempts == 0:
        print(f"You lose. The number is: {random_number}")
        game_over = True
    elif guess > random_number:
        print("Too high. Guess again.")
    elif guess < random_number:
        print("Too low. Guess again.")
