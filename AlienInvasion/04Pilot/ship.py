import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.move_dx = 0

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.recenter()

    def recenter(self):
        # Place ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        self.rect.x += self.move_dx
        
        # Keep on screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.move_dx = 0
        elif self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.move_dx = 0
        
        # Acceleration!
        #self.move_dx *= 1.04
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)