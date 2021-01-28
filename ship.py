import pygame

class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right - 10:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 10:
            self.x -= self.settings.ship_speed
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)