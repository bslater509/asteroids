from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame # type: ignore
import random
from circleshape import CircleShape
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y,radius)


    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #create two smaller asteroids
        log_event("asteroid_split")
        new_rotation = random.uniform(20,50)
        new_size = self.radius - ASTEROID_MIN_RADIUS

        #create two smaller asteroids
        asteroid1 = Asteroid(self.position.x,self.position.y,new_size)
        asteroid1.velocity = self.velocity.rotate(new_rotation)
        asteroid1.velocity *= 1.2

        asteroid2 = Asteroid(self.position.x,self.position.y,new_size)
        asteroid2.velocity = self.velocity.rotate(-new_rotation)
        asteroid2.velocity *= 1.2
