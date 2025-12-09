#beginner stage
import random

def random_guessing(start: int, end: int, max_attempts: int) -> bool:
    """
    Play one round of the guessing game.
    Returns True if user guessed correctly, False otherwise.
    """
    secret = random.randint(start, end)  # inclusive
    attempts = 0

    while attempts < max_attempts:
        try:
            user_guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input — please enter an integer.")
            continue  # invalid input does not consume an attempt

        attempts += 1

        if user_guess < secret:
            print("Your guess is too low.")
        elif user_guess > secret:
            print("Your guess is too high.")
        else:
            print(f"Congratulations — you guessed the number in {attempts} attempt(s)!")
            return True

    print(f"Sorry, you've run out of attempts. The number was {secret}.")
    return False


def get_int(prompt: str, min_value=None) -> int:
    """Helper to repeatedly ask for an integer (optionally enforcing min_value)."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if (min_value is not None) and (value < min_value):
            print(f"Please enter an integer >= {min_value}.")
            continue
        return value


def main():
    print("----- Hello, welcome to the number guessing game -----")

    while True:
        # get lower and upper bounds (ensure lower <= upper)
        start = get_int("Enter the lower bound (smallest possible number): ")
        end = get_int("Enter the upper bound (largest possible number): ")

        if start > end:
            print("Lower bound is greater than upper bound — swapping them for you.")
            start, end = end, start

        max_attempts = get_int("How many attempts do you want to guess the number? ", min_value=1)

        random_guessing(start, end, max_attempts)

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing — goodbye!")
            break


if __name__ == "__main__":
    main()

