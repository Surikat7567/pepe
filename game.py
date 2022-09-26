import pygame
pygame.init()
pygame.display.set_caption('Карти')

sc = pygame.display.set_mode((720,480)) # if it`s more than 900p is superfluous frames
clock = pygame.time.Clock()
fps = 25  # if it`s more than 45 is superfluous frames
bg = pygame.image.load('Assets/bg.bmp')
cb = pygame.image.load('Assets/02.bmp') #card`s back (rubaha)
cf1 = pygame.image.load('Assets/11.bmp') #card`s face (front) pic`s res == 67 x 100
position_of_The_RedKing = (90,50)

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
        
RedKingCard = Card(position_of_The_RedKing, cf1, '1')

while True:
    for event in pygame.event.get():
        
        sc.blit(bg, (0,0))
        if event.type == pygame.QUIT:
            exit()
        elif event.type ==  pygame.MOUSEBUTTONDOWN:
            RedKingCard.status_change_on_active()
        RedKingCard.status_check()
    RedKingCard.current_sts()
    clock.tick(14)
    pygame.display.flip()
    