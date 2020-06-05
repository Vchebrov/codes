test_list = []
for i in range(100):

    import random

    x = 0
    y = 100  # Задай верхнюю границу диапазона
    n = random.randint(x, y)
    print('Угадай число', n)

    c = y - x
    count = 0
    while count != 100:
        z = c
        i = int(z / 2) # начало бинарного поиска

        count += 1 # счётчик попыток
        if i > n:
            y = i
            c = y - x
        elif i < n:
            x = i
            c = x + y
        elif i == n:
            print('Вы угадали число {} с {} попыток'.format(n, count))
            break
        test_list.append(count)

print('Final test results', test_list)
print('Максимальное количество попыток', max(test_list))
print('Минимальное количество попыток', min(test_list))
print('Среднее количество попыток', sum(test_list) / len(test_list))
