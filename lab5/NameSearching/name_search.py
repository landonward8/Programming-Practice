import numpy as np 
import argparse

class NameSearch:

    def __init__(self, Name_List, Name_Algorithm, Name_Length):
        # Matrix of the word search puzzle 
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm
        self.Name_Algorithm = Name_Algorithm
        # Length of the name
        self.Name_Length = Name_Length
        # List of all potential names 
        with open("./data/names/"+Name_List+".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]

    def match_BruteForce(self, pattern, text):
        m = len(pattern)
        n = len(text)
        for i in range(n - m + 1):
            j = 0
            # while j is less than the length of the pattern 
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                return pattern 
        return None
   

    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        # Your code goes here:
        print(pattern)
        
    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix 
        for pattern in self.names:
            # if len(pattern) == length:
                for text in self.matrix:
                        if self.Name_Algorithm == "BruteForce" and self.Name_Length == len(pattern):
                            print(self.match_BruteForce(pattern, text))
                          #  print(pattern)
                           # print(pattern)
                        elif self.Name_Algorithm == "Horspool":
                            self.match_Horspool(pattern, text)
            # call self.match_Horspool(pattern, text)

if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Mexican -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    obj.search()


