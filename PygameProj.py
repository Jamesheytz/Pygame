import sys

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 350))
pygame.display.set_caption("Slime")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Font.ttf", 25)

sky_surface = pygame.image.load("background.png").convert()
sky_scaled_surface = pygame.transform.scale_by(sky_surface, 0.8)
ground_surface = pygame.image.load("ground.png").convert_alpha()
score_surface = test_font.render('Score', False, "Black")
score_rect = score_surface.get_rect(center=(320, 45))


snail_surface = pygame.image.load("snail1.png").convert_alpha()
snail_scaled_surface = pygame.transform.scale_by(snail_surface, 0.7)
snail_rect = snail_scaled_surface.get_rect(midbottom=(600, 250))

player_surface = pygame.image.load("player_stand.png").convert_alpha()
player_scaled_surface = pygame.transform.scale_by(player_surface, 0.7)
player_rect = player_scaled_surface.get_rect(midbottom=(50, 250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("BOOM!")

    # Slime functions
    if snail_rect.right < 0:
        snail_rect.left = 640

    # Player functions
    if player_rect.left > 640:
        player_rect.right = 0
    if player_rect.colliderect(snail_rect):
        print("CRASH!")

    screen.blit(sky_scaled_surface, (0, 0))
    screen.blit(snail_scaled_surface, snail_rect)
    screen.blit(player_scaled_surface, player_rect)
    screen.blit(ground_surface, (0, 250))
    screen.blit(score_surface, score_rect)
    snail_rect.right -= 3
    player_rect.right += 2

    pygame.display.update()
    clock.tick(60)
