def get_data():
    try:
        file = open("Day 9/input.txt", "r")
        lines = [int(line.rstrip()) for line in file]
        file.close()
        return lines
    except Exception as e:
        print(e)


def part_one():
    preamble_len = 25
    data = get_data()

    for i in range(preamble_len, len(data)):
        preamble = data[i-preamble_len:i]
        if (check_if_sum(preamble, data[i])):
            continue
        else:
            return data[i]

def check_if_sum(preamble, sum):
    for p in preamble:
        for x in preamble:
            if p + x == sum:
                return True
    return False

print(part_one())

def part_two():
    target = 731031916
    data = get_data()
    for i in range(len(data)):
        for x in range(len(data)):
            if sum(data[i:x]) == target:
                return min(data[i:x]) + max(data[i:x])
    
print(part_two())