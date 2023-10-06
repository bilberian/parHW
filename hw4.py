import statistics
import cmath

array_x = [0.88, 0.2, 0.7, 0.11, 0.25]
array_y = [0.44, 0.56, 0.12, 0.89, 0.71]

# получение среднео значения элементов массива
mean_x = statistics.mean(array_x)
mean_y = statistics.mean(array_y)

#функция для получения массива из разницы Х[i] (или Y[i]) и их средних значений
def array_subtraction(array, number):
    result_array = []
    for i in range(len(array)):
        result_array.append(array[i] - number)
    return result_array

# возведение в степень элементов массива
def array_exponent(array):
    squared_array = [x * x for x in array]
    return squared_array

# функция для перемножения массивов
def arrays_multiplication (arr1, arr2):
    result_array = []
    for i in range(len(arr1)):
        result_array.append(arr1[i]*arr2[i])  
    return result_array

# функция для вычисления формулы Пирсона
def pearson(array_x, array_y):
    # получаю делимое
    dividend = sum(arrays_multiplication(array_subtraction(array_x, mean_x), array_subtraction(array_y, mean_y)))
    # получаю делитель
    divisor = cmath.sqrt(sum(array_exponent(array_subtraction(array_x, mean_x)))) * cmath.sqrt(sum(array_exponent(array_subtraction(array_y, mean_y))))
    return dividend/divisor

print(pearson(array_x, array_y))
