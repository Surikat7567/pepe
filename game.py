import pygame
pygame.init()
pygame.display.set_caption('Карти')

sc = pygame.display.set_mode((720,480)) # if it`s more than 900p is superfluous frames
clock = pygame.time.Clock()
fps = 25  # if it`s more than 45 is superfluous frames
bg = pygame.image.load('Assets/bg.bmp')
cb = pygame.image.load('Assets/02.bmp') #card`s back (rubaha)
cf1 = pygame.image.load('Assets/11.bmp') #card`s face (front) pic`s res == 67 x 100
rcf = pygame.image.load('Assets/11.bmp') #red card`s face (front) pic`s res == 80 x 120
bcf = pygame.image.load('Assets/blue.bmp')
gcf = pygame.image.load('Assets/green.bmp')
pcf = pygame.image.load('Assets/pink.bmp')
wcf = pygame.image.load('Assets/white.bmp')
winner_screen = pygame.image.load('Assets/win_win.bmp')
position_of_The_Red1 = (141,25)
position_of_The_Red2 = (445,165)
Blue_position1 = (233,165)
Blue_position2 = (405,328)
Green_position1 = (273,25)
Green_position2 = (537,25)
Pink_position1 = (141,328)
Pink_position2 = (537, 328)
White_position1 = (405,25)
White_position2 = (280,328)
click_counter = 0 # counts card clicks to prevent more than two face-up cards from being on the field
Red_Cards_Aktivated = 0 
Green_Cards_Aktivated = 0 
White_Cards_Aktivated = 0
Blue_Cards_Aktivated = 0 
Pink_Cards_Aktivated = 0

class Card:
    def __init__(self, position, cf, status): #cf == card`s face
        self.position = position
        self.cf = cf
        self.status = status
        self.status = 'passive'


    def status_change_on_passive(self):
        self.status = 'passive'

    def status_change_on_active(self):
        self.status = 'active'

    def status_check (self):
        if self.status  == 'passive':
            sc.blit(cb, (self.position))
        elif self.status == 'active':
            sc.blit(self.cf, (self.position)) 
        
    def current_sts(self):
        
        print(self.status)
        
RedCard1 = Card(position_of_The_Red1, rcf, '1')
RedCard2 = Card(position_of_The_Red2, rcf, '1')
GreenCard1 = Card(Green_position1, gcf, '1')
GreenCard2 = Card(Green_position2, gcf, '1')
BlueCard1 = Card(Blue_position1, bcf, '1')
BlueCard2 = Card(Blue_position2, bcf, '1')
PinkCard1 = Card(Pink_position1, pcf, '1')
PinkCard2 = Card(Pink_position2, pcf, '1')
WhiteCard1 = Card(White_position1, wcf, '1')
WhiteCard2 = Card(White_position2, wcf, '1')

while True:
    for event in pygame.event.get():
        
        sc.blit(bg, (0,0))
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (position_of_The_Red1[0] < pygame.mouse.get_pos()[0] < (position_of_The_Red1[0]+80))and(position_of_The_Red1[1] < pygame.mouse.get_pos()[1] < (position_of_The_Red1[1]+120)):
                RedCard1.status_change_on_active()
                click_counter += 1
            
            elif (Green_position1 [0] < pygame.mouse.get_pos()[0] < (Green_position1[0]+80))and(Green_position1[1] < pygame.mouse.get_pos()[1] < (Green_position1[1]+120)):
                GreenCard1.status_change_on_active()
                click_counter += 1

            elif (Green_position2 [0] < pygame.mouse.get_pos()[0] < (Green_position2[0]+80))and(Green_position2[1] < pygame.mouse.get_pos()[1] < (Green_position2[1]+120)):
                GreenCard2.status_change_on_active()
                click_counter += 1

            elif (position_of_The_Red2[0] < pygame.mouse.get_pos()[0] < (position_of_The_Red2[0]+80))and(position_of_The_Red2[1] < pygame.mouse.get_pos()[1] < (position_of_The_Red2[1]+120)):
                RedCard2.status_change_on_active()
                click_counter += 1

            elif (Blue_position1[0] < pygame.mouse.get_pos()[0] < (Blue_position1[0]+80))and(Blue_position1[1] < pygame.mouse.get_pos()[1] < (Blue_position1[1]+120)):
                BlueCard1.status_change_on_active()
                click_counter += 1

            elif (Blue_position2[0] < pygame.mouse.get_pos()[0] < (Blue_position2[0]+80))and(Blue_position2[1] < pygame.mouse.get_pos()[1] < (Blue_position2[1]+120)):
                BlueCard2.status_change_on_active()
                click_counter += 1

            elif (Pink_position1[0] < pygame.mouse.get_pos()[0] < (Pink_position1[0]+80))and(Pink_position1[1] < pygame.mouse.get_pos()[1] < (Pink_position1[1]+120)):
                PinkCard1.status_change_on_active()
                click_counter += 1

            elif (Pink_position2[0] < pygame.mouse.get_pos()[0] < (Pink_position2[0]+80))and(Pink_position2[1] < pygame.mouse.get_pos()[1] < (Pink_position2[1]+120)):
                PinkCard2.status_change_on_active()
                click_counter += 1

            elif (White_position1[0] < pygame.mouse.get_pos()[0] < (White_position1[0]+80))and(White_position1[1] < pygame.mouse.get_pos()[1] < (White_position1[1]+120)):
                WhiteCard1.status_change_on_active()
                click_counter += 1

            elif (White_position2[0] < pygame.mouse.get_pos()[0] < (White_position2[0]+80))and(White_position2[1] < pygame.mouse.get_pos()[1] < (White_position2[1]+120)):
                WhiteCard2.status_change_on_active()
                click_counter += 1


        if click_counter >= 3:
            RedCard1.status_change_on_passive()
            RedCard2.status_change_on_passive()
            GreenCard1.status_change_on_passive()
            GreenCard2.status_change_on_passive()
            BlueCard1.status_change_on_passive()
            BlueCard2.status_change_on_passive()
            PinkCard1.status_change_on_passive()
            PinkCard2.status_change_on_passive()
            WhiteCard1.status_change_on_passive()
            WhiteCard2.status_change_on_passive()
            click_counter = 0

        RedCard1.status_check()
        RedCard2.status_check()
        GreenCard1.status_check()
        GreenCard2.status_check()
        BlueCard1.status_check()
        BlueCard2.status_check()
        PinkCard1.status_check()
        PinkCard2.status_check()
        WhiteCard1.status_check()            
        WhiteCard2.status_check()
        
        if (RedCard1.status == 'active') and (RedCard2.status == 'active'):
            Red_Cards_Aktivated = 1
            print('Red_Cards_Aktivated')
        elif (GreenCard1.status == 'active') and (GreenCard2.status == 'active'):
            Green_Cards_Aktivated = 1
            print('Green_Cards_Aktivated')
        elif (WhiteCard1.status == 'active') and (WhiteCard2.status == 'active'):
            White_Cards_Aktivated = 1
            print('White_Cards_Aktivated')
        elif (PinkCard1.status == 'active') and (PinkCard2.status == 'active'):
            Pink_Cards_Aktivated = 1
            print("Pink_Cards_Aktivated")      
        elif (BlueCard1.status == 'active') and (BlueCard2.status == 'active'):
            Blue_Cards_Aktivated = 1
            print('Blue_Cards_Aktivated')

        if Red_Cards_Aktivated and Green_Cards_Aktivated and White_Cards_Aktivated and Blue_Cards_Aktivated and Pink_Cards_Aktivated == 1:
            sc.blit(winner_screen, (0,0))
            pygame.time.wait(10000)
        print(pygame.mouse.get_pos())
    #RedKingCard.current_sts()
    clock.tick(fps)
    pygame.display.flip()
    
