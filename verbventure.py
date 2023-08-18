import random

# List of words for each level
beginners_words = ["apple", "happy", "cloud", "water", "table"]
moderate_words = ["elephant", "guitar", "diamond", "sunrise", "flamingo"]
expert_words = ["chocolate", "incredible", "juxtapose", "butterfly", "zylophone"]

def select_word(level):
    """Selects a word based on the chosen difficulty level."""
    if level == "beginners":
        return random.choice(beginners_words)
    elif level == "moderate":
        return random.choice(moderate_words)
    elif level == "expert":
        return random.choice(expert_words)
    else:
        return None

def check_guess(word, guess):
    """Compares the user's guess with the secret word and generates feedback."""
    if len(guess) != len(word):
        return "Length mismatch"
    
    result = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            result += guess[i]
        else:
            result += "_"
    return result

def main():
    """Main function to run the Find a Word game."""
    print("Welcome to the Find a Word game!")
    level = input("Choose a level (beginners/moderate/expert): ").lower()
    
    if level not in ["beginners", "moderate", "expert"]:
        print("Invalid level choice.")
        return
    
    secret_word = select_word(level)
    if secret_word is None:
        print("Invalid level choice.")
        return
    
    max_attempts = 5 if level == "beginners" else 7 if level == "moderate" else 10
    
    print(f"Guess the {len(secret_word)}-letter word. You have {max_attempts} attempts.")
    
    attempts = 0
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: ").lower()
        
        if not guess.isalpha() or len(guess) != len(secret_word):
            print("Invalid input. Please enter a valid word.")
            continue
        
        result = check_guess(secret_word, guess)
        print("Result:", result)
        
        if result == secret_word:
            print("Congratulations! You guessed the word!")
            break
        
        attempts += 1
    
    if attempts == max_attempts:
        print("Sorry, you've run out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    main()
