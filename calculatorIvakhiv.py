def plus(a, b):
    print("Результат додавання:", a + b)
def minus(a, b):
    print("Результат віднімання:", a - b)
def multiple(a, b):
    print("Результат множення:", a * b)
def divide(a, b):
    print("Результат ділення:", a / b)
def module(a, b):
    print("Результат залишка від ділення:", a % b)
def exponentiation(a, c):
    print("Результат піднесення числа до певного степіня:", a ** c)
try:
    action = input("Виберіть дію (+, -, *, /, % або **): ")
    if action in ('+', '-', '*', '/', '%'):
        
        number1 = float(input("Введіть перше число: "))
        number2 = float(input("Введіть друге число: "))
        
        if action == '+':
            plus(number1, number2)
        elif action == '-':
            minus(number1, number2)
        elif action == '*':
            multiple(number1, number2)
        elif action == '/':
            divide(number1, number2)
        elif action == '%':
            module(number1, number2)
    elif action == '**':
        number1 = float(input("Введіть число: "))
        number3 = float(input("Введіть степінь: "))
        exponentiation(number1, number3)
    else:
        print("Невідома дія")
except ZeroDivisionError:
    print("Ділення на 0 неможливе.")
except ValueError:
    print("Введіть коректні числа")