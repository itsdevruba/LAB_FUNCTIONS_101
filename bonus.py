
def print_pattern(number):
    pattern = ""

    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j) + " "
        pattern += "\n"

    return pattern


number = int(input("Enter the number: "))

result = print_pattern(number)

print(result)

