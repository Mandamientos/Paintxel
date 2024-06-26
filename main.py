from menus import mainMenu

mainMenu()



"""
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
asciiImg = pygame.image.load("assets/images/ascii.png")
numMatImg = pygame.image.load("assets/images/num_mat.png")
rotateLeftImg = pygame.image.load("assets/images/rotateleft.png")
rotateRightImg = pygame.image.load("assets/images/rotateright.png")
reflectionAxisYImg = pygame.image.load("assets/images/axisy.png")
reflectionAxisXImg = pygame.image.load("assets/images/axisx.png")
crossImg = pygame.image.load("assets/images/cross.png")
negativeImg = pygame.image.load("assets/images/negative.png")
highContrImg = pygame.image.load("assets/images/highcontrast.png")

# Crear objetos botón

uploadBtn = Button(30, 50, uploadImg, root, 50, 50)
saveBtn = Button(100, 50, saveImg, root, 50, 50)
crossBtn = Button(170, 50, crossImg, root, 50, 50)
BrushBtn = Button(70, 230, icon, root, 50, 50)
EraserBtn = Button(150, 230, eraserImg, root, 50, 50)
CircleBtn = Button(70, 300, CircleImg, root, 50, 50)
SquareBtn = Button(150, 300, squareImg, root, 50, 50)
BlackColorBtn = Button(65, 450, blackColorImg, root, 50, 50)
BlueColorBtn = Button(150, 450, blueColorImg, root, 50, 50)
RedColorBtn = Button(65, 520, redColorImg, root, 50, 50)
GreenColorBtn = Button(150, 520, greenColorImg, root, 50, 50)
YellowColorBtn = Button(65, 590, yellowColorImg, root, 50, 50)
MagentaColorBtn = Button(150, 590, magentaColorImg, root, 50, 50)
PinkColorBtn = Button(65, 660, pinkColorImg, root, 50, 50)
OrangeColorBtn = Button(150, 660, orangeColorImg, root, 50, 50)
LBColorBtn = Button(105, 730, LBColorImg, root, 50, 50)
AscBtn = Button(300, 30, asciiImg, root, 100, 100)
NumMat = Button(450, 30, numMatImg, root, 100, 100)
RotateLeft = Button(990, 230, rotateLeftImg, root, 50, 50)
RotateRight = Button(1060, 230, rotateRightImg, root, 50, 50)
ReflectionAxisY = Button(950, 350, reflectionAxisYImg, root, 70, 70)
ReflectionAxisX = Button(1080, 350, reflectionAxisXImg, root, 70, 70)
negativeBtn = Button(957, 500, negativeImg, root, 180, 40)
highContrBtn = Button(957, 570, highContrImg, root, 180, 80)

buttonList = [uploadBtn, saveBtn, BrushBtn, EraserBtn, CircleBtn, SquareBtn, BlackColorBtn, BlueColorBtn, RedColorBtn, GreenColorBtn, YellowColorBtn, MagentaColorBtn, PinkColorBtn, OrangeColorBtn, LBColorBtn, AscBtn, NumMat, RotateLeft, RotateRight, ReflectionAxisY, ReflectionAxisX, crossBtn, negativeBtn, highContrBtn]

selected = SelectedBtn(70, 230, root)

# Texto de la interfaz

font = pygame.font.Font("fonts/PixelifySans-VariableFont_wght.ttf", 36)

toolbarTxt = font.render("TOOLBAR", True, (0, 0, 0))
toolbarTxtRect = toolbarTxt.get_rect(center=(133, 200))

colorsTxt = font.render("COLORS", True, (0, 0, 0))
colorsTxtRect = colorsTxt.get_rect(center=(133, 400))

rotateTxt = font.render("ROTATE", True, (0, 0, 0))
rotateTxtRect = rotateTxt.get_rect(center=(1050, 200))

reflectionsTxt = font.render("REFLECTIONS", True, (0, 0, 0))
reflectionsTxtRect = reflectionsTxt.get_rect(center=(1050, 320))

othersTxt = font.render("OTHERS", True, (0, 0, 0))
othersTxtRect = reflectionsTxt.get_rect(center=(1095, 450))

# Bucle principal del programa

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    root.fill((223, 223, 229))

    nav_rect = pygame.Rect(0, 0, 1200, 150)
    pygame.draw.rect(root, (255, 255, 255), nav_rect)

    root.blit(logoImg, (970, -30))
    root.blit(toolbarTxt, toolbarTxtRect)
    root.blit(colorsTxt, colorsTxtRect)
    root.blit(rotateTxt, rotateTxtRect)
    root.blit(reflectionsTxt, reflectionsTxtRect)
    root.blit(othersTxt, othersTxtRect)

    Eng.createMat(root)
    Eng.drawOverMat()
    Eng.eraseOverMat()

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
    AscBtn.draw()
    NumMat.draw()
    RotateLeft.draw()
    RotateRight.draw()
    ReflectionAxisY.draw()
    ReflectionAxisX.draw()
    crossBtn.draw()
    negativeBtn.draw()
    highContrBtn.draw()

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

"""