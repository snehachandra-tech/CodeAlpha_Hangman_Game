import random

words = ["python", "coding", "github", "hangman"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("You won! The word was:", word)
else:
    print("Game over! The word was:", word)
