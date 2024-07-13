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

# Read the file line by line
with open("formular/formular.txt", "r") as formular_file:
    lines = formular_file.readlines()

# Render each line of the text separately
rendered_text_lines = []
y_offset = 80  # Starting Y position for the text
line_height = font.get_height()  # Height of each line of text

for line in lines:
    rendered_text = font.render(line.strip(), True, BLACK)
    rendered_text_rect = rendered_text.get_rect()
    rendered_text_rect.topleft = (10, y_offset)
    rendered_text_lines.append((rendered_text, rendered_text_rect))
    y_offset += line_height

# Input box settings
input_boxes = [
    {'rect': pygame.Rect(500, 60, 140, 32), 'color': pygame.Color("black"), 'text': '', 'active': False},
    {'rect': pygame.Rect(500, 100, 140, 32), 'color': pygame.Color("black"), 'text': '', 'active': False}
]

input_color_active = pygame.Color("azure3")
input_color_passive = pygame.Color("black")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in input_boxes:
                if box['rect'].collidepoint(event.pos):
                    box['active'] = True
                else:
                    box['active'] = False
        if event.type == pygame.KEYDOWN:
            for box in input_boxes:
                if box['active']:
                    if event.key == pygame.K_BACKSPACE:
                        box['text'] = box['text'][:-1]
                    else:
                        box['text'] += event.unicode

    win.fill(WHITE)

    win.blit(text_heading, text_heading_rect)
    win.blit(rect_img, (0, 300))
    
    for rendered_text, rendered_text_rect in rendered_text_lines:
        win.blit(rendered_text, rendered_text_rect)

    for box in input_boxes:
        box['color'] = input_color_active if box['active'] else input_color_passive
        pygame.draw.rect(win, box['color'], box['rect'], 2)
        text_surface = font.render(box['text'], True, BLACK)
        win.blit(text_surface, (box['rect'].x + 5, box['rect'].y + 5))
        box['rect'].w = max(100, text_surface.get_width() + 10)

    # Calculate and display the result
    try:
        value1 = int(input_boxes[0]['text'])
        value2 = int(input_boxes[1]['text'])
        result = value1 * value2
        result_text = font.render(f'Result: {result}²', True, BLACK)
        win.blit(result_text, (500, 200))
    except ValueError:
        pass

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
