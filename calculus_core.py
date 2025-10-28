"""
Мой модуль с различными математическими операциями
"""
from sympy import *

def derivative(expression: str, variable: str) -> str:
    """
    Вычисление производной математического выражения по заданной переменной.

    Параметры:
    expression: математическое выражение в виде строки
    variable: переменная дифференцирования

    Возвращает:
    Строковое представление производной или сообщение об ошибке.
    """

    try:
        r = diff(expression, variable)
        return str(r)
    except:
        return 'Ошибка, проверьте ввод'
        
def matrix_determinant(matrix: str) -> str:
    """
    Вычисление определителя квадратной матрицы.
    
    Параметры:
        matrix: построчно вводимая матрица 
    
    Возвращает:
        Строковое представление определителя или сообщение об ошибке.
    """

    try:
        matrix_expr = sympify(matrix)
        m = Matrix(matrix_expr)
        r = m.det()
        return str(r)
    except:
        return 'Ошибка, проверьте ввод'

def equation(equation: str, variable: str):
    """
    Решение алгебраического уравнения с помощью solveset.
    
    Параметры:
        equation: уравнение в виде строки "x**2 - 4"
        variable: переменная для решения
    
    Возвращает:
        Строковое представление решения или сообщение об ошибке.
    """
    try:
        var = symbols(variable)
        eq = equation
       
        r = solveset(eq, var)

        if r == EmptySet:
            return 'Уравнение не имеет решений'
        else:
            return str(r)
    except:
        return 'Ошибка, проверьте ввод'

def system_of_equations(equations: str, variables: str) -> str:
    """
    Решение системы алгебраических уравнений.
    
    Параметры:
        equation: уравнения в виде строки "2*x + y - 5, x - y - 1" через запятую
        variable: переменные для решения через запятую
    
    Возвращает:
        Строковое представление решения или сообщение об ошибке.
    """
    try:
        vars = symbols(variables)

        eq_sp = []

        eq = equations.split(',')
        for i in eq:
            equ = i.strip()
            eq_sp.append(equ)

        r = solve(eq_sp, vars)
        if not r:
            return 'Система не имеет решений'
        else:
            return str(r)
            
    except:
        return 'Ошибка, проверьте ввод'


def matrix_addition(matrix1: str, matrix2: str) -> str:
    """
    Сложение двух матриц одной размерности.
    
    Параметры:
        matrix1: первая матрица в виде строки
        matrix2: вторая матрица в виде строки
    
    Возвращает:
        Матрицу-результат сложения матриц в виде строки или сообщение об ошибке.
    """
    try:
        matrix_expr1 = sympify(matrix1)
        matrix_expr2 = sympify(matrix2)
        m1 = Matrix(matrix_expr1)
        m2 = Matrix(matrix_expr2)
        
        r = m1 + m2
        return str(r)
    except:
        return 'Ошибка, проверьте ввод'
    
def matrix_multiplication(matrix1: str, matrix2: str) -> str:
    """
    Умножение двух совместимых матриц.

    Параметры:
        matrix1: первая матрица в виде строки
        matrix2: вторая матрица в виде строки

    Возвращает:
        Матрицу-результат умножения матриц в виде строки или сообщение об ошибке.
    """
    try:
        matrix_expr1 = sympify(matrix1)
        matrix_expr2 = sympify(matrix2)
        m1 = Matrix(matrix_expr1)
        m2 = Matrix(matrix_expr2)
        r = m1 * m2
        return str(r)
    except:
        return 'Ошибка: проверьте ввод'
    
def transpose_matrix(matrix: str)-> str:
    """
    Транспонирование матрицы: смена мест её строк и столбцов.

    Параметры:
        matrix: матрица в виде строки

    Возвращает:
        Транспонированную матрицу в виде строки или сообщение об ошибке.
    """

    try:
        matrix_expr = sympify(matrix)
        m = Matrix(matrix_expr)
        r = m.T
        return str(r)
        
    except:
        return 'Ошибка: проверьте ввод'