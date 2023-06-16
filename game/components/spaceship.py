import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import PLAYER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP


class Spaceship(Sprite):
    def __init__(self):
        super().__init__()
        self.type = PLAYER_TYPE
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 10
        self.shoot_delay = 250
        self.last_shot_time = pygame.time.get_ticks()

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

        now = pygame.time.get_ticks()
        if user_input[pygame.K_SPACE] and now - self.last_shot_time > self.shoot_delay:
            self.last_shot_time = now
            self.shoot(game.bullet_manager)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        else:
            self.rect.x = 0

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10