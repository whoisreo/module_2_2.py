print("Введите три целых числа ")

f = int(input("Введите число : "))
first = f

s = int(input("Введите число : "))
second = s

t = int(input("Введите число : "))
third = t

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
