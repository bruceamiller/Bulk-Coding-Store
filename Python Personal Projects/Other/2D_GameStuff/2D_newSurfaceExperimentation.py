import pygame, sys

""" SCREEN CODE """
SCREEN_WIDTH, SCREEN_HEIGHT = 2500, 1200
FPS = 60
SCREEN_BUFFER = 500


pygameKeyValues = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_1, pygame.K_2, pygame.K_3]
inputNames = ("moveUp", "moveLeft", "moveDown", "moveRight", "equip1", "equip2", "equip3")
isCurrentInputs = [False for i in range(len(pygameKeyValues))]

gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("newSurfaceExperimentation")
clock = pygame.time.Clock()



playerSurface = pygame.Surface((50, 50))
playerSurface.fill((255, 255, 255))
gameWindow.blit(playerSurface, (0, 0))


while True:
    for event in pygame.event.get():
        """ CLOSE BUTTON """
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)