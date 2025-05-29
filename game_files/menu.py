import pygame

# This MenuScreens class contains all the menu stuff like main screen,win screen etc.
class MenuScreens():
    def __init__(self,screen,width,height,game,time):
        self.game = game
        self.screen  = screen
        self.width = width
        self.height = height
        self.time= time
        self.hover_width = self.height * 5/100
        
        self.menu_image = pygame.transform.scale(pygame.image.load('game_files/menu_stuff/main_menu.png').convert_alpha(),(self.width,self.height))
        self.game_over_image = pygame.transform.scale(pygame.image.load('game_files/menu_stuff/game_over.png').convert_alpha(),(self.width,self.height))
        self.game_won_image = pygame.transform.scale(pygame.image.load('game_files/menu_stuff/game_won.png').convert_alpha(),(self.width,self.height))


        # self.menu_image = 
        
    def get_rects(self,left,right,width,height):
        return pygame.Rect(left,right,(width,height))
    
    def get_hover_left(self, target_rect, scale_width, scale_height):
        
        left_img = pygame.transform.scale(
            pygame.image.load('game_files/menu_stuff/hover_left.png').convert_alpha(),
            (scale_width, scale_height)
        )
        left_img_rect = left_img.get_rect(topright=target_rect.topleft)
        self.screen.blit(left_img, left_img_rect)

    def get_hover_right(self, target_rect, scale_width, scale_height):
        right_img = pygame.transform.scale(pygame.image.load('game_files/menu_stuff/hover_right.png').convert_alpha(),(scale_width,scale_height))
        right_img_rect = right_img.get_rect(topleft = target_rect.topright)
        self.screen.blit(right_img,right_img_rect)


    def main_screen(self,mouse):
        self.screen.blit(self.menu_image,(0,0))
        left = (self.width/2)-(self.width*2/100)
        play_top = (self.height/2) - (self.height*5/100)
        quit_top = (self.height/2) + (self.height*9.5/100)
        height = self.height * 9.57 /100
        width = self.width * 12.5 / 100
        play_rect = pygame.Rect(left,play_top,width,height)
        quit_rect = pygame.Rect(left,quit_top,width,height)
        # pygame.draw.rect(self.screen,'black',play_rect)
        # pygame.draw.rect(self.screen,'white',quit_rect)
        mouse_x,mouse_y = mouse
        if play_rect.collidepoint(muse_x,mouse_y):
            self.get_hover_left(play_rect, self.hover_width, height)
            self.get_hover_right(play_rect,self.hover_width,height)        

        elif quit_rect.collidepoint(mouse_x,mouse_y):
            self.get_hover_left(quit_rect,self.hover_width,height)
            self.get_hover_right(quit_rect,self.hover_width,height)
            
        return play_rect,quit_rect
        
    def game_over_screen(self,mouse):
        self.screen.blit(self.game_over_imagoe,(0,0))
        try_again_left = (self.width/2)-(self.width*12/100)
        try_again_top = (self.height/2) - (self.height*11.4/100)
        try_again_width = self.width * 24 / 100
        try_again_height = self.height * 5 /100
        quit_left = (self.width/2) - (self.width * 9/100)
        quit_top = (self.height/2) - (self.height*0.4/100)
        quit_width = self.width * 18.3 /100
        quit_height = self.height * 8.57 /100
        mouse_x,mouse_y = mouse

        try_again_rect = pygame.Rect(try_again_left,try_again_top,try_again_width,try_again_height)
        quit_rect = pygame.Rect(quit_left,quit_top,quit_width,quit_height)
        # pygame.draw.rect(self.screen,'red',try_again_rect)
        # pygame.draw.rect(self.screen,'red',quit_rect)



        if try_again_rect.collidepoint(mouse_x,mouse_y):
            self.get_hover_left(try_again_rect, self.hover_width, try_again_height)
            self.get_hover_right(try_again_rect,self.hover_width,try_again_height)        

        elif quit_rect.collidepoint(mouse_x,mouse_y):
            self.get_hover_left(quit_rect,self.hover_width,quit_height)
            self.get_hover_right(quit_rect,self.hover_width,quit_height)

        return try_again_rect,quit_rect

    def game_won_screen(self,mouse):
        self.screen.blit(self.game_won_image,(0,0))

        play_again_left = (self.width/2)-(self.width*8/100)
        play_again_top = (self.height/2) - (self.height*12.7/100)
        play_again_width = self.width * 27 / 100
        play_again_height = self.height * 5 /100
        quit_left = (self.width/2) + (self.width * 35.8/100)
        quit_top = (self.height/2) - (self.height*45.8/100)
        quit_width = self.width * 11 /100
        quit_height = self.height * 5.4 /100
        mouse_x,mouse_y = mouse

        play_again_rect = pygame.Rect(play_again_left,play_again_top,play_again_width,play_again_height)
        quit_rect = pygame.Rect(quit_left,quit_top,quit_width,quit_height)
        # pygame.draw.rect(self.screen,'red',play_again_rect)
        # pygame.draw.rect(self.screen,'red',quit_rect)

        if play_again_rect.collidepoint(mouse_x,mouse_y):
            self.get_hover_left(play_again_rect, self.hover_width, play_again_height)
            self.get_hover_right(play_again_rect,self.hover_width,play_again_height)        

        elif quit_rect.collidepoint(mouse_x,mouse_y):
            self.get_hover_left(quit_rect,self.hover_width,quit_height)
            self.get_hover_right(quit_rect,self.hover_width,quit_height)

        return play_again_rect,quit_rect
