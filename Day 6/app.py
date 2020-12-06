def get_data():
    try:
        file = open("Day 6/input.txt", "r")
        n = [line for line in file]
        file.close()
        s = "".join(n)
        s = s.split("\n\n")
        new = []
        for x in s:
            new.append(x.split("\n"))

        return new
    except:
        return []


def part_one():
    data = get_data()
    global_count = 0
    
    for group in data:
        seen = []
        
        for person in group:

            for letter in person:
                if letter not in seen:
                    seen.append(letter)

        global_count = global_count + len(seen)

    return global_count

print(part_one())        

def part_two():
    data = get_data()
    global_count = 0
    
    for group in data:
        common = [letter for letter in group[0]] 
        remove = [] 

        
        for person in group:

            for c in common:
                if c not in person:
                    remove.append(c)
            
            for r in remove:
                common.remove(r)

            remove = []

        global_count = global_count + len(common)

    return global_count

# print(part_two())
print(part_two())
