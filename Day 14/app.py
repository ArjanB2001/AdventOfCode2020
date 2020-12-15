import copy

def get_data() :
    try:
        file = open("Day 14/input.txt", "r")
        lines = [line.rstrip() for line in file]

        file.close()
        return lines
    except Exception as e:
        print(e)
        return []

def part_one():
    data = get_data()
    mask = []
    memory = {}
    for d in data:
        d = d.split(" = ")
        if d[0][:4] == "mask":
            mask = list(d[1])
            # print(mask)
        else:
            address = d[0]
            value = list('{0:b}'.format(int(d[1])).zfill(36))
            # print(value)
            # print(mask)
            for i in range(len(mask)):
                if mask[i] == "X":
                    continue
                else:
                    value[i] = mask[i]
            # print(value)
            
            

            value = int("".join(value), 2)
            memory[address] = value

    # print(memory)
    return sum(memory.values())

print(part_one())

def get_addresses(address):
    result = []
    x = address.count("X")
    if x == 1:
        result.append(address.replace("X", "1", 1))
        result.append(address.replace("X", "0", 1))
    else:
        result = result + get_addresses(address.replace("X", "1", 1))
        result = result + get_addresses(address.replace("X", "0", 1))
  
    return result

def part_two():
    data = get_data()
    mask = []
    memory = {}
    for d in data:
        d = d.split(" = ")
        if d[0][:4] == "mask":
            mask = list(d[1])
            # print(mask)
        else:
            address = d[0][4:-1]
            address = list('{0:b}'.format(int(address)).zfill(36))
            value = int(d[1])

            for i in range(len(mask)):
                if mask[i] == "X":
                    address[i] = "X"
                elif mask[i] == "1":
                    address[i] = "1"
                else:
                    continue
            
            for x in get_addresses("".join(address)):
                memory[x] = value
            
        

    # print(memory)
    return sum(memory.values())

print(part_two())

