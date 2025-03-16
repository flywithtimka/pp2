import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

RADIUS = 25
circle_x = WIDTH // 2
circle_y = HEIGHT // 2

MOVE_SPEED = 20

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(WHITE) 

    pygame.draw.circle(screen, RED, (circle_x, circle_y), RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if circle_x - RADIUS - MOVE_SPEED >= 0:
            circle_x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        if circle_x + RADIUS + MOVE_SPEED <= WIDTH:
            circle_x += MOVE_SPEED
    if keys[pygame.K_UP]:
        if circle_y - RADIUS - MOVE_SPEED >= 0:
            circle_y -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        if circle_y + RADIUS + MOVE_SPEED <= HEIGHT:
            circle_y += MOVE_SPEED

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()