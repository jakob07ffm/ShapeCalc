import pygame
import sys

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

win_width = 1000
win_height = 800
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("ShapeCalc")

font_size = 50
font = pygame.font.Font(None, font_size)

class Button:
    def __init__(self, text, width, height, pos, action):
        self.pressed = False
        self.action = action
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = BLACK
        self.text_surf = font.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
    
    def draw(self):
        pygame.draw.rect(win, self.top_color, self.top_rect, border_radius=12)
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

button1 = Button("Click me", 200, 40, (200, 250), button1_action)
button2 = Button("Menu", 200, 40, (20, 500), button2_action)

buttons = [button1, button2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    win.fill(WHITE)

    win_text = font.render("Menu", True, BLACK)
    win.blit(win_text, (0, 0))
    
    for button in buttons:
        button.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()
