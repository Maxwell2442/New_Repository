print("Завдання і: Основні типи даних у Python: ")

# Рядок (String): Змінна a є рядком. Рядок представляє собою послідовність символів у лапках:
a = "Це змінна з текстом, у якій я збережу своє ім'я: Максим!"
print(a)

# Це змінна цілого числа (Integer):
b = 1
print("Ціле число =", b)

# Список (List): Змінна c є списком, що може містити елементи різних типів:
c = ["a", 1, 1.25, "Сонечко"]
print("Список різних типів даних:", c)

# Словник (Dictionary): Змінна d представляє словник, який має ключі та значення:
d = {"a": "Коляда", "b": 1}
print("Словник різних значень та ключів до них:", d)

# Кортеж (Tuple): Змінна e є кортежем. Кортеж з одним елементом повинен мати кому після цього елемента:
e = ("a",)
print("Кортеж з одним елементом:", e)

# Множина (Set): Змінна f є множиною, також має кому після єдиного елемента:
f = {"ss",}
print("Множина із одним елементом:", f, end='\n\n')

print("Завдання іі: Вбудовані константи у Python: ")

# True та False: Логічні константи, які представляють істину та хибу відповідно:
print("Ім'я: Максим", True)
print("Прізвище: Лозинський", False)

# None: Спеціальний об'єкт, що вказує на відсутність значення або "нічого":
print("Вік:", None, end='\n\n')

print("Завдання ііі: Вбудовані функції у Python: ")

numbers = [1, 2, 3, 4, 5]

# Сума sum(): Повертає суму чисел у списку:
print("Сумою списку numbers є", sum(numbers))

# Довжина len(): Повертає довжину об'єкта, наприклад, кількість елементів у списку чи символів у рядку:
print("Довжиною списку numbers є", len(numbers))

# Мінімальний елемент min(): Повертає найменше число ітерації
min_of_numbers = min(numbers)
print("Мінімальним числом списку numbers є", min_of_numbers, end='\n\n')

print("Завдання іv: Цикли у Python: ") 

classmates = ["Dmytro", "Ivanka", "Arsen"]

print("Цикл for по списку одногрупників:")
for classmate in classmates:
    print(classmate)

count = 0

print("Цикл while з виведенням :")
while count < 5:
    print(count)
    count += 1

cars = ["Volvo", "Aston Martin", "Koenigsegg"]

print("Цикл for по списку автомобілів, з пропусками рядків:", end="\n\n")
for car in cars:
    print(car, end="\n\n")

print("Завдання v: Розгалуження у Python: ")

age = 18

print("Перевірка на повноліття -> ", end="")
if age >= 18:
    print("Ви повнолітній")
else:
    print("Ви неповнолітній")

# Розгалуження if-elif-else
note = int(input("Введіть Вашу оцінку: ")) 

if note > 89:
    print("Відмінно")
elif note > 69:
    print("Добре")
elif note > 49:
    print("Задовільно")
else:
    print("Не задовільно")

print("\n\nЗавдання vi: Конструкція try->except->finally у Python: ")

try:
    # Введення користувача
    num_str = input("Введіть число: ")

    # Конвертація рядка у ціле число
    num = int(num_str)

    # Ділення на 0, що призведе до помилки
    result = 10 / num

except ValueError as ve:
    # Виловлюємо помилку, якщо введено не число
    print(f"Помилка: {ve}. Будь ласка, введіть коректне число.")

except ZeroDivisionError:
    # Виловлюємо помилку, якщо введено 0
    print("Помилка: Ділення на 0 не допустиме.")

finally:
    # Код, який виконається завжди, незалежно від наявності помилок
    print("Цей блок завжди виконується, навіть якщо виникає помилка чи ні.")

print("Завдання vii: Контекст-менеджер with у Python: ")

print("Додаємо текст до існуючого файлу за допомогою with: ")
with open("lab_2/README.md", "a") as file:
    file.write("\nЦе буде додано до існуючого вмісту.")

print("\n\nЗавдання vii: Контекст-менеджер with у Python: ")

print("Використання Лямбди: ")
square = lambda x: x**2
print(square(5))