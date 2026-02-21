import pygame
import sys
import random
# from pygame.locals import *

def run_game():
    pygame.init()
    pygame.mixer.init()


    win_width,win_heigth = 400,650
    win = pygame.display.set_mode((win_width,win_heigth))
    pygame.display.set_caption("Banana BongBon")
    pygame.display.set_icon(pygame.image.load("files/img/logo.jpg"))

    # import sond:
    pygame.mixer.music.load("files/sound/Banana_Sn.mp3")
    pygame.mixer.music.play(-1)

    #font:
    font_game = pygame.image.load("files/img/font-flou.jpg")
    font_game = pygame.transform.scale(font_game,(win_width,win_heigth))

    # value:
    game_over = False
    spawn_timer = 0
    foods = []
    # pause = False

    # ---------------------
    files_img = "files/img/"

    # --------------------- panier --------------------------
    class Panier(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.img = pygame.image.load("files/img/pani3.png")
            # self.rect = self.img.get_rect()
            self.width,self.height = self.img.get_size()
            self.rect = self.img.get_rect(topleft=(win_width//2 - self.img.get_width()//2,win_heigth - (self.height+5) ))
            self.velocity = [0,0]
        def update(self):
            self.rect.move_ip(*self.velocity)
    panier = Panier()

    # -------------------------- food --------------------------
    class Food:
        def __init__(self,type):
            self.type = type
            self.size = 30
            self.x = random.randint(0, win_width-30)
            self.y = -self.size
            self.speed = random.randint(2, 5)
            
            # food:
                # ++++++++++++++
            if self.type == "banana":
                self.img = pygame.image.load(files_img+"/Banana2.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 4
            elif self.type == "pineapple":
                self.img = pygame.image.load(files_img+"/ann2.png")
                self.img = pygame.transform.scale(self.img,(40,50))
                self.value = 3
            elif self.type == "bll":
                self.img = pygame.image.load(files_img+"/mes_boul2.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 2
            elif self.type == "pstk":
                self.img = pygame.image.load(files_img+"/pst.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 2
            
                # ----------------
            elif self.type == "doritos":
                self.img = pygame.image.load(files_img+"/chm1.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 1
            elif self.type == "chocolate":
                self.img = pygame.image.load(files_img+"/cho.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 1
            elif self.type == "hotdog":
                self.img = pygame.image.load(files_img+"/hot2.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 1
            elif self.type == "burger":
                self.img = pygame.image.load(files_img+"/mac2.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 1
            elif self.type == "pepsi":
                self.img = pygame.image.load(files_img+"/pepsi.png")
                self.img = pygame.transform.scale(self.img,(30,40))
                self.value = 1
            elif self.type == "pizza":
                self.img = pygame.image.load(files_img+"/pizza2.png")
                self.img = pygame.transform.scale(self.img,(40,40))
                self.value = 1
                
        def update(self):
            self.y += self.speed
            if self.y > win_heigth:
                return False
            return True

    class Score:
        def __init__(self):
            self.value = 0
            self.font = pygame.font.SysFont("Arial", 24)
        def update(self):
            pass
    score = Score()

    class Life:
        def __init__(self):
            self.max_life = 3
            self.life = 3
            self.heart_full = pygame.image.load("files/img/life-.png")
            self.heart_full = pygame.transform.scale(self.heart_full, (32, 32))
            self.spacing = 38
            self.x_start = 10
            self.y = 45

        def draw(self, surface):
            for i in range(self.max_life):
                x = self.x_start + i * self.spacing
                if i < self.life:
                    surface.blit(self.heart_full, (x, self.y))
        def update(self):
            pass
    life = Life()

    class Button:
        def __init__(self, x, y, width, height, text, color, text_color):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.color = color
            self.text_color = text_color
            self.font = pygame.font.SysFont("Arial", 24)
        
        def draw(self, surface):
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
        
        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)

    class GameOver:
        def __init__(self):
            self.font = pygame.font.SysFont("Arial", 48)
            self.restart_btn = Button(0,0, 100, 50, "Restart", (0, 200, 0), (255, 255, 255))
            self.quit_btn = Button(0, 0, 100, 50, "Quitter", (200, 0, 0), (255, 255, 255))
            self.restart_btn.rect.x = win_width // 2 - 150
            self.restart_btn.rect.y = 250
            self.quit_btn.rect.x = win_width // 2 + 50
            self.quit_btn.rect.y = 250
        
        def show(self):
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if self.restart_btn.is_clicked(pos):
                            return "restart"
                        if self.quit_btn.is_clicked(pos):
                            return "quit"
                
                win.fill((135, 206, 235))
                game_over_text = self.font.render("Game Over", True, (255, 0, 0))
                win.blit(game_over_text, (win_width//2 - game_over_text.get_width()//2, 150))
                
                self.restart_btn.draw(win)
                self.quit_btn.draw(win)
                
                pygame.display.flip()
                pygame.time.Clock().tick(60)

    game_over = GameOver()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    panier.velocity[0] = -5
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    panier.velocity[0] = 5
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT):
                    panier.velocity[0] = 0

        if panier.rect.left < 0:
            panier.rect.left = 0
        if panier.rect.right > win_width:
            panier.rect.right = win_width
            
        if life.life <= 0:
            result = game_over.show()
            if result == "restart":
                # Réinitialiser le jeu
                score.value = 0
                life.life = 3
                foods = []
                spawn_timer = 0
                panier = Panier()
            elif result == "quit":
                pygame.quit()
                sys.exit()
        

        spawn_timer += 1
        if spawn_timer >= 30:
            food_type = random.choice(["banana", "pineapple", "doritos", "chocolate", "hotdog", "burger", "bll", "pepsi", "pizza", "pstk"])
            foods.append(Food(food_type))
            spawn_timer = 0  


        # win.fill((135, 206, 235))
        win.blit(font_game,(0,0))

        panier.update()

        bonus_types = ["banana", "pineapple", "bll", "pstk"]
        malus_types = ["hotdog", "burger", "pizza"]
        danger_types = ["doritos", "chocolate", "pepsi"]

        to_remove = []
        for food in foods:
            if not food.update():
                to_remove.append(food)
            else:
                food_rect = pygame.Rect(food.x, food.y, food.img.get_width(), food.img.get_height())
                if food_rect.colliderect(panier.rect):
                    if food.type in bonus_types:
                        score.value += food.value
                    elif food.type in malus_types:
                        score.value -= food.value
                    elif food.type in danger_types:
                        life.life -= food.value
                    to_remove.append(food)
        for food in to_remove:
            foods.remove(food)

        score_text = score.font.render(f"Score: {score.value}", True, (0, 0, 0))
        win.blit(score_text, (10, 10))
        
        score_text = score.font.render(f"Score: {score.value}", True, (0, 0, 0))
        win.blit(score_text, (10, 10))
        life.draw(win)
        
        # Afficher tous les aliments
        for food_item in foods:
            win.blit(food_item.img, (food_item.x, food_item.y))
        
        win.blit(panier.img, panier.rect)

        # # Draw borders for collisions
        # pygame.draw.rect(win, (255,0,0), panier.rect, 2)  # Red for panier
        # for food_item in foods:
        #     food_rect = pygame.Rect(food_item.x, food_item.y, food_item.img.get_width(), food_item.img.get_height())
        #     pygame.draw.rect(win, (0,255,0), food_rect, 2)  # Green for foods

        pygame.display.flip()
        pygame.time.Clock().tick(60)
if __name__=="__main__":
    run_game()