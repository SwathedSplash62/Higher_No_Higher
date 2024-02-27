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


def num_check(question):
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

# Main routine goes here

# what the game is supposed to be
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

yes_no_list = ['yes', 'no']
rps_list = ['rock', 'paper', 'scissors', 'quit']
game_history = []
# Title
statement_generator("Rock, Paper, Scissors", "🗿🏳️🔪")

# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)

# Ask user for number of rounds
num_rounds = num_check("How many rounds would you like? Push <enter> for 🚂infinite mode🚂: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 20

# game loops ends here
while rounds_played < num_rounds:

    # rounds based on mode
    if mode == "infinite":
        rounds_heading = f"\n👏👏👏 Round {rounds_played + 1} (Infinite Mode) 👏👏👏"
    else:
        rounds_heading = f"\n🐪🐪🐪 Round {rounds_played + 1} of {num_rounds} 🐪🐪🐪"

    print(rounds_heading)

    comp_choice = random.choice(rps_list[:-1])

    # RPS
    user_choice = string_checker("Choose: ", rps_list)
    print(f"you chose, {user_choice}  ")

    # alf-f4
    if user_choice == "quit":
        break


print("   Thank you for playing")
statement_generator("Higher Lower", "⬆️⬇️")
print()