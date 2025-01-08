import pygame, pygame.sprite 

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
       pygame.sprite.Sprite.__init__(self)
       self.cur_idx = 0
       self.ct = 0
       self.images = [pygame.image.load('ymid.png'), pygame.image.load('yhigh.png'), pygame.image.load('ydown.png')]
       self.image = self.images[self.cur_idx]
       self.rect = self.image.get_rect()
       self.rect.center = [x, y]
    
    def update(self):
        self.ct += 1
        flap_cooldown = 3
        
        if self.ct > flap_cooldown:
            self.ct = 0
            if self.cur_idx == 2:
                self.cur_idx = 0
            else:
                self.cur_idx += 1
        self.image = self.images[self.cur_idx]

pygame.init()

screen = pygame.display.set_mode((455, 780))
time = pygame.time.Clock()
move_gnd = 0
move_speed = 2.5
running = True

bg = pygame.image.load('bkg_day.png').convert_alpha()
gnd = pygame.image.load('ground.png').convert_alpha()

bg = pygame.transform.scale(bg, (455, 660))
gnd = pygame.transform.scale(gnd, (470, 130))

width = bg.get_width()

group = pygame.sprite.Group()
bird = Bird(50, 390)

group.add(bird)


while running:
    screen.blit(bg, (0, 0))
    group.draw(screen)
    group.update()
    screen.blit(gnd,(move_gnd, 650))
    screen.blit(gnd, (move_gnd + width, 650))    
    time.tick(60)
    
    move_gnd -= move_speed
    if move_gnd <= -width:
        move_gnd = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("blue")
    
    
    pygame.display.update()
pygame.quit()
