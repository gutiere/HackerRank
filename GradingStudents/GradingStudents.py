# Problem: https://www.hackerrank.com/challenges/grading
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 3/22/17

from __future__ import print_function

def main():
    n = int(raw_input().strip())
    for _ in xrange(n):
        grade = int(raw_input().strip())
        if grade >= 38 and getNextMultiple(grade) - grade < 3:
            print(getNextMultiple(grade))
        else:
            print(grade)

def getNextMultiple(number):
    value = number
    while (value % 5 != 0):
        value = value + 1
    return value

if __name__ == "__main__":
    main()
