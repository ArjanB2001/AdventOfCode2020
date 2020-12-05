def get_data():
    try:
        file = open("passes.txt", "r")
        n = [line.rstrip() for line in file]
        file.close()
        return n
    except:
        return []

def part_one():
    passes = get_data()
    highest = 0

    for p in passes:
        lower_row = 0
        upper_row = 127
        final_row = 0

        lower_col = 0
        upper_col = 7
        final_col = 0
        for c in range(7):
            if p[c] == "F":
                d = upper_row - lower_row
                if (d == 1):
                    final_row = lower_row
                else:
                    upper_row = upper_row - round(d/2)
            else:
                d = upper_row - lower_row
                if (d==1):
                    final_row = upper_row
                else:
                    lower_row = lower_row + round(d/2)

        for x in range(7, 10):
            # print(p[x])
            if p[x] == "L":
                d = upper_col - lower_col
                if (d == 1):
                    final_col = lower_col
                else:
                    upper_col = upper_col - round(d/2)
            else:
                d = upper_col - lower_col
                if (d==1):
                    final_col = upper_col
                else:
                    lower_col = lower_col + round(d/2)
        
        id = (final_row * 8) + final_col
        if (id > highest):
            highest = id

    return highest

# print(part_one())

def part_two():
    passes = get_data()
    ids = []
    for p in passes:
        lower_row = 0
        upper_row = 127
        final_row = 0

        lower_col = 0
        upper_col = 7
        final_col = 0
        for c in range(7):
            if p[c] == "F":
                d = upper_row - lower_row
                if (d == 1):
                    final_row = lower_row
                else:
                    upper_row = upper_row - round(d/2)
            else:
                d = upper_row - lower_row
                if (d==1):
                    final_row = upper_row
                else:
                    lower_row = lower_row + round(d/2)

        for x in range(7, 10):
            # print(p[x])
            if p[x] == "L":
                d = upper_col - lower_col
                if (d == 1):
                    final_col = lower_col
                else:
                    upper_col = upper_col - round(d/2)
            else:
                d = upper_col - lower_col
                if (d==1):
                    final_col = upper_col
                else:
                    lower_col = lower_col + round(d/2)
        
        id = (final_row * 8) + final_col
        ids.append(id)

    ids.sort()

    pre = ids[0] - 1
    my = 0
    for i in ids:
        if i == pre + 1:
            pre = i
        else:
            my = i - 1
            pre = i
    return my

# print(part_two())

def input_to_id(s):
    row = s[:7]
    col = s[7:10]
    row = int(row.replace("B", "1").replace("F", "0"), 2)
    col = int(col.replace("R", "1").replace("L", "0"), 2)
    id = (row * 8) + col
    return id

def part_one_V2():
    passes = get_data()
    ids = [input_to_id(p) for p in passes]
    return max(ids)
    

def part_two_V2():
    passes = get_data()
    ids = [input_to_id(p) for p in passes]

    ids.sort()

    pre = ids[0] - 1
    my = 0
    for i in ids:
        if i == pre + 1:
            pre = i
        else:
            my = i - 1
            pre = i
    return my

# print(part_one_V2())


#one-liner part one:
print(max([(int(s[:7].replace("B", "1").replace("F", "0"), 2) * 8) + int(s[7:10].replace("R", "1").replace("L", "0"), 2) for s in [line.rstrip() for line in open("passes.txt", "r")]]))
print(part_two_V2())