from turtle import Screen
import pygame


class Ino(pygame.sprite.Sprite):
    """  класс одного пришельца """

    def __init__(self, screen):
        """инициализируем его """
        super(Ino, self).__init__()
        self.screen = Screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """ отрисовка алиена """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ перемещение алиена """
        self.y += 0.5
        self.rect.y = self.y
