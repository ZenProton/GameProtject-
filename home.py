import pygame 
import sys
import load_game
import load_shop

def main():
    pygame.init()

    win_width,win_heigth = 400,650
    win = pygame.display.set_mode((win_width,win_heigth))
    pygame.display.set_caption("Banana BongBon")
    pygame.display.set_icon(pygame.image.load("files/img/logo.jpg"))

    font = pygame.image.load("files/img/font-Home-.jpg")
    font = pygame.transform.scale(font,(win_width,win_heigth))

    title = pygame.image.load("files/img/Title-Home.png")
    title = pygame.transform.scale(title,(250,150))
    title_rect = title.get_rect()

    button_play = pygame.image.load("files/img/button-play-.jpg")
    button_play = pygame.transform.scale(button_play,(230,85))
    button_play_rect = button_play.get_rect(center = (90,title_rect.bottom + 100))

    button_Shop = pygame.image.load("files/img/button-shop-.jpg")
    button_Shop = pygame.transform.scale(button_Shop,(230,85))
    button_shop_rect = button_Shop.get_rect(center = (90,button_play_rect.bottom + 80))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play_rect.collidepoint(mouse_pos):
                    load_game.main()
                if button_shop_rect.collidepoint(mouse_pos):
                    load_shop.main()
            
        win.blit(font,(0,0))
        win.blit(button_play,button_play_rect.center)
        win.blit(button_Shop,button_shop_rect.center)
        win.blit(title,(win_width // 5.5,5))
        
        pygame.display.flip()
if __name__ == "__main__":
    main()