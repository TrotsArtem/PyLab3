def task_1():
  n = int(input("Введіть розмірність матриці n<= 15: "))
  if n > 15:
    print("За умовою n <= 15")
    n = int(input("Введіть розмірність матриці n<= 15: "))

  print("Введіть елементи матриці по рядках:")
  matrix = []
  for i in range(n):
    row = list(map(int, input(f"Рядок {i+1}: ").split()))
    matrix.append(row)

  matrix.sort(key=lambda row: sum(abs(x) for x in row if x < 0))

  print("\nПеретворена матриця:")
  for row in matrix:
    print(row)


def task_2():
  n = 5
  magazines = []
  print(f"Введіть дані для {n} журналів (ціна та тираж через пробіл, наприклад: 45.5 8500):")

  for i in range(n):
    while True:
      try:
        parts = input(f"Журнал {i+1}: ").split()
        if len(parts) != 2:
          raise ValueError
        price, circulation = float(parts[0]), int(parts[1])
        magazines.append({"price": price, "circulation": circulation})
        break
      except ValueError:
        print("Помилка вводу.")

  filtered_prices = [
      mag["price"] for mag in magazines if mag["circulation"] < 10000
  ]

  if not filtered_prices:
    print("\nНемає журналів з тиражем менше 10000 примірників.")
  else:
    avg_price = sum(filtered_prices) / len(filtered_prices)
    print(
        f"\nСередня вартість журналів з тиражем менше 10000 примірників:"
        f" {avg_price:.2f}"
    )


def task_3():
  print("\n--- Завдання 3: База даних продажів інтернет-магазину ---")
  print(
      "Введіть записи про продажі у форматі '<Покупець> <товар> <кількість>'."
  )
  print("Для завершення введення просто натисніть Enter на порожньому рядку:\n")

  # Базовий словник для зберігання даних
  sales_data = {}

  while True:
    line = input()
    if not line.strip():
      break
    parts = line.strip().split()
    if len(parts) == 3:
      buyer, item, qty_str = parts
      try:
        qty = int(qty_str)

        # Якщо покупця ще немає в словнику, створюємо для нього вкладений словник
        if buyer not in sales_data:
          sales_data[buyer] = {}

        # Якщо товар уже є у цього покупця, додаємо кількість, інакше встановлюємо початкову
        if item in sales_data[buyer]:
          sales_data[buyer][item] += qty
        else:
          sales_data[buyer][item] = qty

      except ValueError:
        print("Помилка: кількість має бути цілим числом.")
    else:
      print("Помилка формату. Введіть: Покупець Товар Кількість")

  print("\nРезультат обробки (у лексикографічному порядку):")
  # Виводимо список усіх покупців у лексикографічному порядку
  for buyer in sorted(sales_data.keys()):
    print(f"{buyer}:")
    # Виводимо список товарів даного покупця у лексикографічному порядку
    for item in sorted(sales_data[buyer].keys()):
      qty = sales_data[buyer][item]
      print(f"  {item} {qty}")


def main():
  while True:
    print("1. Завдання")
    print("2. Завдання")
    print("3. Завдання")
    print("0. Вихід")

    choice = input("Введіть номер завдання: ").strip()

    if choice == "1":
      task_1()
    elif choice == "2":
      task_2()
    elif choice == "3":
      task_3()
    elif choice == "0":
      print("Роботу програми завершено.")
      break
    else:
      print("Невірний вибір.")


if __name__ == "__main__":
  main()