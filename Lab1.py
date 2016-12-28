#ЛАБОРАТОРНАЯ РАБОТА №1
#
import math
#Коллекция документов
d1 = ['green', 'car', 'bus']
d2 = ['car', 'yellow', 'move']
d3 = ['bus', 'green']
d4 = ['white', 'girl', 'head']
d5 = ['blue', 'white', 'blue']

#Подсчитаем количество слов
all_words_temp = d1+d2+d3+d4+d5 # временная переменная для подсчета ко-ва слов
all_words_count = list(set(all_words_temp)) #Уникальные слова
#for i in all_words_temp:
#    if i not in all_words_count:
#        all_words_count.append(i)

W=[[0 for j in range(6)] for i in range(len(all_words_count))] #Создаем матрицу весов TF_IDF и заполняем нулями
n=[[0 for j in range(6)] for i in range(len(all_words_count))] #Количество вхождений слова в довумент
k=[] #Общее число слов в документе
avgd = 0 #Среднее число слов во всей коллекции
tf=[[0 for j in range(6)] for i in range(len(all_words_count))] #tf
dt=[0 for i in range(len(all_words_count))] #Количество документов, где встречается слово
idf=[] #idf
sim = [[0 for j in range(4)] for i in range(4)] #Матрица косинусиной схожести


#Заполняем первый столбец матрицы весов словами из коллекции
j=0
for i in all_words_count:
    W[j][0]= str(i)
    j += 1

#Рассчитываем tf для каждого слова
for i in range(len(all_words_count)):
    for di in range(len(d1)):
        if W[i][0]==d1[di]:
            n[i][1] += 1
    for di in range(len(d2)):
        if W[i][0] == d2[di]:
            n[i][2] += 1
    for di in range(len(d3)):
        if W[i][0] == d3[di]:
            n[i][3] += 1
    for di in range(len(d4)):
        if W[i][0] == d4[di]:
            n[i][4] += 1
    for di in range(len(d5)):
        if W[i][0] == d5[di]:
            n[i][5] += 1

#Вывод n
print('n')
for row in n:
    for elem in row:
        print(elem, end=' ')
    print()

#Вычислим общее число слов в документе
k.append(len(d1))
k.append(len(d2))
k.append(len(d3))
k.append(len(d4))
k.append(len(d5))
avgd = round((len(d1)+len(d2)+len(d3)+len(d4)+len(d5))/5, 2) #Среднее число слов во всех документах, округленное до 2 знаков
print('K')
print(k)
#Высислим tf
for i in range(len(all_words_count)):
    for j in range(6):
        if j!=0:
            tf[i][j]=round(n[i][j]/k[j-1], 2)

#Вывод tf
print('TF')
for row in tf:
    for elem in row:
        print(elem, end=' ')
    print()

#Количество довументов, где встречается слово
for i in range(len(all_words_count)):
    if all_words_count[i] in d1:
        dt[i]+=1
    if all_words_count[i] in d2:
        dt[i]+=1
    if all_words_count[i] in d3:
        dt[i]+=1
    if all_words_count[i] in d4:
        dt[i]+=1
    if all_words_count[i] in d5:
        dt[i]+=1

#Вывод dt
print('dt')
print(dt)
for i in range(len(dt)):
    idf.append(math.log10(5/dt[i]))
print('idf')
print(idf)

#Расчет весов W (tf-idf)
for i in range(len(all_words_count)):
    for j in range(6):
        if j!=0:
            W[i][j]=round(tf[i][j]*idf[i], 2) #Записываем значение с округлением

#Вывод W
print()
print('W=tf*idf')
for row in W:
    for elem in row:
        print(elem, end=' ')
    print()

#***************************
#Расчет косинусной схожестей
AB = 0 #Временная переменная 1
A2 = 0 #Временная переменная 2
B2=0 #Временная переменная 3

for i in range(4):
    for j in range(4):
        AB = 0
        A2 = 0
        B2 = 0
        for row in range(len(all_words_count)):
            if i+2+j>5:
                break
            else:
                AB+=W[row][i+1]*W[row][i+2+j]
                A2+=W[row][i+1]*W[row][i+1]
                B2+=W[row][i+2+j]*W[row][i+2+j]
        if A2==0 or B2==0 or AB==0:
            sim[i][j]=0
        else:
            sim[i][j] = round(AB / (math.sqrt(A2) * math.sqrt(B2)), 2)

print('Косинусиные схожести')
print('d1xd2 d1xd3 d1xd4 d1xd5')
print('d2xd3 d2xd4 d2xd5')
print('d3xd4 d3xd5')
print('d4xd5')

for row in sim:
    for elem in row:
        print(elem, end=' ')
    print()
# ***************************
#Ранжирование документов при запросе q
score_temp = [0 for i in range(5)]
#Ввод запроса q
while True:
    print('Введите два слова для поиска')
    q = [str(i) for i in input().split()]
    if len(q)<2 or len(q)>=3:
        print('Введите 2 слова!')
    else:
        break
#Подсчитываем релевантность каждого документа по запросу q
for word in q:
    for i in range(len(all_words_count)):
        for j in range(6):
            if W[i][j]==word:
                for count in range(1,6,1): #Генерирует числа от 1 до 5 с шагом 1
                    score_temp[count-1]+=(W[i][count]*3)/(tf[i][count]+2*(0.25+0.75*float(k[count-1])/avgd))

print('Вывод значений релевантности:')
score =[[0 for j in range(5)] for i in range(2)]
score[0][0] = 'd1'
score[0][1] = 'd2'
score[0][2] = 'd3'
score[0][3] = 'd4'
score[0][4] = 'd5'
for j in range(5):
    score[1][j]=round(score_temp[j],2)

for row in score:
    for elem in row:
        print(elem, end=' ')
    print()
print()
#Сортировка по релевантности (говнокод)
max =0
temp=0
for j in range(10):
    for i in range(4):
        if score[1][i]<=score[1][i+1]:
            temp = score[1][i]
            score[1][i]=score[1][i+1]
            score[1][i + 1]=temp
            temp = score[0][i]
            score[0][i] = score[0][i + 1]
            score[0][i + 1] = temp
#Вывод поиска, отсортированный по релевантности
print('Вывод результата поиска, отсортированный по релевантности:')
for row in score:
    for elem in row:
        print(elem, end=' ')
    print()