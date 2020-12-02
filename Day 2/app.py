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
            dic = {"bottom": int(p[0][0]), "top": int(p[0][1]), "key": p[1], "password": p[2]}
            new.append(dic)
        return new
    except:
        return []

def is_valid(bottom, top, count):
    return bottom <= count and count <= top

passwords = get_passwords()

valid = 0

for p in passwords:
    c = 0
    for char in p["password"]:
        if char == p["key"]:
            c = c + 1

    if(is_valid(p["bottom"], p["top"], c)):
        valid = valid + 1

print(valid)

valid_two = 0

for p in passwords:
    # print(p["password"] + " | " + p["password"][0])
    bottom_pos = p["password"][p["bottom"]-1] == p["key"]
    top_pos =  p["password"][p["top"]-1] == p["key"]
    if (bottom_pos != top_pos):
        print(("Key: {} - Bottom index: {} - Top Index: {} for character: {}").format(p["password"], p["bottom"], p["top"], p["key"]))
        valid_two = valid_two + 1

print(valid_two)
    