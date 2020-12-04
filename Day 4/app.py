import re

def get_data():
    try:
        file = open("passports.txt", "r")
        n = [line for line in file]
        file.close()
        s = ''.join(n)
        formatted = s.split("\n\n")
        new = []
        for string in formatted:
            # new.append(re.split('\n |\s* ',string))
            newlines = string.splitlines()
            new_newlines = []
            for n in newlines:
                new_newlines = new_newlines + n.split()

            
            newish = []
            for ne in new_newlines:
                newish.append(ne.split(":"))
            
            # print(newish)
            new.append(newish)

        dics = []
        for nope in new:
            dic = {}
            for no in nope:
                dic[no[0]] = no[1]
            dics.append(dic)
        return dics
    except Exception as e:
        print(e)
        return []

def part_one(data):
    valid = 0

    for passport in data:
        if(len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
            valid += 1
    
    return valid

def check_byr(byr):
    byr = int(byr)
    return 1920 <= byr <= 2002

def check_iyr(iyr):
    iyr = int(iyr)
    return 2010 <= iyr <= 2020

def check_eyr(eyr):
    eyr = int(eyr)
    return 2020 <= eyr <= 2030

def check_hgt(height):
    if ('cm' in height):
        height = int(height.replace("cm", ""))
        return 150 <= height <= 193
    elif("in" in height):
        height = int(height.replace("in", ""))
        return 59 <= height <= 76
        

    return False

def check_hcl(hcl):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)

    if match:
        return True

    return False

def check_ecl(ecl):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in colors

def check_pid(pid):
    return len(pid) == 9

def part_two(data):
    valid = 0

    for passport in data:
        if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
            # print("hey")
            if(check_byr(passport["byr"]) and check_iyr(passport["iyr"]) and check_eyr(passport["eyr"]) and check_hgt(passport["hgt"]) and check_hcl(passport["hcl"]) and check_ecl(passport["ecl"]) and check_pid(passport["pid"])):
                valid += 1

    return valid

print(part_one(get_data()))

print(part_two(get_data()))



