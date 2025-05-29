import pygame

# This Game class contains our game logic
class Game:
    def __init__(self,win,width,height):
        self.win = win
        self.width = width
        self.height = height
        self.main_screen = True
        self.game_over = False
        self.game_won = False
        self.game_start = False
        # Player side controllable stick's width, pos_x, pos_y, surface itself and the rect
        self.surface_width = self.width * 1.05/100
        self.surface_height = self.height/6

        # Player side stick
        self.player_surface_x = self.surface_width/2
        self.player_surface_y = self.height /2
        self.player_surface = pygame.Surface((self.surface_width,self.surface_height))
        self.player_surface_rect = self.player_surface.get_rect(center = (self.player_surface_x,self.player_surface_y))
        self.player_stick_velocity = self.height*2/100 # which should equal to speed of 10

        # Bot side stick 
        self.bot_surface_x = self.width - self.surface_width/2
        self.bot_surface_y = self.height/2
        self.bot_surface = pygame.Surface((self.surface_width,self.surface_height))
        self.bot_surface_rect = self.bot_surface.get_rect(center = (self.bot_surface_x,self.bot_surface_y))
        self.bot_stick_velocity = self.height * 1/100

        # Ball's work
        self.ball_image = pygame.image.load('game_files/ball/ball.png').convert_alpha()
        self.image_width,self.image_height = self.ball_image.get_size()
        self.ball_image = pygame.transform.scale(self.ball_image,(31,31))
        self.ball_x = self.width / 2
        self.ball_y = self.height / 2
        self.ball_rect = self.ball_image.get_rect(center = (self.ball_x,self.ball_y))
        self.ball_velocity = pygame.Vector2(self.width*0.7/100,self.height*1/100)

    def draw(self):
        self.player_surface.fill('#8c52ff')
        self.bot_surface.fill('#7e7c72')
        self.win.blit(self.player_surface,self.player_surface_rect)
        self.win.blit(self.ball_image,self.ball_rect)
        self.win.blit(self.bot_surface,self.bot_surface_rect)
    
    def update(self):
        self.ball_y += self.ball_velocity.y
        self.bot_surface_y += self.ball_velocity.y

        self.bot_surface_rect.center = (self.bot_surface_x,self.bot_surface_y)
        
        if self.ball_rect.colliderect(self.player_surface_rect):
            self.ball_velocity.x = -self.ball_velocity.x

            # we find the distance between ball rect centery and stick rect centery and then accordingly make the ball_velocity.y  equal to initial y speed * 4% of new distance. We make some if conditions too so that ball doesn't go insanely at y axis.

            distance =  self.ball_rect.centery-self.player_surface_rect.centery 
            if not distance == 0:
                self.ball_velocity.y = (self.height*1/100)*(distance * 4/ 100)
                if self.ball_velocity.y >= 15:
                    self.ball_velocity.y = 15
                if self.ball_velocity.y <= -15:
                    self.ball_velocity.y = -15

                print(f'Ball_velocity: {self.ball_velocity},distance: {distance}')          

        elif self.ball_rect.bottom >= self.height:
            self.ball_velocity.y = -self.ball_velocity.y

        elif self.ball_rect.top <= 0:
            self.ball_velocity.y = -self.ball_velocity.y

        elif self.ball_rect.colliderect(self.bot_surface_rect):
            self.ball_velocity.x = -self.ball_velocity.x

        elif self.ball_rect.left <= 0:
            self.game_over = True
            self.game_start = False
            self.game_won = False
            self.main_screen = False
        
        elif self.ball_rect.right >= self.width:
            self.game_over = False
            self.game_start = False
            self.game_won = True 
            self.main_screen = False

        self.ball_rect = self.ball_rect.move(self.ball_velocity)

    def player_controls(self,keys):
        if keys[pygame.K_w]:
            self.player_surface_y -= self.player_stick_velocity
            if self.player_surface_y <= 0 + self.surface_height/2:
                self.player_surface_y = self.surface_height/2
        if keys[pygame.K_s]:
            self.player_surface_y += self.player_stick_velocity
            if self.player_surface_y >= self.height - self.surface_height/2:
                self.player_surface_y = self.height - self.surface_height/2
        self.player_surface_rect.center = (self.player_surface_x,self.player_surface_y)