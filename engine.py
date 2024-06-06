import pygame
import tkinter as tk
from tkinter import filedialog
import math


class Engine:
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.cSize = 20
        self.inmcSize = 20
        self.editorMode = "Brush"
        self.color = 9
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.matbbox = pygame.Rect(300, 175, 600, 600)
        self.offset_x = self.matbbox.x
        self.offset_y = self.matbbox.y
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
        # Renderiza la matriz de la cuadrícula en la pantalla.
        mousepos = pygame.mouse.get_pos()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(self.offset_x + j * self.cSize, self.offset_y + i * self.cSize, self.cSize, self.cSize)
                color = self.color_dic[self.matrix[i][j]]
                pygame.draw.rect(root, color, rect)
                pygame.draw.rect(root, (55, 89, 89), rect, 1)

        # if self.matbbox.collidepoint(mousepos) and self.editorMode == "Brush":
        #     pygame.mouse.set_visible(False)
        #
        #     cursor = pygame.image.load("assets/images/brush.png")
        #     cursor = pygame.transform.scale(cursor, (50, 50))
        #
        #     cursorRect = cursor.get_rect()
        #     cursorRect.center = (mousepos[0]+20, mousepos[1]-20)
        #
        #     root.blit(cursor, cursorRect)
        # else:
        #     pygame.mouse.set_visible(True)

    def editorModeSelect(self, mode):
        # Cambia el modo de edición (pincel, círculo, cuadrado, etc.).
        self.editorMode = mode

    def chageColor(self, color):
        # Cambia el color de dibujo.
        self.color = color

    def drawOverMat(self):
        # Dibuja sobre la matriz basado en el modo de edición (pincel, círculo, cuadrado).
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = int((mouse_x - self.offset_x) // self.cSize)
        row = int((mouse_y - self.offset_y) // self.cSize)

        if not (col < 0) and not (row < 0):
            if pygame.mouse.get_pressed()[0] and self.editorMode == "Brush":
                if (0 <= col < self.cols) and (0 <= row < self.rows):
                    self.matrix[row][col] = self.color

            elif pygame.mouse.get_pressed()[0] and self.editorMode == "Circle":

                circle_radius = self.inmcSize // 6

                for i in range(self.rows):
                    for j in range(self.cols):
                        distance_to_center = math.sqrt((i - row) ** 2 + (j - col) ** 2)
                        print(distance_to_center - circle_radius)
                        if abs(distance_to_center - circle_radius) <= 0.5:
                            print("Pixel sobre la circunferencia")
                            self.matrix[i][j] = self.color

            elif pygame.mouse.get_pressed()[0] and self.editorMode == "Square":
                half_side = (self.inmcSize // 2) // 4
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        if (col - half_side <= j <= col + half_side and
                            (i == row - half_side or i == row + half_side)) or \
                                (row - half_side <= i <= row + half_side and
                                 (j == col - half_side or j == col + half_side)):
                            self.matrix[i][j] = self.color

    def eraseOverMat(self):
        # Borra partes de la matriz cuando está en modo borrador.
        if pygame.mouse.get_pressed()[0] and self.editorMode == "Eraser":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = int((mouse_x - self.offset_x) // self.cSize)
            row = int((mouse_y - self.offset_y) // self.cSize)
            if (0 <= col < self.cols) and (0 <= row < self.rows):
                self.matrix[row][col] = 0

    def uploadImg(self):
        # Carga un archivo de imagen en la matriz.
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
        # Guarda la matriz actual como un archivo de imagen.
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

    def viewMatNum(self, root):
        # Renderiza la representación numérica de la matriz.
        font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 20)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(300 + j * self.inmcSize, 175 + i * self.inmcSize, self.inmcSize, self.inmcSize)
                colortxt = font.render(str(self.matrix[i][j]), True, (0, 0, 0))
                colortxtRect = colortxt.get_rect(center=rect.center)
                root.blit(colortxt, colortxtRect)

    def closeImg(self):
        # Borra la matriz.
        self.matrix = [[0 for i in range(self.cols)] for i in range(self.rows)]

    def zoomIn(self):
        # Acerca la vista de la matriz.
        mouse_x, mouse_y = pygame.mouse.get_pos()

        oldcSize = self.cSize
        self.cSize += 5

        scale = self.cSize / oldcSize

        self.offset_x = mouse_x - scale * (mouse_x - self.offset_x)
        self.offset_y = mouse_y - scale * (mouse_y - self.offset_y)


    def zoomOut(self):
        # Aleja la vista de la matriz.
        if self.cSize == 5:
            pass
        else:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            oldcSize = self.cSize
            self.cSize -= 5

            scale = self.cSize / oldcSize

            self.offset_x = mouse_x - scale * (mouse_x - self.offset_x)
            self.offset_y = mouse_y - scale * (mouse_y - self.offset_y)


    def resetZoom(self):
        # Restablece el nivel de zoom de la matriz.
        self.cSize = self.inmcSize
        self.offset_x = self.matbbox.x
        self.offset_y = self.matbbox.y


    def rotateMatRgt(self):
        # Rota la matriz hacia la derecha.
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[j][self.rows - i - 1] = self.matrix[i][j]
        self.rows, self.cols = self.cols, self.rows
        self.matrix = new_matrix

    def rotateMatLft(self):
        # Rota la matriz hacia la izquierda.
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[self.cols - j - 1][i] = self.matrix[i][j]
        self.rows, self.cols = self.cols, self.rows
        self.matrix = new_matrix

    def reflectionH(self):
        # Refleja la matriz horizontalmente.
        new_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix[i][self.cols - j - 1] = self.matrix[i][j]
        self.matrix = new_matrix

    def reflectionV(self):
        # Refleja la matriz verticalmente.
        new_matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            new_matrix[self.rows - i - 1] = self.matrix[i]
        self.matrix = new_matrix

    def contrast(self):
        # Ajusta el contraste de la matriz.
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] <= 4:
                    self.matrix[row][col] = 0
                else:
                    self.matrix[row][col] = 9

    def negative(self):
        # Aplica el efecto negativo a la matriz.
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] != 0:
                    self.matrix[row][col] = 9 - self.matrix[row][col]
                elif self.matrix[row][col] == 0:
                    self.matrix[row][col] = 9

    def ASCIIArt(self, root):
        # Renderiza la representación ASCII de la matriz.
        font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 30)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                rect = pygame.Rect(300 + j * self.inmcSize, 175 + i * self.inmcSize, self.inmcSize, self.inmcSize)
                sym = self.ascii_dic[self.matrix[i][j]]
                colortxt = font.render(sym, True, (0, 0, 0))
                colortxtRect = colortxt.get_rect(center=rect.center)
                root.blit(colortxt, colortxtRect)

    def cColor(self, root):
        # Renderiza el color actualmente seleccionado en la pantalla.
        colorRect = pygame.Rect(720, 60, 80, 80)
        colorRectBorder = colorRect.inflate(10, 10)
        pygame.draw.rect(root, (223, 223, 229), colorRectBorder)
        pygame.draw.rect(root, self.color_dic[self.color], colorRect)


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
