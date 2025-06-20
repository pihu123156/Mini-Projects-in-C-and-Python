import random

def choose_difficulty():
    print("\n Choose Difficulty Level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    
    while True:
        level = input("Enter choice (1/2/3): ")
        if level == '1':
            return 10
        elif level == '2':
            return 50
        elif level == '3':
            return 100
        else:
            print(" Invalid input. Try again.")

def play_game():
    high_score = None

    while True:
        max_num = choose_difficulty()
        number = random.randint(1, max_num)
        attempts = 0

        print(f"\n🤖 I'm thinking of a number between 1 and {max_num}. Try to guess it!")

        while True:
            try:
                guess = int(input("Your guess: "))
                attempts += 1
                if guess < number:
                    print(" Too low!")
                elif guess > number:
                    print(" Too high!")
                else:
                    print(f" Correct! You guessed it in {attempts} tries.")
                    if high_score is None or attempts < high_score:
                        high_score = attempts
                        print(" New high score!")
                    else:
                        print(f" High score to beat: {high_score} tries")
                    break
            except ValueError:
                print(" Please enter a valid number.")

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print(" Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
