import pandas as pd

print("Программа Метод Томаса Саати")

# Задал переменные с которыми в последствии буду работать
nazvanie_Kriteriev = []
nazvanie_KriterievX = []
dp_matrix = []
printik = []
# Ввод критериев, И названия критериев
while True:
    try:
        kolvo_Kriteriev = int(input('Введите количество критериев: '))
        break
    except(ValueError, TypeError):
        print('количество может быть только целочисленным')
print('Введите названия критериев ')
for i in range(kolvo_Kriteriev):
    # Сразу же добавляя значения по словари
    nazvanie_Kriteriev = str(input())
    nazvanie_KriterievX.append(nazvanie_Kriteriev)

for i in range(kolvo_Kriteriev):
    dvoinaiamatriza = []
    for j in range(kolvo_Kriteriev):
        if i == j:
            weight = 1.00
        elif i < j:
            print('Укажите на сколько аргумент {0} более важен чем аргумент {1} '.format(nazvanie_KriterievX[i], nazvanie_KriterievX[j]))
            while True:
                try:
                    weight = float(input())
                    break
                except(ValueError, TypeError):
                    print('Вы ввели не некорректное значение веса, введите иное ')
        else:
            weight = float(1/dp_matrix[j][i])
        dvoinaiamatriza.append(weight)
    dp_matrix.append(dvoinaiamatriza)
sum_matrix = 0

for i in range(kolvo_Kriteriev):
    sum_matrix += sum(dp_matrix[i])

for i in range(kolvo_Kriteriev):
    printik.append(float((sum(dp_matrix[i]) / sum_matrix) // 0.01) / 100)

if sum(printik) > 100:
    printik[printik.index(max(printik))] -= 1

df = pd.DataFrame(dp_matrix, index=nazvanie_KriterievX, columns=nazvanie_KriterievX)# Для красивого вывода
print(df)
print('')
print(printik)




