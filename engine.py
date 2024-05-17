import pygame
import tkinter as tk
from tkinter import filedialog


class Engine:
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.cSize = 20
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def createMat(self, root):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(300 + j * self.cSize, 175 + i * self.cSize, self.cSize, self.cSize)
                pygame.draw.rect(root, (255, 255, 255), rect)
                pygame.draw.rect(root, (55, 89, 89), rect, 2)


    def drawOverMat(self):
        if pygame.mouse.get_pressed()[0]:
            pass


    def uploadImg(self):
        window = tk.Tk()
        window.withdraw()
        path = filedialog.askopenfilename()
        if path == "":
            return
        print(path)

    def saveImg(self):
        pass

    def editImg(self):
        pass

    def viewImg(self):
        print(self.matrix)

    def viewMatNum(self):
        pass

    def closeImg(self):
        pass

    def showImg(self):
        pass

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass

    def rotateMatRgt(self):
        pass

    def rotateMatLft(self):
        pass


class Button:
    def __init__(self, x, y, image, root):
        self.image = pygame.transform.scale(image, (50, 50))
        self.root = root
        self.x = x
        self.y = y
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        self.root.blit(self.image, (self.x, self.y))

    def pressed(self):

        command = False
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                command = True
                self.clicked = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return command
