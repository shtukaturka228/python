n=int(input())
if n%2==0:
    print('Чётное')
else:
    print('Нечётное')
if n>0:
    print('Положительное')
elif n<0:
    print('Отрицательное')
else:
    print('Ноль')
if 10<=n<=50:
    print('В диапазоне')
else:
    print('Не в диапазоне')
