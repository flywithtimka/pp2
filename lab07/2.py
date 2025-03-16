import pygame
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

playlist = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3"
]

current_song_index = 0
is_playing = False

def play_song():
    global is_playing
    try:
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()
        is_playing = True
        print(f"Plays: {playlist[current_song_index]}")
    except Exception as e:
        print(f"error: {e}")

def stop_song():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    print("Stopped")

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_song()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play_song()

clock = pygame.time.Clock()
FPS = 30

running = True
while running:
    screen.fill(BLACK) 

    instructions = [
        "Space: Play/Pause",
        "N: Next song",
        "P: Previous song",
        "S: Stop",
    ]

    for i, text in enumerate(instructions):
        label = font.render(text, True, WHITE)
        screen.blit(label, (20, 20 + i * 40))

    if len(playlist) > 0:
        song_label = font.render(f"Now: {playlist[current_song_index]}", True, WHITE)
        screen.blit(song_label, (20, HEIGHT - 60))
    else:
        no_song_label = font.render("No songs loaded!", True, WHITE)
        screen.blit(no_song_label, (20, HEIGHT - 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_playing:
                    play_song()
                else:
                    pygame.mixer.music.pause()
                    is_playing = False
                    print("Пауза")

            if event.key == pygame.K_s:
                stop_song()

            if event.key == pygame.K_n:
                next_song()

            if event.key == pygame.K_p:
                prev_song()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
