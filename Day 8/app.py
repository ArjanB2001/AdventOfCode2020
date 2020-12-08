import copy

def get_data():
    try:
        file = open("Day 8/input.txt", "r")
        lines = [[line.rstrip().split(), 0] for line in file]
        file.close()
        return lines
    except Exception as e:
        print(e)

def part_one():
    data = get_data()
    acc = 0
    i = 0
    while True:
        if data[i][1] == 1:
            # loop
            break
        elif data[i][0][0] == "nop":
            data[i][1] = 1
            i = i + 1
        elif data[i][0][0] == "jmp":
            data[i][1] = 1
            i = i + int(data[i][0][1])
        elif data[i][0][0] == "acc":
            acc = acc + int(data[i][0][1])
            data[i][1] = 1
            i = i + 1

    return acc

print(part_one())

def terminates(data):
    da = copy.deepcopy(data)
    i = 0
    while True:
        if i == len(da):
            return True
        elif da[i][1] == 1:
            # print("loop")
            return False
        elif da[i][0][0] == "nop":
            da[i][1] = 1
            i = i + 1
        elif da[i][0][0] == "jmp":
            da[i][1] = 1
            i = i + int(da[i][0][1])
        elif da[i][0][0] == "acc":
            da[i][1] = 1
            i = i + 1

def get_acc(data):
    d = copy.deepcopy(data)
    i = 0
    acc = 0
    while True:
        if i == len(d):
            return acc
        elif d[i][1] == 1:
            # loop
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            break
        elif d[i][0][0] == "nop":
            d[i][1] = 1
            i = i + 1
        elif d[i][0][0] == "jmp":
            d[i][1] = 1
            i = i + int(d[i][0][1])
        elif d[i][0][0] == "acc":
            acc = acc + int(d[i][0][1])
            d[i][1] = 1
            i = i + 1

def part_two():
    data = get_data()
    i = 0
    while True:
        if i == len(data):
            print("Welp")
        if data[i][0][0] == "acc":
            i = i + 1
            continue
        elif data[i][0][0] == "nop":
            c = copy.deepcopy(data)
            c[i][0][0] = "jmp"
            if terminates(c):
                acc = get_acc(c)
                return acc
            else :
                i = i + 1
        elif data[i][0][0] == "jmp":
            c = copy.deepcopy(data)
            c[i][0][0] = "nop"
            if terminates(c):
                acc = get_acc(c)
                return acc
            else:
                i = i + 1

print(part_two())


