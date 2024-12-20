import sys
import pygame
from pygame.locals import *
from utils import update_map, print_map

pygame.init()

WIDTH = 200
HEIGHT = 200
BACKGROUND = (150, 150, 150)
VELOCITY = 5
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("SLAM")


# robot info
robot_radius = 5
robot_x, robot_y = 100, 100
robot_rect = pygame.Rect(
        robot_x-robot_radius, robot_y-robot_radius, robot_radius*2, robot_radius*2
)

# obstacles
obstacle1 = Rect(40, 20, 10, 40)
obstacle2 = Rect(150, 140, 10, 40)

# list of obstacles
obstacles = [obstacle1, obstacle2]


# creating a Map
dynamic_map = {}


running = True
prev_position = (robot_rect.centerx, robot_rect.centery)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
                #pygame.display.quit()
                #sys.exit()
    

    # LOGIC for robot movement
    keys = pygame.key.get_pressed()
    current_position = robot_rect.center


    prev_position = robot_rect.topleft # saving the previous position 
    if keys[pygame.K_LEFT] and robot_rect.left > 0:
        robot_rect.move_ip(-VELOCITY, 0)
    if keys[pygame.K_RIGHT] and robot_rect.right < WIDTH:
        robot_rect.move_ip(VELOCITY, 0)
    if keys[pygame.K_UP] and robot_rect.top > 0:
        robot_rect.move_ip(0, -VELOCITY)
    if keys[pygame.K_DOWN] and robot_rect.bottom < HEIGHT:
        robot_rect.move_ip(0, VELOCITY)




    # if collision happens just move to previous movement
    if any(robot_rect.colliderect(obstacle) for obstacle in obstacles):
        dynamic_map[robot_rect.center] = 'X'
        robot_rect.center = current_position
    else:
        update_map(dynamic_map, robot_rect.center, current_position)



    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, BLUE, robot_rect.center, robot_radius)
    pygame.draw.rect(screen, RED, obstacle1)
    pygame.draw.rect(screen, RED, obstacle2)

    pygame.display.flip()

print_map(dynamic_map)
pygame.display.quit()
pygame.quit()
