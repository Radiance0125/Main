def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("input the first number"))
num2 = int(input("input the second number"))
calculate = True

if ((num1 == 0) or (num2 == 0)):
    calculate = False
else:
    calculate = True

if(calculate == True):
    print("The L.C.M. is", compute_lcm(num1, num2))
else:
    print("numbers invalid, no LCM")