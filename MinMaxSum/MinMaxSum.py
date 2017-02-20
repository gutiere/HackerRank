# Problem: https://www.hackerrank.com/challenges/mini-max-sum
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 2/19/17

# Algorithm
# 1) Record indices of l and s values.
# 2) Print sum of numbers without the l index.
# 3) Print sum of numbers without the s idex.

def main():
    numbers = [int(x) for x in raw_input().split(" ")] # List elements
    total, large, small = 0, 0, 0
    for i in range(0, len(numbers)):
        if (numbers[large] < numbers[i]): large = i
        if (numbers[small] > numbers[i]): small = i
        total = total + numbers[i]
    print("{} {}".format(total - numbers[large], total - numbers[small]))

if __name__ == "__main__":
    main()
