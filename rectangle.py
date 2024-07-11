import pygame
import sys

pygame.init()

width, height = 1000, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("RECTANGLE")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 32)
text_heading = font.render('RECTANGLE', True, BLACK)
text_heading_rect = text_heading.get_rect()
text_heading_rect.center = (width // 2, 40)

big_rect_img = pygame.image.load("Shape_img/RECTANGLE.png")
big_rect_img_size = big_rect_img.get_size()
scale_factor = 0.5
rect_img_size = (int(big_rect_img_size[0] * scale_factor), int(big_rect_img_size[1] * scale_factor))
rect_img = pygame.transform.scale(big_rect_img, rect_img_size)

with open("formular/formular.txt", "r") as formular_file:
    formular = formular_file.read()

rect_formular_text = font.render(formular, True, BLACK)
rect_formular_rect = rect_formular_text.get_rect()
rect_formular_rect.topleft = (10, 80) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    win.fill(WHITE) 
    
    win.blit(text_heading, text_heading_rect)
    win.blit(rect_img, (width // 2 - rect_img_size[0] // 2, height // 2 - rect_img_size[1] // 2))
    win.blit(rect_formular_text, rect_formular_rect)
    
    pygame.display.flip()
    
    clock.tick(30)

pygame.quit()
sys.exit()
