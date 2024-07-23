def fiponacci (i) :
    if i == 0 :
        return 0
    elif i == 1 :
        return 1
    else :
        return fiponacci(i-2) + fiponacci(i-1)

number = int(input("Enter your number : "))
for x in range (number):
    print (fiponacci(x))