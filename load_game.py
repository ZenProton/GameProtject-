import pygame
import load
import game
    
def main():
    pygame.init()


    load.run_loading_screen()
    game.run_game()


if __name__ == "__main__":
    main()