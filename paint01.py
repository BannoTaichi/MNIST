import pygame

pygame.init()
W, H = 600, 400
win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
win.fill((255, 255, 255))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(60)
