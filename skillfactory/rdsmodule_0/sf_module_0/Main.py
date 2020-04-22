#!/usr/bin/env python
# coding: utf-8

# In[1]:


test_list = []
for i in range(100):
    
    import random
    
    # x = int(input('Укажите нижний диапазон:'))
    # y = int(input('Укажите верхний диапазон:'))
    x = 0
    y = 100 # Задай верхнюю границу диапазона
    n = random.randint(x,y)
    print('Угадай число', n)
    
    c = y - x
    count = 0
    while count!= 100:
        z = c
        i = int(z/2)
#         print(i,x,y)
        count += 1
        if i > n:
#             print('more')
            y = i
            c = y - x
        elif i < n:
#             print('less')
            x = i
            c = x + y
        elif i == n:
            print('Вы угадали число {} с {} попыток'.format(n,count))
            break
        test_list.append(count)
print('Final test results', test_list)
print('Максимальное количество попыток', max(test_list))
print('Минимальное количество попыток', min(test_list))
print('Среднее количество попыток', sum(test_list)/len(test_list))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




