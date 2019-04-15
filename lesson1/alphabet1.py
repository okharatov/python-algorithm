a = input("Введите первую букву ")
b = input("Введите вторую букву ")

a_ind = ord(a) - ord("a") + 1
b_ind = ord(b) - ord("a") + 1
print(f"{a} - {a_ind} буква алфавита")
print(f"{b} - {b_ind} буква алфавита")
print(f"Между ниими {abs(a_ind - b_ind)} буквы")
