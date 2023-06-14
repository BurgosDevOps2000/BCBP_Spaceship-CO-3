import pygame

from game.utils.constants import BULLET

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = BULLET  # Imagen de la bala (bullet)
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # Posición inicial en el eje x
        self.rect.bottom = y  # Posición inicial en el eje y
        self.speed = 5  # Velocidad de la bala (puedes ajustarla según tus necesidades)

    def update(self):
        self.rect.y -= self.speed  # Mover la bala hacia arriba