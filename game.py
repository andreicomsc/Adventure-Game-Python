from map import rooms
from player import *
from gameparser import *
import os, sys, time
import Cutscene

def list_of_items(items):

    itemslst = []
    if len(items) == "0":
        return ""
    else:
        for i in items:
            itemslst.append(i["name"])
        return ", ".join(itemslst)


def print_room_items(room):

    if len(room["items"]) > 0:
        print(f"There is a {list_of_items(room['items'])} here.\n")


def print_inventory_items(items):

    if len(items) > 0:
        print(f"You have {list_of_items(items)}.\n")

    else: print("You have no items.\n")

    print("USE (ITEM) to use an item.")
    print("TAKE (ITEM) to pickup an item.")
    print("DROP (ITEM) to drop an item.")
    print("INSPECT (ITEM) to study an item.")


def print_room(room):


    print(f"{room['name'].upper()}")

    # Chooses between the Morgue descriptions
    global morgue_entry
    if room == f3room_morgue:
        if morgue_entry == 1:
            print(f"{room['description1']}")
            morgue_entry += 1
        elif not item_file in inventory:
            print(f"{room['description2']}")
        else:
            print(f"{room['description']}")
    else:
        if room["cleared"] == False:
            print(f"{room['description']}")
        else: print(f"{room['description_cleared']}")

    print_room_items(room)


def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):

    floor2 = ["Large Tree Clearing", "Wooden Shack", "Middle of the Woods", "Rock Circle Clearing", "Altar"]

    if current_room["name"] in floor2 and not floor2End and rooms[leads_to]["visible"]:
        if not floor2End:
            print("GO " + direction.upper() + " to ?????")
        else:
            print("GO " + direction.upper() + " to " + leads_to + ".")
    else:
        if rooms[leads_to]["visible"]:
            print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):

    print("You can:")

    if current_room["name"] in floor2:
        print("Their is too much fog, you  appear lost.")

    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    #print("You can TAKE (ITEM), DROP (ITEM), USE (ITEM) or INSPECT (ITEM)")

    #for item in room_items:
    #    if item["Carriable"]:
    #        print(f"TAKE {item['id'].upper()} to take {item['name']}.")
    #    else:
    #        print(f"INSPECT {item['id'].upper()} to take {item['name']}.")

    #for item in inv_items:
    #    print(f"DROP {item['id'].upper()} to drop {item['name']}.")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    if chosen_exit in exits:
        if rooms[exits[chosen_exit]]["visible"] == True:
            return True
        else:
           return False
    else:
       return False


def execute_go(direction):
    global reAsk

    global current_room

    if is_valid_exit(current_room["exits"], direction) == True:
        reAsk = False
        current_room = rooms[current_room["exits"][direction]]
    else:
        printslow("You cannot go there.")


# calculates if an item can be picked up or if it is too heavy
def carry_mass(inventory, newItemMass):
    inventmass = 0
    for item in inventory:
        inventmass += item["mass"]
    if inventmass + newItemMass > carryMass:
        return False
    else:
        return True


def execute_take(item_id):
    global reAsk
    noitem = True
    for item in current_room["items"]:
        if item["id"] == item_id:
            noitem = False
            reAsk = False
            if item["Carriable"] == True:
                if carry_mass(inventory, item["mass"]) == True:
                    inventory.append(item)
                    current_room["items"].remove(item)
                    print("You pick up the item.")
                else:
                    print("This item will bring you over your carry limit.")
            else:
                print("This item cannot be picked up.")
    if noitem == True:
        print("You cannot find this item.")


def useportal():
    print("GO RECEPTION to go to the Reception.")
    print("GO WOODS to go to the Woods entrance.")
    print("GO MORGUE to go to the Morgue.")
    print("GO MINE to go to the Mine entrance.")
    print("Press Enter to return")

    command = input()
    if command == "":
        return

    command = normalise_input(command)[1]
    global current_room
    if command == "reception":
        current_room = rooms["Reception"]
    elif command == "woods":
        current_room = rooms["Large Tree Clearing"]
    elif command == "morgue":
        current_room = rooms["Morgue"]
    elif command == "mine":
        current_room = rooms["Mine Entrance"]
    else:
        print("Where do you want to teleport? \n")
        useportal()


# Anagram puzzle used on floor 2 - can be adapted for future floors with different anagrams
# Pass the anagram and soltuion to the anagraam to the anagram_puzzle function.
def anagram_puzzle(anagram, solution):
    global floor2End
    solved = False
    anagram, solution = anagram, solution
    print("Your puzzle is to solve this anagram: {}".format(anagram))

    while not solved:
        puzzle_guess = input(">>> ")
        if puzzle_guess.lower() == solution.lower():
            solved = True
        else: print("That is incorrect. Try again.")

    print("Congratulations. You have solved the anagram - {}".format(solution))
    time.sleep(1)
    floor2End = True
    f2room_altar["description"] = """The candles around the altar continue to glow soft orange light.
The fog has started to disperse."""


# Floor 2 specific. Allows the player to use lighter to light candles around the altar
def use_lighter():
    global current_room
    # If the candles are not already lit, the player lits candles and is then 
    # presented with an anagram puzzle needed to complete the floor.
    if current_room == rooms["Altar"] and not rooms["Altar"]["candles_lit"]:
        desc = """You have successfully lit the candles around the altar!
The skulls' eyes in the centre of the altar begin to glow red.
You are now presented with an anagram puzzle."""
        printslow(desc)
        rooms["Altar"]["candles_lit"] = True
        anagram_puzzle("lil rik", "Kirill")
        current_room = rooms["Morgue"]
    else: print("You cannot do that.")


def use_dynamite():
    if current_room == rooms["Mineshaft Tunnel"]:
        printslow("A path has been cleared.")
        rooms["Mineshaft Gate"]["visible"] = True
        rooms["Mineshaft Tunnel"]["cleared"] = True
        inventory.remove(item_dynamite)
    else: print("I cant use that here.")


def use_goldkey():
     if current_room == rooms["Mineshaft Gate"]:
        printslow("The gate has opened.")
        rooms["Haunted Mineshaft"]["visible"] = True
        rooms["Mineshaft Gate"]["cleared"] = True
        inventory.remove(item_mineKey)
     else: print("I cant use that here.")


def use_toy():
     if current_room == rooms["Haunted Mineshaft"]:
        printslow("The Ghost seems content.")
        rooms["Iron Door"]["visible"] = True
        rooms["Haunted Mineshaft"]["cleared"] = True
        inventory.remove(item_toy)
     else: print("I cant use that here.")

def use_old_book():
    if current_room == rooms["Your Tutors Office"]:
        printslow("Placing the book in the bookcase")
        printslow("...")
        printslow("The bookcase slides to the side and the portal room is unlocked")
        rooms["Your Tutors Office"]["exits"]["east"] = "Abacws Portal Room"
        inventory.remove(item_Old_Book)
    else:
        print("This cant be used in this room")

def use_laptop():
    passkey = "kill-stud3ntS"
    data = input("Please enter the password: ")
    if data == passkey:
        rooms["Abacws Portal Room"]["exits"]["through"] = "Large Tree Clearing"
        printslow("Portal.exe ran succefully")
        printslow("....")
        printslow("Portal active")
    else:
        print("That is the wrong password")


def execute_use(item_id):
    global reAsk
    noitem = True
    for item in inventory:
        if item["id"] == item_id:
            noitem = False
            reAsk = False
            if item_id == "portalgun":
                useportal()
            elif item_id == "lighter":
                use_lighter()
            elif item_id == "dynamite":
                use_dynamite()
            elif item_id == "goldkey":
                use_goldkey()
            elif item_id == "toy":
                use_toy()
            elif item_id == "oldbook":
                use_old_book()
            else:
                printslow("You cannot use that.")
    if noitem == True:
        printslow("You dont have that item.")


def execute_drop(item_id):
    global reAsk
    noitem = True
    for item in inventory:
        if item["id"] == item_id:
            noitem = False
            reAsk = False
            current_room["items"].append(item)
            inventory.remove(item)
    if noitem == True:
        printslow("You cannot drop that.")

def use_keypad():
    if input("Passkey: ") == "3239":
        Cutscene.start()
    else:
        print("Wrong passkey.")
    time.sleep(2)
    os.system("cls")

def execute_inspect(item_id):
    global reAsk
    noitem = True
    for item in inventory:
        if item["id"] == item_id:
            noitem = False
            reAsk = False
            printslow(item["description"])

    for item in current_room["items"]:
        if item["id"] == item_id:
            noitem = False
            reAsk = False
            printslow(item["description"])

            if item_id == "window":
                rooms["Garden"]["visible"] = True
            if item_id == "laptop":
                use_laptop()
            if item_id == "keypad":
                use_keypad()
    if noitem == True:
        print("You cannot inspect that.")


def execute_command():

    global current_room
    global morgue_entry
    global inventory
    global reAsk
    reAsk = True
    while reAsk == True:
        command = menu(current_room["exits"], current_room["items"], inventory)
        if 0 == len(command):
            print("This makes no sense.")
        elif command[0] == "go":
            if len(command) > 1:
                # Checks if the transfer is possible
                if current_room == rooms["Morgue"] and command[1] == 'north' and morgue_entry > 1 and item_file in inventory:
                    os.system("cls")
                    print()
                    printslow('''As you walk into the surgery, you notice a husk of a person hovering infront of you.              
He notices you have the file. They are filled with rage and glide straight into the floor.
As you glance down, woundering where he went, the floor shatters beneath you. You plumet down.''')
                    current_room = rooms["Mine Entrance"]
                    reAsk = False
                    input("Press enter to continue")
                else:
                    execute_go(command[1])
            
            else:
                print("Go where?")

        elif command[0] == "take":
            if len(command) > 1:
                execute_take(command[1])
                input("Press enter to continue")
            else:
                printslow("Take what?")

        elif command[0] == "drop":
            if len(command) > 1:
                execute_drop(command[1])
            else:
                printslow("Drop what?")

        elif command[0] == "use":
            if len(command) > 1:
                execute_use(command[1])
                input("Press enter to continue")
            else:
                printslow("Use what?")

        elif command[0] == "inspect":
            if len(command) > 1:
                execute_inspect(command[1])
                input("Press enter to continue")
            else:
                printslow("inspect what?")

        else:
            printslow("This makes no sense.")

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    if user_input == "exit":
        os.system("cls")
        exit()

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):

    # Next room to go to
    return rooms[exits[direction]]
    

# This is the entry point of our program
def main():
    os.system("cls")
    print("Welcome to Freaky Deaky Tower")
    input("Press enter to continue")
    global current_room
    global morgue_entry
    global reAsk
    # Morgue entries counter
    morgue_entry = 1
    
    os.system("cls")

    # Main game loop
    while True:
        global floor2End

        # Display game status (room description, inventory etc.)

        print("=" * 120)
        print_room(current_room)

        print("=" * 120)

        print_inventory_items(inventory)
        print("=" * 120)

        # Show the menu with possible actions and ask the player


        # Clears the command prompt
        
        # Execute the player's command
        execute_command()
        os.system("cls")
        


if __name__ == "__main__":
    main()

