import sys
import pygame

def display_score():
    current_time = int(pygame.time.get_ticks() / 250) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(320, 45))
    screen.blit(score_surface, score_rect)
    return current_time

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

#score_surface = test_font.render('Score', False, "Black")
#score_rect = score_surface.get_rect(center=(320, 45))


snail_surface = pygame.image.load("snail1.png").convert_alpha()
snail_scaled_surface = pygame.transform.scale_by(snail_surface, 0.7)
snail_rect = snail_scaled_surface.get_rect(midbottom=(600, 250))

player_surface = pygame.image.load("player_stand.png").convert_alpha()
player_scaled_surface = pygame.transform.scale_by(player_surface, 0.7)
player_rect = player_scaled_surface.get_rect(midbottom=(50, 250))
second_player_scaled_surface = pygame.transform.scale_by(player_surface, 1)
second_player_rect = second_player_scaled_surface.get_rect(center=(320, 150))
player_gravity = 0

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
                    snail_rect.left = 640
                    player_rect.right = 10
                    start_time = int(pygame.time.get_ticks() / 250)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom >= 250:
                    player_gravity = - 17

    if game_active:
        screen.blit(sky_scaled_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))
        #screen.blit(score_surface, score_rect)
        screen.blit(snail_scaled_surface, snail_rect)
        screen.blit(player_scaled_surface, player_rect)
        score = display_score()


        snail_rect.right -= 3

        if snail_rect.right < 0:
            snail_rect.left = 640

        if snail_rect.colliderect(player_rect):
            game_active = False

        player_rect.right += 2
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.left > 640:
            player_rect.right = 0
        if player_rect.bottom >= 250:
            player_rect.bottom = 250

    else:
        screen.fill("#619182")
        screen.blit(second_player_scaled_surface, second_player_rect)
        screen.blit(menu_font_surface, menu_font_rect)
        score_menu = test_font.render(f'Your score is: {score}', False, (70, 104, 93))
        score_menu_rect = score_menu.get_rect(center=(320, 285))
        if score == 0:
            screen.blit(menu_font_surface, menu_font_rect)
        else:
            screen.blit(score_menu, score_menu_rect)

    pygame.display.update()
    clock.tick(60)
