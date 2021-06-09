import threading


def addTotalCost(total_cost, finalMatrix, nextpos):
    if finalMatrix[nextpos[0]][nextpos[1]] == "1":
        total_cost += 1
    elif finalMatrix[nextpos[0]][nextpos[1]] == "2":
        total_cost += 5
    elif finalMatrix[nextpos[0]][nextpos[1]] == "3":
        total_cost += 10
    elif finalMatrix[nextpos[0]][nextpos[1]] == "4":
        total_cost += 15

    return total_cost


def printPath(nextPos, grid, flag):
    x, y = nextPos
    spot = grid[x][y]
    node = spot
    if flag == 0:  # Visitados
        node.make_closed()  # Amarelo -> Ja foi visitado
    elif flag == 1:  # Borda
        node.make_barrier()  # Nextpos -> Preto
    else:  # Best Way
        node.make_end()


def uniform_Cost_Search(start, end, finalMatrix, grid):
    q = []
    visited = []
    nodesTravelled, total_cost, distance = 0, 0, 0
    current = []
    nextpos = []
    getValue = []
    path = set()
    q.append((start, total_cost, [start]))
    isEnd = False
    while not isEnd:
        q.sort(key=lambda q: q[1])
        getValue = q.pop(0)  # Valor da distancia
        current = getValue[0]
        total_cost = getValue[1]
        path = getValue[2]
        nodesTravelled += 1
        printPath(current, grid, 1)

        if current[0] == end[0] and current[1] == end[1]:
            print("Total de nos: ", nodesTravelled)
            print("Best Way", path)
            for i in range(len(path)):
                printPath(path[i], grid, 2)
            print("Custo: ", total_cost)
            isEnd = True

        else:
            if current not in visited:
                visited.append(current)

            if int(current[0]) > 0:  # Up
                nextpos = (int(current[0])) - 1, int(current[1])

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    distance = addTotalCost(total_cost, finalMatrix, nextpos)
                    q.append((nextpos, distance, path + [nextpos]))
                    visited.append(nextpos)

            if int(current[0]) < 41:  # Down
                nextpos = ((int(current[0])) + 1), (int(current[1]))

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    distance = addTotalCost(total_cost, finalMatrix, nextpos)
                    q.append((nextpos, distance, path + [nextpos]))
                    visited.append(nextpos)

            if int(current[1]) < 41:  # Right
                nextpos = (int(current[0])), (int(current[1]) + 1)

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    distance = addTotalCost(total_cost, finalMatrix, nextpos)
                    q.append((nextpos, distance, path + [nextpos]))
                    visited.append(nextpos)

            if int(current[1]) > 0:  # Left
                nextpos = (int(current[0])), (int(current[1]))

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    distance = addTotalCost(total_cost, finalMatrix, nextpos)
                    q.append((nextpos, distance, path + [nextpos]))
                    visited.append(nextpos)


# ---------------------------------- A STAR ---------------------------------------------------------------------

def manhattanDistance(nextPos, end):
    return abs(nextPos[0] - end[0]) + abs(nextPos[1] - end[1])


def aStar(start, end, finalMatrix, grid):
    q = []
    visited = []
    nodesTravelled, total_cost, distance = 0, 0, 0
    current = []
    nextpos = []
    getValue = []
    path = set()
    q.append((start, distance, [start], total_cost))
    isEnd = False

    while not isEnd:
        q.sort(key=lambda q: q[1])
        getValue = q.pop(0)  # Valor da distancia
        current = getValue[0]
        path = getValue[2]
        total_cost = getValue[3]
        nodesTravelled += 1
        printPath(current, grid, 1)

        if current[0] == end[0] and current[1] == end[1]:
            print("Total de nos: ", nodesTravelled)
            print("Best Way", path)
            for i in range(len(path)):
                printPath(path[i], grid, 2)

            path.pop(0)
            total_cost = 0
            for i in range(len(path)):
                total_cost = addTotalCost(total_cost, finalMatrix, path[i])

            print("Custo: ", total_cost)
            isEnd = True

        else:
            if current not in visited:
                visited.append(current)

            if int(current[0]) > 0:  # Up
                nextpos = (int(current[0])) - 1, int(current[1])

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    aux = addTotalCost(total_cost, finalMatrix, nextpos)
                    distance = aux + manhattanDistance(nextpos, end)
                    q.append((nextpos, distance, path + [nextpos], aux))
                    visited.append(nextpos)

            if int(current[0]) < 41:  # Down
                nextpos = ((int(current[0])) + 1), (int(current[1]))

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    aux = addTotalCost(total_cost, finalMatrix, nextpos)
                    distance = aux + manhattanDistance(nextpos, end)
                    q.append((nextpos, distance, path + [nextpos], aux))
                    visited.append(nextpos)

            if int(current[1]) < 41:  # Right
                nextpos = (int(current[0])), (int(current[1]) + 1)

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    aux = addTotalCost(total_cost, finalMatrix, nextpos)
                    distance = aux + manhattanDistance(nextpos, end)
                    q.append((nextpos, distance, path + [nextpos], aux))
                    visited.append(nextpos)

            if int(current[1]) > 0:  # Left
                nextpos = (int(current[0])), (int(current[1]))

                if nextpos not in visited:
                    printPath(nextpos, grid, 0)
                    aux = addTotalCost(total_cost, finalMatrix, nextpos)
                    distance = aux + manhattanDistance(nextpos, end)
                    q.append((nextpos, distance, path + [nextpos], aux))
                    visited.append(nextpos)
