def compute_hcf(x, y):
    
    if x < y:
        least = x
    else:
        least = y
    
    while(True):
      
        if ((x % least == 0) and (y % least == 0)):
            lcm = least
            break
        least -= 1 
    
    return least

num1 = int(input("input the first number:"))
num2 = int(input("input the second number:"))
calculate = True

if((num1 == 0) or (num2 ==0)):
    calculate = False
else:
    calculate = True

if (calculate == True):
    print("the H.C.F. is", compute_hcf(num1, num2))
else:
    print("numbers invalid, no LCM")