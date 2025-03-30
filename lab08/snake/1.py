import pygame
import random
from color_palette import *

pygame.init()

# Размеры окна
WIDTH = 600
HEIGHT = 600

# Создаём экран игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Размер клетки
CELL = 30

# Количество клеток по горизонтали и вертикали
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL

# Функция отрисовки шахматной сетки
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(COLS):
        for j in range(ROWS):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки (координаты элемента змеи или еды)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # направление по X
        self.dy = 0  # направление по Y

    def move(self):
        # Сохраняем предыдущие позиции сегментов тела
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Двигаем голову змеи
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        # Рисуем голову змеи
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        # Рисуем тело змеи
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        # Если голова змеи совпала с едой
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            # Добавляем новый сегмент в хвост змеи, чтобы не было самопоедания
            tail = self.body[-1]
            self.body.append(Point(tail.x, tail.y))
            return True
        return False

    def check_wall_collision(self):
        head = self.body[0]
        # Проверка выхода за пределы поля
        if head.x < 0 or head.x >= COLS or head.y < 0 or head.y >= ROWS:
            print("Hit the wall!")
            return True
        # Проверка столкновения с телом змеи
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                print("Hit itself!")
                return True
        return False

# Класс еды
class Food:
    def __init__(self, snake_body):
        self.pos = self.generate_new_position(snake_body)

    def generate_new_position(self, snake_body):
        while True:
            x = random.randint(0, COLS - 1)
            y = random.randint(0, ROWS - 1)
            # Проверка, не попала ли еда на тело змеи
            is_on_snake = any(segment.x == x and segment.y == y for segment in snake_body)
            if not is_on_snake:
                return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# Параметры игры
FPS = 5  # начальная скорость
clock = pygame.time.Clock()

# Объекты игры
snake = Snake()
food = Food(snake.body)

# Счёт и уровень
score = 0
level = 1

# Флаги состояния игры
running = True
game_over = False

# Игровой цикл
while running:
    # Обработка событий (нажатия клавиш, выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Управление направлением змеи
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    if not game_over:
        # Отрисовываем поле
        draw_grid_chess()

        # Двигаем змею
        snake.move()

        # Проверка съедания еды
        if snake.check_collision(food):
            score += 1
            # Увеличиваем уровень каждые 3 очка
            if score % 3 == 0:
                level += 1
                FPS += 2  # увеличиваем скорость игры
                print(f"LEVEL UP! New Level: {level}")

            # Генерация новой еды
            food = Food(snake.body)

        # Проверка на столкновение со стеной или с собой
        if snake.check_wall_collision():
            game_over = True

        # Отрисовываем змею и еду
        snake.draw()
        food.draw()

        # Отображаем счёт и уровень
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, colorBLACK)
        level_text = font.render(f"Level: {level}", True, colorBLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

    else:
        # Выводим сообщение об окончании игры
        screen.fill(colorWHITE)
        font_big = pygame.font.SysFont("Arial", 48)
        game_over_text = font_big.render("GAME OVER", True, colorRED)
        font_small = pygame.font.SysFont("Arial", 32)
        score_text = font_small.render(f"Your Score: {score}", True, colorBLACK)
        restart_text = font_small.render("Press R to Restart or ESC to Exit", True, colorBLACK)

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

        # Обработка кнопок рестарта и выхода
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Перезапускаем игру
            snake = Snake()
            food = Food(snake.body)
            score = 0
            level = 1
            FPS = 5
            game_over = False
        if keys[pygame.K_ESCAPE]:
            running = False

    # Обновляем экран
    pygame.display.flip()
    # Контролируем FPS
    clock.tick(FPS)

# Выход из игры
pygame.quit()