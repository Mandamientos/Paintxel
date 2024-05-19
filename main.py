import pygame
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

logoImg = pygame.image.load("assets/images/logopaint.png")
logoImg = pygame.transform.scale(logoImg, (200, 200))

uploadImg = pygame.image.load("assets/images/Upload.png")
saveImg = pygame.image.load("assets/images/Save.png")
eraserImg = pygame.image.load("assets/images/eraser.png")
blackColorImg = pygame.image.load("assets/images/black.png")
blueColorImg = pygame.image.load("assets/images/blue.png")
redColorImg = pygame.image.load("assets/images/red.png")
greenColorImg = pygame.image.load("assets/images/green.png")
yellowColorImg = pygame.image.load("assets/images/yellow.png")
magentaColorImg = pygame.image.load("assets/images/magenta.png")
pinkColorImg = pygame.image.load("assets/images/pink.png")
orangeColorImg = pygame.image.load("assets/images/orange.png")
LBColorImg = pygame.image.load("assets/images/light_blue.png")
CircleImg = pygame.image.load("assets/images/circle.png")
squareImg = pygame.image.load("assets/images/square.png")


# Crear objetos botón

uploadBtn = Button(30, 50, uploadImg, root)
saveBtn = Button(100, 50, saveImg, root)
BrushBtn = Button(70, 230, icon, root)
EraserBtn = Button(150, 230, eraserImg, root)
CircleBtn = Button(70, 300, CircleImg, root)
SquareBtn = Button(150, 300, squareImg, root)
BlackColorBtn = Button(65, 450, blackColorImg, root)
BlueColorBtn = Button(150, 450, blueColorImg, root)
RedColorBtn = Button(65, 520, redColorImg, root)
GreenColorBtn = Button(150, 520, greenColorImg, root)
YellowColorBtn = Button(65, 590, yellowColorImg, root)
MagentaColorBtn = Button(150, 590, magentaColorImg, root)
PinkColorBtn = Button(65, 660, pinkColorImg, root)
OrangeColorBtn = Button(150, 660, orangeColorImg, root)
LBColorBtn = Button(105, 730, LBColorImg, root)


buttonList = [uploadBtn, saveBtn, BrushBtn, EraserBtn, CircleBtn, SquareBtn, BlackColorBtn, BlueColorBtn, RedColorBtn, GreenColorBtn, YellowColorBtn, MagentaColorBtn, PinkColorBtn, OrangeColorBtn, LBColorBtn]

selected = SelectedBtn(70, 230, root)

# Texto de la interfaz

font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 36)

toolbarTxt = font.render("TOOLBAR", True, (0, 0, 0))
toolbarTxtRect = toolbarTxt.get_rect(center=(133, 200))

colorsTxt = font.render("COLORS", True, (0, 0, 0))
colorsTxtRect = colorsTxt.get_rect(center=(133, 400))

# Bucle principal del programa

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if uploadBtn.pressed():
        Eng.uploadImg()
    if saveBtn.pressed():
        print("Save presionado")
    if BrushBtn.pressed():
        Eng.editorModeSelect("Brush")
        selected.changePos(70, 230)
    if EraserBtn.pressed():
        Eng.editorModeSelect("Eraser")
        selected.changePos(150, 230)
    if CircleBtn.pressed():
        Eng.editorModeSelect("Circle")
        selected.changePos(70, 300)

    root.fill((223, 223, 229))

    nav_rect = pygame.Rect(0, 0, 1200, 150)
    pygame.draw.rect(root, (255, 255, 255), nav_rect)

    root.blit(logoImg, (970, -30))
    root.blit(toolbarTxt, toolbarTxtRect)
    root.blit(colorsTxt, colorsTxtRect)

    Eng.createMat(root)
    Eng.drawOverMat()

    selected.drawRect()

    EraserBtn.draw()
    BrushBtn.draw()
    CircleBtn.draw()
    SquareBtn.draw()
    saveBtn.draw()
    uploadBtn.draw()
    BlackColorBtn.draw()
    BlueColorBtn.draw()
    RedColorBtn.draw()
    GreenColorBtn.draw()
    YellowColorBtn.draw()
    MagentaColorBtn.draw()
    PinkColorBtn.draw()
    OrangeColorBtn.draw()
    LBColorBtn.draw()

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

pygame.quit()