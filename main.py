"""
Главный файл приложения, который импортирует модуль calculus_core и реализует взаимодействие с пользователем для вычисления математических операций.

Перечень операций:

1. Вычисление производной
    - Вычисляет производную математического выражения
    - Пример: x**2 → 2*x

2. Решение уравнения
    - Решает алгебраическое уравнение
    * Предполагется, что в правой части уравнения стоит число 0

3. Решение системы уравнений
    - Решает систему уравнений
    * Предполагется, что в правых частях уравнения стоит число 0
   
4. Вычисление определителя матрицы
    - Вычисляет определитель квадратной матрицы

5. Сложение матриц
    - Складывает две матрицы одинакового размера

6. Умножение матриц
    - Умножает две совместимые матрицы
    - Условие: столбцы 1-й матрицы = строки 2-й матрицы

7. Транспонирование матрицы
    - Меняет местами строки и столбцы заданной матрицы
"""

from calculus_core import derivative, matrix_determinant, equation, system_of_equations, matrix_addition, matrix_multiplication, transpose_matrix

while True:
    print('Выберите действие')
    print('1. Вычисление производной')
    print('2. Решение уравнения')
    print('3. Решение системы уравнений')
    print('4. Вычисление определителя матрицы')
    print('5. Сложение матриц')
    print('6. Умножение матриц')
    print('7. Транспонирование матрицы')
    a = input('Введите порядковый номер операции:')


    if a == '1':

        while True:
            expression = input('Введите математическое выражение: ')
            if not expression:
                print('Ошибка: Выражение не введено')
                continue  
            else:
                break 

        while True:
            variable = input('Введите переменную дифференцирования: ')
            if not variable:
                print('Ошибка: Переменная не введена')
                continue  
            else:
                break

        r = derivative(expression, variable)
        print('Производная:', r)
    
    
    elif a == '2':

        print('Введите уравнение в формате x**2 - 4')

        while True:
            equat = input('Введите уравнение: ')
            if not equat:
                print('Ошибка: Уравнение не введено')
                continue
            else:
                break

        while True:
            variable = input('Введите переменную: ')
            if not variable:
                print('Ошибка: Переменная не введена')
                continue
            else:
                break 
        
        r = equation(equat, variable)
        print('Решение:', r)


    elif a == '3':
        print('Введите уравнения в формате 2*x + y - 5, x - y - 1')
        while True:
            equations = input('Введите уравнения через запятую: ')
            if not equations:
                print('Ошибка: Уравнения не введены')
                continue
            else:
                break
    
        while True:
            variables = input('Введите переменные через запятую: ')
            if not variables:
                print('Ошибка: Переменные не введены')
                continue
            else:
                break

        r = system_of_equations(equations, variables)
        print('Решение:', r)
        

    elif a == '4':
        print('Введите матрицу в формате [1,2],[3,4]')

        while True:
            matrix = input("Матрица: ")
            if not matrix:
                print('Ошибка: Матрица не введена')
                continue
            else:
                break

        r = matrix_determinant(matrix)
        print('Определитель:', r)
    

    elif a == '5':
        print('Пример ввода матриц: [1,2],[3,4]')

        while True:
            matrix1 = input('Введите первую матрицу: ')
            if not matrix1:
                print('Ошибка: Первая матрица не введена')
                continue  
            else:
                break  

        while True:
            matrix2 = input('Введите вторую матрицу: ')
            if not matrix2:
                print('Ошибка: Вторая матрица не введена')
                continue  
            else:
                break

        r = matrix_addition(matrix1, matrix2)
        print('Сумма матриц:', r)

    elif a == '6':
        print('Пример ввода матриц: [1,2],[3,4]')

        while True:
            matrix1 = input('Введите первую матрицу: ')
            if not matrix1:
                print('Ошибка: Первая матрица не введена')
                continue  
            else:
                break  

        while True:
            matrix2 = input('Введите вторую матрицу: ')
            if not matrix2:
                print('Ошибка: Вторая матрица не введена')
                continue  
            else:
                break

        r = matrix_multiplication(matrix1, matrix2)
        print('Произведение матриц:', r)


    elif a =='7':
        print('Пример ввода матриц: [1,2],[3,4]')

        while True:
            matrix = input('Введите матрицу: ')
            if not matrix:
                print('Ошибка: матрица не введена')
                continue
            else:
                break
        r = transpose_matrix(matrix)
        print('Транспонированная матрица:', r)

    
    
    while True:
        cont = input('Хотите продолжить вычисления? (да/нет): ').lower()
        if cont == 'нет' or cont == 'ytn':
            print('Вы вышли из программы')  
        elif cont == 'да' or cont == 'lf':
            break