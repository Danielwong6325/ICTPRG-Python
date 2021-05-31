def PrintBoxByWidth(width, height):
    for row in range (height):
        for col in range(width):
            if col == 0 or col == width-1 or row ==0 or row == height -1:
                print("x", end="")
            elif (row == height//2):
                print("o",end="")
            else:
                print(" ", end="")
        print("")
PrintBoxByWidth(60,5)

