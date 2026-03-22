# Word Guessing Game (Wordle-style)
# Author: Hudson Lee
#
# Creativity additions: The secret word is randomly chosen from a built-in list each game
# so no two games are the same. A play-again loop lets you keep playing without restarting,
# and a running list of already-tried letters is shown after each valid guess to help
# narrow down choices faster.

import random

# ── Secret word list (all lowercase) ─────────────────────────────────────────
WORDS = [
    "mosiah", "helaman", "moroni", "temple", "record",
    "python", "castle", "bridge", "planet", "forest",
    "candle", "silver", "rocket", "frozen", "marble",
    "sunset", "window", "basket", "breeze", "gravel",
    "coding", "garden", "harbor", "jungle", "mirror",
    "blanket", "captain", "digital", "explore", "freedom",
    "journey", "mystery", "rainbow", "science", "thunder",
]

# ─────────────────────────────────────────────────────────────────────────────

def build_hint(secret, guess):
    """
    Build one line of hint characters:
      UPPERCASE  → correct letter, correct position
      lowercase  → letter is in the word but wrong position
      _          → letter not in the word at all
    Characters are separated by spaces.
    """
    hint_chars = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            hint_chars.append(guess[i].upper())
        elif guess[i] in secret:
            hint_chars.append(guess[i].lower())
        else:
            hint_chars.append("_")
    return " ".join(hint_chars)


def play_game():
    secret = random.choice(WORDS)
    word_length = len(secret)
    guesses = 0
    used_letters = []

    print()
    print("Welcome to the word guessing game!")
    print()

    # Show initial hint of underscores
    initial = " ".join(["_"] * word_length)
    print(f"Your hint is: {initial}")

    while True:
        # Show used letters (creativity feature)
        if used_letters:
            unique_used = sorted(set(used_letters))
            print(f"Letters tried: {' '.join(unique_used)}")

        guess = input("What is your guess? ").strip().lower()
        guesses += 1

        # Check length before anything else
        if len(guess) != word_length:
            print("Sorry, the guess must have the same number of letters as the secret word.")
            print()
            continue

        # Track letters used in valid guesses
        for ch in guess:
            used_letters.append(ch)

        # Win condition
        if guess == secret:
            print(f"Congratulations! You guessed it!")
            print(f"It took you {guesses} {'guess' if guesses == 1 else 'guesses'}.")
            return

        # Show hint for this guess
        hint = build_hint(secret, guess)
        print(f"Your hint is: {hint}")


# ── Main loop ─────────────────────────────────────────────────────────────────
while True:
    play_game()
    print()
    again = input("Would you like to play again? (yes or no) ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break
