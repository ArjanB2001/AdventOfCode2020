import copy

def get_data() :
    try:
        file = open("Day 16/input.txt", "r")
        lines = [line.rstrip() for line in file]

        file.close()
        return lines
    except Exception as e:
        print(e)
        return []


def part_one():
    input = get_data()
    ranges = []
    for i, line in enumerate(input):
        if line == "":
            break
        for l in line.split(": ")[1].split(" or "):
            ranges.append([int(x) for x in l.split("-")])

    print(ranges)

    nearby_tickets = []
    nearby = False
    for i, line in enumerate(input):
        if nearby:
            nearby_tickets.append([int(x) for x in line.split(",")])
        if line == "nearby tickets:":
            nearby = True

    invalid = []
    invalid_tickets = []
    for i, ticket in enumerate(nearby_tickets):
        for x, value in enumerate(ticket):
            valid = False
            for range in ranges:
                if range[0] <= value <= range[1]:
                    valid = True
                    break
                
            if not valid:
                invalid.append(value)
                invalid_tickets.append(ticket)
                



    return sum(invalid)


print(part_one())

def part_two():
    input = get_data()
    classes = {}
    for i, line in enumerate(input):
        if line == "":
            break
        classes[line.split(": ")[0]] = [[int(x) for x in y.split("-")] for y in line.split(": ")[1].split(" or ")]

    print(classes)

    nearby_tickets = []
    nearby = False
    for i, line in enumerate(input):
        if nearby:
            nearby_tickets.append([int(x) for x in line.split(",")])
        if line == "nearby tickets:":
            nearby = True

    invalid = []
    invalid_tickets = []
    for i, ticket in enumerate(nearby_tickets):
        for x, value in enumerate(ticket):
            valid = False
            for c in classes:
                if classes[c][0] <= value <= classes[c][1]:
                    valid = True
                    break
                
            if not valid:
                invalid.append(value)
                invalid_tickets.append(ticket)

    # print(nearby_tickets)
    # print(len(nearby_tickets))
    # nearby_tickets = nearby_tickets - invalid_tickets
    # print(nearby_tickets)
    # print(len(nearby_tickets))
    return sum(invalid)

print(part_two())