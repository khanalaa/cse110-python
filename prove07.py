secret_word = "temple"

print("Welcome to the guessing game!!!")

count = 0
for letter in secret_word:
    count += 1

print("\nYour hint is: " + ("_ "*count))

display = []
guess = input("What is your guess? ").lower()
guess_count = 0
for char in guess:
    guess_count += 1
    display += "_"


is_true = False
loop_count = 0

while not is_true :
    loop_count += 1
    if len(guess) != count:
        print("\nSorry, the guess must have the same number of letters as the secret word.")
        guess = input("What is your guess? ").lower()
    else:
        if secret_word == guess:
            print("\nCongratulations! You guessed it!")
            is_true = True
        else:
            position = 0
            for char in guess:
                if char == secret_word[position]:
                    display[position] = char.upper()
                else:
                    for i in secret_word:
                        if i == char:
                            display[position] = char
                position += 1

            print(f"\nYour hint is:{' '.join(display)}")
            guess = input("What is your guess? ").lower()
    
    
print(f"It took you {loop_count} guesses.")