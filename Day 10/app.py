import copy

def get_data() :
    try:
        file = open("Day 10/input.txt", "r")
        lines = [int(line.rstrip()) for line in file]
        lines.append(0)
        lines.append(max(lines) + 3)
        lines = sorted(lines)
        file.close()
        return lines
    except Exception as e:
        print(e)
        return []

def part_one():
    diff = [0, 0, 0]
    data = get_data()
    for i in range(len(data) - 1):
        current = data[i]
        next = 0
        next = data[i+1]

        dif = next - current
        diff[dif-1] += 1
    
    # print(diff)
    return diff[0] * diff[2]

print(part_one())

# couldn't figure it out myself so part 2 is mostly copied from reddit
def part_two(index, adapters, done):
    if index == len(adapters) - 1:
        return 1
    if index in done:
        return done[index]
    arrangements = 0
    next_possibilities = [p for p in range(len(adapters)) if 1<= adapters[p] - adapters[index] <= 3]
    for x in next_possibilities:
        arrangements += part_two(x, adapters, done)
    
    done[index] = arrangements
    return arrangements

print(part_two(0, get_data(), {}))

    