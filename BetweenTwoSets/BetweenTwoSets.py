# Problem: https://www.hackerrank.com/challenges/between-two-sets
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 2/24/17

# Algorithm
# 1) Find smallest element of 16, this is the upper bound to possible x.
# 2) For all possible values of x, find the valid conditions.
# 3) Increment counter when valid value of x is found.

def main():
    # Get input
    ab = [int(x) for x in raw_input().split(" ")] # Get list lengths.
    A = [int(x) for x in raw_input().split(" ")] # Get 'A' list elements.
    B = [int(x) for x in raw_input().split(" ")] # Get 'B' list elements.

    # General instantiations.
    counter = 0
    smallest = 100

    # Find smallest element in B list.
    for b in B:
        if (smallest > b):
            smallest = b

    # Loop through all possible values of x in the range [1 - b].
    for x in range(1, smallest + 1):
        bFactor = True
        # Loop through all values of B to confirm x is a factor of b.
        for b in B:
            if (b % x != 0):
                bFactor = False

        if (bFactor):
            aFactor = True
            # Loop through all values of A to confirm a is a factor of x.
            for a in A:
                if (x % a != 0):
                    aFactor = False
            # a is a factor of x and x is a factor of b.
            if (aFactor):
                counter += 1

    print(counter)

if __name__ == "__main__":
    main()
