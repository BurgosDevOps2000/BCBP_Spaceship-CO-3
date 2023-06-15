import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
   SPEED = 20
   ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
   SPACESHIP_BULLET_IMG = pygame.transform.scale(BULLET, (9, 32))
   def __init__(self, spaceship):
      if spaceship.type == ENEMY_TYPE:
         self.image = self.ENEMY_BULLET_IMG
      else:
         self.image = self.SPACESHIP_BULLET_IMG

      self.rect = self.image.get_rect()
      self.rect.center = spaceship.rect.center
      self.owner = spaceship

   def update(self, bullets):
      if self.owner.type == ENEMY_TYPE:
         self.rect.y += self.SPEED
         if self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)


   def draw(self, screen):
      screen.blit(self.image, (self.rect.x, self.rect.y))
