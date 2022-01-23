import random
import time
import os

from allowed_words import allowed_words_list

class WordleSolver:

    five_letter_words = allowed_words_list

    success = False

    def get_first_word(self):
        first_choice_word = random.choice(self.five_letter_words)
        while len(set(first_choice_word)) != len(first_choice_word):
            first_choice_word = random.choice(self.five_letter_words)

        return first_choice_word

    def get_word(self):
        return random.choice(self.five_letter_words)

    def print_color_meanings(self):
        print("\n'g': green - correct letter and correct placement\n")
        print("'y': yellow - correct letter but incorrect placement\n")
        print("'b': black - incorrect letter and incorrect placement\n")
        print("'!': error - word is not a valid English word\n")
        print("'s': success - word is complete and game is over\n\n")

    def print_underlined_char(self, word, index):
        word_to_print = ''
        for selected_index, char in enumerate(word):
            if selected_index == index:
                word_to_print += f"\033[4m{char}\033[0m"
            else:
                word_to_print += char
            word_to_print += ' '

        print(f'\t{word_to_print}')

    def check_guess(self, word):
        for index, char in enumerate(word):
            os.system('clear')
            self.print_color_meanings()
            self.print_underlined_char(word, index)
            result = input('\n\tEnter result of letter: ')
            result = result.lower()

            if result != 's':
                self.five_letter_words = [value for value in self.five_letter_words if value != word]
            
            if result == 'g':
                self.five_letter_words = [word for word in self.five_letter_words if word[index] == char]

            if result == 'y':
                self.five_letter_words = [word for word in self.five_letter_words if word[index] != char and char in word]

            if result == 'b':
                self.five_letter_words = [word for word in self.five_letter_words if char not in word]

            if result == '!':
                self.five_letter_words = [item for item in self.five_letter_words if word != item]
                return

            if result == 's':
                self.success = True
                for i in range(5):
                    print('\n\n\t\t\t\tCongratulations!\n\n')
                    time.sleep(0.4)
                    os.system('clear')
                return

def main():
    wordle_solver = WordleSolver()
    first_guess = wordle_solver.get_first_word()
    wordle_solver.check_guess(first_guess)
    while not wordle_solver.success:
        next_guess = wordle_solver.get_word()
        if not wordle_solver.five_letter_words:
            print('Out of possible guesses. Sorry.')
            return
        wordle_solver.check_guess(next_guess)


if __name__ == '__main__':
    main()