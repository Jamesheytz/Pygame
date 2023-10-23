import sys
import pygame
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 250) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(320, 45))
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 250:
                screen.blit(snail_scaled_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


pygame.init()
screen = pygame.display.set_mode((640, 350))
pygame.display.set_caption("Slime")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Font.ttf", 25)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load("background.png").convert()
sky_scaled_surface = pygame.transform.scale_by(sky_surface, 0.8)
ground_surface = pygame.image.load("ground.png").convert_alpha()
menu_font_surface = test_font.render("Press Space bar to Start", False, (70, 104, 93))
menu_font_rect = menu_font_surface.get_rect(center=(320, 250))

snail_surface = pygame.image.load("snail1.png")
snail_scaled_surface = pygame.transform.scale_by(snail_surface, 0.7).convert_alpha()

fly_surface = pygame.image.load("fly.png")

obstacle_rect_list = []

player_surface = pygame.image.load("player_stand.png")
player_scaled_surface = pygame.transform.scale_by(player_surface, 0.7).convert_alpha()
player_rect = player_scaled_surface.get_rect(midbottom=(50, 250))
menu_player_scaled_surface = pygame.transform.scale_by(player_surface, 1)
menu_player_rect = menu_player_scaled_surface.get_rect(center=(320, 150))
player_gravity = 0

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    player_rect.right = 100
                    start_time = int(pygame.time.get_ticks() / 250)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom >= 250:
                    player_gravity = - 17

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_scaled_surface.get_rect(midbottom=(randint(640, 900), 250)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midbottom=(randint(640, 900), 160)))

    if game_active:

        screen.blit(sky_scaled_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))
        screen.blit(player_scaled_surface, player_rect)
        score = display_score()

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

# Player Functions
        player_rect.right += 0
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.left > 640:
            player_rect.right = 0
        if player_rect.bottom >= 250:
            player_rect.bottom = 250

    else:
        screen.fill("#619182")
        screen.blit(menu_player_scaled_surface, menu_player_rect)
        screen.blit(menu_font_surface, menu_font_rect)
        score_menu = test_font.render(f'Your score is: {score}', False, (70, 104, 93))
        score_menu_rect = score_menu.get_rect(center=(320, 285))

        if score == 0:
            screen.blit(menu_font_surface, menu_font_rect)
        else:
            screen.blit(score_menu, score_menu_rect)

    pygame.display.update()
    clock.tick(60)
