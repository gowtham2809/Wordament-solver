import re, random
from Data_struct import Trie

list_words = []


class Grid(object):
    SIZE = 4
    path = []
    paths = []
    ADJACENT_POINTS = {(0, 0):[(0, 1), (1, 0), (1, 1)],
                       (0, 1):[(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)],
                       (0, 2):[(0, 1), (0, 3), (1, 1), (1, 2), (1, 3)],
                       (0, 3):[(0, 2), (1, 2), (1, 3)],
                       (1, 0):[(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)],
                       (1, 1):[(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
                       (1, 2):[(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)],
                       (1, 3):[(0, 2), (0, 3), (1, 2), (2, 2), (2, 3)],
                       (2, 0):[(1, 0), (1, 1), (2, 1), (3, 0), (3, 1)],
                       (2, 1):[(1, 0), (1, 1), (2, 2), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2)],
                       (2, 2):[(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)],
                       (2, 3):[(1, 2), (1, 3), (2, 2), (3, 2), (3, 3)],
                       (3, 0):[(2, 0), (2, 1), (3, 1)],
                       (3, 1):[(2, 0), (2, 1), (2, 2), (3, 0), (3, 2)],
                       (3, 2):[(2, 1), (2, 2), (2, 3), (3, 1), (3, 3)],
                       (3, 3):[(2, 2), (2, 3), (3, 2)]}

    def __init__(self, tiles='abcdefghijklmnopqrstuvwxyz'):
        self.tiles = []
        self.grid = []

        
        r = re.compile(r'[a-z]|[(][a-z]+[)]', re.IGNORECASE)
        for tile in r.findall(tiles):
            self.tiles.append(tile.strip('(').strip(')'))

        
        for i in range(Grid.SIZE):
            self.grid.append([])
            for j in range(Grid.SIZE):
                self.grid[i].append(self.tiles[i * Grid.SIZE + j])

        self.words = []


    def suffix_from_point(self, node, valid_points, start_point, prefix, pth):
        
        if node.is_word and prefix not in self.words and len(prefix) > 2:
            #print("word : ", prefix)
            self.words.append(prefix)
            str = ""
            for i in pth:
                str += self.tiles[i[0] * 4 + i[1]]
            #print("path : ", str)
            self.paths.append(pth)           
        
        valid_points.remove(start_point) 
                
        valid_steps = []
        
        
        for point in self.ADJACENT_POINTS[start_point]:
            if point in valid_points:
                valid_steps.append(point)    
        
        
        for step in valid_steps:
            k, l = step
            tile = self.grid[k][l]
            if len(tile) > 1:
                
                curNode = node
                for letter in tile:
                    
                    if letter in curNode.letters.keys():
                        curNode = curNode.letters[letter]
                        
                    else:                        
                        return
                # print(prefix)
                pth.append((k, l)) 
                self.suffix_from_point(curNode, valid_points[:], (k, l), prefix + tile, pth[:])
                pth.pop()
            else:                
                if tile in node.letters.keys():
                    # print(prefix+tile,"\t(",k,",",l,")")
                    pth.append((k, l))
                    self.suffix_from_point(node.letters[tile], valid_points[:], (k, l), prefix + tile, pth[:])
                    pth.pop()

    def find_dictionary_words(self, loaded_trie):
        
        valid_points = []
        for i in range(Grid.SIZE):
            for j in range(Grid.SIZE):
                valid_points.append((i, j))
        
        
        for i in range(Grid.SIZE):
            for j in range(Grid.SIZE):                
                letter = self.grid[i][j]
                if letter in loaded_trie.root.letters:
                    # print("\n",letter,"\n"*2)                    
                    self.suffix_from_point(loaded_trie.root.letters[letter], valid_points[:], (i, j), self.grid[i][j], [(i, j)])
        
        #self.words = sorted(list(set(self.words)))
        flag = True
        while flag:
        	flag=False
        	for i in range(len(self.paths)-1):
        		if len(self.words[i]) < len(self.words[i+1]):
        			temp = self.words[i]
        			self.words[i] = self.words[i+1]
        			self.words[i+1] = temp
        			temp1 = self.paths[i]
        			self.paths[i]=self.paths[i+1]
        			self.paths[i+1] = temp1
        			flag = True
        			

        '''for i in self.words:
            #list_words.append(i)
            print(i)
        for i in self.paths:
            print(i)'''

	return self.words


def main():
    print ('Loading dictionary into trie...')
    
    # Implementing a trie data structure
    t = Trie()
    t.load_file("dictionary.txt")    
    print("Dictionary loaded")
    
    
    # g = Grid(input("Grid : "))
    g = Grid("abcdabcdabcdabcd")
    list1 = g.find_dictionary_words(t)
    
    list1 = sorted(list1, key=len, reverse=True)
    '''for i in list1:
       print(i + "\n")
    print(len(list1))'''
                    
if __name__ == '__main__':
    main()
