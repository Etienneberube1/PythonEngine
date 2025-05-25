import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_rect(self, color, rect, width=0):
        pygame.draw.rect(self.screen, color, rect, width)

    def draw_circle(self, color, pos, radius, width=0):
        pygame.draw.circle(self.screen, color, pos, radius, width)

    def draw_image(self, image, pos):
        self.screen.blit(image, pos)

    def draw_text(self, text, pos, font, color=(255, 255, 255)):
        surface = font.render(text, True, color)
        self.screen.blit(surface, pos)
