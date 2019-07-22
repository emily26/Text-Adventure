
# Update this text to match your story.
start = '''
You wake up with no memory of how you got there. You turn to leave but are faced with a door with 3 locks, what will you do?
There is a hallway to your right and left, and a stairwell in front of you.
'''
user_input = input()
srKey = False
stKey = False
fdKeys = 0

gameFinished = False
location = "entry"
print(start)
if gameFinished == False:
    while location == "entry":
        user_input = input("You find yourself in the main hallway, there is a staircase in front of you, a large metal door behind you, and two doors on each side, what do you do? (type left, right, back or up)")
        if user_input == "left":
            print("You enter the library,")
            location = "library"
        if user_input == "right":
            print("you enter the dinning room")
            location = "dr"
        if  user_input == "up":
            print("You climb the stairs and enter the upper hall")
            location = "upperhall"
        if user_input == "back" and (fdKeys == 1 or fdKeys == 2):
            print("you place the keys into the holes, but they won't turn until all the keys are in place")
            location = "entry"
        if user_input == "back" and fdKeys == 0:
            print("The door will not open until you find all three keys")
            location = "entry"
        if user_input == "back" and fdKeys == 3:
            print("all three keys slide into place and begin to turn on thier own, the metal door swings open revealing the gardens out front")
            gameFinished = True

    while location == "upperhall":
        user_input = input("You find yourself in a smaller hallway with doors on all three sides, what do you do? (type back, left, right, or straight)")
        if user_input == "back":
            print("you descend down the stairs, returning to the entryway")
            location = "entry"
        if user_input == "left":
            print("you enter the master bedroom")
            location = "masterbr"
        if user_input == "right":
            print("you enter the nursery")
            location = "nursery"
        if user_input == "straight" and srKey == False:
            print("Locked! maybe the key is in another room!")
            location = "upperhall"
        if user_input == "straight" and srKey == True:
            print("you put the key into the lock and open the door into the sitting room")
            location = "sr"

    while location == "library":
        user_input = input("You are in the library, there is a door across from the big desk. Do you continue, look around or turn back? (type continue, look around or back)")
        if user_input == "look around":
            print("You find a key to the study on an endtable")
            stKey = True
            location = "library"
        if user_input == "back":
            print("You return to the main entryway")
            location = "entry"
        if user_input == "continue" and stKey == False:
            print("Locked, maybe the key is somewhere else")
            location = "library"
        if user_input == "continue" and stKey == True:
            user_input = input("You enter the study. Do you look around or go back? (type look around or back)")
            if user_input == "look around":
                print("While snooping through the drawers, you find a key labeled front door, you get scared by a bat and run out of the study")
                fdKeys += 1
                print("you have", 3 - fdKeys, "left to find")
                location = "entry"
            if user_input == "back":
                print("You do a u-turn back into the library")
                location = "library"

    while location == "dr":
        user_input = input("You are in the dining hall, choose to go into the kitchen or turn back (type kitchen or back)")
        if user_input == "kitchen":
            print("You find a key in the fridge labeled front door, scared by a sudden clang you run back into the entryway")
            location = "entry"
            fdKeys += 1
            print("you have", 3 - fdKeys, "left to find")
        if user_input == "back":
            print("You are back at the entry way")
            location = "entry"

    while location == "sr":
        user_input = input("you find yourself in a grand sitting room, what do you do? (look around or go back?)")
        if user_input == "look around":
            print("you find a key labeled front door in the fireplace, confused about how or why you got there, you wander back into the entryway")
            location = "entry"
            fdKeys += 1
            print("you have", 3 - fdKeys, "left to find")
        if user_input == "go back":
            print("you return to the upper hallway")
            location = "upperhallway"

    while location == "nursery":
        user_input = input("you are in the nursery, what do you do? (look around or go back)")
        if user_input == "look around":
            print("you see a spider and run away screaming into the hallway")
            location = "upperhallway"
        if user_input == "go back":
            print("you are back in the upper hall")
            location = "upperhallway"
    while location == "masterbr":
        user_input = input("you find yout slefin the master bedroom, what do you do? (look around or go back)")
        if user_input == "look around":
            print("you find yourslef going through the large wardrobe and decide to try on a coat, reaching into it's pocket you find a key labeled 'sitting room' feeling bad about snooping, you leave")
            location = "upperhallway"
            srKey = True
        if user_input == "go back":
            print("you return to the upper hallway")
            location = "upperhallway"
