import sys
import pygame
from utils import Robot

pygame.init()

WIDTH = 200
HEIGHT = 200
BACKGROUND = (224, 192, 160)
VELOCITY = 5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("SLAM")

# robot info
robot = Robot(100, 100, 7) 

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.display.quit()
                sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if robot.x - robot.radius > 0:
            robot.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        if robot.x + robot.radius < WIDTH:
            robot.x += VELOCITY
    if keys[pygame.K_UP]:
        if robot.y - robot.radius > 0:
            robot.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        if robot.y + robot.radius < HEIGHT:
            robot.y += VELOCITY


    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, (0, 0, 255) ,(robot.x, robot.y), robot.radius)

    pygame.display.flip()


pygame.display.quit()
pygame.quit()
