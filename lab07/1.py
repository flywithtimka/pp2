import pygame
import time
import math
pygame.init()
clock_face = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")
clock_width, clock_height = clock_face.get_size()
center = (clock_width // 2, clock_height // 2)
screen = pygame.display.set_mode((clock_width, clock_height))
pygame.display.set_caption("Mickey Clock")
def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=pos).center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

     
    sec_angle = -seconds * 6   
    min_angle = -minutes * 6   

     
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    
     
    blit_rotate_center(screen, second_hand, center, sec_angle)
    blit_rotate_center(screen, minute_hand, center, min_angle)
    
    pygame.display.flip()
    pygame.time.delay(1000)   

pygame.quit()
