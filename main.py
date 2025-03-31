import text_styles as ts
import random

# global variables
map: dict[str, str] = {"A":"A", "B":"B", "C":"C"}
doors = ['A', 'B', 'C']
prize_door: str = ""
car: str = ts.bold + ts.purple + "CAR" + ts.reset
goat: str = ts.bold + "GOAT" + ts.reset

def random_door() -> str:
    global doors
    rand: str = random.choice(doors)
    return rand

def print_map() -> None:
    global map
    print(f"| {map["A"]} | {map["B"]} | {map["C"]} |\n")

def player_choices(opened_door: str, stage: int) -> str:
    player_input: str = ""
    if stage == 0:
        player_input = input("Choose a door (A, B, C): ").upper()
        return player_input
    else:
        # Prevent the player from choosing the opened door
        match opened_door:
            case 'A':
                player_input = input("Choose a door (B or C): ").upper()
                while player_input == opened_door:
                    print(ts.red + "You cannot choose the opened door.", ts.reset)
                    player_input = input("Choose a door (B or C): ").upper()
                return player_input
            
            case 'B':
                player_input = input("Choose a door (A or C): ").upper()
                while player_input == opened_door:
                    print(ts.red + "You cannot choose the opened door.", ts.reset)
                    player_input = input("Choose a door (A or C): ").upper()
                return player_input
            
            case 'C':
                player_input = input("Choose a door (A or B): ").upper()
                while player_input == opened_door:

                    print(ts.red + "You cannot choose the opened door.", ts.reset)
                    player_input = input("Choose a door (A or B): ").upper()
                return player_input
            
def handle_input(player_input: str) -> int:
    match player_input:
        case 'A' | 'B' | 'C':
            print(ts.cyan + "You choose the door {}!".format(player_input), ts.reset)
            return 1
        case 'Q':
            print(ts.bold + ts.green + "=== Quit the game ===", ts.reset  + '\n')
            return -1
        case _:
            print(ts.red + "Invalid choice. Please choose A, B, or C", ts.reset + '\n')
            return 0
            
def door_open(player_input: str, stage: int) -> int:
    global map, prize_door, doors
    opened_door: str = ""
    if stage == 0:
        for door in doors:
            if (door != player_input) and (door != prize_door):
                map[door] = goat
                opened_door = door
                break   
    else:
        map[prize_door] = car
        opened_door = prize_door

    print_map()
    return opened_door
        
def reset_global() -> None:
    global map, prize_door
    map["A"] = "A"
    map["B"] = "B"
    map["C"] = "C"
    prize_door = ""
    prize_door = random_door()

def gameloop() -> None:
    opened_door: str = ""
    stage: int = 0

    print(ts.bold, ts.green + "=== Welcome to the Monty hall game! ===", ts.reset)
    print("You have three doors to choose from: A, B, and C")
    print_map()
    reset_global()

    while True:
        print(ts.bold + "-- Round {} --".format(stage+1) + ts.reset)
        print("type", ts.bold + ts.orange + "Q" + ts.reset, "to quit the game")
        player_input: str = player_choices(opened_door, stage)
        status: int = handle_input(player_input)
        if status == -1:
            break
        elif status == 0:
            continue

        opened_door = door_open(player_input, stage) 

        if stage == 1:
            if (player_input == prize_door):
                print(ts.yellow + "You won!", ts.reset)
                print(ts.bold + ts.green + "=== Congratulations! ===", ts.reset + '\n')
            else:
                print(ts.red + "You lost!", ts.reset)
                print(ts.bold + ts.green + "=== Better luck next time! ===", ts.reset + '\n')

        stage += 1
        if stage > 1:
            reset_global()
            opened_door = ""
            stage = 0
            print(ts.bold + "Pressed ENTER to play again", ts.reset)
            input()


if __name__ == "__main__":
    gameloop()
