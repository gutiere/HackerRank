# Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 3/15/17

# Algorithm
# 1) Find all substrings through nested for loop.
# 2) Record total anagram equivelencies in dictionary.
# 3) Calculate total pairs per total anagram equivelencies.
# 4) Sum all pairs.

def main():
    cases = int(raw_input())

    for _ in range(cases):
        string = str(raw_input())
        print(calculateTotalPairs(getSubstrings(string)))

def getSubstrings(string):
    substrings = dict()
    for i in range(0, len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            anagram = ''.join(sorted(string[i:j]))
            if (anagram in substrings):
                substrings[anagram] = substrings[anagram] + 1
            else:
                substrings[anagram] = 1
    return substrings

def calculateTotalPairs(substrings):
    total = 0
    for key in substrings:
        total = total + totalPairsForDuplicates(substrings[key])
    return total

def totalPairsForDuplicates(number):
    total = 0
    for x in range(1, number):
        total = total + x
    return total

if __name__ == "__main__":
    main()
