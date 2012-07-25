#!/usr/bin/python

import sys, pygame, random

def main():
    pygame.init()

    size = width, height = 640, 480
    speed = [7, 7]
    speed2 = [7, 7]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("ball.gif")
    ballrect = ball.get_rect()

    ball2 = pygame.image.load("ball.gif")
    ballrect2 = ball2.get_rect()
    ballrect2 = ballrect2.move((random.randint(0, width), random.randint(0, height)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        ballrect2 = ballrect2.move(speed2)
        if ballrect2.left < 0 or ballrect2.right > width:
            speed2[0] = -speed2[0]
        if ballrect2.top < 0 or ballrect2.bottom > height:
            speed2[1] = -speed2[1]

        if is_intersecting(ballrect,ballrect2):
            speed1 = reflect(speed1)
            speed2 = reflect(speed2)

        screen.fill(black)
        screen.blit(ball, ballrect)
        screen.blit(ball2, ballrect2)
        pygame.display.flip()

def is_intersecting(rect1, rect2):
    return False

def reflect(speed):
    return speed

if __name__ == '__main__':
    main()
