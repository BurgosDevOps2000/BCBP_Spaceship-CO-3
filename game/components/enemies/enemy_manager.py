from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        if not self.enemies:
            self.spawn_enemy()
            
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.append(enemy)
    