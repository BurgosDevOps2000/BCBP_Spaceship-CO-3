import random

import pygame
from game.components.powerups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD

class Manager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = random.randint(2, 5)

    def generate_power_up(self):
        shield = Shield()
        self.when_appears = random.randint(10000, 15000)
        self.power_ups.append(shield)
    
    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time
                game.player.set_image((70, 80), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 10000, now + 15000)