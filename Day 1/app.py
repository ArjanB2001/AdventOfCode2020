def get_numbers():
    try:
        file = open("numbers.txt", "r")
        n = [int(line.rstrip()) for line in file]
        file.close()
        return n
    except:
        return []
    
numbers = get_numbers()

for i in numbers:
    for j in numbers:
        for x in numbers:
            # if (i == j or i == x or j == x):
                # print("skip " + " " + str(i) + " " + str(j) + ' ' + str(x))
            if (i + j + x) == 2020:
                print(i)
                print(j)
                print(x)
                print(i*j*x)
                exit()
            