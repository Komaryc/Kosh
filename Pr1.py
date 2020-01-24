try:
    v0=float(input())
    v=float(input())
    t=float(input())
except ValueError:
    print('Ошибка! Значения переменных не цифры')
    v0=0
    v=1
    t=1
def decorator(uskorenie):
    def wrapper(c,b,d):
        uskorenie(c,b,d)
        try:
            s=(((b-c)/d)*(d*d))/2
        except ZeroDivisionError:
            s=(((b-c)/1)*(1*1))/2
        else:
            s=(((b-c)/d)*(d*d))/2
        finally:
            print(s)
    return wrapper
@decorator
def uskorenie(c,b,d):
    try:
        a=(b-c)/d
    except ZeroDivisionError:
        print('Ошибка! Время равно 0, теперь его значение равно 1')
        a=(b-c)/1
    else:
        a=(b-c)/d
    finally:
        print(a)
uskorenie(v0,v,t)