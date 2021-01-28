import sys
import pygame
from snowman import Snowman
class Hero:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        # self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption("Hero")
        self.bg_color = (0, 191, 255)
        self.snowman = Snowman(self)

    def run_hero(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Отображение последнего прорисованного экрана.
            self.screen.fill(self.bg_color)
            self.snowman.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    hero = Hero()
    hero.run_hero()
