import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooting Game")

# Player settings
player_img = pygame.Surface((20, 20))
player_img.fill((0, 255, 255))
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 70
player_speed = 6

# Bullet settings
bullet_img = pygame.Surface((5, 15))
bullet_img.fill((255, 255, 0))
bullets = []

# Alien settings
alien_img = pygame.Surface((40, 40))
alien_img.fill((0, 255, 0))  # Green for aliens
aliens = []
alien_speed = 3
for _ in range(8):  # More aliens
    x = random.randint(0, WIDTH - 40)
    y = random.randint(-600, -40)
    aliens.append([x, y])

score = 0
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
run = True
game_over = False

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + 22, player_y])

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
            player_x += player_speed

        # Move bullets
        for bullet in bullets[:]:
            bullet[1] -= 10
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Move aliens
        for alien in aliens:
            alien[1] += alien_speed
            if alien[1] > HEIGHT:
                alien[0] = random.randint(0, WIDTH - 40)
                alien[1] = random.randint(-600, -40)

        # Bullet-alien collision
        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 15)
            for alien in aliens:
                alien_rect = pygame.Rect(alien[0], alien[1], 40, 40)
                if bullet_rect.colliderect(alien_rect):
                    bullets.remove(bullet)
                    alien[0] = random.randint(0, WIDTH - 40)
                    alien[1] = random.randint(-600, -40)
                    score += 1

        # Alien-player collision
        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        for alien in aliens:
            alien_rect = pygame.Rect(alien[0], alien[1], 40, 40)
            if player_rect.colliderect(alien_rect):
                game_over = True
  
    win.fill((10, 10, 30))
    win.blit(player_img, (player_x, player_y))
    for bullet in bullets:
        win.blit(bullet_img, (bullet[0], bullet[1]))
    for alien in aliens:
        win.blit(alien_img, (alien[0], alien[1]))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("Game Over!", True, (255, 0, 0))
        win.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))

    pygame.display.update()

pygame.quit()