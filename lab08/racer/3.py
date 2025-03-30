import pygame
import random
import time

pygame.init()  # Initializes pygame

# Screen dimensions
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load assets
background = pygame.image.load('resources/AnimatedStreet.png')
player_img = pygame.image.load('resources/Player.png')
enemy_img = pygame.image.load('resources/Enemy.png')
coin_img = pygame.image.load('resources/Coin.png')  # New coin image
coin_img = pygame.transform.scale(coin_img, (50, 30))

# Load sounds
background_music = pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')
coin_sound = pygame.mixer.Sound('resources/coin.wav')  # New coin sound

# Fonts
font = pygame.font.SysFont("Verdana", 60)
score_font = pygame.font.SysFont("Verdana", 30)  # Font for score display
game_over = font.render("Game Over", True, "black")

# Start background music
pygame.mixer.music.play(-1)

# Constants
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 5  # Coin falls down like enemy
COIN_SPAWN_RATE = 100  # Lower = more frequent

# Score tracker
collected_coins = 0

# Clock
clock = pygame.time.Clock()


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)

        # Keep player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h  # Starts above the screen


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = -self.rect.h  # Starts above the screen

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.kill()  # Remove coin when it goes off-screen


# Create player and enemy objects
player = Player()
enemy = Enemy()

# Sprite groups
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn coins at random intervals
    if random.randint(1, COIN_SPAWN_RATE) == 1:
        new_coin = Coin()
        all_sprites.add(new_coin)
        coin_sprites.add(new_coin)

    # Move player, enemy, and coins
    player.move()
    enemy.move()
    for coin in coin_sprites:
        coin.move()

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Check for collisions with enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)

        screen.fill("red")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)

        pygame.display.flip()
        time.sleep(2)
        running = False

    # Check for coin collection
    collected = pygame.sprite.spritecollide(player, coin_sprites, True)
    if collected:
        collected_coins += len(collected)
        coin_sound.play()  # Play coin sound

    # Display collected coins
    score_text = score_font.render(f"Coins: {collected_coins}", True, "black")
    screen.blit(score_text, (WIDTH - 120, 20))

    pygame.display.flip()  # Update the screen
    clock.tick(FPS)  # Maintain FPS

pygame.quit()
