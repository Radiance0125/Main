def compute_lcm(x, y, z):

   if (x > y) and (x > z):
       greater = x
   else:
       if y > z:
           greater = y
       else:
           greater = z

   while(True):
       if((greater % x == 0) and (greater % y == 0) and (greater % z == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("input the first number"))
num2 = int(input("input the second number"))
num3 = int(input("input the third number"))
calculate = True

if ((num1 == 0) or (num2 == 0) or (num3 == 0)):
    calculate = False
else:
    calculate = True

if ( calculate == True):
   print("The L.C.M. is", compute_lcm(num1, num2, num3))
else:
    print ("numbers invalid, no LCM")