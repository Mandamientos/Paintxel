import sys
import time

import pygame
import os
from engine import Engine, Button, SelectedBtn

pygame.init()

Eng = Engine()
isOnButton = False
icon = pygame.image.load("assets/images/brush.png")
root = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Paintxel")
pygame.display.set_icon(icon)
root.fill((223, 223, 229))

# Cargar y mostrar imágenes

listImgs = os.listdir("assets/images")
pygameImgs = []
print(listImgs)

for i in range(len(listImgs)):
    img = pygame.image.load("assets/images/"+listImgs[i])
    print(listImgs[i], i)
    pygameImgs.append(img)

pygameImgs[12] = pygame.transform.scale(pygameImgs[12], (200, 200))

# Crear objetos botón

uploadBtn = Button(30, 50, pygameImgs[23], root, 50, 50)
saveBtn = Button(100, 50, pygameImgs[21], root, 50, 50)
crossBtn = Button(170, 50, pygameImgs[7], root, 50, 50)
BrushBtn = Button(70, 230, pygameImgs[5], root, 50, 50)
EraserBtn = Button(150, 230, pygameImgs[8], root, 50, 50)
CircleBtn = Button(70, 300, pygameImgs[6], root, 50, 50)
SquareBtn = Button(150, 300, pygameImgs[22], root, 50, 50)
BlackColorBtn = Button(65, 450, pygameImgs[3], root, 50, 50)
BlueColorBtn = Button(150, 450, pygameImgs[4], root, 50, 50)
RedColorBtn = Button(65, 520, pygameImgs[18], root, 50, 50)
GreenColorBtn = Button(150, 520, pygameImgs[9], root, 50, 50)
YellowColorBtn = Button(65, 590, pygameImgs[25], root, 50, 50)
MagentaColorBtn = Button(150, 590, pygameImgs[13], root, 50, 50)
PinkColorBtn = Button(65, 660, pygameImgs[17], root, 50, 50)
OrangeColorBtn = Button(150, 660, pygameImgs[16], root, 50, 50)
LBColorBtn = Button(105, 730, pygameImgs[11], root, 50, 50)
AscBtn = Button(300, 30, pygameImgs[0], root, 100, 100)
NumMat = Button(450, 30, pygameImgs[15], root, 100, 100)
RotateLeft = Button(990, 230, pygameImgs[19], root, 50, 50)
RotateRight = Button(1060, 230, pygameImgs[20], root, 50, 50)
ReflectionAxisY = Button(950, 350, pygameImgs[2], root, 70, 70)
ReflectionAxisX = Button(1080, 350, pygameImgs[1], root, 70, 70)
negativeBtn = Button(957, 500, pygameImgs[14], root, 180, 40)
highContrBtn = Button(957, 570, pygameImgs[10], root, 180, 80)
homeBtn = Button(70, 50, pygameImgs[26], root, 50, 50)

buttonList = [uploadBtn, saveBtn, BrushBtn, EraserBtn, CircleBtn, SquareBtn, BlackColorBtn, BlueColorBtn, RedColorBtn, GreenColorBtn, YellowColorBtn, MagentaColorBtn, PinkColorBtn, OrangeColorBtn, LBColorBtn, AscBtn, NumMat, RotateLeft, RotateRight, ReflectionAxisY, ReflectionAxisX, crossBtn, negativeBtn, highContrBtn]
buttonListNumMat = [homeBtn]

selected = SelectedBtn(70, 230, root)

# Texto de la interfaz

font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 36)

font2 = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 50)

toolbarTxt = font.render("TOOLBAR", True, (0, 0, 0))
toolbarTxtRect = toolbarTxt.get_rect(center=(133, 200))

numMatTxt = font2.render("Numeric Matrix", True, (0, 0, 0))
numMatTxtRect = numMatTxt.get_rect(center=(600, 70))

asciiTxt = font2.render("ASCII ART", True, (0, 0, 0))
asciiTxtRect = numMatTxt.get_rect(center=(680, 70))

colorsTxt = font.render("COLORS", True, (0, 0, 0))
colorsTxtRect = colorsTxt.get_rect(center=(133, 400))

rotateTxt = font.render("ROTATE", True, (0, 0, 0))
rotateTxtRect = rotateTxt.get_rect(center=(1050, 200))

reflectionsTxt = font.render("REFLECTIONS", True, (0, 0, 0))
reflectionsTxtRect = reflectionsTxt.get_rect(center=(1050, 320))

othersTxt = font.render("OTHERS", True, (0, 0, 0))
othersTxtRect = reflectionsTxt.get_rect(center=(1095, 450))

# Bucle principal del programa

def mainMenu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if uploadBtn.pressed():
            Eng.uploadImg()
        if saveBtn.pressed():
            Eng.saveImg()
        if BrushBtn.pressed():
            Eng.editorModeSelect("Brush")
            selected.changePos(70, 230)
        if EraserBtn.pressed():
            Eng.editorModeSelect("Eraser")
            selected.changePos(150, 230)
        if CircleBtn.pressed():
            Eng.editorModeSelect("Circle")
            selected.changePos(70, 300)
        if BlackColorBtn.pressed():
            Eng.chageColor(9)
        if BlueColorBtn.pressed():
            Eng.chageColor(1)
        if RedColorBtn.pressed():
            Eng.chageColor(2)
        if GreenColorBtn.pressed():
            Eng.chageColor(3)
        if YellowColorBtn.pressed():
            Eng.chageColor(4)
        if MagentaColorBtn.pressed():
            Eng.chageColor(5)
        if PinkColorBtn.pressed():
            Eng.chageColor(6)
        if OrangeColorBtn.pressed():
            Eng.chageColor(7)
        if LBColorBtn.pressed():
            Eng.chageColor(8)
        if RotateLeft.pressed():
            Eng.rotateMatLft()
        if RotateRight.pressed():
            Eng.rotateMatRgt()
        if ReflectionAxisX.pressed():
            Eng.reflectionV()
        if ReflectionAxisY.pressed():
            Eng.reflectionH()
        if crossBtn.pressed():
            Eng.closeImg()
        if negativeBtn.pressed():
            Eng.negative()
        if highContrBtn.pressed():
            Eng.contrast()
        if NumMat.pressed():
            for k in buttonList:
                k.undraw()
            numMatMenu()
        if AscBtn.pressed():
            for k in buttonList:
                k.undraw()
            asciiArtMenu()

        root.fill((223, 223, 229))

        nav_rect = pygame.Rect(0, 0, 1200, 150)
        pygame.draw.rect(root, (255, 255, 255), nav_rect)

        root.blit(pygameImgs[12], (970, -30))
        root.blit(toolbarTxt, toolbarTxtRect)
        root.blit(colorsTxt, colorsTxtRect)
        root.blit(rotateTxt, rotateTxtRect)
        root.blit(reflectionsTxt, reflectionsTxtRect)
        root.blit(othersTxt, othersTxtRect)

        Eng.createMat(root)
        Eng.drawOverMat()
        Eng.eraseOverMat()

        selected.drawRect()

        for i in buttonList:
            i.draw()

        for i in range(1):
            for j in buttonList:
                if j.hover():
                    isOnButton = True
                    break
                else:
                    isOnButton = False
            if isOnButton:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def numMatMenu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        root.fill((223, 223, 229))

        nav_rect = pygame.Rect(0, 0, 1200, 150)
        pygame.draw.rect(root, (255, 255, 255), nav_rect)

        root.blit(pygameImgs[12], (970, -30))
        root.blit(numMatTxt, numMatTxtRect)

        homeBtn.draw()

        Eng.viewMatNum(root)

        if homeBtn.pressed():
            time.sleep(0.2)
            mainMenu()

        pygame.display.flip()

def asciiArtMenu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        root.fill((223, 223, 229))

        nav_rect = pygame.Rect(0, 0, 1200, 150)
        pygame.draw.rect(root, (255, 255, 255), nav_rect)

        root.blit(pygameImgs[12], (970, -30))
        root.blit(asciiTxt, asciiTxtRect)

        homeBtn.draw()

        Eng.ASCIIArt(root)

        if homeBtn.pressed():
            time.sleep(0.2)
            mainMenu()

        pygame.display.flip()