import random

textFile = open('words.txt', 'r')

wordList = []

for line in textFile:
    if "'" not in line or "." not in line:
        wordList.append(line.lower()[:-1])


# Hangman:
# random word picked from the list
# game shows number of letters in the word
# letter is guessed
# if letter is in the word, the position of the letter is shown
# if letter is not in the word, the letter is shown in incorrect letters and a line is drawn


def start():
    print("Let's play Hangman!\n"
          "_____________\n"
          "|		    |\n"
          "|		    |\n"
          "|		  (   )\n"
          "|		    | \n"
          "|		  / | \ \n"
          "|		/   |   \ \n"
          "|		   / \ \n"
          "|		  /   \ \n"
          "|	     /     \ \n"
          "| \ \n"
          "|   \ \n"
          "=================== \n ")
    x = bool(input("Press any key to continue: "))
    if x is True:
        game()


def check_for_dash(x, empty, list_of_word):
    if "-" not in x:
        for i in range(len(list_of_word)):
            list_of_word[i] = "_"
        return empty.join(list_of_word)

    else:
        for i in range(len(list_of_word)):
            if list_of_word[i] != "-":
                list_of_word[i] = "_"
        return empty.join(list_of_word)


def game():
    x = random.choice(wordList)
    empty = ""
    list_of_word = list(x)
    count = 0
    u = True
    guessed = []
    y = check_for_dash(x, empty, list_of_word)
    print("Your word is", y)

    while u is True:
        letter = input("Your guess: ")
        if letter not in guessed:
            y = empty.join(correct_guess(x, y, letter, count))
            print(y)
            if letter not in x and count <= 10:
                count += 1
                guessed.append(letter)
                print("Wrong letters guessed", guessed)
            elif count == 10:
                u = False
            elif "_" not in y:
                print("You Win!")
                u = False
        else:
            print("You've already guessed that!")
            print("Wrong letters guessed", guessed)


def correct_guess(word, empty, letter, count):
    list_of_word = list(word)
    empty_list = list(empty)
    if letter in word:
        for i in range(len(list_of_word)):
            if list_of_word[i] == letter:
                empty_list[i] = letter
    elif count == 0:
        print("Guess again!\n===================")
    elif count == 1:
        print("Guess again!\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n===================")
    elif count == 2:
        print("Guess again!\n_____________\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n===================")
    elif count == 3:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|\n|\n|\n|\n|\n|\n|\n|\n|\n===================")
    elif count == 4:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|		  \n|		    \n|		  \n|		\n|		   \n|		  \n|	     \n| \ \n|   \ \n=================== \n")
    elif count == 5:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|		  (   )\n|		     \n|		   \n|		 \n|		    \n|		   \n|	     \n| \ \n|   \ \n=================== \n ")
    elif count == 6:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|		  (   )\n|		    | \n|		    |   \n|		    |     \n|		       \n|		        \n|	             \n| \ \n|   \ \n=================== \n ")
    elif count == 7:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|		  (   )\n|		    | \n|		  / |   \n|		/   |     \n|		       \n|		        \n|	             \n| \ \n|   \ \n=================== \n ")
    elif count == 8:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|		  (   )\n|		    | \n|		  / | \ \n|		/   |   \ \n|		       \n|		        \n|	             \n| \ \n|   \ \n=================== \n ")
    elif count == 9:
        print("Guess again!\n_____________\n|		    |\n|		    |\n|		  (   )\n|		    | \n|		  / | \ \n|		/   |   \ \n|		   /   \n|		  /     \n|	     /       \n| \ \n|   \ \n=================== \n ")
    elif count == 10:
        print("You Lose!\n_____________\n|		    |\n|		    |\n|		  (   )\n|		    | \n|		  / | \ \n|		/   |   \ \n|		   / \ \n|		  /   \ \n|	     /     \ \n| \ \n|   \ \n=================== \n ")
        print("The answer was", word)
    return empty_list


start()
