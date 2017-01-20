#ЛАБОРАТОРНАЯ РАБОТА №2
#
matrix_rate = [[0 for i in range(5)] for i in range(6)] #5 пользователей и 6 объектов
matrix_rate_cluster = [[0 for i in range(5)] for i in range(6)] #Рейтинг по кластаризации пользователей
matrix_rate_user = [[0 for i in range(5)] for i in range(6)]    #Рейтинг по коллаборации пользователей
matrix_rate_item = [[0 for i in range(5)] for i in range(6)]    #Рейтинг по коллаборации объектов

matrix_rate[0] = [5,5,4,5,0] #item1
matrix_rate[1] = [4,5,2,0,4] #item2
matrix_rate[2] = [5,2,0,3,3] #item3
matrix_rate[3] = [1,5,0,4,5] #item4
matrix_rate[4] = [3,0,3,3,5] #item5
matrix_rate[5] = [0,2,2,5,2] #item5

print('Исходная матрица рейтингов')
for row in matrix_rate:
    for elem in row:
        print(elem, end=" ")
    print()
print()

print('КЛАСТЕРИЗАЦИЯ ПОЛЬЗОВАТЕЛЕЙ')
#Среднее значение объектов по пользователям
for i in range(len(matrix_rate)): # i - номер объекта
    for j in range (len(matrix_rate[0])): #j - номер пользователея
        if matrix_rate[i][j]==0: #Поиск отсутствия рейтинга
            avg=0
            count_item=0
            for k in range(5):
                if k!=j and matrix_rate[i][k]!=0:
                    avg+=matrix_rate[i][k]
                    count_item+=1
                    matrix_rate_cluster[i][j]=avg//count_item
        else:
            matrix_rate_cluster[i][j]=matrix_rate[i][j]

print('Матрица рейтинга на основе средних оценок всех постальных пользователей в кластере')
for row in matrix_rate_cluster:
    for elem in row:
        print(elem, end=" ")
    print()
print()

print('КОЛЛАБОРАТИВНАЯ ФИЛЬТРАЦИЯ, ОСНОВАННАЯ НА ПОЛЬЗОВАТЕЛЯХ')
#Выбираются пользователи, поставившие схожие оценки другим объектам, как и сам пользователь. Находится среднее значение их оценки и проставляется для выбранного пользователя.
#Например, пользователь_1 поставил 5 первому объекту, такую же оценку поставил и пользователь_4, более того, их оценки схожи и для 5-го объекта. Значит пользователь_4 будет для пользователя_1 своего рода рекомендателем.
#Так для каждого пользователя находятся все возможные рекомендатели и выставляется среднее их значение объекту с отсутствием оценки для пользователя.

user_similitary=[[0 for i in range(5)] for i in range(5)] # Матрица похожести оценок пользователей

for k in range(5): #Для каждого пользователя
    for j in range(k+1,len(matrix_rate[0])):
        temp=0
        for i in range(6):
            if matrix_rate[i][k]==matrix_rate[i][j] and matrix_rate[i][k]!=0 and matrix_rate[i][j]!=0:
                temp+=1
        user_similitary[k][j]=temp
        user_similitary[j][k] = temp

print('Матрица схожести оценок пользователей')
for row in user_similitary:
    for elem in row:
        print(elem, end=" ")
    print()
print()

#Среднее значение оценок пользователей, схожих с конкретным пользователем
for i in range(len(matrix_rate)): # i - номер объекта
    for j in range (len(matrix_rate[0])): #j - номер пользователея
        if matrix_rate[i][j]==0: #Поиск отсутствия рейтинга
            avg=0
            count_item=0
            for k in range(5): #k - номер пользователя, с которым сравнивается пользователь j в матрице схожести
                if user_similitary[j][k]==max(user_similitary[j]) and j!=k: #Перебираем оценки максимально похожих пользователей
                    avg += matrix_rate[i][k]
                    count_item+=1
            matrix_rate_user[i][j]=avg//count_item
        else:
            matrix_rate_user[i][j] = matrix_rate[i][j]

print('Матрица рейтингов по коллаборативной фильтрации, основанной на пользователях')
for row in matrix_rate_user:
    for elem in row:
        print(elem, end=" ")
    print()
print()

print('КОЛЛАБОРАТИВНАЯ ФИЛЬТРАЦИЯ, ОСНОВАННАЯ НА ОБЪЕКТАХ')

item_similitary=[[0 for i in range(6)] for i in range(6)] # Матрица похожести оценок пользователей
for k in range(6):
    for j in range(k + 1, len(matrix_rate)):
        temp=0
        for i in range(5):
            if matrix_rate[k][i]==matrix_rate[j][i] and matrix_rate[k][i]!=0 and matrix_rate[j][i]!=0:
                temp+=1
        item_similitary[j][k]=temp
        item_similitary[k][j]=temp

print('Матрица схожести оценок объектов')
for row in item_similitary:
    for elem in row:
        print(elem, end=" ")
    print()
print()

#Среднее значение рейтинга объектов по схожести оценок объектов
for i in range(len(matrix_rate)): # i - номер объекта
    for j in range (len(matrix_rate[0])): #j - номер пользователея
        if matrix_rate[i][j]==0: #Поиск отсутствия рейтинга
            avg=0
            count_item=0
            for k in range(6): #k - номер объекта, с которым сравнивается пользователь j в матрице схожести
                if item_similitary[i][k]==max(item_similitary[i]) and i!=k:
                    avg+=matrix_rate[k][j]
                    count_item+=1
            matrix_rate_item[i][j]=avg//count_item
        else:
            matrix_rate_item[i][j] = matrix_rate[i][j]

print('Матрица рейтингов по коллаборативной фильтрации, основанной на объектах')
for row in matrix_rate_item:
    for elem in row:
        print(elem, end=" ")
    print()
print()
