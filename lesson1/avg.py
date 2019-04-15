a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))

if a > b and a < c or a < b and a > c:
	print(a)
elif b > a and b < c or b < a and b > c:
	print(b)
else:
	print(c)
