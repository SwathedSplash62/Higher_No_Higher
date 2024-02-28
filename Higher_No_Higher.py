import math
import random


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


def num_check(question, low=None, exit_code=None, high=None):
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

        if response == exit_code:
            return response

        try:
            response = int(response)

            # if too low
            if low is not None and response < low:
                print(error)

            # is more than low num
            elif high is not None and respose > high:
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

Then play against the computer. YOu can choose between R (rock), P (paper) or S (scissors).

The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper

Type <quit> to end the game at anytime.

💀💀💀Good Luck💀💀💀
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
rounds_tied = 0
rounds_lost = 0

yes_no_list = ['yes', 'no']
game_history = []
# Title
statement_generator("Higher Lower", "👆👇")

# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)
if want_instructions == "yes":
    instructions()
# Guessing Loop

# replace the number b;pw with a random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# set guesses, you'll have zero at the start of each round
guesses_used = 0
already_guessed = []


guess = ""

# Ask user for number of rounds
num_rounds = num_check("How many rounds would you like? Push <enter> for ⌚️infinite mode⌚️: ", low=1, exit_code=" ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

low_num = num_check("Low Number? ")
print(f"You chose a low number of {low_num}")

high_num = num_check("High Number? ", low=1)
print(f"You chose a high number of {high_num}")
guesses_allowed = calc_guesses(low_num, high_num)

# game loops ends here
while rounds_played < num_rounds:

    # rounds based on mode
    if mode == "infinite":
        rounds_heading = f"\n🐂🐂🐂 Round {rounds_played + 1} (Infinite Mode) 🐂🐂🐂"
    else:
        rounds_heading = f"\n🍙🍙🍙 Round {rounds_played + 1} of {num_rounds} 🍙🍙🍙"

    print(rounds_heading)

    comp_choice = random.choice(rps_list[:-1])

    # RPS
    user_choice = string_checker("Choose: ", rps_list)
    print(f"you chose, {user_choice}  ")

    # alf-f4
    if user_choice == "quit":
        break
while guess !=secret and guesses_used < guesses_allowed:

    # ask user to guess
    guess = int(input("Guess: "))

    # check they don't want to quit
    if guess == "quit":
        end_game = "yes"
        break

    # check that the guess is not a dupe
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still used {guesses_used} / {guesses_allowed} guesses")
        continue

    # if guess wasn't a dupe add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    # adds one to the number of guesses used
    guesses_used += 1

    # if have guesses left
    if guess < secret and guesses_used < guesses_allowed:
        feedback = f"Too low, please try a higher number. You've used {guesses_used} / {guesses_allowed} guesses"
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = f"Too high, please try a lower number. You've used {guesses_used} / {guesses_allowed} guesses"

    elif guess == secret:

        if guesses_used == 1:
            feedback = "Damn, first try"
        elif guesses_used == guesses_allowed:
            feedback = f"Good, you finally got it in {guesses_used} guesses"
        else:
            feedback = f"Congrats, you got it in {guesses_used} guesses"

    else:
        feedback = "You have lost, get luckier"

    print(feedback)

    if guesses_used == guesses_allowed -1:
        print("You have one guess left")
# para

print("   Thank you for playing")
statement_generator("Higher Lower", "👆👇")
print()
