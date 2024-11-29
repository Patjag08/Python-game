#create a map
import random
import os as o
import time as t

office_conc = {
    "Bottom": "" 
}
living_room_conc = {
    "Left": "",
    "Right": "",
    "Up": "",
    "Down": ""
}
dining_room_conc = {
    "Left": "",
    "Right": "",
    "Up": "",
    "Down": ""
}
kitchen_conc = {
    "Left": "",
    "Right": "",
    "Up": "",
    "Down": ""
}
entrace_hall_conc = {
    "Left" : "",
    "Right" : "",
}


current_room = ""
    
spawnedrooms = {
    "Living room": False,
    "Kitchen": False,
    "Dining room": False,
    "Office": False,
    "Entrance hall":False
}
has_treasure = {
    "Living room": False,
    "Kitchen": False,
    "Dining room": False,
    "Office": False,
    "Entrance hall":False
}
roomdescriptions = {
    "Living room": "main room of the building (Spawn)",
    "Kitchen": "medium sized room full of cookware",
    "Dining room": "large room consisting of a table and chairs",
    "Office": "Small room with a desk and only one entrance",
    "Entrance hall":"Long corridor with rooms on both sides"
}
def generate_map():
    #Hall connections
    spawnedrooms["Entrance hall"] = True
    if random.randint(1,2) == 1:
        entrace_hall_conc["Left"] = "Living room"
        entrace_hall_conc["Right"] = "Kitchen"
        living_room_conc["Right"] = "Entrance hall"
        kitchen_conc["Left"] = "Entrance hall"
        spawnedrooms["Living room"] = True
        spawnedrooms["Kitchen"] = True
    else:
        entrace_hall_conc["Right"] = "Living room"
        entrace_hall_conc["Left"] = "Kitchen"
        living_room_conc["Left"] = "Entrance hall"
        kitchen_conc["Right"] = "Entrance hall"
        spawnedrooms["Living room"] = True
        spawnedrooms["Kitchen"] = True
    #Living room connections
    random_living = random.randint(1,3)
    if random_living == 1 and living_room_conc["Left"] == "Entrance hall" and spawnedrooms["Office"] == False:
        if random.randint(1,2) == 1:
            living_room_conc["Up"] = "Office"
            office_conc["Bottom"] = "Living room"
            spawnedrooms["Office"] = True
        else:
            living_room_conc["Up"] = "Wall"
    elif random_living == 2 and living_room_conc["Left"] == "Entrance hall" and spawnedrooms["Dining room"] == False:
        living_room_conc["Right"] = "Dining room"
        dining_room_conc["Left"] = "Living room"
        spawnedrooms["Dining room"] = True
    elif random_living == 3 and living_room_conc["Left"] == "Entrance hall" and spawnedrooms["Dining room"] == False:
        living_room_conc["Down"] = "Dining room"
        dining_room_conc["Up"] = "Living room"
        spawnedrooms["Dining room"] = True
    elif random_living == 1 and living_room_conc["Right"] == "Entrance hall" and spawnedrooms["Office"] == False:
        if random.randint(1,2) == 1:
            living_room_conc["Up"] = "Office"
            office_conc["Bottom"] = "Living room"
            spawnedrooms["Office"] = True
        else:
            living_room_conc["Up"] = "Wall"
    elif random_living == 2 and living_room_conc["Right"] == "Entrance hall" and spawnedrooms["Dining room"] == False:
        living_room_conc["Left"] = "Dining room"
        dining_room_conc["Right"] = "Living room"
        spawnedrooms["Dining room"] = True
    elif random_living == 3 and living_room_conc["Right"] == "Entrance hall" and spawnedrooms["Dining room"] == False:
        living_room_conc["Down"] = "Dining room"
        dining_room_conc["Up"] = "Living room"
        spawnedrooms["Dining room"] = True
    
    for i in range(3):
        if i == 0:
            if living_room_conc["Down"] == "":
                living_room_conc["Down"] = "Wall"
            if living_room_conc["Up"] == "":
                living_room_conc["Up"] = "Wall"
            if living_room_conc["Left"] == "":
                living_room_conc["Left"] = "Wall"
            if living_room_conc["Right"] == "":
                living_room_conc["Right"] = "Wall"
        if i == 1:
            if dining_room_conc["Down"] == "":
                dining_room_conc["Down"] = "Wall"
            if dining_room_conc["Up"] == "":
                dining_room_conc["Up"] = "Wall"
            if dining_room_conc["Left"] == "":
                dining_room_conc["Left"] = "Wall"
            if dining_room_conc["Right"] == "":
                dining_room_conc["Right"] = "Wall"
        if i == 2:
            if kitchen_conc["Down"] == "":
                kitchen_conc["Down"] = "Wall"
            if kitchen_conc["Up"] == "":
                kitchen_conc["Up"] = "Wall"
            if kitchen_conc["Left"] == "":
                kitchen_conc["Left"] = "Wall"
            if kitchen_conc["Right"] == "":
                kitchen_conc["Right"] = "Wall"
    # "Living room": False,
    # "Kitchen": False,
    # "Dining room": False,
    # "Office": False,
    # "Entrance hall":False
    chance_treasure = random.randint(1,4)
    if chance_treasure == 1:
        has_treasure["Living room"] = True
    elif chance_treasure == 2:
        has_treasure["Kitchen"] = True
    elif chance_treasure == 3:
        has_treasure["Dining room"] = True
    elif chance_treasure == 4:
        has_treasure["Office"] = True

def menu():
    print("""
          |-------------------------------------------------------------------|
          |                                                                   |
          |                      Welcome to the game                          |
          |                     Press enter to proceed                        |
          |                                                                   |
          |-------------------------------------------------------------------|
          """)
    input()
    o.system("cls")
    print("""
          |-------------------------------------------------------------------|
          |                       Bad adventure game:                         |
          |                     1) Play                                       |
          |                     2) Settings                                   |
          |                     3) Something                                  |
          |-------------------------------------------------------------------|
          """)
    choice = input("")
    if choice == "1":
        o.system("cls")
        generate_map()
        #print(kitchen_conc)
        #print(spawnedrooms)
        play()
    else:
        print("Nerd")
def play():
    current_room = "Entrance hall"
    played = True
    moved = False
    plays = 5
    while played == True:
        moved = False
        if plays <= 0:
            print("End of the road hear, (Your flashlight slowly dies leaving you in the dark)")
            t.sleep(1)
            print(".")
            t.sleep(0.5)
            print("..")
            t.sleep(0.5)
            print("...")
            t.sleep(2)
            o.system("cls")
            played = False
        else:
            print(f"You are in {current_room}, a {roomdescriptions[current_room].lower()}")
            if current_room == "Entrance hall" and has_treasure[current_room] == False:
                while moved == False:
                    print(f"""Your choices are:
                        L : {entrace_hall_conc['Left']}
                        R : {entrace_hall_conc["Right"]}""")
                    next_choice = input("Which direction do you want to go? (U,D,L,R)")
                    if next_choice == "L" and entrace_hall_conc["Left"] != "Wall":
                        current_room = entrace_hall_conc["Left"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "L" and entrace_hall_conc["Left"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "R" and entrace_hall_conc["Right"] != "Wall":
                        current_room = entrace_hall_conc["Right"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "R" and entrace_hall_conc["Right"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    else:
                        print("Invalid selection")
                        t.sleep(2)
                        moved = False
                        o.system("cls")
                        print(f"You are in {current_room}, a {roomdescriptions[current_room].lower()}")
                        # "Living room": False,
                        # "Kitchen": False,
                        # "Dining room": False,
                        # "Office": False,
                        # "Entrance hall":False
            elif current_room == "Living room" and has_treasure[current_room] == False:
                while moved == False:
                    print(f"""Your choices are:
                    U : {living_room_conc['Up']}
                    D : {living_room_conc['Down']}
                    L : {living_room_conc['Left']}
                    R : {living_room_conc["Right"]}""")
                    next_choice = input("Which direction do you want to go? (U,D,L,R)")
                    if next_choice == "L" and living_room_conc["Left"] != "Wall":
                        current_room = living_room_conc["Left"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "L" and living_room_conc["Left"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "R" and living_room_conc["Right"] != "Wall":
                        current_room = living_room_conc["Right"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "R" and living_room_conc["Right"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "U" and living_room_conc["Up"] != "Wall":
                        current_room = living_room_conc["Up"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "U" and living_room_conc["Up"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "D" and living_room_conc["Down"] != "Wall":
                        current_room = living_room_conc["Down"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "D" and living_room_conc["Down"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    else:
                        print("Invalid selection")
                        t.sleep(2)
                        moved = False
                        o.system("cls")
                        print(f"You are in {current_room}, a {roomdescriptions[current_room].lower()}")
            elif current_room == "Kitchen" and has_treasure[current_room] == False:
                while moved == False:
                    print(f"""Your choices are:
                    U : {kitchen_conc['Up']}
                    D : {kitchen_conc['Down']}
                    L : {kitchen_conc['Left']}
                    R : {kitchen_conc["Right"]}""")
                    next_choice = input("Which direction do you want to go? (U,D,L,R)")
                    if next_choice == "L" and kitchen_conc["Left"] != "Wall":
                        current_room = kitchen_conc["Left"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "L" and kitchen_conc["Left"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "R" and kitchen_conc["Right"] != "Wall":
                        current_room = kitchen_conc["Right"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "R" and kitchen_conc["Right"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "U" and kitchen_conc["Up"] != "Wall":
                        current_room = kitchen_conc["Up"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "U" and kitchen_conc["Up"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "D" and kitchen_conc["Down"] != "Wall":
                        current_room = kitchen_conc["Down"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "D" and kitchen_conc["Down"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    else:
                        print("Invalid selection")
                        t.sleep(2)
                        moved = False
                        o.system("cls")
                        print(f"You are in {current_room}, a {roomdescriptions[current_room].lower()}")
            elif current_room == "Dining room" and has_treasure[current_room] == False:
                while moved == False:
                    print(f"""Your choices are:
                    U : {dining_room_conc['Up']}
                    D : {dining_room_conc['Down']}
                    L : {dining_room_conc['Left']}
                    R : {dining_room_conc["Right"]}""")
                    next_choice = input("Which direction do you want to go? (U,D,L,R)")
                    if next_choice == "L" and dining_room_conc["Left"] != "Wall":
                        current_room = dining_room_conc["Left"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "L" and dining_room_conc["Left"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "R" and dining_room_conc["Right"] != "Wall":
                        current_room = dining_room_conc["Right"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "R" and dining_room_conc["Right"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "U" and dining_room_conc["Up"] != "Wall":
                        current_room = dining_room_conc["Up"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "U" and dining_room_conc["Up"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    elif next_choice == "D" and dining_room_conc["Down"] != "Wall":
                        current_room = dining_room_conc["Down"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "D" and dining_room_conc["Down"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    else:
                        print("Invalid selection")
                        t.sleep(2)
                        moved = False
                        o.system("cls")
                        print(f"You are in {current_room}, a {roomdescriptions[current_room].lower()}")
            elif current_room == "Office" and has_treasure[current_room] == False:
                while moved == False:
                    print(f"""Your choices are:
                    D : {office_conc['Down']}""")
                    next_choice = input("You can only go down (D) Please enter the key to go down")
                    if next_choice == "D" and office_conc["Down"] != "Wall":
                        current_room = office_conc["Left"]
                        plays -= 1
                        moved = True
                        o.system("cls")
                    elif next_choice == "D" and office_conc["Down"] == "Wall":
                        print("You bumped your head on the wall and wasted a go.")
                        t.sleep(2)
                        plays -= 1
                        moved = False
                        o.system("cls")
                    else:
                        print("Invalid selection")
                        t.sleep(2)
                        moved = False
                        o.system("cls")
                        print(f"You are in {current_room}, a {roomdescriptions[current_room].lower()}")
            elif current_room == "Living room" and has_treasure[current_room] == True:
                print(f"You enter the {current_room.lower()} and shine your flashlight into the room.")
                print("In front of you a large slightly open chest, you found it.")
                print("You found the rumoured tresure.")
                print("")
                print(f"""Final stats:
                      Moves left: {plays}
                      Treasure room: {current_room.lower()}
                      Moves used: {5 - plays}""")
                played = False
                break
            elif current_room == "Kitchen" and has_treasure[current_room] == True:
                print(f"You enter the {current_room.lower()} and shine your flashlight into the room.")
                print("In front of you a large slightly open chest, you found it.")
                print("You found the rumoured tresure.")
                print("")
                print(f"""Final stats:
                      Moves left: {plays}
                      Treasure room: {current_room.lower()}
                      Moves used: {5 - plays}""")
                played = False
                break
            elif current_room == "Dining room" and has_treasure[current_room] == True:
                print(f"You enter the {current_room.lower()} and shine your flashlight into the room.")
                print("In front of you a large slightly open chest, you found it.")
                print("You found the rumoured tresure.")
                print("")
                print(f"""Final stats:
                      Moves left: {plays}
                      Treasure room: {current_room.lower()}
                      Moves used: {5 - plays}""")
                played = False
                break
            elif current_room == "Office" and has_treasure[current_room] == True:
                print(f"You enter the {current_room.lower()} and shine your flashlight into the room.")
                print("In front of you a large slightly open chest, you found it.")
                print("You found the rumoured tresure.")
                print("")
                print(f"""Final stats:
                      Moves left: {plays}
                      Treasure room: {current_room.lower()}
                      Moves used: {5 - plays}""")
                played = False
                break
        

while True:
    o.system("cls")
    menu()
#print(spawnedrooms)