def get_map():
    try:
        file = open("trees.txt", "r")
        n = [line.rstrip() for line in file]
        file.close()
        new = []
        for t in n:
            new.append(list(t))
        return new
    except:
        return []


def slope_calc(x, y):
    trees = get_map()
    count = 0
    number_of_rows = len(trees)
    current_number_of_columns = len(trees[0])
    current_y = 0
    current_x = 0

    while current_y < number_of_rows:
        if(current_x >= current_number_of_columns):
            trees = extend_map(trees)
            current_number_of_columns = len(trees[0])

        if(trees[current_y][current_x] == "#"):
            count += 1

        current_y += y
        current_x += x

    return count  

def part_one():
    return slope_calc(3, 1) 

def extend_map(map):
    new = []
    for t in map:
        new.append(t + t)

    return new

def part_two():
    return slope_calc(1,1) * slope_calc(3,1) * slope_calc(5,1) * slope_calc(7,1) * slope_calc(1,2)

print(part_one())
print(part_two())

