WIDTH = 101
HEIGHT = 103

bots = []
with open("2024/prompts/14p.txt") as f:
    for line in f:
        line = line.strip()
        line = line.replace("p=", "")
        line = line.replace("v=", "")
        line = line.split(" ")
        line[0] = line[0].split(",")
        line[1] = line[1].split(",")

        x = int(line[0][0])
        y = int(line[0][1])
        xvel = int(line[1][0])
        yvel = int(line[1][1])
        bots.append([[x, y], [xvel, yvel]])

finalLocation = []
for bot in bots:
    finalx = bot[0][0] + bot[1][0]*100
    finaly = bot[0][1] + bot[1][1]*100
    while finalx >= WIDTH:
        finalx -= WIDTH
    while finalx < 0:
        finalx += WIDTH
    while finaly >= HEIGHT:
        finaly -= HEIGHT
    while finaly < 0:
        finaly += HEIGHT
    finalLocation.append([finalx, finaly])

quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0
for location in finalLocation:
    if location[0] < WIDTH/2-1 and location[1] < HEIGHT/2-1:
        quad1 += 1
    elif location[0] > WIDTH/2 and location[1] < HEIGHT/2-1:
        quad2 += 1
    elif location[0] < WIDTH/2-1 and location[1] > HEIGHT/2:
        quad3 += 1
    elif location[0] > WIDTH/2 and location[1] > HEIGHT/2:
        quad4 += 1

total = quad1 * quad2 * quad3 * quad4
print("Part1:", total)

second = 0
while second < 10000:
    for i, bot in enumerate(bots):
        finalx = bot[0][0] + bot[1][0]
        finaly = bot[0][1] + bot[1][1]
        if finalx >= WIDTH:
            finalx -= WIDTH
        if finalx < 0:
            finalx += WIDTH
        if finaly >= HEIGHT:
            finaly -= HEIGHT
        if finaly < 0:
            finaly += HEIGHT
        bot[0] = [finalx,finaly]
        bots[i] = bot

    second += 1

    if (second - 14) % 101 == 0 and (second-76) % 103 == 0:
        for y in range(HEIGHT):
            line = ""
            for x in range(WIDTH):
                count = 0
                for bot in bots:
                    if bot[0] == [x, y]:
                        count += 1
                if count == 0:
                    line += "."
                else:
                    line = line + str(count)
            print(line)

        print("Part2, second: ", second)
        input()

# 14 and 76 are notable
# 76 - 14 = 62
# 14 vertical
# 115 vertical
# 76 horizontal
# 179 horizontal

total = quad1 * quad2 * quad3 * quad4
print("Part2 Sanity:", total)