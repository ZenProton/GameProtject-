import pygame
# from pygame.locals import *
# import math
import sys

pygame.init()

win_width,win_heigth = 400,650
win = pygame.display.set_mode((win_width, win_heigth))
pygame.display.set_caption("Banana BongBon")

# Charger l'image
img = pygame.image.load("files/img/play.png")
original_img = pygame.transform.scale(img, (200, 250))

class LoadingAnimation:
    def __init__(self):
        self.progress = 0
        self.timer = 0
        self.finished = False  # Nouveau: indique si le chargement est fini
        
        # Animation de l'image
        self.image_scale = 0.1
        self.target_scale = 1.0
        
        # Position de l'image
        self.image_x = win_width // 2
        self.image_y = win_heigth // 2 - 50
        
        # Barre de chargement
        self.loading_bar_width = 200
        self.loading_bar_height = 10
        self.loading_bar_x = win_width // 2 - self.loading_bar_width // 2
        self.loading_bar_y = win_heigth - 100
        
        # Messages
        self.messages = [
            "Initialisation...",
            "Chargement...",
            "Préparation...",
            "Presque terminé...",
            "Prêt !"
        ]
        self.current_message = 0
        
        # Couleurs
        self.bg_color = (25, 25, 112)
        self.loading_bg = (40, 40, 60)
        self.loading_fill = (50, 205, 50)
        self.text_color = (255, 255, 255)
        
        # Police
        self.font_small = pygame.font.Font(None, 22)
        self.font_medium = pygame.font.Font(None, 26)
        self.font_title = pygame.font.Font(None, 36)
        
        # Titre
        self.title = "Loading"
        self.title_alpha = 0
    
    def update(self):
        if self.finished:
            return
            
        self.timer += 1
        
        # Augmenter la progression
        if self.progress < 100:
            self.progress += 0.7
        
        # Faire grandir l'image
        if self.image_scale < self.target_scale:
            self.image_scale = min(self.target_scale, 
                                  self.image_scale + 0.015)
        
        # Mettre à jour le message
        self.current_message = min(len(self.messages) - 1, 
                                  int(self.progress / 25))
        
        # Faire apparaître le titre
        if self.progress > 20 and self.title_alpha < 255:
            self.title_alpha += 3
        
        # Vérifier si le chargement est terminé
        if self.progress >= 100 and self.image_scale >= self.target_scale:
            self.finished = True
    
    def draw_loading_bar(self, surface):
        # Fond de la barre
        pygame.draw.rect(surface, self.loading_bg,
                        (self.loading_bar_x, self.loading_bar_y,
                         self.loading_bar_width, self.loading_bar_height),
                        border_radius=5)
        
        # Barre de progression
        if self.progress > 0:
            fill_width = int((self.progress / 100) * self.loading_bar_width)
            color_intensity = min(255, 50 + int(self.progress * 2))
            fill_color = (50, color_intensity, 50)
            
            pygame.draw.rect(surface, fill_color,
                           (self.loading_bar_x, self.loading_bar_y,
                            fill_width, self.loading_bar_height),
                           border_radius=5)
        
        # Contour
        pygame.draw.rect(surface, (100, 100, 120),
                        (self.loading_bar_x, self.loading_bar_y,
                         self.loading_bar_width, self.loading_bar_height),
                        border_radius=5, width=1)
        
        # Pourcentage
        percent_text = self.font_medium.render(f"{int(self.progress)}%", 
                                              True, self.text_color)
        percent_rect = percent_text.get_rect(
            center=(win_width // 2, self.loading_bar_y - 20)
        )
        surface.blit(percent_text, percent_rect)
    
    def draw_message(self, surface):
        message = self.messages[self.current_message]
        message_text = self.font_small.render(message, True, self.text_color)
        message_rect = message_text.get_rect(
            center=(win_width // 2, self.loading_bar_y + 30)
        )
        surface.blit(message_text, message_rect)
    
    def draw_title(self, surface):
        if self.title_alpha > 0:
            title_text = self.font_title.render(self.title, True, (255, 215, 0))
            title_text.set_alpha(self.title_alpha)
            title_rect = title_text.get_rect(center=(win_width // 2, 40))
            surface.blit(title_text, title_rect)
    
    def draw_image(self, surface):
        if self.image_scale > 0:
            current_width = int(original_img.get_width() * self.image_scale)
            current_height = int(original_img.get_height() * self.image_scale)
            
            if current_width > 0 and current_height > 0:
                scaled_img = pygame.transform.smoothscale(original_img, 
                                                        (current_width, current_height))
                img_rect = scaled_img.get_rect(center=(self.image_x, self.image_y))
                surface.blit(scaled_img, img_rect)
    
    def draw(self, surface):
        self.draw_image(surface)
        self.draw_title(surface)
        self.draw_loading_bar(surface)
        self.draw_message(surface)

def run_loading_screen():
    """Fonction qui lance l'écran de chargement et retourne quand c'est fini"""
    animation = LoadingAnimation()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        animation.update()
        
        # Si le chargement est terminé, sortir de la boucle
        if animation.finished:
            # Petite pause pour voir "Prêt !"
            pygame.time.wait(500)
            return
        
        win.fill(animation.bg_color)
        animation.draw(win)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run_loading_screen()