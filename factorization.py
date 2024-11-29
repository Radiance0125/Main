number = int(input(f"what is the number you wish to have factorized?\n"))

factors = []

prime = 2

if number.isdigit() == False:
    print("input error")
    exit()

def findprime():
    global prime
    prime += 1
    currentnum = prime-1
    for i in range(prime-2):
        if prime%currentnum == 0:
            findprime()
            break
        else:
            currentnum -= 1

def calculate():
    global number

    divisions = 0

    while number%prime == 0:
        number /= prime
        divisions += 1
    
    if divisions != 0:
        factors.append(f"{prime}^{divisions}")
    findprime()

while number != 1:
    calculate()

print(factors)