
#Owner Gowtham Raj

import pygame, sys, operator,time
from Data_struct import Trie
from Main import Grid
from threading import Thread




class Game(Grid):    
    def __init__(self):        
        pygame.init()
        self.size = 800, 800
        self.textColor = 255, 255, 255
        self.coOrdinates_list = [(100, 75), (250, 75), (400, 75), (550, 75),
                            (100, 225), (250, 225), (400, 225), (550, 225),
                            (100, 375), (250, 375), (400, 375), (550, 375),
                            (100, 525), (250, 525), (400, 525), (550, 525)
                            ]

        self.screen = pygame.display.set_mode(self.size)

        # loading BackGround
        self.bg = pygame.image.load("res/background.png")
        self.bgRect = self.bg.get_rect()
        self.screen.blit(self.bg, self.bgRect)        

        # load fonts
        self.font = pygame.font.Font("res/SEGOEUI.TTF", 80)        
        
        # load the Dictionary
        print("Loading Dictionary")
        self.t = Trie()
        self.t.load_file("dictionary.txt")
        print("Dictionary Loaded")
        
        # get the list of words from Main.py file
        self.text = raw_input("Grid : ")
        super(Game,self).__init__(self.text)
        self.words_list = self.find_dictionary_words(self.t)
        #print(self.words_list)
        
        # display the 4*4 boxes
        self.display_grid()
    
    #display orange grid
    def display_grid(self):
        gridImg = pygame.image.load("res/grid.png")
        
        # display the grid
        for i in range(16):
            singleGrid = gridImg.get_rect()
            singleGrid = singleGrid.move(self.coOrdinates_list[i])
            self.screen.blit(gridImg, singleGrid)
        self.put_text()
        
        # put text in that grid
    def put_text(self):
        
        for i in range(16):
            txt = self.tiles[i]
            txt = txt.upper()
            letter = self.font.render(txt, 1, (255, 255, 255))
            letter_rect = letter.get_rect()
            pos = tuple(map(operator.add, self.coOrdinates_list[i], (50, 15)))
            letter_rect = letter_rect.move(pos)
            self.screen.blit(letter, letter_rect)
        self.render()
    
	#display word by word
    def display_word(self,path,word):
	gridImg = pygame.image.load("res/selectedgrid.png")
	self.screen.blit(self.bg, self.bgRect)
	self.display_grid()
	txt = word
	txt = txt.upper()
        letter = self.font.render(txt, 1, (255, 255, 255))
        letter_rect = letter.get_rect()
        pos = (0,-10)
        letter_rect = letter_rect.move(pos)
        self.screen.blit(letter, letter_rect)
	self.render()
        for i in path:
            index = i[0]*4+i[1]
            singleGrid = gridImg.get_rect()
            singleGrid = singleGrid.move(self.coOrdinates_list[index])
            self.screen.blit(gridImg, singleGrid)
            self.put_text()
	    pygame.time.delay(400)
	
            
        
        
         
    def render(self):
        pygame.display.flip()
        
    def run(self):
        
        for i in range(len(self.paths)):
            self.display_grid()
            self.display_word(self.paths[i],self.words[i])
	    pygame.time.delay(400)
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

x = Game()
x.run()

