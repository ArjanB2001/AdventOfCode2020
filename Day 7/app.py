def get_data():
    try:
        file = open("Day 7/input.txt", "r")
        lines = [line for line in file]
        file.close()
        rules = {}
        for line in lines:
            line = line.split(" contain ")
            line[0] = line[0].split()
            rules[line[0][0] + " " + line[0][1]] = [(word.split()[0] + " " + word.split()[1] + " " + word.split()[2]) for word in line[1].split(", ")]

        return rules
    except Exception as e:
        print(e)

rules = get_data()

def recursive_part_one(name):
    global rules
    inner_bags = rules[name]
    count = 0
    for bag in inner_bags:
        # print(bag)
        if bag == "no other bags.":
            continue
        elif bag[2:] == "shiny gold":
            count = count + int(bag[0])
        else:
            # print(bag)
            count = count + (int(bag[0]) * int(recursive_part_one(bag[2:])))

    return count

def part_one():
    global rules
    global_count = 0
    for rule in rules:
        if(recursive_part_one(rule) > 0):
            global_count = global_count + 1
    
    return global_count

print(part_one())

def recursive_part_two(name):
    global rules
    count = 0
    outer_bag = rules[name]
    for bag in outer_bag:
        if bag == "no other bags.":
            continue
        else:
            count = count + (int(bag[0])) * recursive_part_two(bag[2:])



    return count + 1

def part_two():
    global rules
    global_count = 0
    shiny_gold = rules["shiny gold"]
    for bag in shiny_gold:
        global_count = global_count + (int(bag[0]) * recursive_part_two(bag[2:]))

    return global_count

print(part_two())

