# Problem: https://www.hackerrank.com/challenges/almost-sorted
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 2/19/17

# Algorithm
# 1) Record index of first and last '<' in comparison to the index's successor.
# 2) If all '<'s total 1 or 2, swap list[first - 1] with list[last]
# 3) Else, reverse list[first - 1] to list[last]

def main():
    #############################-Input-From-File-##############################
    # testCase = "AlmostSortedTestCase.txt"
    # file = open(testCase, "r")
    # file.readline()
    # numbers = [int(x) for x in str(file.readline()).split(" ")] # List elements
    ############################################################################
    raw_input() # Dummy input, not used.
    numbers = [int(x) for x in raw_input().split(" ")] # List elements

    if (check(numbers)): print("yes") # Already solved.
    else: # Not solved.
        info = sort(numbers) # Sort list if possible and recieve directions.
        if (info == None): # List is still not solved after one operation.
            print("no")
        else: # Print solving directions
            print("yes")
            print("{} {} {}".format(str(info[0]), str(info[1]), str(info[2])))

def swap(numbers, i, j): # Swap the two indices in a list.
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp

def reverse(numbers, i, j): # Reverse the list within the given indices.
    numbers[i:j + 1] = reversed(numbers[i:j + 1])

def sort(numbers): # Sort the given list and return feedback of the process.
    first, last, counter = None, None, 0
    for x in range(1, len(numbers)): # Find all "<"s.
        if (numbers[x] < numbers[x - 1]):
            if (first == None):
                first, last, counter = x, x, 1
            else:
                last, counter = x, counter + 1

    if (counter == 1 or counter == 2):
        swap(numbers, first - 1, last)
        return ["swap", first, last + 1]

    elif (counter > 2):
        reverse(numbers, first - 1, last)
        return ["reverse", first, last + 1]

    return None

def check(numbers): # Check if the list is solved.
    for x in range(1, len(numbers)): # Loop through list to identify "<"s.
        if (numbers[x] < numbers[x - 1]): return False
    return True

if __name__ == "__main__":
    main()
