import pygame

pygame.init()

screen = pygame.display.set_mode((640,140))
clock = pygame.time.Clock()
#sound = pygame.mixer.Sound('clank.wav')
#sound.play()
running = True

goku_img = pygame.image.load('imgs/goku-still.png').convert()
goku_img = pygame.transform.scale(goku_img, (goku_img.get_width() *0.4,goku_img.get_height() *0.4))

goku_img.set_colorkey((255,0,255,255))

font = pygame.font.Font(None, size=30)
moving = False

#gokus = pygame.Surface((64,64), pygame.SRCALPHA)
#gokus.blit(goku_img, (0,0))
#gokus.blit(goku_img, (20,0))
#gokus.blit(goku_img, (10,0))



x = 0

delta_time = 0.1

while running:
    screen.fill((255,255,255))

    goku_img.set_alpha(max(0, 255, - x))
    screen.blit(goku_img, (x,30))
    #x += 50 * delta_time

    # Objetos
    hitbox = pygame.Rect(x, 30, goku_img.get_width(),goku_img.get_height())
    mpos = pygame.mouse.get_pos()

    target = pygame.Rect(300,0,160,280)
    collision = hitbox.colliderect(target)
    # mouse
    mouse_collision = target.collidepoint(mpos)
    pygame.draw.rect(screen, (255 * collision,255 *mouse_collision,0), target)
    # mouse

    text = font.render('Hello World!', True, (0,0,0))
    screen.blit(text, (300,100))

    if moving:
        x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving = False
    pygame.display.flip()
    delta_time = clock.tick(60) /1000
    delta_time = max(0.001, min(0.1, delta_time))
pygame.quit()