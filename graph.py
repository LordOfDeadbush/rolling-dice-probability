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

histo([1,2,3,2,1])
print("a")