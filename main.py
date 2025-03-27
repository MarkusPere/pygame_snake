import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

x, y = 100, 100
dx, dy = 20, 0

snake_body = [(x, y)]
snake_length = 1

def generate_food():
    random_nums = list(range(20, 580 + 1, 20))
    a = random.choice(random_nums)
    b = random.choice(random_nums)
    return a, b

a, b = generate_food()

score = 0
font = pygame.font.SysFont('arial', 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -20
            if event.key == pygame.K_DOWN:
                dx, dy = 0, 20
            if event.key == pygame.K_LEFT:
                dx, dy = -20, 0
            if event.key == pygame.K_RIGHT:
                dx, dy = 20, 0

    x += dx
    y += dy

    snake_body.insert(0, (x, y))
    if len(snake_body) > snake_length:
        snake_body.pop()

    if x == a and y == b:
        score += 1
        snake_length += 1
        a, b = generate_food()

    if (x, y) in snake_body[1:]:
        running = False
    if x < 0 or x > 580 or y < 0 or y > 580:
        running = False

    screen.fill((255, 255, 255))

    for segment in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 20, 20))

    pygame.draw.rect(screen, (255, 0, 0), (a, b, 20, 20))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(10)

pygame.quit()