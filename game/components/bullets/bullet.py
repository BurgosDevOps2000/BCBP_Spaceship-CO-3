import pygame
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE, SCREEN_HEIGHT, BULLET


class Bullet(Sprite):
    SPEED = 20
    BULLETS = {
        ENEMY_TYPE: pygame.transform.scale(BULLET, (9, 32)),
        PLAYER_TYPE: pygame.transform.scale(BULLET, (9, 32))
    }

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
        self.last_shoot_time = pygame.time.get_ticks()

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y < 0:
                bullets.remove(self)

        elif self.owner == PLAYER_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y < 0:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
