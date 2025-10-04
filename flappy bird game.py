import pygame
import random

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird settings
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 20
bird_vel =0   
gravity = 0.5
jump_strength =-6
 

# Pipe settings
pipe_width = 60
pipe_gap = 300
pipe_vel = 3
pipes = []
score = 0

font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()
run = True

def add_pipe():
    top_height = random.randint(50, HEIGHT - pipe_gap - 50)
    pipes.append([WIDTH, top_height])

add_pipe()

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = jump_strength

    # Bird movement
    bird_vel += gravity
    bird_y += bird_vel

    # Pipe movement
    for pipe in pipes:
        pipe[0] -= pipe_vel

    # Add new pipes
    if pipes[-1][0] < WIDTH // 2:
        add_pipe()

    # Remove off-screen pipes
    if pipes[0][0] < -pipe_width:
        pipes.pop(0)
        score += 1

    # Collision detection
    for pipe in pipes:
        pipe_x = pipe[0]
        top_height = pipe[1]
        if (bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width):
            if bird_y - bird_radius < top_height or bird_y + bird_radius > top_height + pipe_gap:
                run = False

    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        run = False

    # Drawing
    win.fill((135, 206, 235))  # Sky blue
    pygame.draw.circle(win, (255, 255, 0), (bird_x, int(bird_y)), bird_radius)  # Bird

    for pipe in pipes:
        pipe_x = pipe[0]
        top_height = pipe[1]
        pygame.draw.rect(win, (34, 139, 34), (pipe_x, 0, pipe_width, top_height))  # Top pipe
        pygame.draw.rect(win, (34, 139, 34), (pipe_x, top_height + pipe_gap, pipe_width, HEIGHT - top_height - pipe_gap))  # Bottom pipe

    score_text = font.render(str(score), True, (255, 255, 255))
    win.blit(score_text, (WIDTH // 2, 20))

    pygame.display.update()
    
pygame.quit()