import math
import random


def round_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        if to_check == "":
            return ""

        try:

            # ask user to enter a number
            response = int(to_check)

            # checks number is more than one
            if response < 1:
                print(error)
            # Outputs error if input is invalid
            else:
                return response

        except ValueError:
            print(error)


def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        # print error when error
        print(error)
        print()


def int_check(question, low=None, exit_code=None, high=None):


    # if any integer is allowed. . .

    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = f"Please enter an integer that is more than / equal to {low}"

    # if the number needs to between low & high
    else:
        error = f"Please enter an integer that is between {low} and {high} inclusive"

    while True:
        response = input(question).lower()

        try:

            if response == exit_code:
                return response

            response = int(response)

            # if too low
            if low is not None and response < low:
                print(error)

            # is more than low num
            elif high is not None and response > high:
                print(error)

            # if valid then return
            else:
                return response

        except ValueError:
            print(error)


def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 2

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions/information", "-")
    print('''
To begin, choose the number of rounds (or press <enter> for infinite mode).

You will then chose a lower and higher number (inclusive) that will contain your secret number 

You will then try to guess the number while the computer will give you hints for each guess

You will receive statistics on your guesses used and will be able to see your game history at the end of the game 

Type <quit> to end the game at anytime.

🎂🎂🎂Good Luck🎂🎂🎂
''')
    print()
    return ""


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main routine goes here

# what the game is supposed to be
mode = "regular"
rounds_played = 0
feedback = ""
end_game = "no"
guess = 0
yes_no_list = ['yes', 'no']
game_history = []
all_scores = []
# Title
statement_generator("Higher Lower", "👆👇")

# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds
num_rounds = round_check("How many rounds would you like? Push <enter> for ⌚️infinite mode⌚️: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to change the default game number range '
default_params = ("Do you want to use the default game parameters? ", yes_no_list)
if default_params == "yes":
    low_num = 0
    high_num = 10
    guess = 0
# allow user to choose the high/low num
else:
    low_num = int_check("Low Number? ",exit_code="quit")
    print(f"You chose a low number of {low_num}")
    high_num = int_check("High Number? ",exit_code="quit", low=low_num+1)
    print(f"You chose a high number of {high_num} ")

guesses_allowed = calc_guesses(low_num, high_num)
# game loops ends here
while rounds_played < num_rounds:

    if mode == "infinite":
        num_rounds += 1

    if guess == "quit":
        end_game = "yes"
        break

    # rounds based on mode
    if mode == "infinite":
        rounds_heading = f"\n🐂🐂🐂 Round {rounds_played + 1} (Infinite Mode) 🐂🐂🐂"
    else:
        rounds_heading = f"\n🍙🍙🍙 Round {rounds_played + 1} of {num_rounds} 🍙🍙🍙"

    print(rounds_heading)

    # round starts here
    # set stuff to zero at the start of round
    guesses_used = 0
    already_guessed = []

    # Choose the right number between the high and low num
    secret = random.randint(low_num, high_num)

    guess = ""

    while guess != secret and guesses_used < guesses_allowed:

        # ask user to guess
        guess = int_check("Guess: ", low=low_num, high=high_num, exit_code="quit")

        # check they don't want to quit
        if guess == "quit":
            end_game = "yes"
            break

        # check that the guess is not a dupe
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used {guesses_used} / {guesses_allowed} guesses")
            continue

        # if guess wasn't a dupe add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # adds one to the number of guesses used
        guesses_used += 1

        # if you have guesses left
        if guess < secret and guesses_used < guesses_allowed:
            feedback = f"Too low, please try a higher number. You've used {guesses_used} / {guesses_allowed} guesses"
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = f"Too high, please try a lower number. You've used {guesses_used} / {guesses_allowed} guesses"
            if guesses_used == guesses_allowed - 1:
                print("You have one guess left")

        elif guess == secret:

            if guesses_used == 1:
                feedback = "Damn, first try"
                rounds_played += 1
                all_scores.append(guesses_used)
                game_history.append(feedback)
            elif guesses_used == guesses_allowed:
                feedback = f"Good, you finally got it in {guesses_used} guesses"
                rounds_played += 1
                all_scores.append(guesses_used)
                game_history.append(feedback)
            else:
                feedback = f"Congrats, you got it in {guesses_used} guesses"
                rounds_played += 1
                all_scores.append(guesses_used)
                game_history.append(feedback)

        else:
            feedback = "You have lost, get luckier"
            rounds_played += 1
            game_history.append(feedback)

        print(feedback)

if rounds_played > 0:

    # Behold, stats
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output stats
    print("📈📈📈 Game Statistics 📈📈📈")
    print(
        f"Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f}")
    print()

    see_history = string_checker("Do you want to see your game history? ", yes_no_list)
    if see_history == "yes":
        for item in game_history:
            print(item)

else:
    "..."

# para

print("   Thank you for playing")
statement_generator("Higher Lower", "👆👇")
print()
