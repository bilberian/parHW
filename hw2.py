

number = int(input('Insert a number: '))

def multTable(num):
    for i in range(1, num):
        for j in range (1, num):
            print(i,"+", j, "=", i * j)
        print()

multTable(number)