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
    return 0