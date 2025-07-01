
import random

words = ['Python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

org= random.choice(words)
mix = ''.join(random.sample(org, len(org)))

print("Word Scramble Game!")
print("Guess the correct word from this scrambled:")
print("Scrambled word:", mix)

attempts = 0
while True:
    guess = input("Your guess: ").strip()
    attempts += 1

    if guess.lower() == org.lower():
        print(f"Correct! The word was '{org}'. You guessed it in {attempts} attempts.")
        break
    else:
        print("Incorrect. Try again.")
