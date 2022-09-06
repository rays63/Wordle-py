from cmd import PROMPT
import random
import rich
from rich.prompt import Prompt
from rich.console import Console
from Words import Words


def get_words(word):
    word = random.choice(word)
    return word.upper()


def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def score_guess(guess, answer):
    score = []
    for index, letter in enumerate(guess):
        if answer[index] == guess[index]:
            score += correct_place(index)
        elif letter in guess:
            score += correct_letter(index)
        else:
            score += incorrect_letter(index)
    return ''.join(score)


def main():
    rich.print(correct_place("welcome") + " " + correct_letter("To") +
               " " + incorrect_letter("Wordle.Py") + "/n")
    tries = 6

    console = Console()
    answer = get_words(Words)

    while tries != 0:
        tries = tries - 1
        user_inp = Prompt.ask("Enter your Guess: ")
        console.print(score_guess(user_inp, answer))
        if user_inp == answer:
            break


if __name__ == '__main__':
    main()
