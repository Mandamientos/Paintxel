import pygame
import tkinter as tk
from tkinter import filedialog
import math


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
        self.ascii_dic = {
            0: "",
            1: ".",
            2: ":",
            3: "-",
            4: "=",
            5: "¡",
            6: "&",
            7: "$",
            8: "%",
            9: "@"

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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = (mouse_x - 300) // self.cSize
        row = (mouse_y - 175) // self.cSize
        if pygame.mouse.get_pressed()[0] and self.editorMode == "Brush":
            if (0 <= col < self.cols) and (0 <= row < self.rows):
                self.matrix[row][col] = self.color

        elif pygame.mouse.get_pressed()[0] and self.editorMode == "Circle":

            circle_radius = self.cSize // 6

            for i in range(self.rows):
                for j in range(self.cols):
                    distance_to_center = math.sqrt((i - row) ** 2 + (j - col) ** 2)
                    if abs(distance_to_center - circle_radius) <= 0.5:
                        self.matrix[i][j] = self.color

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
        path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if path == "":
            return

        image_surface = pygame.image.load(path)

        expected_signature = [(255, 0, 255), (0, 255, 255), (255, 255, 0)]
        actual_signature = [image_surface.get_at((i, 0))[:3] for i in range(3)]

        if actual_signature != expected_signature:
            print("El archivo seleccionado no es válido.")
            return

        image_surface = pygame.transform.scale(image_surface, (self.cols * self.cSize, self.rows * self.cSize))

        for row in range(self.rows):
            for col in range(self.cols):
                pixel_color = image_surface.get_at(
                    (col * self.cSize + self.cSize // 2, row * self.cSize + self.cSize // 2))[:3]
                for color_index, color_value in self.color_dic.items():
                    if pixel_color == color_value:
                        self.matrix[row][col] = color_index
                        break

    def saveImg(self):
        image_surface = pygame.Surface((self.cols * self.cSize, self.rows * self.cSize))

        for row in range(self.rows):
            for col in range(self.cols):
                color = self.color_dic[self.matrix[row][col]]
                rect = pygame.Rect(col * self.cSize, row * self.cSize, self.cSize, self.cSize)
                pygame.draw.rect(image_surface, color, rect)

        signature = [(255, 0, 255), (0, 255, 255), (255, 255, 0)]
        for i, color in enumerate(signature):
            image_surface.set_at((i, 0), color)

        window = tk.Tk()
        window.withdraw()
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if save_path:
            pygame.image.save(image_surface, save_path)
            print(f"Imagen guardada en {save_path}")

    def editImg(self):
        pass

    def viewImg(self):
        print(self.matrix)

    def viewMatNum(self, root):
        font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 20)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(300 + j * self.cSize, 175 + i * self.cSize, self.cSize, self.cSize)
                colortxt = font.render(str(self.matrix[i][j]), True, (0, 0, 0))
                colortxtRect = colortxt.get_rect(center=rect.center)
                root.blit(colortxt, colortxtRect)

    def closeImg(self):
        self.matrix = [[0 for i in range(self.cols)] for i in range(self.rows)]

    def showImg(self):
        pass

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass
    def rotateMatRgt(self):
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[j][self.rows - i - 1] = self.matrix[i][j]
        self.rows, self.cols = self.cols, self.rows
        self.matrix = new_matrix

    def rotateMatLft(self):
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[self.cols - j - 1][i] = self.matrix[i][j]
        self.rows, self.cols = self.cols, self.rows
        self.matrix = new_matrix

    def reflectionH(self):
        new_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[i][self.cols - j - 1] = self.matrix[i][j]
        self.matrix = new_matrix

    def reflectionV(self):
        new_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            new_matrix[self.rows - i - 1] = self.matrix[i]
        self.matrix = new_matrix

    def contrast(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] <= 4:
                    self.matrix[row][col] = 0
                else:
                    self.matrix[row][col] = 9

    def negative(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] != 0:
                    self.matrix[row][col] = 9 - self.matrix[row][col]

    def ASCIIArt(self, root):
        font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 30)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(300 + j * self.cSize, 175 + i * self.cSize, self.cSize, self.cSize)
                sym = self.ascii_dic[self.matrix[i][j]]
                colortxt = font.render(sym, True, (0, 0, 0))
                colortxtRect = colortxt.get_rect(center=rect.center)
                root.blit(colortxt, colortxtRect)


class Button:
    def __init__(self, x, y, image, root, scale, scale2):
        self.image = pygame.transform.scale(image, (scale, scale2))
        self.root = root
        self.x = x
        self.y = y
        self.drawed = False
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        self.root.blit(self.image, (self.x, self.y))
        self.drawed = True

    def pressed(self):

        command = False
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.drawed:
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

    def undraw(self):
        self.drawed = False

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
