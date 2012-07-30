#!/usr/bin/python

import sys, pygame, random

def main():
    pygame.init()

    size = width, height = 800, 480
    speed = [random.randrange(1,10), random.randrange(1,10)]
    speed2 = [random.randrange(1,10), random.randrange(1,10)]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    ball = pygame.image.load("ball.gif")
    ballrect = ball.get_rect()

    ball2 = pygame.image.load("ball.gif")
    ballrect2 = ball2.get_rect()
    ballrect2 = ballrect2.move((random.randint(0, width - ballrect2.width), random.randint(0, height - ballrect2.height)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                sys.exit()
                
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
            speed = reflect(speed)
            speed2 = reflect(speed2)

        screen.fill(black)
        screen.blit(ball, ballrect)
        screen.blit(ball2, ballrect2)
        pygame.display.flip()

def is_intersecting(rect1, rect2):
    return rect1.colliderect(rect2)

def reflect(speed):
    return [-speed[0], -speed[1]]


if __name__ == '__main__':
    main()
