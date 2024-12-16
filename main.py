import pygame
from asteroid import Asteroid
import constants
from player import Player
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for entity in updatable:
            entity.update(dt)
        for asteroid in asteroids:
            if player.check_colision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_colision(shot):
                    asteroid.split()
                    shot.kill()
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == '__main__':
    main()