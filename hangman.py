import random

# Words with hints
words = {
    "python": "A popular programming language",
    "computer": "An electronic device used for computing",
    "coding": "The process of writing programs",
    "student": "A person who studies",
    "project": "A task completed for learning or work"
}

# Select random word
secret_word = random.choice(list(words.keys()))
hint = words[secret_word]

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 50)
print("              HANGMAN GAME")
print("=" * 50)
print("Guess the hidden word one letter at a time!")
print(f"Hint: {hint}")
print(f"You have {max_wrong_guesses} incorrect guesses.\n")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", " ".join(guessed_letters))
    print(f"Attempts Left: {max_wrong_guesses - wrong_guesses}/6")

    # Win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word successfully!")
        print("Word:", secret_word)
        break

    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Duplicate guess check
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct or wrong guess
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("Better luck next time!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")