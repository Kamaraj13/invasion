import pygame

class Ship():

    def _init_(self,screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        self.image = pygame.image.load('image/space_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)