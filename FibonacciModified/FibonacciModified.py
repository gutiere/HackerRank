# Problem: https://www.hackerrank.com/challenges/fibonacci-modified
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 2/21/17

# Algorithm
# 1) Build memory array.
# 2) Add input to memory array indices 1 & 2.
# 3) Induce for loop from 3 to n.
# 4) Build memory based on last 2 consecutive elements in the memory array.

def main(): # Get input and print the result of getFib().
    numbers = [int(x) for x in raw_input().split(" ")]
    print(getFib(numbers[0], numbers[1], numbers[2]))

def getFib(i, j, n): # Return the modified Fibonacci value at index n.
    memory = [-1] * (n + 1)
    memory[1], memory[2] = i, j
    for x in range(3, n + 1):
        memory[x] = memory[x - 2] + (memory[x - 1] * memory[x - 1])
    return memory[n]

if __name__ == "__main__":
    main()
