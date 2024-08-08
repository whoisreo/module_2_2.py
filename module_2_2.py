print("Введите три целых числа ")

f = int(input("Введите число :"))
first = []
first.append(f)

s = int(input("Введите число : "))
second = []
second.append(s)

t = int(input("Введите число : "))
third = []
third.append(t)

if first == second == third :
    print(3)
elif first == second or first == third or second == third :
    print(2)
else:
    print(0)
