import pygame
from engine import Engine, Button

pygame.init()

Eng = Engine()
icon = pygame.image.load("assets/images/brush.png")
root = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Paintxel")
pygame.display.set_icon(icon)
root.fill((223, 223, 229))

# --> Elementos de la interfaz gráfica

nav_rect = pygame.Rect(0, 0, 1200, 150)
pygame.draw.rect(root, (255, 255, 255), nav_rect)

# Cargar y mostrar imágenes

logoImg = pygame.image.load("assets/images/logopaint.png")
logoImg = pygame.transform.scale(logoImg, (200, 200))
root.blit(logoImg, (970, -30))

uploadImg = pygame.image.load("assets/images/Upload.png")
saveImg = pygame.image.load("assets/images/Save.png")

# Crear objetos botón

uploadBtn = Button(30, 50, uploadImg, root)
uploadBtn.draw()
saveBtn = Button(100, 50, saveImg, root)
saveBtn.draw()

# Crear la matriz dentro de la UI

Eng.createMat(root)

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

    Eng.drawOverMat()

    pygame.display.update()

pygame.quit()