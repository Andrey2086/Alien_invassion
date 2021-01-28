
import pygame

class Snowman:
    def __init__(self, hero):
        self.screen = hero.screen
        self.screen_rect = hero.screen.get_rect()
        self.image = pygame.image.load('images/christmas.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)