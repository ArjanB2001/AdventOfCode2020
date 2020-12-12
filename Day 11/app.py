import copy

def get_data() :
    try:
        file = open("Day 11/input.txt", "r")
        lines = [line.rstrip() for line in file]
        new = []
        for l in lines:
            new.append([c for c in l])

        file.close()
        return new
    except Exception as e:
        print(e)
        return []

def get_next_one(data, i, j):
    status = data[i][j]

    if status == ".":
        return "."
    elif status == "L":
        for x in range(3):
            for y in range(3):
                loc_i = (i-1) + y
                loc_j = (j-1) + x
                if loc_i < 0 or loc_j < 0:
                    continue
                if x == 1 and y == 1:
                    continue
                else:
                    try:
                        if data[(i - 1) + y][(j-1) + x] == "#":
                            return "L"
                    except IndexError:
                        continue

        return "#"
    elif status == "#":
        counter = 0
        for x in range(3):
            for y in range(3):
                if x == 1 and y == 1:
                    continue
                else:
                    try:
                        loc_i = (i-1) + y
                        loc_j = (j-1) + x
                        if loc_i < 0 or loc_j < 0:
                            continue
                        if data[(i - 1) + y][(j-1) + x] == "#":
                            # print(str(x) + " | " + str(y) + " || " + str(i) + " | " + str(j))
                            counter += 1
                    except IndexError as e:
                        continue
        if counter > 3:
            return "L"
        else:
            return "#"
    else:
        print("PANIK")
        exit()

def part_one():
    data = get_data()
    
    prev = copy.deepcopy(data)

    while True:
        # print("=====================")
        # for p in prev:
        #     s = ""
        #     for m in p:
        #         s = s + m
        #     print(s)
        c = copy.deepcopy(prev)
        changes = []
        for i in range(len(c)):
            for j in range(len(c[i])):
                changes.append([i, j, get_next_one(c, i , j)])

        for change in changes:
            c[change[0]][change[1]] = change[2]

        if c == prev:
            count = 0
            for i in range(len(c)):
                for j in range(len(c[i])):
                    if c[i][j] == "#":
                        count += 1
            return count

        prev = copy.deepcopy(c)

    return data

def get_neighbours(data, i, j):
    neighbours = []
    for y in range(-1, 2, 1):
        for x in range(-1, 2, 1):
            if not (x == 0 and y == 0):
                try:
                    loc_i = i + y
                    loc_j = j + x
                    
                    if loc_i < 0 or loc_j < 0:
                        continue

                    symbol = data[loc_i][loc_j]

                    while symbol == ".":
                        loc_i = loc_i + y
                        loc_j = loc_j + x
                        if loc_i < 0 or loc_j < 0:
                            break
                        symbol = data[loc_i][loc_j]
                        # print(str(loc_j) + " - " + str(loc_i) + " : " + symbol)
                        # print(x)
                        # print(y)
                        # print(i)
                        # print(j)


                    neighbours.append(symbol)
                except IndexError:
                    # print("hmm")
                    continue
    
    while "." in neighbours:
        neighbours.remove(".")
    return neighbours

# print(get_neighbours(get_data(), 3, 3))

def get_next_two(data, i, j):
    status = data[i][j]
    neighbours = get_neighbours(data, i, j)
    if status == ".":
        return "."
    elif status == "L":
        ret = "#"
        for neighbour in neighbours:
            if neighbour == "#":
                ret = "L"
        return ret
    elif status == "#":
        counter = 0
        for neighbour in neighbours:
            if neighbour == "#":
                counter += 1
        if counter > 4:
            return "L"
        else:
            return "#"

def part_two():
    data = get_data()
    
    prev = copy.deepcopy(data)
    counters = 0
    while True:
        # print("Iteration " + str(counters))
        # print("=====================")
        # for p in prev:
        #     s = ""
        #     for m in p:
        #         s = s + m
        #     print(s)
        c = copy.deepcopy(prev)
        changes = []
        for i in range(len(c)):
            # print("===========")
            # print(i)
            for j in range(len(c[i])):
                changes.append([i, j, get_next_two(c, i , j)])
                # print(changes)
                # print(j)
            
            

        
        for change in changes:
            c[change[0]][change[1]] = change[2]

        if c == prev:
            count = 0
            for i in range(len(c)):
                for j in range(len(c[i])):
                    if c[i][j] == "#":
                        count += 1
            return count

        prev = copy.deepcopy(c)
        counters += 1

    return

# print(get_data())
print(part_one())
print(part_two())
# print(get_neighbours(get_data(), 0, 8))
# print(get_next_two(get_data(), 0 , 8))