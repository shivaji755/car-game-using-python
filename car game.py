import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

car_img = pygame.Surface((50, 50))
car_img.fill((0, 255, 0))
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 120

obstacle_img = pygame.Surface((50, 100))
obstacle_img.fill((255, 0, 0))

obstacles = []
for _ in range(3):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(-600, -100)
    obstacles.append([x, y])

obstacle_speed = 5
clock = pygame.time.Clock()
run = True
score = 0
font = pygame.font.SysFont(None, 36)
game_over = False

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= 5
        if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
            car_x += 5

        for obs in obstacles:
            obs[1] += obstacle_speed
            if obs[1] > HEIGHT:
                obs[0] = random.randint(0, WIDTH - 50)
                obs[1] = random.randint(-600, -100)
                score += 1

        # Collision detection
        car_rect = pygame.Rect(car_x, car_y, 50, 100)
        for obs in obstacles:
            obstacle_rect = pygame.Rect(obs[0], obs[1], 50, 100)
            if car_rect.colliderect(obstacle_rect):
                game_over = True

    win.fill((255, 232, 0))
    win.blit(car_img, (car_x, car_y))
    for obs in obstacles:
        win.blit(obstacle_img, (obs[0], obs[1]))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("Game Over!", True, (255, 0, 0))
        win.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))

    pygame.display.update()

pygame.quit()