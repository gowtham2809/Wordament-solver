
class Node(object):
    def __init__(self):
        self.letters = {}
        self.is_word = False

    
    def add_letter(self, letter):
        if letter in self.letters:
            return self.letters[letter]
        self.letters[letter] = Node()
        return self.letters[letter]

class Trie(object):
    def __init__(self):
        self.root = Node()

    def load_word(self, word):
        curRef = self.root
        
        
        for letter in word:
            curRef = curRef.add_letter(letter)

        
        curRef.is_word = True

    
    def load_file(self, file_name):
        f = open(file_name)
        for line in f.readlines():
            word = line.strip()
            self.load_word(word)
        f.close()

    def print_recursive(self, node, prefix):
        
        if node.letters == {}:
            print (prefix)
            return
        
        if node.is_word:
            print (prefix)

        
        sortedKeys = sorted(node.letters.keys())
        for letter in sortedKeys:
            self.print_recursive(node.letters[letter], prefix + letter)

    
    def print_words(self):
        self.print_recursive(self.root, '')

    
    def has_word(self, word):
        curRef = self.root
        for letter in word:
            if letter in curRef.letters:
                curRef = curRef.letters[letter]
            else:
                return False
        if curRef.is_word:
            return True
        return False
            
def main():
    print ("Loading dictionary file...")
    t = Trie()
    t.load_file('dictionary.txt')
    print ("Dictionary loaded.\n")


if __name__ == '__main__':
    main()
