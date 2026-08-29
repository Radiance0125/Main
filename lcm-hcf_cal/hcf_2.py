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

num1 = int(input(f"input the first number:\n"))
num2 = int(input(f"input the second number:\n"))
calculate = True

if((num1 == 0) or (num2 ==0)):
    calculate = False
else:
    calculate = True

if (calculate == True):
    print("the H.C.F. is", compute_hcf(num1, num2))
else:
    print("numbers invalid, no LCM")