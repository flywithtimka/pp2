import pygame
import sys
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Program Extended")
clock = pygame.time.Clock()

# Default settings
radius = 5
color = (0, 0, 255)
tool = "line"  # 'line', 'rect', 'circle', 'square', 'triangle', 'rhombus', 'eraser'
drawing = False
start_pos = (0, 0)

def draw_rectangle(surface, start, end, color, thickness):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_square(surface, start, end, color, thickness):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surface, color, (start[0], start[1], side, side), thickness)

def draw_circle(surface, start, end, color, thickness):
    dx, dy = end[0] - start[0], end[1] - start[1]
    radius = int(math.sqrt(dx**2 + dy**2))
    pygame.draw.circle(surface, color, start, radius, thickness)

def draw_right_triangle(surface, start, end, color, thickness):
    points = [start, (start[0], end[1]), (end[0], end[1])]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_equilateral_triangle(surface, start, end, color, thickness):
    base = abs(end[0] - start[0])
    height = (math.sqrt(3) / 2) * base
    points = [start, (start[0] + base, start[1]), (start[0] + base // 2, start[1] - height)]
    pygame.draw.polygon(surface, color, points, thickness)

def draw_rhombus(surface, start, end, color, thickness):
    width, height = abs(end[0] - start[0]), abs(end[1] - start[1])
    points = [
        (start[0] + width // 2, start[1]),
        (start[0] + width, start[1] + height // 2),
        (start[0] + width // 2, start[1] + height),
        (start[0], start[1] + height // 2)
    ]
    pygame.draw.polygon(surface, color, points, thickness)

def main():
    global radius, color, tool, drawing, start_pos
    running = True
    screen.fill((255, 255, 255))  # White background

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                if event.key == pygame.K_g:
                    color = (0, 255, 0)
                if event.key == pygame.K_b:
                    color = (0, 0, 255)

                # Tool selection
                if event.key == pygame.K_1:
                    tool = "line"
                if event.key == pygame.K_2:
                    tool = "rect"
                if event.key == pygame.K_3:
                    tool = "circle"
                if event.key == pygame.K_4:
                    tool = "square"
                if event.key == pygame.K_5:
                    tool = "triangle"
                if event.key == pygame.K_6:
                    tool = "rhombus"
                if event.key == pygame.K_7:
                    tool = "eraser"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    drawing = True
                    start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos
                    if tool == "rect":
                        draw_rectangle(screen, start_pos, end_pos, color, radius)
                    if tool == "square":
                        draw_square(screen, start_pos, end_pos, color, radius)
                    if tool == "circle":
                        draw_circle(screen, start_pos, end_pos, color, radius)
                    if tool == "triangle":
                        draw_right_triangle(screen, start_pos, end_pos, color, radius)
                    if tool == "rhombus":
                        draw_rhombus(screen, start_pos, end_pos, color, radius)

            if event.type == pygame.MOUSEMOTION:
                if drawing and tool == "eraser":
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

main()