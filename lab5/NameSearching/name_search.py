import numpy as np 
import argparse
# landon ward
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
        m = 0
        n = self.Name_Length
        while m + n <= len(text):
            shift = text[m:m+n]
            isWord = False
            for i in range(len(pattern)):
                if pattern[i] != shift[i]:
                    break
            else:
                isWord = True

            if isWord:
                print(shift)
                return
            else:
                m += 1
        

    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        # Your code goes here:
        # 
# Horspool’s algorithm
# Step 1 For a given pattern of length m and the alphabet used in both the pattern and text, construct the shift table as described above.
# Step 2 Align the pattern against the beginning of the text.
# Step 3 Repeat the following until either a matching substring is found or the pattern reaches beyond the last character of the text. Starting with the last character in the pattern, compare the corresponding characters in the pattern and text until either all m characters are matched (then
        # HorspoolMatching(P [0..m − 1], T [0..n − 1] ) //Implements Horspool’s algorithm for string matching
# //Input: Pattern P [0..m − 1] and text T [0..n − 1]
# //Output: The index of the left end of the first matching substring // or −1 if there are no matches
# ShiftTable(P [0..m − 1] ) i ← m − 1
# while i ≤ n − 1 do
# k ← 0
# while k ≤ m − 1 and P [m − 1 − k] = T [i − k] do
# k←k+1 if k = m
# return i − m + 1 else i←i+Table[T[i]]
# return −1
# I did use chatgpt to help me understand the algorithm because I did not get help from my lab partner, but did not use code from chatpgt. Happy to explain my code if needed.
        #setp 1
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shift_table = {letter: self.Name_Length for letter in alphabet}
        for letter in alphabet:
            shift_table[letter] = self.Name_Length

        for i in range(self.Name_Length - 1):
            shift_table[pattern[i]] = self.Name_Length - 1 - i
        # step 2
        m = 0
        n = len(pattern)
        # step 3
        while m <= len(text) - n:
            shift = text[m:m+n]
            if pattern[-1] == shift[-1]:
                isWord = True
                for i in reversed(range(n-1)):
                    if pattern[i] != shift[i]:
                        m += shift_table.get(shift[-1], self.Name_Length)
                        isWord = False
                        break
                if isWord:
                    print(shift)
                m += 1
            else:
                m += shift_table.get(shift[-1], self.Name_Length)

        
    def search(self):
    # pattern is each name in self.names
    # text is each horizontal, vertical, and diagonal strings in self.matrix 
        row, col = self.matrix.shape
        name = []
        for n in self.names:
            if len(n) == self.Name_Length:
                name.append(n)
        if self.Name_Algorithm == "BruteForce":
            for i in range(row):
                for j in range(col):
                    for n in name:
                        self.match_BruteForce(n, self.matrix[i, :])
                        self.match_BruteForce(n, self.matrix[:, j])
            for k in reversed(range(row)):
                for l in range(col):
                    for n in name:
                        self.match_BruteForce(n, np.diagonal(self.matrix, k - l))
                        self.match_BruteForce(n, np.diagonal(np.fliplr(self.matrix), l - k))
        if self.Name_Algorithm == "Horspool":
            for i in range(row):
                for j in range(col):
                    for n in name:
                        self.match_Horspool(n, self.matrix[i, :])
                        self.match_Horspool(n, self.matrix[:, j])
            for k in reversed(range(row)):
                for l in range(col):
                    for n in name:
                        self.match_Horspool(n, np.diagonal(self.matrix, k - l))
                        self.match_Horspool(n, np.diagonal(np.fliplr(self.matrix), l - k))
                

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
    print("Done")


