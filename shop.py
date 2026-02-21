import pygame
import home

def main():
    pygame.init()

    win_width,win_heigth = 400,650
    win = pygame.display.set_mode((win_width,win_heigth))
    pygame.display.set_caption("Banana BongBon")
    pygame.display.set_icon(pygame.image.load("files/img/logo.jpg"))
    
    button_return = pygame.image.load("files/img/flech-2.png")
    button_return = pygame.transform.scale(button_return,(60,60))
    button_return_rect = button_return.get_rect(center = (5,5))
    
    font = pygame.font.SysFont("Arial", 32)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_return_rect.collidepoint(mouse_pos):
                    home.main()
        
        win.fill((255,165,0))
        win.blit(button_return,button_return_rect.center)
        
# ------------------------------------------------------------------------------
        text_surface = font.render("En plain </Dev>", True, (255,0,0))
        win.blit(text_surface, (win_width//6+25, win_heigth//2))
                    
        pygame.display.flip()

if __name__ == "__main__":
    main()