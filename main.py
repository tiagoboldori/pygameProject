import random
import sys
import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 280)

uNumber = 15
uSize = 30

screen = pygame.display.set_mode((uSize * uNumber, uSize * uNumber))

powerup = pygame.mixer.Sound('powerup.mp3')

class FOOD(pygame.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(0, uNumber-1)
        self.y = random.randint(0, uNumber-1)
        self.pos = pygame.math.Vector2(self.x * uSize, self.y * uSize)
        pygame.sprite.Sprite.__init__(self, frutaGroup)

    def drawfood(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, uSize, uSize)
        pygame.draw.rect(screen, (125, 0, 0), fruit_rect)


class SNAKEBODY(pygame.sprite.Sprite):
    def __init__(self):
        self.x = -1
        self.y = -1
        self.pos = pygame.math.Vector2(self.x * uSize, self.y * uSize)
        pygame.sprite.Sprite.__init__(self, cobraGroup)
        self.posOld = 0

    def drawbody(self):
        body_rect = pygame.Rect(self.pos.x, self.pos.y, uSize, uSize)
        pygame.draw.rect(screen, (0, 125, 0), body_rect)


class SNAKE(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 10
        self.y = 10
        self.direction = 1
        self.pos = pygame.math.Vector2(self.x * uSize, self.y * uSize)
        pygame.sprite.Sprite.__init__(self, cabecaGroup)
        self.posOld = 0
        snake_rect = pygame.Rect(self.pos.x, self.pos.y, uSize, uSize)

    def drawsnake(self):
        snake_rect = pygame.Rect(self.pos.x, self.pos.y, uSize, uSize)
        pygame.draw.rect(screen, (0, 105, 0), snake_rect)


direction = 1
cont = 0
aux = []

cobraGroup = pygame.sprite.Group()
frutaGroup = pygame.sprite.Group()
cabecaGroup = pygame.sprite.Group()

fruta = FOOD()
frutaGroup.add(fruta)

corpo = SNAKEBODY()
cobraGroup.add(corpo)


cobra = SNAKE()
cabecaGroup.add(cobra)

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.USEREVENT:

            if direction == 1:
                cobra.posOld = pygame.math.Vector2(cobra.pos)
                cobra.pos.y -= 30

            if direction == 2:
                cobra.posOld = pygame.math.Vector2(cobra.pos)
                cobra.pos.y += 30

            if direction == 3:
                cobra.posOld = pygame.math.Vector2(cobra.pos)
                cobra.pos.x -= 30

            if direction == 4:
                cobra.posOld = pygame.math.Vector2(cobra.pos)
                cobra.pos.x += 30

            for b in range(len(cobraGroup)):
                if b == 0:
                    corpo.posOld = pygame.math.Vector2(corpo.pos)
                    corpo.pos = cobra.posOld
                if b > 0:
                    cobraGroup.sprites()[b].posOld = pygame.math.Vector2(cobraGroup.sprites()[b].pos)
                    cobraGroup.sprites()[b].pos = pygame.math.Vector2(cobraGroup.sprites()[b-1].posOld)
                    print(cobraGroup.sprites()[b])

        if pygame.Rect.colliderect(pygame.Rect(cobra.pos.x, cobra.pos.y, uSize, uSize), pygame.Rect(fruta.pos.x,fruta.pos.y, uSize,uSize)):
            cobraGroup.add(SNAKEBODY())
            fruta.pos.x = random.randint(0, uNumber-1)*uSize
            fruta.pos.y = random.randint(0, uNumber-1)*uSize
            pygame.mixer.Sound.play(powerup)

        for i in cobraGroup.sprites():
            if pygame.Rect.colliderect(pygame.Rect(cobra.pos.x, cobra.pos.y, uSize, uSize), pygame.Rect(i.pos.x,i.pos.y, uSize,uSize)):
                pygame.quit()

    # movement direction
    if keys[pygame.K_w]:
        if direction != 2:
            direction = 1

    if keys[pygame.K_s]:
        if direction != 1:
            direction = 2

    if keys[pygame.K_a]:
        if direction != 4:
            direction = 3

    if keys[pygame.K_d]:
        if direction != 3:
            direction = 4

    screen.fill((150, 180, 70))

    fruta.drawfood()
    cobra.drawsnake()
    corpo.drawbody()
    for i in cobraGroup.sprites():
        i.drawbody()

    pygame.display.update()

    clock.tick(60)
