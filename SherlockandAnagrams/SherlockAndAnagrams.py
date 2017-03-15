def main():
    cases = int(raw_input())

    for _ in range(cases):
        string = str(raw_input())
        # string = 'pvmupwjjjf'

        # Get all possible substrings of variable 'string'.
        subStrings = getSubstrings(string)

        # Get the number of anagram substring pairs in list.
        pairs = findPairs(subStrings)
        print(pairs)

def getSubstrings(string):
    substrings = []
    for i in range(0, len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    return substrings

def findPairs(subStrings):
    pairs = 0
    for i in range(0, len(subStrings)):
            for j in range(i + 1, len(subStrings)):
                if (compareSubstrings(subStrings[i], subStrings[j])):
                    pairs = pairs + 1
    return pairs

def compareSubstrings(sub1, sub2):
    return ''.join(sorted(sub1)) == ''.join(sorted(sub2))











if __name__ == "__main__":
    main()
