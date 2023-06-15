import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE


class BulletManager:
    def __init__(self):
        self.bullets: list[Bullet] = []
        self.enemy_bullet: list[Bullet] = []

    def update(self, game):
        for bullet in self.enemy_bullet:
            bullet.update(self.enemy_bullet)

            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullet.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

    def draw(self, screen):
        for bullet in self.enemy_bullet:
            bullet.draw(screen)
    
    def add_bullet(self, bullet):
        if bullet.owner.type == ENEMY_TYPE:
            self.enemy_bullet.append(bullet)
