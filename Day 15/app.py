def simulate(end):
    spoken = [14,3,1,0,9,5]
    history = {}
    turn = len(spoken) + 1

    for i, value in enumerate(spoken):
        history[value] = [i + 1]

    # print(history)

    while True:
        last = spoken[-1]
        if len(history[last]) == 1:
            speak = 0
            spoken.append(speak)
            if speak not in history:
                history[speak] = [turn]
            else:
                history[speak].append(turn)
        else:
            h = history[last]
            speak = h[-1] - h[-2]
            spoken.append(speak)
            if speak not in history:
                history[speak] = [turn]
            else:
                history[speak].append(turn)

        if turn == end:
            return spoken[-1]
        turn += 1

print(simulate(2020))
print(simulate(30000000))
