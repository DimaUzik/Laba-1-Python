# Лабораторна робота №1. Основи Python
# Варіант: 13
# ПІБ: Юзков Дмитро Олександрович

# Перевіряємо всі данні на корректність
while True:
    try:
        kredit = float(input("Введіть суму кредиту: "))
        if kredit <= 0:
            raise ValueError("Сума має бути більшою за 0")
        break
    except ValueError as e:
        print(f"Помилка: {e} Спробуйте ще раз\n")

while True:
    try:
        stavka = float(input("Введіть річну ставку(%): "))
        if stavka < 0:
            raise ValueError("Ставка не може бути від'ємною")
        break
    except ValueError as e:
        print(f"Помилка: {e} Спробуйте ще раз\n")

while True:
    try:
        termin = int(input("Введіть термін (міс): "))
        if termin <= 0:
            raise ValueError("Термін має бути хоча б 1 місяць")
        break
    except ValueError as e:
        print(f"Помилка: {e} Спробуйте ще раз\n")
# Обчислення
if stavka == 0:
    platej = kredit / termin
else:
    monthly = (stavka / 100) / 12
    platej = kredit * (monthly * (1 + monthly) ** termin) / ((1 + monthly) ** termin - 1)

payment = platej * termin
pereplata = payment - kredit

# Виведення результатів
print("\nРезультати розрахунку:")
print(f"Щомісячний платіж: {platej:.2f} грн")
print(f"Загальна сума виплат: {payment:.2f} грн")
print(f"Переплата за відсотками: {pereplata:.2f} грн")

if pereplata > kredit * 0.5:
    print("Примітка: Переплата становить більше 50% від суми кредиту!")
else:
    print("Примітка: Переплата в межах норми.")
