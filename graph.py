from math import floor

def histo(arr):
    height = max(arr)

    for i in range(height, 0, -1):
        printstring = ""
        for j in arr:
            if j >= i:
                printstring += "#"
            else:
                printstring += " "
        print(printstring)

def rolldice(sides, numdice):
    # min = numdice
    # max = numdice * sides
    results = [0 for i in range(sides ** numdice)]
    for i in range(sides ** numdice):
        roll_result = 0
        for j in range(numdice) :
            roll_result += floor(j/(6 ** j)) % (6 ** (1 - j)) + 1
        results[roll_result] += 1
    return results

print(rolldice(6,1))