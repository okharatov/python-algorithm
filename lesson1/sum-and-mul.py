i = int(input('Введите трехзначное чсило '))
a = i // 100
b = i // 10 % 10
c = i % 10
print(f"Произведение: {a*b*c}\nСумма: {a+b+c}")
