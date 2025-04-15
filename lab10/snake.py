import pygame
import random
import psycopg2
from color_palette import *

# PostgreSQL setup
def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="snake",
        user="postgres",
        password="timunja07"
    )

def get_user_id(username):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id

def load_progress(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level 
                FROM user_score 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            row = cur.fetchone()
            return row if row else (0, 1)

def save_progress(user_id, score, level):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
            conn.commit()

# User setup
USERNAME = input("Enter your username: ")
USER_ID = get_user_id(USERNAME)
saved_score, saved_level = load_progress(USER_ID)

# Game setup
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL = 30
COLS, ROWS = WIDTH // CELL, HEIGHT // CELL
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Draw grid
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(COLS):
        for j in range(ROWS):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = Point(self.body[i - 1].x, self.body[i - 1].y)
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(self.body[-1].x, self.body[-1].y))
            return True
        return False

    def check_wall_collision(self):
        head = self.body[0]
        if head.x < 0 or head.x >= COLS or head.y < 0 or head.y >= ROWS:
            return True
        return any(head.x == segment.x and head.y == segment.y for segment in self.body[1:])

class Food:
    def __init__(self, snake_body):
        self.pos = self.generate_new_position(snake_body)
        self.weight = random.randint(1, 3)
        self.timer = 200

    def generate_new_position(self, snake_body):
        while True:
            x, y = random.randint(0, COLS - 1), random.randint(0, ROWS - 1)
            if not any(segment.x == x and segment.y == y for segment in snake_body):
                return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def pause_game():
    save_progress(USER_ID, score, level)
    font = pygame.font.SysFont("Arial", 24)
    paused_text = font.render("Paused - Press C to Continue, Q to Quit", True, colorBLACK)
    while True:
        screen.fill(colorWHITE)
        screen.blit(paused_text, (WIDTH // 2 - paused_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(USER_ID, score, level)
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
                elif event.key == pygame.K_q:
                    save_progress(USER_ID, score, level)
                    pygame.quit()
                    exit()

FPS = 5 + (saved_level - 1) * 2
score, level = saved_score, saved_level
clock = pygame.time.Clock()
snake = Snake()
food = Food(snake.body)

game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress(USER_ID, score, level)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                pause_game()
            elif event.key == pygame.K_r and game_over:
                save_progress(USER_ID, score, level)
                snake = Snake()
                food = Food(snake.body)
                score, level, FPS = 0, 1, 5
                game_over = False
            elif event.key == pygame.K_ESCAPE:
                save_progress(USER_ID, score, level)
                running = False

    if not game_over:
        draw_grid_chess()
        snake.move()

        if snake.check_collision(food):
            score += food.weight
            if score % 5 == 0:
                level += 1
                FPS += 2
            food = Food(snake.body)

        food.timer -= 1
        if food.timer <= 0:
            food = Food(snake.body)

        if snake.check_wall_collision():
            game_over = True

        snake.draw()
        food.draw()

        font = pygame.font.SysFont("Arial", 24)
        screen.blit(font.render(f"Score: {score}", True, colorBLACK), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, colorBLACK), (10, 40))

    else:
        screen.fill(colorWHITE)
        font_big = pygame.font.SysFont("Arial", 48)
        game_over_text = font_big.render("GAME OVER", True, colorRED)
        font_small = pygame.font.SysFont("Arial", 32)
        score_text = font_small.render(f"Your Score: {score}", True, colorBLACK)
        restart_text = font_small.render("Press R to Restart or ESC to Exit", True, colorBLACK)

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
