import pygame

# Definicao de cores
GREEN = (0, 255, 0)  # Plano
BROWN = (139, 69, 19)  # Montanhoso
BLUE = (0, 0, 255)  # Pantano
RED = (255, 0, 0)  # Fogo
ORANGE = (255, 164, 0)  # Inicio
PURPLE = (128, 0, 128)  # Fim
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


class Nodes:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = YELLOW

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = PURPLE

    def make_mountain(self):
        self.color = BROWN

    def make_water(self):
        self.color = BLUE

    def make_fire(self):
        self.color = RED

    def make_plane(self):
        self.color = GREEN

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.y, self.x, self.width, self.width))

    def __lt__(self, other):
        return False


# Faz o grid -> Gera o grid em um vetor 2d
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Nodes(i, j, gap, rows)
            grid[i].append(node)

    return grid


# Desenha o grid por linha
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


# Função principal, reposponsavel por desenhar realmente o grid
def draw(win, grid, rows, width):
    win.fill(BLACK)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def divXY(pos):
    # gap = width // rows
    x, y = pos

    row = int(x)
    col = int(y)

    return row, col


def inicial_values(string):
    text = string.readline()
    a = text.strip().split(",")
    t, t1 = divXY(a)
    a = (t, t1)

    return a


def read1on1(string):
    content = string.read()
    content = content.replace("\n", "").replace(",", "")

    return content


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


def VettoMatrix(string):
    Matrix = []
    for x in range(42):
        Matrix.append((Convert(string[(x * 42):((x + 1) * 42)])))

    return Matrix


def printMap(rows, grid, vetSpots, start, end):
    i = 0

    for x in range(rows):
        for y in range(rows):
            if vetSpots[i] == " ":
                i += 1
            elif vetSpots[i] == "1":
                i += 1
                spot = grid[x][y]
                node = spot
                node.make_plane()
            elif vetSpots[i] == "2":
                i += 1
                spot = grid[x][y]
                node = spot
                node.make_mountain()
            elif vetSpots[i] == "3":
                i += 1
                spot = grid[x][y]
                node = spot
                node.make_water()
            elif vetSpots[i] == "4":
                i += 1
                spot = grid[x][y]
                node = spot
                node.make_fire()

    row, col = divXY(start)
    spot = grid[row][col]
    node = spot

    node.make_start()

    row, col = divXY(end)
    spot = grid[row][col]
    node = spot

    node.make_end()