import pygame

pygame.init()
W, H = 600, 400
win = pygame.display.set_mode((W, H))
drawing = False
eraser = False
clock = pygame.time.Clock()
win.fill((255, 255, 255))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if e.type == pygame.MOUSEBUTTONUP:
            drawing = False
        # 『e』のキーボードで消しゴム切り替え
        if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
            eraser = not eraser
        # 『c』のキーボードで全クリア
        if e.type == pygame.KEYDOWN and e.key == pygame.K_c:
            win.fill((255, 255, 255))

    if drawing:
        pygame.draw.circle(
            win,
            (255, 255, 255) if eraser else (0, 0, 0),
            pygame.mouse.get_pos(),
            4 if eraser else 2,
        )
    pygame.display.flip()
    clock.tick(60)
