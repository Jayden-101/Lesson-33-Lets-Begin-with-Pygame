import pygame

pygame.init()

screen_w, screen_l = 500,500

screen = pygame.display.set_mode((screen_w, screen_l))

pygame.display.set_caption("My First Game Screen")


penguin_image = pygame.transform.scale(pygame.image.load('Penguin.png').convert_alpha(), (300,300))

penguin_rect = penguin_image.get_rect(center=(screen_l // 2, screen_w // 2))

background_color = (58, 58, 58)

running = True

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    screen.blit(background_color, (0, 0))
    screen.blit(penguin_image, penguin_rect)

    pygame.display.flip()
