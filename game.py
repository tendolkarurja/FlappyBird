import pygame
pygame.init()

screen = pygame.display.set_mode((600, 780))
time = pygame.time.Clock()
running = True

bg = pygame.image.load('flappy/bkg_day.png').convert_alpha()
bg = pygame.transform.scale(bg, (600, 780))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("blue")
    
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    time.tick(60)
pygame.quit()