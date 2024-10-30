def compute_hcf(x, y, z):
    
    if (x < y) and (x > z):
        least = x
    else:
        if (y < z):
            least = y
        else:
            least = z
    
    while (True):
        if((x % least == 0) and (y % least == 0) and (z % least == 0)):
            hcf = least
            break
        least -= 1
    
    return hcf

num1 = int(input("input the first number"))
num2 = int(input("input the second number"))
num3 = int(input("input the third number"))
calculate = True

if ((num1 == 0) or (num2 == 0) or (num3 == 0)):
    calculate = False
else:
    calculate = True

if (calculate == True):
    print ("the H.C.F. is", compute_hcf(num1, num2, num3))
else:
    print("numbers invalid, no HCF")