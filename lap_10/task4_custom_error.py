# Менюді файлдан оқу
menu = {}

with open("menu.txt", "r", encoding="utf-8") as file:
    for line in file:
        if ", " in line:
            product, price = line.strip().split(", ")
            menu[product.lower()] = int(price)

print("🍽 МЕНЮ:")
for item, price in menu.items():
    print(f"- {item.title()} — {price} тг")

total = 0

print("\nКлиенттің тапсырысын енгізіңіз ('және болды' деп тоқтатыңыз):")

# Клиенттен тапсырыс алу
while True:
    choice = input("Тамақ атауы: ").lower().strip()

    if choice == "болды":
        break

    if choice in menu:
        total += menu[choice]
        print(f"{choice.title()} қосылды! Бағасы: {menu[choice]} тг")
    else:
        print("Мұндай тамақ жоқ! Дұрыс атау енгізіңіз.")

# Қорытынды
print(f"\n💰 Жалпы сумма: {total} теңге")
