#beginner stage
import random
class wordguess:
    def __init__(self,wordlist,maxattempts):
        self.curattrempt=0
        self.wordlist=wordlist
        self.maxattempts=maxattempts
        self.guesses=[]
        self.currattempt=0
        self.secertword=random.choice(self.wordlist)
        self.accuracy=0
        self.won=False
    def play(self):
       self.curattrempt+=1
       if self.curattrempt<=self.maxattempts:
        print(f"you have remaining {self.maxattempts-len(self.guesses)} to guess the word ")
        guess=input("enter word that you are thinking that matches the computer guess:")
        self.guesses.append(guess)
        if self.secertword==guess:
           print(f"you have correct guess in {len(self.guesses)} choices")
           self.won=True
        else:
           self.play()
       else:
          print("you ran out of choices to guess")
      
    def get_accuracy(self):
        attempts = len(self.guesses)
        if self.won:
            # attempts >= 1 and <= max_attempts
            return max(0.0, (1 - (attempts - 1) / self.max_attempts) * 100)
        return 0.0

def getandstart(wordlist):
    # wordlist=[]
     if not wordlist:
      while True:
       word=input("Enter a word to create first wordlist then guess words:")
       wordlist.append(word)
       choice=input("Do you want to insert more words or not if you want enter yes or else any key:")
       if choice.lower()=="yes":
          continue
       else:
          break
    
    #print(wordlist)
     try:
      maxattempts=int(input("enter maximum attempts you want to guess the word:"))
     except ValueError:
       print("Invalid input for maximum attempts:setting default value is 5")
       maxattempts=5
     game=wordguess(wordlist,maxattempts)
     game.play()
     play_again=input("do you want to play:yes or no:")
     while play_again.lower()=="yes":
       choice=input("Enter yes to make guess with same word list or with separate wordlist:")
       if choice=="yes":
          getandstart(wordlist)
       else:
          getandstart([])

       
       
if __name__=="__main__":
    print("-"*10,"welcome to word guessgame:","-"*10)
    getandstart([])
# import random
# from typing import List


# class WordGuess:
#     """Simple word-guessing game."""

#     def __init__(self, wordlist: List[str], max_attempts: int = 5):
#         if not wordlist:
#             raise ValueError("wordlist must contain at least one word.")
#         self.wordlist = [w.strip() for w in wordlist if w.strip()]
#         self.max_attempts = max(1, int(max_attempts))
#         self.secret_word = random.choice(self.wordlist).lower()
#         self.guesses: List[str] = []
#         self.won = False

#     def play(self) -> None:
#         """Run the guessing loop (non-recursive)."""
#         print(f"\nYou have {self.max_attempts} attempts to guess the secret word.")
#         while len(self.guesses) < self.max_attempts:
#             remaining = self.max_attempts - len(self.guesses)
#             print(f"\nRemaining attempts: {remaining}")
#             guess = input("Enter your guess: ").strip()
#             if not guess:
#                 print("Please enter a non-empty word.")
#                 continue

#             self.guesses.append(guess)
#             if guess.lower() == self.secret_word:
#                 self.won = True
#                 attempts_used = len(self.guesses)
#                 print(f"\n🎉 Correct! You guessed the word in {attempts_used} attempt(s).")
#                 print(f"Secret word: {self.secret_word}")
#                 print(f"Accuracy: {self.get_accuracy():.1f}%")
#                 break
#             else:
#                 print("Incorrect guess.")
#                 # Optionally give a tiny hint (uncomment if you want):
#                 # print(f"Hint: the word has {len(self.secret_word)} letters.")

#         if not self.won:
#             print("\n🚫 You ran out of attempts.")
#             print(f"The secret word was: {self.secret_word}")
#             print(f"Accuracy: {self.get_accuracy():.1f}%")

#     def get_accuracy(self) -> float:
#         """
#         Compute a simple accuracy score:
#           - If guessed, accuracy = (1 - (attempts_used - 1)/max_attempts) * 100
#             (first try => 100%, last try => ~1/max_attempts*100).
#           - If not guessed, accuracy = 0.0
#         """
#         attempts = len(self.guesses)
#         if self.won:
#             # attempts >= 1 and <= max_attempts
#             return max(0.0, (1 - (attempts - 1) / self.max_attempts) * 100)
#         return 0.0


# def get_and_start(existing_wordlist: List[str] = None):
#     """Collect words (if needed) and start one or more games. Loop-based control flow."""
#     if existing_wordlist is None:
#         existing_wordlist = []

#     # If no words provided, prompt user to create a wordlist
#     if not existing_wordlist:
#         print("Create your initial word list. Enter words one at a time.")
#         while True:
#             w = input("Enter a word (or just press Enter to stop adding): ").strip()
#             if not w:
#                 if existing_wordlist:
#                     break
#                 print("Wordlist is empty — please add at least one word.")
#                 continue
#             existing_wordlist.append(w)
#             more = input("Add more? Type 'yes' to continue, or anything else to stop: ").strip().lower()
#             if more != "yes":
#                 break

#     # Validate and clean the list
#     existing_wordlist = [w.strip() for w in existing_wordlist if w.strip()]
#     if not existing_wordlist:
#         print("No valid words supplied. Exiting.")
#         return

#     # Get max attempts
#     try:
#         max_attempts = int(input("Enter maximum attempts (default 5): ").strip() or 5)
#     except ValueError:
#         print("Invalid input. Using default of 5 attempts.")
#         max_attempts = 5

#     # Main play loop (allows replaying)
#     while True:
#         game = WordGuess(existing_wordlist, max_attempts)
#         game.play()

#         again = input("\nPlay again? Type 'yes' to continue, anything else to quit: ").strip().lower()
#         if again != "yes":
#             print("Thanks for playing — goodbye!")
#             break

#         reuse = input("Use the same word list? Type 'yes' to reuse, anything else to create a new list: ").strip().lower()
#         if reuse == "yes":
#             # continue with same existing_wordlist
#             continue
#         else:
#             # reset wordlist and re-run collection
#             existing_wordlist = []
#             print("\nCreate a new word list.")
#             while True:
#                 w = input("Enter a word (or just press Enter to stop adding): ").strip()
#                 if not w:
#                     if existing_wordlist:
#                         break
#                     print("Wordlist is empty — please add at least one word.")
#                     continue
#                 existing_wordlist.append(w)
#                 more = input("Add more? Type 'yes' to continue, or anything else to stop: ").strip().lower()
#                 if more != "yes":
#                     break

#             # Ask again for max_attempts or reuse previous
#             try:
#                 max_attempts = int(input("Enter maximum attempts (default 5): ").strip() or 5)
#             except ValueError:
#                 print("Invalid input. Using default of 5 attempts.")
#                 max_attempts = 5


# if __name__ == "__main__":
#     print("-" * 8, "Welcome to Word Guess Game", "-" * 8)
#     get_and_start()

