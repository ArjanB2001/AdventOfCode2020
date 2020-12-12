import copy

def get_data() :
    try:
        file = open("Day 12/input.txt", "r")
        lines = [[l[0], int(l[1:])] for l in (line.rstrip() for line in file)]
        file.close()
        return lines
    except Exception as e:
        print(e)
        return []

def part_one():
    data = get_data()
    x = 0
    y = 0
    o = 90
    for ins in data:
        command = ins[0]
        argument = ins[1]
        if command == "N":
            y = y + argument
        elif command == "E":
            x = x + argument
        elif command == "S":
            y = y - argument
        elif command == "W":
            x = x - argument
        elif command == "L":
            o = (o - argument) % 360
        elif command == "R":
            o = (o + argument) % 360
        elif command == "F":
            if o == 0:
                y = y + argument
            elif o == 90:
                x = x + argument
            elif o == 180:
                y = y - argument
            elif o == 270:
                x = x - argument
            else:
                print("Ehm what?")
                exit()
        else:
            print("This shouldnt happen")
            exit()
        

    return abs(x) + abs(y)

print(part_one())

def part_two():
    data = get_data()
    ship_x = 0
    ship_y = 0
    w_x = 10
    w_y = 1
    o = 90
    for ins in data:
        # print(w_x)
        # print(w_y)
        command = ins[0]
        argument = ins[1]
        if command == "N":
            w_y = w_y + argument
        elif command == "E":
            w_x = w_x + argument
        elif command == "S":
            w_y = w_y - argument
        elif command == "W":
            w_x = w_x - argument
        elif command == "L":
            old_x = w_x
            if argument == 90:
                w_x = -w_y
                w_y = old_x
            elif argument == 180:
                w_x = -w_x
                w_y = -w_y
            elif argument == 270:
                w_x = w_y
                w_y = -old_x
        elif command == "R":
            old_x = w_x
            if argument == 90:
                w_x = w_y
                w_y = -old_x
            elif argument == 180:
                w_x = -w_x
                w_y = -w_y
            elif argument == 270:
                w_x = -w_y
                w_y = old_x
        elif command == "F":
            ship_x = ship_x + argument * w_x
            ship_y = ship_y + argument * w_y
        else:
            print("This shouldnt happen")
            exit()
        

    return abs(ship_x) + abs(ship_y)

print(part_two())
