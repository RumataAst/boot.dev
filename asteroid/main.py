import pygame
import sys

from logger import log_state, log_event
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    #Game loop
    while 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()


        for screen_object in asteroids:
            if screen_object.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for screen_object in drawable:
            screen_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
