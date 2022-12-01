# 🎬 Cinephile's Window 📺
#### Video Demo:  <https://youtu.be/qP9L58txdYw>
#### Description:
This game is designed for Harvard CS50P's final project. It is a multiple-choice quiz game.

To run the program 'python project.py' must be entered within the project directory. The game will then begin with a greeting. The player is given a guideline which includes how to check the game rules, check the high scores, selecting difficulty and returning to the menu.

There will be 10 film or TV related questions each game. Every correct answer gives you 10 points, every wrong answer costs you 5 points. If The player doesn't want to answer a question, they can opt to pass. In that case this will be accepted as a wrong answer. The current score and the question number are displayed during the gameplay.

Scores will be added in a csv file after every game which includes the player name and the difficulty level.



## Libraries and Modules Used
* os: used for clearing the terminal window so it gives a nice and neat playing area to the game and contributes to user experience.
* cowsay: used for printing guidance text and questions by different animalistic characters as if they talk to the player to make the game more visually appealing.
* sys: used for exiting the program when desired.
* random: used for shuffling correct and incorrect answers.
* requests : used for supplying the questions from an API date set.
* csv: used for recording the high scores.
* tabulate: used for putting the choices in a table
* rich: used for printing colorful text, tabulating the game rules and the high scores.

## Data Source
* All the questions and the answers are provided by this address <https://the-trivia-api.com/>  which you can find much more data for free for your own projects as well.

## Documentation
#### Functions (excluding main)


```hash
greeting():

    Greets the player with a heading and prints a message to let the user know how to continue
    then summarize the aim of the game. If anything other than enter is inputted, the program
    constantly asks the user to press enter. After any unacceptable input, the terminal window will be
    cleaned.

    :return: None
    :rtype: NoneType

get_player_name():

    Asks a player name until the user inputs min 4, max 10 character or 100 wrong input.
    After any unwanted input, terminal window will be cleaned.

    :return: if conditions are met, returns the inputted user name. Otherwise sends an
    error message with a bold red font and asks constantly for a new input. To avoid to
    stuck in a loop possible inputs are limited.
    :rtype: str or raises SystemExit

menu(playerName):

    Clears the terminal window and then prints a message by a fox which addresses the user name
    asked previously. At the same time gives to the player options with desired letters.
    According to the response, another functions are executed.

    :param playerName: player name
    :type playerName: str
    :return: None
    :rtype: NoneType

game_rules():

    Clears the terminal window first. Prints the game rules in a table with a given style and a header.
    Prints the options: going back or exiting the program.

    :return: None
    :rtype: NoneType

high_scores():

    Clears the terminal window first. Reads the "high_scores.csv" file by using
    csv.DictReader. Appends the data into an empty list. Sorts the list within the
    score key in a decending order and prints in a nicely formatted table. Displays
    the rank, player name, and difficulty levels. Gives the options: going back or
    exiting the program by pressing desired letters. Otherwise, the same screen will
    keep refreshing.

    :return: None
    :rtype: NoneType

get_difficulty(playerName):

    Clears the terminal window and then prints a message that introduces diffuculty levels by a fox
    At the same time gives the player options with numbers or letter 'b' to go back. Any other input
    is not accepted and refresh the current screen.

    :param playerName: player name
    :type playerName: str
    :return: the difficulty level as a set of str or executes the main(playerName) function
    :rtype: str or NoneType

get_data_and_play(difficulty, playerName):

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

score_recorder(playerName, score, difficulty):

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

play_more(score):

    Clears the terminal window. A demonic character says 'game over' and reveals the final score.
    Asks for a new game. If yes, executes main function. Otherwise exits the program with
    a message saying 'see you next time' by a turtle.

    :param score: score
    :type score: int
    :return: None
    :rtype: NoneType