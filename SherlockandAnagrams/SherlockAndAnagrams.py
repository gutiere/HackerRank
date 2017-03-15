# Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 3/15/17

# Algorithm
# 1) Find all substrings through nested for loop.
# 2) Record total anagram equivelencies in dictionary.
# 3) Calculate total pairs per total anagram equivelencies.
# 4) Sum all pairs.

def main():

    # Total number of cases.
    cases = int(raw_input())

    # Loop through all cases.
    for _ in range(cases):
        # Get get next string.
        string = str(raw_input())

        # Get dictionary of anagrams and their recurrences.
        substrings = getAnagrams(string);

        # Get total pairs of anagrams.
        totalPairs = calculateTotalPairs(substrings)

        # Total pairs.
        print(totalPairs)

# Returns a dictionary of anagrams and their recurrence quantites.
def getAnagrams(string):

    # Dictionary where key = anagram, value = anagram recurrence.
    getAnagrams = dict()

    for i in range(0, len(string) + 1):
        for j in range(i + 1, len(string) + 1):

            # Alphabetically sorted substrings.
            anagram = ''.join(sorted(string[i:j]))

            # Anagram already exists.
            if (anagram in getAnagrams):
                getAnagrams[anagram] = getAnagrams[anagram] + 1

            # New anagram.
            else:
                getAnagrams[anagram] = 1
    return getAnagrams

# Returns the total number of pairs given a the quantities of recurrences.
def calculateTotalPairs(anagrams):

    totalPairs = 0

    # Loop through all anagrams.
    for anagram in anagrams:

        # Sum all anagram pairs.
        totalPairs = totalPairs + totalPairsForRecurrences(anagrams[anagram])

    return totalPairs

# Calculate the total pairs for all recurrences.
def totalPairsForRecurrences(recurrences):

    totalPairs = 0

    # Loop through every word and total all pairs per node (recurrence).
    for x in range(recurrences):

        # Sum all recurrence pairs.
        totalPairs = totalPairs + x

    return totalPairs

if __name__ == "__main__":
    main()
