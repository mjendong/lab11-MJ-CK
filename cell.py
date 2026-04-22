import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

        # Dimensions & Colors
        self.cell_size = 60  # Adjusted based on a standard 540x540 board
        self.font = pygame.font.Font(None, 40)
        self.sketch_font = pygame.font.Font(None, 30)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.cell_size
        y = self.row * self.cell_size

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), 3)
        else:
            pygame.draw.rect(self.screen, (200, 200, 200), (x, y, self.cell_size, self.cell_size), 1)

        if self.value != 0:
            text_surface = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
            self.screen.blit(text_surface, text_rect)

        elif self.sketched_value != 0:
            sketch_surface = self.sketch_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketch_surface, (x + 5, y + 5))