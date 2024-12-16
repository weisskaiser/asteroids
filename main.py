import pygame
import constants
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == '__main__':
    main()