# Word Guessing Game (Wordle-style)
# Author: Hudson Lee
#
# Creativity additions: The secret word is randomly selected from a built-in word list each
# game, so the experience is different every time. The game also enforces a 6-guess limit like
# real Wordle, tracks and displays already-used letters after each round, and includes a
# play-again loop so you can keep going without restarting the program.

import random

# ─── Word list ────────────────────────────────────────────────────────────────
# Words of varying lengths — one is picked at random each game.
WORD_LIST = [
    # 5 letters
    "frost", "blaze", "crane", "crisp", "dwarf",
    "flint", "grasp", "heist", "knack", "lymph",
    "maple", "ninja", "optic", "pixel", "quill",
    "scone", "tiger", "ulcer", "vivid", "waltz",
    # 6 letters
    "bridge", "castle", "candle", "forest", "frozen",
    "garden", "harbor", "jungle", "marble", "mirror",
    "planet", "pillow", "rocket", "silver", "stream",
    "sunset", "window", "basket", "breeze", "gravel",
    # 7 letters
    "blanket", "captain", "digital", "explore", "freedom",
    "journey", "mystery", "rainbow", "science", "thunder",
    "whisper", "capable", "distant", "exhibit", "fantasy",
]

MAX_GUESSES = 6


# ─── Core logic ───────────────────────────────────────────────────────────────

def initial_hint(secret):
    """Return a hint of underscores matching the length of secret."""
    return " ".join(["_"] * len(secret))


def build_hint(secret, guess):
    """
    Return a hint string for one guess:
      UPPERCASE  → correct letter, correct position
      lowercase  → correct letter, wrong position
      _          → letter not in secret word at all
    """
    hint_parts = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            hint_parts.append(guess[i].upper())
        elif guess[i] in secret:
            hint_parts.append(guess[i].lower())
        else:
            hint_parts.append("_")
    return " ".join(hint_parts)


# ─── One game ─────────────────────────────────────────────────────────────────

def play_game():
    secret = random.choice(WORD_LIST)
    guesses = 0
    used_letters = set()

    print()
    print("=" * 50)
    print("   Welcome to the word guessing game!")
    print("=" * 50)
    print(f"  The word has {len(secret)} letters.")
    print(f"  You have {MAX_GUESSES} guesses. Good luck!")
    print()
    print(f"Your hint is: {initial_hint(secret)}")

    while guesses < MAX_GUESSES:

        # Show used letters once at least one guess has been made
        if used_letters:
            print(f"Letters tried: {' '.join(sorted(used_letters))}")

        guess = input("What is your guess? ").strip().lower()
        guesses += 1

        # ── Length check ──
        if len(guess) != len(secret):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            print()
            continue

        # ── Track letters ──
        for ch in guess:
            used_letters.add(ch)

        # ── Win condition ──
        if guess == secret:
            print()
            print("Congratulations! You guessed it!")
            print(f"It took you {guesses} {'guess' if guesses == 1 else 'guesses'}.")
            return

        # ── Show hint ──
        hint = build_hint(secret, guess)
        print(f"Your hint is: {hint}")

        remaining = MAX_GUESSES - guesses
        if remaining == 1:
            print("  (Last guess!)")
        elif remaining > 0:
            print(f"  ({remaining} guesses remaining)")
        print()

    # ── Out of guesses ──
    print()
    print(f"Game over! You used all {MAX_GUESSES} guesses.")
    print(f"The secret word was: {secret}")


# ─── Main loop ────────────────────────────────────────────────────────────────

while True:
    play_game()
    print()
    again = input("Would you like to play again? (YES or NO) ").strip().lower()
    if again != "yes":
        print()
        print("Thanks for playing! Goodbye.")
        break
