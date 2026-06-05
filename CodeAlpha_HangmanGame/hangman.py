import random

# Word list
WORDS = ["python", "laptop", "garden", "jungle", "bridge"]

# Hangman stages (using raw strings to avoid warnings)
HANGMAN = [
    r"""
   -----
   |   |
       |
       |
       |
       |
==========""",
    r"""
   -----
   |   |
   O   |
       |
       |
       |
==========""",
    r"""
   -----
   |   |
   O   |
   |   |
       |
       |
==========""",
    r"""
   -----
   |   |
   O   |
  /|   |
       |
       |
==========""",
    r"""
   -----
   |   |
   O   |
  /|\  |
       |
       |
==========""",
    r"""
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
==========""",
    r"""
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
==========""",
]

def play_hangman():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0
    max_wrong = 6

    print("\n🎮 Welcome to HANGMAN!")
    print("Guess the word letter by letter. You have 6 wrong guesses.\n")

    while wrong < max_wrong:
        print(HANGMAN[wrong])

        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Wrong guesses left: {max_wrong - wrong}")
        print(f"Letters guessed: {', '.join(sorted(guessed)) if guessed else 'None'}")

        if all(letter in guessed for letter in word):
            print(f"\n🎉 You WIN! The word was: {word.upper()}")
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single letter!")
            continue

        if guess in guessed:
            print("⚠ You already guessed that letter!")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            wrong += 1
            print(f"❌ '{guess}' is NOT in the word!")

    print(HANGMAN[wrong])
    print(f"\n💀 GAME OVER! The word was: {word.upper()}")

def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != "yes":
            print("\nThanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
