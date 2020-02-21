import math
def CheckIfStringIsPrime(string):
    string=''.join(str(ord(c)) for c in string)
    number=int(string)
    print("String in ASCII is:",number)
    #Using eratosthenes'sieve to check if the given number is a string
    PrimesToNumber=[]
    for i in range(2,number+1):
        PrimesToNumber.append(i)

    i = 2
    #from 2 to sqrt(number)
    while(i <= int(math.sqrt(number))):
        #if i is in list
        #then we gotta delete its multiples
        if i in PrimesToNumber:
            #j will give multiples of i,
            #starting from 2*i
            for j in range(i*2, number+1, i):
                if j in PrimesToNumber:
                    #deleting the multiple if found in list
                    PrimesToNumber.remove(j)
        i = i+1
    if number in PrimesToNumber:
        print("Your number is a prime")
    else:
        print("Not a prime")
    return 0    


print(CheckIfStringIsPrime("h"))

