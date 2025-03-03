import pygame
import random as r
import time
from config import *
from enemy import Enemy
from player import Player
from bullet import Bullet



class BlockFight():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.project_name = "BlockFight"

        pygame.display.set_caption(self.project_name)

        # Loop until the user clicks the close button.
        self.running = True

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.bullet = pygame.image.load("assets/bullet_right.png")
        self.enemy_image = pygame.image.load("assets/enemy_1.png")
        self.enemy_image = pygame.transform.scale(self.enemy_image, (50 * 1.25, 50))
        self.game_start_time = pygame.time.get_ticks()
        self.credit_button = pygame.image.load("assets/credit_button.png")

        self.enemy_group = pygame.sprite.Group()


        self.player_group = pygame.sprite.GroupSingle()
        self.player = (Player(self.screen, WIDTH/2, HEIGHT/2, 54, self))
        self.player_group.add(self.player)

        self.bullet_group = pygame.sprite.Group()
        self.damage = 1
        pygame.mixer.music.load("assets/backgroundmusic.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-2)

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 100, True)
        self.font_small = pygame.font.SysFont("Arial", 50, True)

        self.enemy_spawn_timer = FPS
        self.enemy_count = 1


        self.bullet_spawn_timer = 0.5


        self.clock_delay_timer = 1
        self.game_mode = PROLOGUE
    def game_loop(self):
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            self.screen.blit(self.background, (0,0))

            if self.game_mode == PROLOGUE:
                self.prologue()
            if self.game_mode == LANDING_PAGE:
                self.landing_page()
            elif self.game_mode == GAME_IN_SESSION:
                self.game_in_session()
            elif self.game_mode == GAME_OVER:
                self.game_over_page()
            elif self.game_mode == GAME_WIN:
                self.game_win_page()
            elif self.game_mode == CREDITS:
                self.game_credit_page()
            elif self.game_mode == CREDITS_2:
                self.game_credit_page2()


            self.clock.tick(FPS)
            current_fps = str(self.clock.get_fps())
            pygame.display.set_caption(f'{self.project_name}, fps: {current_fps}')

        # Close the window and quit.
        pygame.quit()
    def draw_count_down(self):
        time_elapsed = pygame.time.get_ticks() - self.game_start_time
        self.count_down = GAME_DURATION - int(time_elapsed / 1000)
        img = self.font_small.render(f" Count down {self.count_down}", 1, RED)
        self.screen.blit(img, (WIDTH/2 - 150, HEIGHT/2 - 100))

        if self.count_down <= 0:
            if self.score < MINIMUM_SCORE:
                self.game_mode = GAME_OVER
            else:
                self.game_mode = GAME_WIN
    def draw_score(self):
        img = self.font_small.render(f" Score {self.score}", 1, RED)
        self.screen.blit(img, (WIDTH/2 - 150, HEIGHT/2 - 50))

    def prologue(self):
        self.screen.blit(self.background, (0, 0))
        text_img = self.font.render(f"Russissmart Production ", 1, BLACK)
        self.screen.blit(text_img, (WIDTH/4-150 - 70, HEIGHT/2 - 100))
        self.display_regular_text(WIDTH / 2 - 200, HEIGHT / 2, "Press [P] To Continue", RED)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_p]:
            self.game_mode = LANDING_PAGE
    def game_in_session(self):
        self.screen.blit(self.background, (0,0))
        self.create_enemy()
        self.create_bullet()
        self.enemy_group.update()
        self.player_group.update()
        self.bullet_group.update()
        self.draw_count_down()
        self.draw_score()

        pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, True, True, self.bullet_enemy_collision)
        pygame.sprite.groupcollide(self.enemy_group, self.player_group, True, True, self.player_enemy_collision)


    def landing_page(self):
        self.screen.blit(self.background, (0,0))
        text_img = self.font.render(f"BLOCK FIGHT ", 1, BLACK)
        self.display_regular_text(WIDTH/2-300, HEIGHT/2, "Press [Z] For Arcade Mode!", RED)
        self.display_regular_text(WIDTH / 2 - 350, HEIGHT / 2+100, "Press [C] To See Controls and Credits", RED)
        self.display_regular_text(WIDTH / 2 -275, HEIGHT / 2+200, "Story Mode [Coming Soon]", RED)
        self.screen.blit(text_img, (WIDTH/4 - 70, HEIGHT/2 - 100))
        self.screen.blit(self.enemy_image, (WIDTH/2 + 250, HEIGHT/2 - 65))
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_z]:
            print(int(self.game_mode))
            self.game_mode = GAME_IN_SESSION
        if keys_pressed[pygame.K_c]:
            print(int(self.game_mode))
            self.game_mode = CREDITS





    def game_over_page(self):
        self.screen.blit(self.background, (0,0))
        self.count_down = GAME_DURATION
        text_img = self.font.render(f"GAME_OVER", 1, RED)
        self.display_regular_text(WIDTH/2-150, HEIGHT/2, "Press [Z] To Try Again", RED)
        self.screen.blit(text_img, (WIDTH / 4 - 70, HEIGHT / 2 - 100))
        self.screen.blit(self.enemy_image, (WIDTH/2 + 250, HEIGHT/2 - 65))
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_z]:
            self.game_mode = GAME_IN_SESSION





    def game_win_page(self):
        self.screen.blit(self.background, (0,0))
        self.count_down = GAME_DURATION
        text_img = self.font.render(f"YOU WON! :)", 1, RED)
        self.display_regular_text(WIDTH/2-150, HEIGHT/2, "Press [Z] To Go Back To Town", RED)
        self.screen.blit(text_img, (WIDTH / 4 - 70, HEIGHT / 2 - 100))
        self.screen.blit(self.enemy_image, (WIDTH/2 + 250, HEIGHT/2 - 65))


    def display_regular_text(self, x, y, text, color=BLACK):
        text_img = self.font_small.render(text, 1, color)
        self.screen.blit(text_img, (x, y))

    def game_credit_page(self):
        self.screen.blit(self.background, (0,0))
        x = (WIDTH / 2) - 400
        self.display_regular_text(x, 50, "Game Developer: Russell Sebastian", RED)
        self.display_regular_text(x, 100, "Game Asset: grapicriver.net and Pixbay.com", RED)
        self.display_regular_text(x, 200, "EDIT: Thank you for all your support!", RED)
        self.display_regular_text(x, 250, "Github: @Hiiamruss", RED)
        self.display_regular_text(x, 300, "[->] Next Page, [B] Back", RED)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.game_mode = CREDITS_2
        if keys_pressed[pygame.K_b]:
            self.game_mode = LANDING_PAGE

    def game_credit_page2(self):
        self.screen.blit(self.background, (0,0))
        x = (WIDTH / 2) - 400
        self.display_regular_text(x, 50, "       Controls", RED)
        self.display_regular_text(x, 100, "[Z] Start", RED)
        self.display_regular_text(x, 200, "[WASD] Move Around", RED)
        self.display_regular_text(x, 250, "[C] Controls", RED)
        self.display_regular_text(x, 300, "[<-] Last Page, [B] Back", RED)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_b]:
            self.game_mode = LANDING_PAGE
        if keys_pressed[pygame.K_LEFT]:
            self.game_mode = CREDITS










    def create_enemy(self):
        random_location = r.choice(ENEMY_LOCATIONS)
        self.enemy_spawn_timer -= 1
        if self.enemy_spawn_timer == 0:
            self.enemy_group.add(Enemy(self.screen, random_location[0], random_location[1], random_location[2]))
            self.enemy_spawn_timer = FPS

    def create_bullet(self):
        self.bullet_spawn_timer -= 1
        if self.bullet_spawn_timer <= 0:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                    self.bullet_spawn_timer = 15
                    self.bullet_group.add(Bullet(self.screen, self.player.x_coordinate, self.player.y_coordinate + 10, self.player.direction))



    def bullet_enemy_collision(self, bullet, enemy):
        if bullet.rect.colliderect(enemy.rect):
            self.score += 1
            print(self.score)
            return True
        else:
            return False

    def player_enemy_collision(self, player, enemy):
        if player.rect.colliderect(enemy.rect):
            self.damage = 0
            print(self.damage)
            self.game_mode = GAME_OVER





if __name__ == '__main__':
    sb = BlockFight()
    sb.game_loop()

