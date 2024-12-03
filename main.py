string_1 = str(input("Введите первую строку: ")) # ввод строк
string_2 = str(input("Введите вторую строку: "))

if string_1 == string_2: # проверка 1
    print("Строки не являются анаграммами.")
    quit()

elif len(string_1)!=len(string_2): # проверка 2
    print("Строки не являются анаграммами.")
    quit()

is_anagr = 0 # переменная, нужная для проверки, являются ли строки анаграммами

for i in string_1: # проверка одинаковых символов
    for j in string_2:
        if i == j:
            is_anagr+=1
            break

if is_anagr == len(string_1): # 
    print("Строки являются анаграммами.")
else:
    print("Строки не явлются анаграммами.")