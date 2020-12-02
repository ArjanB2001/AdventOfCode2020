def get_passwords():
    try:
        file = open("passwords.txt", "r")
        n = [line.rstrip() for line in file]
        file.close()
        new = []
        for p in n:
            p = p.split()
            p[1] = p[1].rstrip(":")
            p[0] = p[0].split("-")
            dic = {"least": int(p[0][0]), "most": int(p[0][1]), "key": p[1], "password": p[2]}
            new.append(dic)
        return new
    except:
        return []

def is_valid(least, most, count):
    return least <= count and count <=most

passwords = get_passwords()

valid = 0

for p in passwords:
    c = 0
    for char in p["password"]:
        if char == p["key"]:
            c = c + 1

    if(is_valid(p["least"], p["most"], c)):
        valid = valid + 1

print(valid)

valid_two = 0

for p in passwords:
    # print(p["password"] + " | " + p["password"][0])
    first_post = p["password"][p["least"]-1] == p["key"]
    second_pos =  p["password"][p["most"]-1] == p["key"]
    if (first_post != second_pos):
        valid_two = valid_two + 1

print(valid_two)
    