numbers = [1,4,23,3,2,1,0,9,7]

def sort_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    print(numbers)


def sort_declarative(numbers):
    numbers.sort(reverse = True)  
    print(numbers)

sort_imperative(numbers)
sort_declarative(numbers)
