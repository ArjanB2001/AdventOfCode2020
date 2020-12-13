import copy

def get_data() :
    try:
        file = open("Day 13/input.txt", "r")
        lines = [l.split(",") for l in (line.rstrip() for line in file)]
        file.close()
        return lines
    except Exception as e:
        print(e)
        return []

def part_one():
    data = get_data()
    leave = int(data[0][0])
    current = leave
    timestamps = data[1]

    while True:
        for timestamp in timestamps:
            if timestamp == "x":
                continue
            id = int(timestamp)
            mod = current % id
            if mod == 0:
                return id * (current - leave)
        current += 1

print(part_one())

def part_two():
    data = get_data()
    d = data[1]
    sequence = []
    for s in d:
        try:
            sequence.append(int(s))
        except ValueError:
            sequence.append(s)
    
    t = 0
    jump = 1

    for i in range(len(sequence)):
        if sequence[i] == "x":
            continue

        # print(sequence[i])
        while (t + i) % sequence[i] != 0:
            # print(t)
            t = t + jump
        jump *= sequence[i]

    return t


print(part_two())


