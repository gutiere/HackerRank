# Problem: https://www.hackerrank.com/challenges/bear-and-steady-gene
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 3/15/17

# Algorithm
# 1)


def main():
    raw_input()
    print(findAllSubstrings(str(raw_input())))

# Returns true if the replacing this subgene can create a stable gene.
def possiblility(gene, subgene):

    diff = gene.replace(subgene, '', 1)

    letters = {'A': diff.count('A'),
            'C': diff.count('C'),
            'T': diff.count('T'),
            'G': diff.count('G')}

    difference = 0
    highest = max(letters, key=letters.get)
    for letter in letters:
        difference = difference + letters[highest] - letters[letter]
    return difference == len(subgene)

def findAllSubstrings(gene):
    if gene.count('A') == gene.count('C') == gene.count('T') == gene.count('G'):
        return 0

    # Loop through every possible subgene length, 1 to the length of the gene.
    for subLength in range(1, len(gene) + 1):
        for shift in range(len(gene) - subLength + 1):
            if possiblility(gene, gene[shift:shift + subLength]):
                return subLength
    return -1

if __name__ == "__main__":
    main()
