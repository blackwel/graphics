#!/usr/bin/python

import sys, pygame, random

def main():
    pygame.init()

    size = width, height = 1400, 900
    black = 0, 0, 0

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    mario_sprite = pygame.image.load('mario2.png')
    mario_rect = mario_sprite.get_rect()

    frame_width = mario_rect.width / 6 + 1
    frame_height = mario_rect.height / 4
    frame = pygame.Rect(0, 0, frame_width, frame_height)

    frame = frame.move(0, frame_height * 3)

    frame_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                sys.exit()
                

        screen.fill(black)

        current_frame = frame.move(frame_counter * frame_width, 0)

        screen.blit(mario_sprite, mario_rect, current_frame)
        pygame.display.flip()

        frame_counter = (frame_counter + 1) % 6

        pygame.time.delay(100)

if __name__ == '__main__':
    main()
