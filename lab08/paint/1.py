import pygame
import sys

# Инициализация
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Program Extended")
clock = pygame.time.Clock()

# Переменные по умолчанию
radius = 5
color = (0, 0, 255)
points = []
tool = "line"  # 'line', 'rect', 'circle', 'eraser'
drawing = False
start_pos = (0, 0)

def main():
    global radius, color, tool, drawing, start_pos, points

    running = True
    screen.fill((255, 255, 255))  # Белый фон

    while running:
        pressed = pygame.key.get_pressed()

        # Модификаторы
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_w and ctrl_held:
                    running = False
                if event.key == pygame.K_F4 and alt_held:
                    running = False

                # Выбор цвета
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                if event.key == pygame.K_g:
                    color = (0, 255, 0)
                if event.key == pygame.K_b:
                    color = (0, 0, 255)
                if event.key == pygame.K_p:
                    x, y = pygame.mouse.get_pos()
                    color = screen.get_at((x, y))[:3]

                # Выбор инструмента
                if event.key == pygame.K_1:
                    tool = "line"
                if event.key == pygame.K_2:
                    tool = "rect"
                if event.key == pygame.K_3:
                    tool = "circle"
                if event.key == pygame.K_4:
                    tool = "eraser"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    drawing = True
                    start_pos = event.pos
                    if tool == "line":
                        points.append(event.pos)
                elif event.button == 3:  # Правая кнопка
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = event.pos

                    # Прямоугольник и круг отрисовываются после отпускания ЛКМ
                    if tool == "rect":
                        draw_rectangle(screen, start_pos, end_pos, color, radius)
                    if tool == "circle":
                        draw_circle(screen, start_pos, end_pos, color, radius)

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_pos = event.pos

                    if tool == "line":
                        pygame.draw.line(screen, color, start_pos, current_pos, radius)
                        start_pos = current_pos

                    if tool == "eraser":
                        eraser_color = (255, 255, 255)
                        pygame.draw.circle(screen, eraser_color, current_pos, radius)

        # UI: текущий инструмент и цвет
        pygame.display.set_caption(f"Tool: {tool.upper()} | Color: {color} | Radius: {radius}")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def draw_rectangle(surface, start, end, color, thickness):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, thickness)

def draw_circle(surface, start, end, color, thickness):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    radius = int((dx ** 2 + dy ** 2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, thickness)

main()