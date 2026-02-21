import pygame
import load
import shop
    
def main():
    pygame.init()


    load.run_loading_screen()
    shop.main()


if __name__ == "__main__":
    main()