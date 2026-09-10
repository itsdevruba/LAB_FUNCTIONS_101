
def print_numbers (number):
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print (j,end=" ")

        print()



number = int(input("enter the number:"))

print_numbers(number)




