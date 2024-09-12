import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Game Over!', False, (0, 0, 0))
    surface = pygame.Surface((200, 100))
    surface.fill((0, 0, 0))  # Fill with black
    text_surface = my_font.render('Game Over!', True, (255, 0, 0))
    surface.blit(text_surface, (10, 10))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatable =  pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (asteroid_field, updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    new_asteroid_field = AsteroidField()
    


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        for astroid in asteroids:
            if astroid.collision_detection(player):
                screen.fill((0, 0, 0))
                screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width() / 2, SCREEN_HEIGHT / 2 - text_surface.get_height() / 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                sys.exit()

            for shot in shots:
                if astroid.collision_detection(shot):
                    shot.kill()
                    split_asteroids = astroid.split()
                    if split_asteroids:
                        asteroids.add(*split_asteroids)
                    pygame.display.flip()

        screen.fill((0, 0, 0))
        
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()