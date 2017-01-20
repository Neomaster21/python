#ЛАБОРАТОРНАЯ РАБОТА №3
#
import random

#Функция подсчета среднего значения c округлением до десятых
def avg(x):
    y=0
    for i in x:
        y+=i
    y=y/len(x)
    return round(y, 2)

#Функция рассчета моды (самого частого значения в последовательности)
def moda(x):
    y = [0 for i in range(5)]
    for i in x:
        y[i-1]+=1
    return y.index(max(y))+1

#Функция рассчета медианы. Медиана — это такое число выборки, что ровно половина из элементов выборки больше него, а другая половина меньше него
def mediana(x):
    y = sorted(x)
    #print(y) #Отсортированный список чисел
    return (y[int(len(y)/2)]+y[int(len(y)/2)+1])//2

#Функция нахождения межквартильного размаха. Это значения остортированного массива от 25-ой процентили до 75-ой.
def razmah(x):
    rz=[]
    y = sorted(x)
    for i in range(int (len(y)/4), int (len(y)/4*3)):
        rz.append(y[i])
    return rz

#Функция для нахождения дисперсии. Формуля для рассчета взята из источника: http://statistica.ru/theory/opisatelnye-statistiki/
def dispersia(x):
    avg_temp = avg(x)
    y=0
    for i in x:
        y+=(i-avg_temp)**2
    y = round(y/(len(x)-1),2)
    return y

#Функция для подсчета частотности значений
def frequency(x):
    y = [0 for i in range(5)]
    for i in x:
        y[i-1]+=1
    return y

#Функция для подсчета кумуляты
def cumulative(x):
    y = 0
    cum=[]
    for i in x:
        y+=i
        cum.append(y)
    return cum

list = [5, 2, 2, 5, 5, 3, 4, 4, 4, 3, 3, 5, 4, 5, 2, 2, 3, 1, 1, 1, 4, 3, 3, 5, 4, 4, 5, 1, 3, 4] #Последовательность для проверки
#list=[]
#for i in range(30):
#    list.append(random.randint(1,5))

print('Сгенерированная последовательность из 30-и чисел')
print(list)
print()
print('Среднее значение – ', end=' ')
print(avg(list))
print('Мода – ', end=' ')
print(moda(list))
print('Медиана – ', end=' ')
print(mediana(list))

print()
print('Межквартильный размах – ', end=' ')
print(razmah(list))
print('Дисперсия– ', end=' ')
print(dispersia(list))

print()
print('Частота встречаемых значений – ', end=' ')
print(frequency(list))
print('Кумулята – ', end=' ')
print(cumulative(frequency(list)))

