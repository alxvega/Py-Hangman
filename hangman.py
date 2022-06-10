class Hangman():
    def __init__(self, word):
        self.word = word.lower().strip()
        self.guesses = 6 #Set number counting legs and arms.
        self.word_as_list = list(self.word)
        self.word_completion = list("_" * len(self.word))
        self.guessed_letters = []
        self.finished = False
        self.start = self.get_user_input()

    def get_user_input(self):
        """This is the main function that iterates the user input and refers to the others"""
        while self.guesses > 0 and self.finished == False:
            usr_input = input('Please enter the letter/word guess: ')
            if len(usr_input) > 1:
                self.check_risk_guess(usr_input)
            else:
                self.check_letter(usr_input)
                
        if self.guesses == 0:
            print('Better luck next time! :)')
            
        if self.word_as_list == self.word_completion:
            print("Congrats!! You guessed correctly :) ")
            self.finished = True
            
    def check_letter(self,letter):
        "Single letter user input check."
        if letter not in self.word:
            self.guesses -=1
            print( f'{letter} was not in the word. You have {self.guesses} guesses remaining.')
            self.display_hangman()
        elif letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            for index, char in enumerate(self.word_as_list):
                if char in self.guessed_letters:
                    self.word_completion[index] = char
            self.display_hangman()
            print(self.word_completion)
        else:
            print(f'{letter} is already in the guessed letters. Try another one.')
    
    def check_risk_guess(self, guess):
        "Checks for total guess comparison, ends the game if not correct."
        if guess != self.word:
            print(f'That was a risky guess. You lost. The word was {self.word}')
            self.finished = True
            self.display_hangman()
        else:
            print("Congrats!! You guessed correctly :) ")
            print(f'{self.word_as_list}')
            self.finished = True
        

    def display_hangman(self):
        """Prints the current status of lives. """
        stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
        ]
  
        return print(stages[self.guesses] )



def main():
    print('Welcome to the Hangman.py game :)')
    choice = input('Please enter Y to continue or N to quit: ').upper()
    while choice != 'Y' and choice != 'N':
        choice = input('Ooops. Seems something was wrong. Please enter Y to continue or N to quit: ').upper()
    if choice == 'N':
        print('Goodbye')
    else:
        word = input("Alright! Let's begin. Enter a single word to guess: ")
        while len(word.split()) > 1:
            word = input("That didn't seem quite right. Please enter only ONE word: ")
            
        #Game starts
        new_game = Hangman(word)
        new_game.start
 
    

if __name__ == '__main__':
    main()
        
        