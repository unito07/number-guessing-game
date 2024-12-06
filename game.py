import random

def play_game():
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    while True:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    play_game()
    
    while input("\nWould you like to play again? (yes/no): ").lower().startswith('y'):
        play_game()