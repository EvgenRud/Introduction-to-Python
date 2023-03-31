# Функция для расчета среднего арифметического
def average(numbers):
    value = sum(numbers) / len(numbers)
    print(f'Функцию вызвали с параметром {value}')
    return value

my_list = [4,7,2,5,4]
average(my_list)





