product = input("Тамақ атауын енгізіңіз: ").strip()

while True:
    price = input("Бағасын енгізіңіз: ").strip()
    if price.isdigit():
        break
    print("Баға тек сан болуы керек! Қайта енгізіңіз.")

with open("menu.txt", "a", encoding="utf-8") as file:
    file.write(f"\n{product}, {price}")

print("Жаңа тауар сәтті қосылды!")
