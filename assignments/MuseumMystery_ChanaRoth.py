# Chana Roth
# MCON 141 - Mystery Museum Assignment
# Interactive museum themed escape game - players need to solve three puzzles and collect clues to escape/win.


#main function to run the whole game and manage as player plays
def main():

    print()
    print("It is 5:59 PM. The museum doors have locked!")
    print("Solve the curator's three challenges to escape")
    name = input("What is your name, explorer? ")
    #Game information/Data
    energy = 10
    clues = []
    clues_count = 0
    escaped = False

    #Repeat game until gamer escapes/energy = 0
    while energy > 0 and not escaped:

        show_menu(energy, clues_count, name) #menu function and choices

        #ask for choice, validate. Then use if statments for what number the player chose.
        try:
            choice = int(input("\nChoose one of the above options: "))

            if choice < 1 or choice > 6:
                raise ValueError("Choice can only be one of the 6 options above.")


            if choice == 6:
                print("Goodbye, thanks for playing!")
                break
            elif choice == 1:
                print("Entering Gallery 1")
                energy, clues_count, solved = gallery_one(energy, clues_count, clues)

            elif choice == 2:
                print("Entering Gallery 2")
                energy, clues_count, solved = gallery_two(energy, clues_count, clues)

            elif choice == 3:
                print("Entering Gallery 3")
                energy, clues_count, solved = gallery_three(energy, clues_count, clues)

            elif choice == 4:
                show_clues(clues)


            else:#this is choice 5.
                energy, clues_count, escaped = attempt_escape(energy, clues_count, clues, name)

        except ValueError as e:
            print(f"Error: {e}")
            continue
    if energy == 0:
        print("\n========================================================")
        print("--OUT OF ENERGY! The musuem remains locked. Game Over!--")
        print("========================================================")


#Displays the main menu of game with players name, energy, and collected clues.
def show_menu(energy, clues_count,name):


    print()
    print('=================================')
    print('    THE GREAT MUSEUM MYSTERY:')
    print('=================================')

    print(f"Welcome, {name}")
    print(f"Energy: {energy}")
    print(f"Clues Collected: {clues_count} of 3")
    print()
    print("1. Enter Gallery 1")
    print("2. Enter Gallery 2")
    print("3. Enter Gallery 3")
    print("4. View collected clues")
    print("5. Attempt to escape")
    print("6. Quit the museum")

#first game - math puzzle, award clue if correct, subtract 1 energy point if wrong - return to main menu each time.
def gallery_one(energy, clues_count, clues):

#FIRST CHECK if this clue was solved already
    found_clue = "Golden 4"
    if found_clue in clues:
        print("You already solved this room.")
        return energy, clues_count, False
    else:
        print()
        print("ANCIENT NUMBERS ROOM: ")
        print("Figure out the two digit code by solving this problem and receive your first clue:")
        print("When A is subtracted from B, the result is 3. If A = 6, and C is the product of 3 and B, what is the value of C? ")
        try:
            riddle = int(input("Enter your answer here: "))
        except ValueError:
            print("Invalid input, no energy lost.")
            return energy, clues_count, False

        if riddle == 27:
            print("Correct! You received the clue: Golden 4.")#solved correctly
            clues.append(found_clue)
            clues_count += 1
            solved = True

        else:
            print("Incorrect. Lose 1 energy. You may try again!") #not solved
            energy = reduce_energy(energy, 1)
            solved = False
        return energy, clues_count, solved

#second game - similar to gallery 1, different clue given though.
def gallery_two(energy, clues_count, clues):

    #FIRST CHECK if this clue was solved already (if yes, print a message and exit)
    found_clue = "Silver 1"
    if found_clue in clues:
        print("You aready solved this room.")
        return energy, clues_count, False
    else:
        print()
        print("THE CLOCKWORK CODE:")
        print("Fix the clockwork machine and receive a clue by solving this problem.")
        print("How many numbers are divisible by 3 in the range 1 to 10? ")
        try:
            user_num = int(input("Enter your answer here: "))


        except ValueError:
            print(f"Invalid input, no energy lost, please try again.")
            return energy, clues_count, False

        count = 0

        for number in range (1,11):
            if number % 3 == 0:
                count += 1

        if user_num == count:
            print("Correct! you received the clue: Silver 1")#solved
            clues.append(found_clue)
            clues_count += 1
            solved = True

        else:
            print("Incorrect. Lose 1 energy. You may try again!")#not solved
            energy = reduce_energy(energy, 1)
            solved = False
        return energy, clues_count, solved

# game 3 - similar also to gal 1 and 2, different clue.
def gallery_three(energy, clues_count, clues):

    #FIRST CHECK if this clue was solved already (if yes, print a message and exit)
    found_clue = "Crystal 5"
    if found_clue in clues:
        print("You aready solved this room.")
        return energy, clues_count, False
    else:
        print()
        print("THE LOGIC CHAMBER DOOR:")
        print("The chamber door opens when both lamps are on and the key is inserted, or if just the silver latch is up.")
        print("Lamp A = ON: Lamp B = OFF: Key = INSERTED: Silver Latch = UP: Is the chamber open? (Enter 1 for yes and 2 for no)")

        try:
            user_answer = int(input("Enter your answer here: "))
            if user_answer <1 or user_answer > 2:
                raise ValueError("Answer must be 1 or 2.")

        except ValueError as e:
            print(f"Invalid input, no energy lost: {e}.")
            return energy, clues_count, False

        lamp_a = True
        lamp_b = False
        key_inserted = True
        latch_up = True

        chamber_open = (lamp_a and lamp_b and key_inserted) or latch_up

        if (user_answer == 1 and chamber_open) or (user_answer == 2 and not chamber_open):
            print("Correct! You receive the clue Crystal 5.")
            clues.append(found_clue)
            clues_count += 1
            solved = True

        else:
            print("Incorrect. Lose 1 energy. You may try again!")
            energy = reduce_energy(energy, 1)
            solved = False
        return energy, clues_count, solved

#function for hwne energy need to be subtracted for wrong answers.
def reduce_energy(energy, cost):

    energy = energy - cost

    if energy < 0:
        energy = 0

    return energy

#Function for clues - option 4 - helpful message when player has no clues, or display player's current collected clues.
def show_clues(clues):
    print()
    print("========-COLLECTED CLUES-========")

    if clues == []:
        print("\nYou have no clues yet.")


    else:
        print("\nYou have collected the following clues:")

        for clue in clues:
            print(clue)


# Choice 5 - escaping, allow only if have all 3 clues and energy > 1. Players inserts code (from clues), validate. Print congrats escape message. Reduce energy for wrong code.
def attempt_escape(energy, clues_count, clues, name):

    if clues_count == 3 and energy >= 1:
        print("Congrats! You have all 3 clues and now may attempt to escape.")

        try:
            Code = int(input("Enter code to escape - use the numbers from your three clues in order of galleries 1, 2, and 3: "))
        except ValueError:
            print("Invalid input, no lost energy.")
            return energy, clues_count, False

        if Code == 415:
            print()
            print("==========================")
            print("       YOU ESCAPED!     ")
            print("==========================")
            print()
            print(f"Congratulations, {name}!")
            print("\nYou collected all three clues,")
            print("disabled the museum security system,")
            print(f"and escaped with {energy} energy points!")
            print()
            print("The curator would be proud.")
            print("==================================")

            return energy, clues_count, True

        else:
            print("Incorrect code. Lose 1 energy.")
            energy = reduce_energy(energy, 1)
            return energy, clues_count, False

    else:
        print("You do not have enough clues to escape.")

        if clues_count < 3:
            print(f"You only have {clues_count} out of 3 clues.")
        return energy, clues_count, False

#mutation demenstarion.
def mutation_demo(my_list):
    print()
    print("======-Mutation Vs Rebinding-======")

    my_list.append("New Clue")
    print("After append:",my_list)

    my_list = ["Different list"]
    print("After rebinding:", my_list)

main()


demo_list = ['Original Clue']

mutation_demo(demo_list)

print("Original list is outside the function:", demo_list)





# REFLECTION:

# 1. The function most difficult was the mutation_demo just fully figuring that out. And for some reason the show_clues function took me a while to format, I kept getting syntax errors that were hard to figure out. Not really sure why, but otherwise, I found most of the functions pretty similar when constructing.

#2. I used the return value in most of my other functions (such as gallery functions) so it can return to main menu and update clues/energy. The calling code was used to update the results of gamer's actions.

#3. append() changed the original list, so the change was seen outside the function. While, rebinding changed only the local parameter, it didn't replace the original list.

#4. Logic Bug: At first, after player escapes, the game returned to the main menu instead of breaking/ending the program. This one actually took a while but in the end I corrected it by adding a Boolean variable (escaped). So when player escapes it would become true and while loop can end.




















