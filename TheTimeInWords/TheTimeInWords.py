# Problem: https://www.hackerrank.com/challenges/the-time-in-words
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 3/22/17

# Note: Sloppy solution, I'll come back to optimize eventually.

from __future__ import print_function

def main():
    h = int(raw_input().strip())
    m = int(raw_input().strip())
    calculateWords(h,m)

    # TEST
    # h = 5
    # m = 45
    # for m in range(60):
    #    calculateWords(h, m)

def calculateWords(h, m):
        hours = {12:"twelve", 11:"eleven", 10:"ten", 9:"nine", 8:"eight", 7:"seven", 6:"six", 5:"five", 4:"four", 3:"three", 2:"two", 1:"one"}
        fractions = {45:"quarter to ", 30:"half past ", 15:"quarter past "}
        minutes = {20:"twenty", 19:"nineteen", 18:"eighteen", 17:"seventeen", 16:"sixteen", 14:"fourteen", 13:"thirteen", 12:"twelve", 11:"eleven", 10:"ten"}
        ones = {9:"nine", 8:"eight", 7:"seven", 6:"six", 5:"five", 4:"four", 3:"three", 2:"two", 1:"one"}
        string = ""

        # On the hour.
        if m == 0:
            string = hours[h] + " o' clock"
        else:
            # 45, 30, or 15 minutes.
            if m in fractions:
                if m == 45:
                    h = h + 1
                string = fractions[m] + hours[h]
            else:
                # Minutes below 10.
                if m < 10:
                    if m == 1:
                        string = ones[m] + " minute past " + hours[h]
                    else:
                        string = ones[m] + " minutes past " + hours[h]
                # Minutes below 21
                elif m <= 20:
                    string = minutes[m] + " minutes past " + hours[h]
                elif m < 30:
                    string = "twenty " + ones[m - 20] + " minutes past " + hours[h]
                # Minutes 21 to 29
                else:
                    h = h + 1
                    if m > 30:
                        m = 60 - m
                    if m > 20:
                        string = "twenty " + ones[m - 20] + " minutes to " + hours[h]
                    elif m > 9:
                        string = minutes[m] + " minutes to " + hours[h]
                    else:
                        if m == 1:
                            string = ones[m] + " minute to " + hours[h]
                        else:
                            string = ones[m] + " minutes to " + hours[h]
        print(string)

if __name__ == "__main__":
    main()
