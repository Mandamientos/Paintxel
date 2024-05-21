import pygame
import tkinter as tk
from tkinter import filedialog


class Engine:
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.cSize = 20
        self.editorMode = "Brush"
        self.color = 9
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.color_dic = {
            0: (255, 255, 255), # White
            1: (0, 126, 255), # Blue
            2: (255, 0, 0), # Red
            3: (0, 255, 18), # Green
            4: (246, 255, 0), # Yellow
            5: (186, 0, 255), # Purple
            6: (250, 207, 249), # Pink
            7: (244, 196, 64), # Orange
            8: (0, 255, 204), # Light Blue
            9: (0, 0, 0) # Black
        }

    def createMat(self, root):
        matbbox = pygame.Rect(300, 175, 600, 600)
        mousepos = pygame.mouse.get_pos()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(300 + j * self.cSize, 175 + i * self.cSize, self.cSize, self.cSize)
                color = self.color_dic[self.matrix[i][j]]
                pygame.draw.rect(root, color, rect)
                pygame.draw.rect(root, (55, 89, 89), rect, 1)

        if matbbox.collidepoint(mousepos) and self.editorMode == "Brush":
            pygame.mouse.set_visible(False)

            cursor = pygame.image.load("assets/images/brush.png")
            cursor = pygame.transform.scale(cursor, (50, 50))

            cursorRect = cursor.get_rect()
            cursorRect.center = (mousepos[0]+20, mousepos[1]-20)

            root.blit(cursor, cursorRect)
        else:
            pygame.mouse.set_visible(True)

    def editorModeSelect(self, mode):
        self.editorMode = mode

    def chageColor(self, color):
        self.color = color

    def drawOverMat(self):
        if pygame.mouse.get_pressed()[0] and self.editorMode == "Brush":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = (mouse_x - 300) // self.cSize
            row = (mouse_y - 175) // self.cSize
            if (0 <= col < self.cols) and (0 <= row < self.rows):
                self.matrix[row][col] = self.color

    def eraseOverMat(self):
        if pygame.mouse.get_pressed()[0] and self.editorMode == "Eraser":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = (mouse_x - 300) // self.cSize
            row = (mouse_y - 175) // self.cSize
            if (0 <= col < self.cols) and (0 <= row < self.rows):
                self.matrix[row][col] = 0


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

    def hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


class SelectedBtn:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.root = root
        self.rect = pygame.Rect(x, y, 55, 55)

    def drawRect(self):
        rectangle = pygame.draw.rect(self.root, (204, 204, 255), self.rect)

    def changePos(self, x, y):
        self.rect.x = x
        self.rect.y = y