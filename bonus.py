
def print_number2(number):
    pattern = ""

    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j) + " "
        pattern += "\n"

    return pattern


number = int(input("Enter the number: "))

result = print_number2(number)

print(result)

