from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
    
    def update(self, game):
        if not self.enemies:
            self.enemies.append(Enemy())
            
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)