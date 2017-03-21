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
    return difference(diff) == len(subgene)

def findAllSubstrings(gene):
    if gene.count('A') == gene.count('C') == gene.count('T') == gene.count('G'):
        return 0

    # Loop through every possible subgene length, 1 to the length of the gene.
    for subLength in range(difference(gene) / 4, len(gene) + 1):
        for shift in range(len(gene) - subLength + 1):
            if possiblility(gene, gene[shift:shift + subLength]):
                return subLength
    return -1
def difference(gene):
    letters = {'A': gene.count('A'),
            'C': gene.count('C'),
            'T': gene.count('T'),
            'G': gene.count('G')}

    difference = 0
    highest = max(letters, key=letters.get)
    for letter in letters:
        difference = difference + letters[highest] - letters[letter]
    return difference

if __name__ == "__main__":
    main()
