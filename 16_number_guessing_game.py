# Mystery Number Guessing Game
# This program generates a random number and challenges the user to guess it within 7 attempts.

import random

def start_guessing_game():
    """Main game loop for the Number Guessing Game."""
    # Generating a random target number between 1 and 100
    mystery_number = random.randint(1, 100)
    MAX_GUESS_LIMIT = 7
    total_attempts_made = 0
    
    print("\n--- WELCOME TO THE NUMBER GUESSING CHALLENGE ---")
    print(f"I have chosen a number between 1 and 100. Can you guess it in {MAX_GUESS_LIMIT} tries?")
    
    # Loop for managing attempts
    for attempt in range(1, MAX_GUESS_LIMIT + 1):
        try:
            user_guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            total_attempts_made = attempt
            
            # Game logic: Checking the guess against the mystery number
            if user_guess == mystery_number:
                print(f"Fantastic! You've guessed the mystery number in {attempt} attempts.")
                return # Exiting the game function upon winning
            elif user_guess < mystery_number:
                print("Hint: Your guess is too low.")
            else:
                print("Hint: Your guess is too high.")
            
            # Notifying remaining attempts
            remaining = MAX_GUESS_LIMIT - attempt
            if remaining > 0:
                print(f"Keep trying! You have {remaining} attempts left.")
                
        except ValueError:
            # Handling non-integer inputs without docking an attempt if desired
            # But here we let the loop continue and count the bad input as an attempt for simplicity
            print("Input Error: Please enter a valid whole number. (Attempt counted)")
    
    # Executed if the user fails to guess within the limit
    print(f"\nGame Over! You've used all {MAX_GUESS_LIMIT} attempts.")
    print(f"The mystery number was actually: {mystery_number}")

# Offering the user the chance to play multiple rounds
if __name__ == "__main__":
    while True:
        start_guessing_game()
        play_again_choice = input("\nWould you like to play another round? (y/n): ").lower().strip()
        if play_again_choice != 'y':
            print("Thanks for playing! Goodbye.")
            break
