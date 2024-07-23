list = []



def add ():
    addition = input("add your tasks")
    list.append(addition)
    print("Done")

def viewing ():
    view_q = input( "Would you like to view all list / yes or no" )
    if view_q == "yes":
        print (list)
    else :
        print(" ")

def delete ():
    del_q = input("Do you want to delete any thing  yes / no :")
    if del_q == "yes" :
        re = (input("Enter its arrangement to remove "))
        list.remove(re)
    else:
        print("")

def marking ():
    number=int(input("How many numbers do you finish"))
    for i in range (number):
        print(list[i]+"finished")

add()
print(add)
viewing()
print(viewing)
delete()
print (delete)
marking()
print(marking)