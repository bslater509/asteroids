import pygame # type: ignore
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from shot import Shot
from logger import log_state, log_event
import sys
from asteroidfield import AsteroidField

def load_high_score():
    #create high score file if it doesn't exist
    try:
        high_score_file = open("high_score.txt")
        high_score = high_score_file.read()
        high_score_file.close()
        return high_score
    except FileNotFoundError:
        high_score_file = open("high_score.txt", "w")
        high_score_file.write("0")
        high_score_file.close()
        return 0

def store_high_score(score):
    high_score_file = open("high_score.txt", "w")
    high_score_file.write(str(int(score)))
    high_score_file.close()



def main():
    #initialize pygame and create window
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    high_score = load_high_score()
    print(f"High Score: {high_score}")
    score = int(0)
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    dt = 0
    score_font = pygame.font.SysFont('Comic Sans MS', 30)

    #setup sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable, drawable,shots)

    #create game objects
    score_surface = score_font.render(f"Score: {score} - High Score: {high_score}", False, "white")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    #game loop
    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #update and draw all sprites
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!") 
                if score > int(high_score):
                    store_high_score(score)
                    print(f"New high score: {score}!")
                sys.exit(0)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += asteroid.score_points
                    score_surface = score_font.render(f"Score: {int(score)} - High Score: {high_score}", False, "white")
                    shot.kill()
                    asteroid.split()


        for sprite in drawable:
            sprite.draw(screen)
        screen.blit(score_surface, (0,0))
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
