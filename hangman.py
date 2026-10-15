import random

# List of possible words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
word = random.choice(words)

# Create hidden version of the word
display = ["_"] * len(word)

# Track wrong guesses
wrong_guesses = 0

# Store letters already guessed
guessed_letters = []

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.")
print(" ".join(display))

while "_" in display and wrong_guesses < 6:
    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1
        print("Wrong guesses:", wrong_guesses, "/ 6")

    print("Word:", " ".join(display))

# Display final result
if "_" not in display:
    print("Congratulations!You guessed the word:", word)
else:
    print("Game over!")
    print("The word was:", word)