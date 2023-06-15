import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP 


class Spaceship(Sprite):
    def __init__(self):
        self.type = 'player'  # Agregar atributo 'type' con valor 'player'
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500  
        self.shoot_delay = 250  # Retardo entre disparos
        self.last_shot_time = pygame.time.get_ticks()  # Último momento en que se realizó un disparo
        self.auto_shoot_delay = 1000  # Retardo entre disparos automáticos
        self.last_auto_shot_time = pygame.time.get_ticks()  # Último momento en que se realizó un disparo automático



    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_rigth()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
    
        now = pygame.time.get_ticks()
        if now - self.last_auto_shot_time > self.auto_shoot_delay:
            self.last_auto_shot_time = now
            self.auto_shoot(game.bullet_manager)

        # Verificar si se presionó la tecla de disparo y es momento de disparar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and now - self.last_shot_time > self.shoot_delay:
            self.last_shot_time = now
            self.auto_shoot(game.bullet_manager)
        
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH

    def move_rigth(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y < SCREEN_HEIGHT // 2:
             self.rect.y += 10
             
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 40:
            self.rect.y += 10


    def draw(self, screen):
       screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def auto_shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
