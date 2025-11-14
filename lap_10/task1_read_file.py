with open("menu.txt", "r", encoding="utf-8") as file:
    prices = []
    for line in file:
        product, price = line.strip().split(", ")
        prices.append(int(price))
        print(f"Тағам аты: {product} — Бағасы: {price} теңге")

    print("\nОрташа цек:", sum(prices) / len(prices), "теңге")