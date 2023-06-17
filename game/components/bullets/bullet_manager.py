from game.components.enemies.enemy import Enemy
from game.components.dead import YouDied
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE, SHIELD_TYPE

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        self.update_enemy_bullets(game)
        self.update_bullets(game)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == PLAYER_TYPE:
            self.bullets.append(bullet)

    def update_enemy_bullets(self, game):
        bullets_to_remove = []
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                bullets_to_remove.append(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    you_died_screen = YouDied(game.score, game.max_score) # Crear una instancia de la clase YouDied
                    you_died_screen.run(game)# Mostrar la pantalla de "Has muerto"
                    break
        for bullet in bullets_to_remove:
            if bullet in self.enemy_bullets:
                self.enemy_bullets.remove(bullet)

    def update_bullets(self, game):
        bullets_to_remove = []
        enemies_to_remove = []
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullets_to_remove.append(bullet)
                    enemies_to_remove.append(enemy)
            if bullet.rect.y < 0:
                bullets_to_remove.append(bullet)

        for bullet in bullets_to_remove:
            if bullet in self.bullets:
                self.bullets.remove(bullet)

        for enemy in enemies_to_remove:
            if enemy in game.enemy_manager.enemies:
                game.enemy_manager.enemies.remove(enemy)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []