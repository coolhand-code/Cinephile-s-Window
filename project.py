import os
import cowsay
import sys
import random
import requests
import csv

from tabulate import tabulate
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def main():
    greeting()
    playerName = get_player_name()
    menu(playerName)
    difficulty = get_difficulty(playerName)
    score = get_data_and_play(difficulty, playerName)
    score_recorder(playerName, score, difficulty)
    play_more(score)


def greeting():
    """
    Greets the player with a heading and print a message to let the user know how to continue
    then summerize the aim of the game. If anything other than enter is inputted, the progam
    constantly asks for pressing enter. After any unacceptable input, terminal window will be
    cleaned.

    :return: None
    :rtype: NoneType
    """
    LINER = "[bright_white]" + "><" * 25 + "[/]"
    while True:
        os.system("clear")
        greetingMessage = console.input(
            f"{LINER}\n"
            "[light_steel_blue]Greetings! Welcome to the 🎬 Cinephile's Window 📺[/]\n"
            f"{LINER}\n\n"
            "press <enter> to continue... "
        )

        if greetingMessage != "":
            pass
        else:
            while True:
                aimMessage = input(
                    "\nThe aim of the game is to test your film and TV knowledge.\n"
                )
                if aimMessage != "":
                    os.system("clear")
                    print("press <enter> to continue... ")
                    pass
                else:
                    return False


def get_player_name():
    """
    Asks a player name until the user inputs min 4, max 10 character or 100 wrong input.
    After any unwanted input, terminal window will be cleaned.

    :return: if conditions are met, returns the inputted user name. Otherwise sends an
    error message with a bold red font and asks constantly for a new input. To avoid to
    stuck in a loop possible inputs are limited.
    :rtype: str or raises SystemExit
    """
    os.system("clear")
    INPUT_LIMIT = 10
    for _ in range(INPUT_LIMIT):

        playerName = input("Please, enter a player name: ").strip()

        if 4 <= len(playerName) <= 10:
            return playerName
        else:
            os.system("clear")
            console.print("[bold red]Player name must consist of 4 to 10 characters[/]")

    cowsay.daemon(
        "Uh-Oh! It looks like you've wasted too much time trying to think of a perfect player name. Better luck next time!"
    )
    sys.exit()


def menu(playerName):
    """
    Clears the terminal window and then prints a message by a fox which addresses the user name
    asked previously. At the same time gives to the player options with desired letters.
    According to the response, another functions are executed.

    :param playerName: player name
    :type playerName: str
    :return: None
    :rtype: NoneType
    """
    for i in range(10):
        os.system("clear")
        cowsay.fox(f"Alright, {playerName}!")
        option = input(
            "\nTo see the game rules press <r> and <enter>\n"
            "To see the highscore board press <h> and <enter>\n"
            "To go to select difficulty level press <d> and <enter>\n"
            "To exit press <e> and <enter>... "
        )

        if option == "r":
            game_rules()
        elif option == "h":
            high_scores()
        elif option == "d":
            break
        elif option == "e":
            os.system("clear")
            cowsay.turtle("See you next time!")
            sys.exit()


def game_rules():
    """
    Clears the terminal window first. Prints the game rules in a table with a given style and a header
    Prints the options: going back or exiting the program.

    :return: None
    :rtype: NoneType
    """
    RULES = [
        "1. You will be asked 10 questions about film and television.",
        "2. To answer a question, you just need to type the letter next to the given choice and press <enter>.",
        "3. Every correct answer is 10 points.",
        "4. Any input other than given choice passes the question and will be accepted as a wrong answer.",
        "5. Every wrong answer is -5 points.",
    ]

    while True:
        os.system("clear")
        table = Table(box=box.DOUBLE_EDGE, expand=False)
        for i in range(len(RULES)):
            if i == 0:
                table.add_column(
                    header="Game Rules", header_style="bright_green", justify="center"
                )
            table.add_row(RULES[i])

        console.print(table)

        response = input(
            "\nTo go back to the menu press <b> and <enter>\n"
            "To exit the program press <e> and <enter>... "
        )
        if response == "e":
            os.system("clear")
            cowsay.turtle("See you next time!")
            sys.exit()
        elif response == "b":
            break
        else:
            pass


def high_scores():
    """
    Clears the terminal window first. Reads the "high_scores.csv" file by using
    csv.DictReader. Appends the data into an empty list. Sort the list within the
    score key in a decending order and prints in a nicely formatted table.Displays
    the rank, player name, and difficulty levels. Gives the options: going back or
    exiting the program with pressing desired letters.Otherwise same screen is
    kept refreshing.

    :return: None
    :rtype: NoneType
    """
    while True:
        os.system("clear")
        score_list = []
        with open("high_scores.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                score_list.append(
                    {
                        "player_name": row["player_name"],
                        "score": row["score"],
                        "difficulty": row["difficulty"],
                    }
                )

        sorted_score_table = Table(
            title="HIGH SCORES",
            box=box.DOUBLE_EDGE,
            style="cyan",
            expand=False,
            title_style="light_goldenrod1",
            header_style="gold3",
        )
        sorted_score_table.add_column(header="Rank")
        sorted_score_table.add_column(
            header="Player Name",
        )
        sorted_score_table.add_column(header="Score")
        sorted_score_table.add_column(header="Difficulty")

        n = 0
        for i in sorted(score_list, key=lambda i: int(i["score"]), reverse=True):
            if n < 10:
                n += 1
                sorted_score_table.add_row(
                    f"{str(n)}.", i["player_name"], i["score"], i["difficulty"]
                )

        console.print(sorted_score_table)

        i = input(
            "\nTo go back to the menu press <b> and <enter>\n"
            "To exit the program press <e> and <enter>... "
        )
        if i == "e":
            os.system("clear")
            cowsay.turtle("See you next time!")
            sys.exit()
        elif i == "b":
            break
        else:
            pass


def get_difficulty(playerName):
    """
    Clears the terminal window and then prints a message that introduces diffuculty levels by a fox
    At the same time gives the player options with numbers or letter 'b' to go back. Any other input
    is not accepted and refresh the current screen.

    :param playerName: player name
    :type playerName: str
    :return: the difficulty level as a set of str or executes the main(playerName) function
    :rtype: str or NoneType


    """
    INPUT_LIMIT = 10
    for _ in range(INPUT_LIMIT):
        os.system("clear")
        cowsay.fox("There are 3 difficulty levels\n\n")
        response = input(
            "Easy       <1>\n"
            "Medium     <2>\n"
            "Hard       <3>\n\n"
            "To select difficulty, press any number above and <enter>\n"
            "To go back, press <b> and <enter>\n"
            "To exit, press <e> and <enter>: "
        )
        os.system("clear")
        if response == "1":
            return "easy"
        elif response == "2":
            return "medium"
        elif response == "3":
            return "hard"
        elif response == "e":
            cowsay.turtle("See you next time!")
            sys.exit()
        elif response == "b":
            menu(playerName)
        else:
            pass
    cowsay.daemon(
        " Oh, well! Looks like you are not so keen to read instructions, doesn't it? Alright, then let's end your pain. Game over. Better luck for next time!"
    )
    sys.exit()


def get_data_and_play(difficulty, playerName):
    """
    Gets the data from a API data set. Initilize the score as 0. Displays the ruled game title
    on the top of the screen, generates the score, shows player name and which question the
    player on. Asks 10 questions one by one using a stegosaurus that wears a hat. Shows questions
    and choices in a table. Expects answer.

    :param difficulty: difficulty level
    :type difficulty: str
    :param playerName: player name
    :type playerName: str
    :return: score
    :rtype: int
    """
    info = requests.get(
        f"https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=20&region=GB&difficulty={difficulty}"
    )
    i = info.json()
    score = 0
    NUMBER_OF_QUESTIONS = 10
    for k in range(NUMBER_OF_QUESTIONS):
        console.rule("🎬 Cinephile's Window 📺", style="deep_pink4")
        console.print(
            f"[dark_slate_gray1]Level:[/] {difficulty.title()}\n"
            f"[dark_slate_gray1]Score:[/] {score}\n"
            f"[dark_slate_gray1]Player Name:[/] {playerName}\n",
            style="bold",
        )
        console.rule(f"Question: {k + 1}", style="deep_pink4")
        cowsay.stegosaurus(f'{i[k]["question"]}')
        choices = []
        choices.append(i[k]["correctAnswer"])
        choices.append(i[k]["incorrectAnswers"][0])
        choices.append(i[k]["incorrectAnswers"][1])
        choices.append(i[k]["incorrectAnswers"][2])
        correct_answer = i[k]["correctAnswer"]
        random.shuffle(choices)

        table = [
            ["A:", choices[0]],
            ["B:", choices[1]],
            ["C:", choices[2]],
            ["D:", choices[3]],
        ]

        print(tabulate(table, tablefmt="fancy_outline"))

        answer = str.upper(input("Answer: "))
        os.system("clear")
        if (
            answer == "A"
            and choices[0] == correct_answer
            or answer == "B"
            and choices[1] == correct_answer
            or answer == "C"
            and choices[2] == correct_answer
            or answer == "D"
            and choices[3] == correct_answer
        ):
            score += 10
        else:
            score -= 5
    return score


def score_recorder(playerName, score, difficulty):
    """
    Opens a file named 'high_scores.csv'. Saves the game's data such as diffuculty
    level, score and user name into that file.

    :param playerName: player name
    :type playerName: str
    :param score: total score after the 10 questions
    :type score: int
    :param difficulty: difficulty level
    :type difficulty: str
    :return: None
    :rtype: NoneType
    """
    with open("high_scores.csv", "a") as file:
        file.write(f"{playerName},{score},{difficulty}\n")


def play_more(score):
    """
    Clears th terminal window.A demonic character says game over and the final score.
    Asks for a new game. If yes executes main function. Otherwise exits the program with
    a message saying see youu next time by a turtle.

    :param score: score
    :type score: int
    :return: None
    :rtype: NoneType
    """
    while True:
        os.system("clear")
        cowsay.daemon(f"Game over! Your final score is {score}.")
        i = input("\nDo you want to play a new game? (y/n) :")
        if i == "y":
            main()
        elif i == "n":
            os.system("clear")
            cowsay.turtle("See you next time!")
            sys.exit()


if __name__ == "__main__":
    main()
