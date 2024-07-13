import pygame
import sys

pygame.init()

# Farben
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fenstergröße
win_width = 1000
win_height = 800
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("ShapeCalc")

# Schriftart und -größe
font_size = 50
font = pygame.font.Font(None, font_size)
button_font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, text, width, height, pos, action):
        self.pressed = False
        self.action = action
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = BLACK
        self.hover_color = GRAY
        self.text_surf = button_font.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
    
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.top_color
        
        pygame.draw.rect(win, color, self.top_rect, border_radius=12)
        win.blit(self.text_surf, self.text_rect)
        self.check_click()
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.action()
                    self.pressed = False

def button1_action():
    print("Button 1 pressed")

def button2_action():
    print("Button 2 pressed")

# Buttons erstellen
button1 = Button("Click me", 200, 60, (400, 300), button1_action)
button2 = Button("Menu", 200, 60, (400, 400), button2_action)

buttons = [button1, button2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    win.fill(WHITE)

    # Menüüberschrift
    win_text = font.render("Menu", True, BLACK)
    win_text_rect = win_text.get_rect(center=(win_width // 2, 100))
    win.blit(win_text, win_text_rect)
    
    # Buttons zeichnen
    for button in buttons:
        button.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()
