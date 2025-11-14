try:
    with open("menu.txt", "r", encoding="utf-8") as file:
        data = [line.strip() for line in file if line.strip()]

except FileNotFoundError:
    print("Қате: menu.txt файлы табылмады!")

else:
    print("Файл сәтті оқылды:")
    for line in data:
        print(line)

finally:
    print("Бағдарлама орындалды.")
