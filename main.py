import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatable =  pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (asteroid_field, updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    new_asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for item in updatable:
            item.update(dt)

        screen.fill((0, 0, 0))

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()