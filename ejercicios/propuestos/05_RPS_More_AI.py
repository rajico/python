"""
Nombre del programa: Piedra, Papel, Tijera, Lagarto o Spock
Descripción:
Partiendo del código disponible en fichero adjunto añade la funcionalidad necesaria para ofrecer la variante lagarto,
Spock del juego piedra, papel o tijeras.

Usa las diferentes situaciones de juego, junto con su resultado, del archivo victories.xml que se adjunta.

Sustituye el diccionario Victories por alguna referencia que permita acceder al contenido de victories.xml.

Recomiendo usar el módulo xml.etree.ElementTree para procesar el archivo victories.xml.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 17/12/22
"""

# !/usr/bin/python3

import random
from enum import IntEnum
from statistics import mode
import xml.etree.ElementTree as ET

tree = ET.parse('victories.xml')
root = tree.getroot()


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


# Victories = {
#    GameAction.Rock: GameAction.Paper,
#    GameAction.Paper: GameAction.Scissors,
#    GameAction.Scissors: GameAction.Rock,
#    GameAction.Lizard: GameAction.Rock,
#    GameAction.Spock: GameAction.Lizard
# }

NUMBER_RECENT_ACTIONS = 5


def assess_game(user_action, computer_action):
    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Rock crushes lizard. You won!")
            game_result = GameResult.Victory
        else:
            if computer_action == GameAction.Paper:
                print("Paper covers rock. You lost!")
                game_result = GameResult.Defeat
            elif computer_action == GameAction.Spock:
                print("Spock vaporizes rock. You lost!")
                game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Paper disallows Spock. You won!")
            game_result = GameResult.Victory
        else:
            if computer_action == GameAction.Scissors:
                print("Scissors cuts paper. You lost!")
                game_result = GameResult.Defeat
            elif computer_action == GameAction.Lizard:
                print("Lizard eats paper. You lost!")
                game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Spock:
            print("Spock breaks scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            if computer_action == GameAction.Paper:
                print("Scissors cuts paper. You won!")
                game_result = GameResult.Victory
            elif computer_action == GameAction.Lizard:
                print("Scissors beheads lizard. You won!")
                game_result = GameResult.Victory

    # You picked Lizard
    elif user_action == GameAction.Lizard:
        if computer_action == GameAction.Scissors:
            print("Scissors beheads lizard. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Rock:
            print("Rock crushes lizard. You lost!")
            game_result = GameResult.Defeat
        else:
            if computer_action == GameAction.Spock:
                print("Lizard poisons Spock. You won!")
                game_result = GameResult.Victory
            elif computer_action == GameAction.Paper:
                print("Lizard eats paper. You won!")
                game_result = GameResult.Victory

    # You picked Spock
    elif user_action == GameAction.Spock:
        if computer_action == GameAction.Paper:
            print("Paper disallows Spock. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Lizard:
            print("Lizard poisons Spock. You lost!")
            game_result = GameResult.Defeat
        else:
            if computer_action == GameAction.Scissors:
                print("Spock breaks scissors. You won!")
                game_result = GameResult.Victory
            elif computer_action == GameAction.Rock:
                print("Spock vaporizes rock. You won!")
                game_result = GameResult.Victory

    return game_result


def get_computer_action(user_actions_history, game_history):
    # No previous user actions => random computer choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()
    # Alternative AI functionality
    # Choice that would beat the user's most frequent recent choice
    else:
        most_frequent_recent_computer_action = GameAction(mode(user_actions_history[-NUMBER_RECENT_ACTIONS:]))
        computer_action = get_winner_action(most_frequent_recent_computer_action)

    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def get_random_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)

    return computer_action


def get_winner_action(game_action):
    com_choice = GameAction
    for victory in root.findall('victory'):
        if victory.get('choice') == "Rock" and game_action == GameAction.Rock:
            com_choice = [GameAction.Paper, GameAction.Spock]
        elif victory.get('choice') == "Paper" and game_action == GameAction.Paper:
            com_choice = [GameAction.Scissors, GameAction.Lizard]
        elif victory.get('choice') == "Scissors" and game_action == GameAction.Scissors:
            com_choice = [GameAction.Rock, GameAction.Spock]
        elif victory.get('choice') == "Lizard" and game_action == GameAction.Lizard:
            com_choice = [GameAction.Rock, GameAction.Scissors]
        elif victory.get('choice') == "Spock" and game_action == GameAction.Spock:
            com_choice = [GameAction.Scissors, GameAction.Lizard]

    return random.choice(com_choice)


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    game_history = []
    user_actions_history = []

    while True:
        try:
            user_action = get_user_action()
            user_actions_history.append(user_action)
        except ValueError as e:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user_actions_history, game_history)
        game_result = assess_game(user_action, computer_action)
        game_history.append(game_result)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
