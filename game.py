import pygame
pygame.init()
pygame.display.set_caption('Карти')
pygame.mixer.pre_init(44100, -16, 1, 512)

sc = pygame.display.set_mode((1200,750)) # if it`s more than 900p is superfluous frames
clock = pygame.time.Clock()
fps = 25  # if it`s more than 30 is superfluous frames
bg = pygame.image.load('Assets/bg.png')
cb = pygame.image.load('Assets/02.png') #card`s back (rubaha)
rcf = pygame.image.load('Assets/11.png') #red card`s face (front) pic`s res == 80 x 120
bcf = pygame.image.load('Assets/blue.jpg')
gcf = pygame.image.load('Assets/green.png')
pcf = pygame.image.load('Assets/pink.jpeg')
wcf = pygame.image.load('Assets/white.png')
winner_screen = pygame.image.load('Assets/win_win.png')
pygame.mixer.music.load('Assets/sounds/Shadilay - P.E.P.E. - Lyrics.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.0)
sound_card = pygame.mixer.Sound('Assets/sounds/sound_16516.mp3')
nice = pygame.mixer.Sound('Assets/sounds/Nice.ogg')
win_win = pygame.mixer.Sound('Assets/sounds/Omedetou - Evangelion.mp3')
position_of_The_Red1 = (80,25)
position_of_The_Red2 = (740,255)
Blue_position1 = (233,255)
Blue_position2 = (620,495)
Green_position1 = (350,25)
Green_position2 = (890,25)
Pink_position1 = (80,495)
Pink_position2 = (890, 495)
White_position1 = (620,25)
White_position2 = (350,495)
click_counter = 0 # counts card clicks to prevent more than two face-up cards from being on the field
Red_Cards_Aktivated = 0 
Green_Cards_Aktivated = 0 
White_Cards_Aktivated = 0
Blue_Cards_Aktivated = 0 
Pink_Cards_Aktivated = 0
cb1 = pygame.image.load('Assets/02(1).png')
cb2 = pygame.image.load('Assets/02(2).png')
cb3 = pygame.image.load('Assets/02(3).png')
pausT= 70
trash_didg = 0 


class Card:
    def __init__(self, position, cf, status): #cf == card`s face
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]
        self.cf = cf
        self.status = status
        self.status = 'passive'
        self.hitbox = (self.x, self.y, 230, 210)

    def status_change_on_passive(self):
        self.status = 'passive'

    def status_change_on_active(self):
        sound_card.play()
        sc.blit(self.cf, (self.position))
        sc.blit(cb1, (self.position))
        pygame.display.update(pygame.Rect(self.x, self.y, 230, 210)), pygame.time.wait(pausT),
        sc.blit(self.cf, (self.position))
        sc.blit(cb2, (self.position))
        pygame.display.update(pygame.Rect(self.x, self.y, 230, 210)), pygame.time.wait(pausT),
        sc.blit(self.cf, (self.position))
        sc.blit(cb3, (self.position))
        pygame.display.update(pygame.Rect(self.x, self.y, 230, 210)), pygame.time.wait(pausT),
        sc.blit(self.cf, (self.position))
        #Animashka ends
        self.status = 'active'
        clock.tick(fps)

    def status_check (self):
        if self.status  == 'passive':
            sc.blit(cb, (self.position))
        elif self.status == 'active':
            
            sc.blit(self.cf, (self.position)) 
        pygame.draw.rect(sc, (255,0,0), self.hitbox,2)

    def current_sts(self):
        
        print(self.position, '\n', self.x , self.y)
        
    
        
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
            if (position_of_The_Red1[0] < pygame.mouse.get_pos()[0] < (position_of_The_Red1[0]+230))and(position_of_The_Red1[1] < pygame.mouse.get_pos()[1] < (position_of_The_Red1[1]+210)):
                RedCard1.status_change_on_active()
                click_counter += 1
            
            elif (Green_position1 [0] < pygame.mouse.get_pos()[0] < (Green_position1[0]+230))and(Green_position1[1] < pygame.mouse.get_pos()[1] < (Green_position1[1]+210)):
                GreenCard1.status_change_on_active()
                click_counter += 1

            elif (Green_position2 [0] < pygame.mouse.get_pos()[0] < (Green_position2[0]+230))and(Green_position2[1] < pygame.mouse.get_pos()[1] < (Green_position2[1]+210)):
                GreenCard2.status_change_on_active()
                click_counter += 1

            elif (position_of_The_Red2[0] < pygame.mouse.get_pos()[0] < (position_of_The_Red2[0]+230))and(position_of_The_Red2[1] < pygame.mouse.get_pos()[1] < (position_of_The_Red2[1]+210)):
                RedCard2.status_change_on_active()
                click_counter += 1

            elif (Blue_position1[0] < pygame.mouse.get_pos()[0] < (Blue_position1[0]+230))and(Blue_position1[1] < pygame.mouse.get_pos()[1] < (Blue_position1[1]+210)):
                BlueCard1.status_change_on_active()
                click_counter += 1

            elif (Blue_position2[0] < pygame.mouse.get_pos()[0] < (Blue_position2[0]+230))and(Blue_position2[1] < pygame.mouse.get_pos()[1] < (Blue_position2[1]+210)):
                BlueCard2.status_change_on_active()
                click_counter += 1

            elif (Pink_position1[0] < pygame.mouse.get_pos()[0] < (Pink_position1[0]+230))and(Pink_position1[1] < pygame.mouse.get_pos()[1] < (Pink_position1[1]+210)):
                PinkCard1.status_change_on_active()
                click_counter += 1

            elif (Pink_position2[0] < pygame.mouse.get_pos()[0] < (Pink_position2[0]+230))and(Pink_position2[1] < pygame.mouse.get_pos()[1] < (Pink_position2[1]+210)):
                PinkCard2.status_change_on_active()
                click_counter += 1

            elif (White_position1[0] < pygame.mouse.get_pos()[0] < (White_position1[0]+230))and(White_position1[1] < pygame.mouse.get_pos()[1] < (White_position1[1]+210)):
                WhiteCard1.status_change_on_active()
                click_counter += 1

            elif (White_position2[0] < pygame.mouse.get_pos()[0] < (White_position2[0]+230))and(White_position2[1] < pygame.mouse.get_pos()[1] < (White_position2[1]+210)):
                WhiteCard2.status_change_on_active()
                click_counter += 1
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (RedCard1.status == 'active') and (RedCard2.status == 'active'):
                Red_Cards_Aktivated = 1
                nice.play()
                print('Red_Cards_Aktivated')
            elif (GreenCard1.status == 'active') and (GreenCard2.status == 'active'):
                Green_Cards_Aktivated = 1
                nice.play()
                print('Green_Cards_Aktivated')
            elif (WhiteCard1.status == 'active') and (WhiteCard2.status == 'active'):
                White_Cards_Aktivated = 1
                nice.play()
                print('White_Cards_Aktivated')
            elif (PinkCard1.status == 'active') and (PinkCard2.status == 'active'):
                Pink_Cards_Aktivated = 1
                nice.play()
                print("Pink_Cards_Aktivated")      
            elif (BlueCard1.status == 'active') and (BlueCard2.status == 'active'):
                Blue_Cards_Aktivated = 1
                nice.play()
                print('Blue_Cards_Aktivated')


            else:
                click_counter += 1

        if click_counter >= 3:
            pygame.time.delay(80)
            click_counter += 1
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
        
       
        if (Red_Cards_Aktivated and Green_Cards_Aktivated and White_Cards_Aktivated and Blue_Cards_Aktivated and Pink_Cards_Aktivated) == 1:
            Red_Cards_Aktivated = '2' 
            Green_Cards_Aktivated = '2' 
            White_Cards_Aktivated = '2' 
            Blue_Cards_Aktivated = '2'
            Pink_Cards_Aktivated = '2'
            pygame.time.delay(100)
            pygame.mixer.music.set_volume(0.0)
            print(Green_Cards_Aktivated)
            win_win.play()
            print('wtf')
            win_win.set_volume(0.3)
            sc.blit(winner_screen, (0,40))
            trash_didg += 1
            #pygame.display.flip()
        if trash_didg >= 1 :
            sc.blit(winner_screen, (0,40))
        #print(pygame.mouse.get_pos())
    clock.tick(fps)
    pygame.display.flip()
    