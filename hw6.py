array = [2, 6, 44, 35, -3, 18, 22]
array.sort()
print(array)
 
num = int(input("Insert number to find: "))
 
left = 0
right = len(array) - 1
 
while left <= right:
    center = (left + right) 
    if num == array[center]:
        print("Index of", num, "in list =", center)
        break
    if num > array[center]:
        left = center + 1
    else:
        right = center - 1
else:
    print("No such number")