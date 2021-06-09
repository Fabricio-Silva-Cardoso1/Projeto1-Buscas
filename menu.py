from tkinter.filedialog import askopenfilename

import pygame
import tkinter as tk
from tkinter import filedialog

import DrawMap
import SearchAlgorithms

WIDTH = 800
# Tela do jogo
WIN = pygame.display.set_mode((WIDTH, WIDTH))
# Nome e icone da tela do jogo
pygame.display.set_caption("Projeto 1 - Buscas")


def main():
    ROWS = 42  # Tamanho da matriz
    grid = DrawMap.make_grid(ROWS, WIDTH)
    finalMatrix = []
    # root = tk.Tk()
    # root.withdraw

    file_path = askopenfilename()

    f = open(file_path, "r")
    start = DrawMap.inicial_values(f)
    end = DrawMap.inicial_values(f)

    vetSpots = DrawMap.read1on1(f)
    finalMatrix = DrawMap.VettoMatrix(vetSpots)

    f.close()

    DrawMap.printMap(ROWS, grid, vetSpots, start, end)

    run = True
    while run:
        DrawMap.draw(WIN, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Se apertar o X, encerra o programa
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SearchAlgorithms.aStar(start, end, finalMatrix, grid)
                    # SearchAlgorithms.uniform_Cost_Search(start, end, finalMatrix, grid)

    pygame.quit()


main()
