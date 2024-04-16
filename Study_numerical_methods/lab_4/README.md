# Звіт до роботи №6
## Тема: Робота з числовими даними в Python
## Мета: Навчитися працювати з числовими даними у мові програмування Python

---
### Виконання роботи

1. Підготовка до роботи:
    - Для зручності створили нову папку `lab_4` та новий файл Python з ім'ям `2_lab_numpy.ipynb`. 

1. Результати виконання завдань - "Робота з масивами за бібліотеки Numpy" - Визначення однорідного масиву:

```py
import numpy as np
lst = [ [3.4, 8.7, 9.9], 
        [1.1, -7.8, -0.7],
        [4.1, 12.3, 4.8] ]

A = np.array(lst, dtype=np.int8)
print(f"Отриманий масив має вигляд:\n{repr(A)}")
B = np.array(lst, dtype=np.float16)
print(f"Отриманий масив має вигляд:\n{repr(B)}")

homework("Згадуючи ООП, що робить функція repr?")
homework("У чому різниця між масивами A i B?")
```

```text
Отриманий масив має вигляд:
array([[ 3,  8,  9],
       [ 1, -7,  0],
       [ 4, 12,  4]], dtype=int8)
Отриманий масив має вигляд:
array([[ 3.4,  8.7,  9.9],
       [ 1.1, -7.8, -0.7],
       [ 4.1, 12.3,  4.8]], dtype=float16)

>>>>> Згадуючи ООП, що робить функція repr? 


>>>>> У чому різниця між масивами A i B? 
```

- Згадуючи ООП, що робить функція repr?

Функція repr() є вбудованою функцією у мові програмування Python, яка призначена для представлення об'єкта у вигляді рядка (string representation).

- У чому різниця між масивами A i B?

Різниця між масивами полягає в типах даних елементів. Всі елементи в масиві A будуть приведені до типу np.int8, що означає 8-бітні цілі числа. Всі елементи в масиві B будуть приведені до типу np.float16, що означає 16-бітні числа з плаваючою комою.


1. Результати виконання завдання - "Задаємо свій тип даних":

```py
dt = np.dtype([('name', np.compat.unicode, 20), ('mark', np.int8)])
arr = [
    ("Bohdan", 4), 
    ("Marta", 5),
    ("Noname", 0)
    ]
C = np.array(arr, dtype=dt)
print(f"Отриманий масив має вигляд:\n{C}")
print(f"Доступитись до певної колонки тепер можна за її іменем: {C['mark']}")

homework("Як вивести всі імена присутні в даному масиві?")
print(f"Всі імена в даному масиві:\n{C['name']}")
```

```text
Отриманий масив має вигляд:
[('Bohdan', 4) ('Marta', 5) ('Noname', 0)]
Доступитись до певної колонки тепер можна за її іменем: [4 5 0]

>>>>> Як вивести всі імена присутні в даному масиві? 

Всі імена в даному масиві:
['Bohdan' 'Marta' 'Noname']
```

1. Результати виконання завдань - "Запис та зчитування з файлу, формат CSV":

```py
print("Вихідний масив: ", C)
np.savez("my_mass.npz", my_mass=C)
D = np.load("my_mass.npz")
print("Прочитаний з файлу: ", D["my_mass"])

filename = "temp.csv"
print(f"Записуємо у CSV файл {filename} значення: {C}")
np.savetxt(filename, C, fmt="%s,%d", header="name,mark", delimiter=",")

import os
print(f"Перевіряємо чи файл {filename} створився: {os.listdir()}")

print("Читаємо файл за допомогою оператора with та методу readlines")
with open(filename) as f:
    D = f.readlines()

print(f"Прочитаний файл:\n {D} \n- як бачимо - {len(D)} елементи є стрічками {type(D[0])}.")

D = np.genfromtxt(filename, dtype=dt, delimiter=",")
print(f"Зчитане значення з файла:\n {D}, як бачимо - {D.size} елементи це {type(D[0])} \n- вбудований клас бібліотеки numpy.")
print(f"Доступитись до певного елемента можна наступним чином, наприклад імя першого елементу: {D[0]['name']}")

homework("""Створіть додаткове поле group - яке буде вказувати групу. 
Допишіть Ваше імя, оцінку та групу до масиву. 
Збережіть та вичитайте дані у файл.
Прочитайте саме Ваше імя з масиву.""")
```

```text
Вихідний масив:  [('Bohdan', 4) ('Marta', 5) ('Noname', 0)]
Прочитаний з файлу:  [('Bohdan', 4) ('Marta', 5) ('Noname', 0)]
Записуємо у CSV файл temp.csv значення: [('Bohdan', 4) ('Marta', 5) ('Noname', 0)]
Перевіряємо чи файл temp.csv створився: ['2_lab_numpy.ipynb', 'my_mass.npz', 'README.md', 'temp.csv']
Читаємо файл за допомогою оператора with та методу readlines
Прочитаний файл:
 ['# name,mark,group\n', 'Bohdan,4\n', 'Marta,5\n', 'Noname,0\n'] 
- як бачимо - 4 елементи є стрічками <class 'str'>.
Зчитане значення з файла:
 [('Bohdan', 4) ('Marta', 5) ('Noname', 0)], як бачимо - 3 елементи це <class 'numpy.void'> 
- вбудований клас бібліотеки numpy.
Доступитись до певного елемента можна наступним чином, наприклад імя першого елементу: Bohdan

>>>>> Створіть додаткове поле group - яке буде вказувати групу. 
Допишіть Ваше імя, оцінку та групу до масиву. 
Збережіть та вичитайте дані у файл.
Прочитайте саме Ваше імя з масиву. 
 ```

- Створіть додаткове поле group - яке буде вказувати групу. Допишіть Ваше імя, оцінку та групу до масиву. 
Збережіть та вичитайте дані у файл. Прочитайте саме Ваше імя з масиву.

> Задаємо свій тип даних

``` py
dt = np.dtype([('name', np.compat.unicode, 20), ('mark', np.int8), ('group', np.compat.unicode, 10)])
arr = [
    ("Bohdan", 4, "КН-42"), 
    ("Marta", 5, "КН-42"),
    ("Noname", 0, "КН-41")
    ]
C = np.array(arr, dtype=dt)

new_entry = ("Максим", 5, "КН-41")
C = np.append(C, np.array([new_entry], dtype=dt))

print(f"Отриманий масив має вигляд:\n{C}")
print(f"Доступитись до певної колонки тепер можна за її іменем: {C['mark']}")

homework("Як вивести всі імена присутні в даному масиві?")
print(f"Всі імена в даному масиві:\n{C['name']}")
```

```text
Отриманий масив має вигляд:
[('Bohdan', 4, 'КН-42') ('Marta', 5, 'КН-42') ('Noname', 0, 'КН-41')
 ('Максим', 5, 'КН-41')]
Доступитись до певної колонки тепер можна за її іменем: [4 5 0 5]

>>>>> Як вивести всі імена присутні в даному масиві? 

Всі імена в даному масиві:
['Bohdan' 'Marta' 'Noname' 'Максим']
```

> Запис та зчитування з файлу, формат CSV

```py
print("Вихідний масив: ", C)
np.savez("my_mass.npz", my_mass=C)
D = np.load("my_mass.npz")
print("Прочитаний з файлу: ", D["my_mass"])

filename = "temp.csv"
print(f"Записуємо у CSV файл {filename} значення: {C}")
np.savetxt(filename, C, fmt="%s,%d,%s", header="name,mark,group", delimiter=",")

import os
print(f"Перевіряємо чи файл {filename} створився: {os.listdir()}")

print("Читаємо файл за допомогою оператора with та методу readlines")
with open(filename) as f:
    D = f.readlines()

print(f"Прочитаний файл:\n {D} \n- як бачимо - {len(D)} елементи є стрічками {type(D[0])}.")

D = np.genfromtxt(filename, dtype=dt, delimiter=",")
print(f"Зчитане значення з файла:\n {D}, як бачимо - {D.size} елементи це {type(D[0])} \n- вбудований клас бібліотеки numpy.")
print(f"Доступитись до певного елемента можна наступним чином, наприклад імя першого елементу: {D[3]['name']}")
```

```text
Вихідний масив:  [('Bohdan', 4, 'КН-42') ('Marta', 5, 'КН-42') ('Noname', 0, 'КН-41')
 ('Максим', 5, 'КН-41')]
Прочитаний з файлу:  [('Bohdan', 4, 'КН-42') ('Marta', 5, 'КН-42') ('Noname', 0, 'КН-41')
 ('Максим', 5, 'КН-41')]
Записуємо у CSV файл temp.csv значення: [('Bohdan', 4, 'КН-42') ('Marta', 5, 'КН-42') ('Noname', 0, 'КН-41')
 ('Максим', 5, 'КН-41')]
Перевіряємо чи файл temp.csv створився: ['2_lab_numpy.ipynb', 'my_mass.npz', 'README.md', 'temp.csv']
Читаємо файл за допомогою оператора with та методу readlines
Прочитаний файл:
 ['# name,mark,group\n', 'Bohdan,4,КН-42\n', 'Marta,5,КН-42\n', 'Noname,0,КН-41\n', 'Максим,5,КН-41\n'] 
- як бачимо - 5 елементи є стрічками <class 'str'>.
Зчитане значення з файла:
 [('Bohdan', 4, 'КН-42') ('Marta', 5, 'КН-42') ('Noname', 0, 'КН-41')
 ('Максим', 5, 'КН-41')], як бачимо - 4 елементи це <class 'numpy.void'> 
- вбудований клас бібліотеки numpy.
Доступитись до певного елемента можна наступним чином, наприклад імя першого елементу: Максим
```

1. Результати виконання завдань - "Операції над масивами":

```py
l = (3, 3)

O = np.ones(l)
R = np.random.random(l)
Z = np.zeros(l)
C = np.arange(l[0])

print(f"""
Віднімання:\n {C - (O + 10)}
Множення:\n {O * R}
Ділення:\n {R / C}
Степінь:\n {C ** Z}
Поріняння:\n {R > 0.5}
Ділення на 0:\n {O / Z}
""")
homework("""
- Створіть власну матрицю за допомогою методу eye та виконайте порівняння на наявність 1.
- Створіть матрицю ones та відніміть від неї матрицю eye (щоб у результаті вийшла матриця де цетнтральні діагональ все нулі).
""")
E = np.eye(l[0])
print(f"""Порівняння на наявність 1 в матриці E:\n {E == 1}""")

result_matrix = O - np.eye(l[0])
print(f"Матриця з центральною діагоналлю нулів:\n{result_matrix}")
```

```text
Віднімання:
 [[-11. -10.  -9.]
 [-11. -10.  -9.]
 [-11. -10.  -9.]]
Множення:
 [[0.81405366 0.64131092 0.7947486 ]
 [0.60673679 0.35472955 0.72753451]
 [0.32522455 0.96844383 0.73824769]]
Ділення:
 [[       inf 0.64131092 0.3973743 ]
 [       inf 0.35472955 0.36376725]
 [       inf 0.96844383 0.36912384]]
Степінь:
 [[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
Поріняння:
 [[ True  True  True]
 [ True False  True]
 [False  True  True]]
Ділення на 0:
 [[inf inf inf]
 [inf inf inf]
 [inf inf inf]]

>>>>> 
- Створіть власну матрицю за допомогою методу eye та виконайте порівняння на наявність 1.
- Створіть матрицю ones та відніміть від неї матрицю eye (щоб у результаті вийшла матриця де цетнтральні діагональ все нулі).
 
Порівняння на наявність 1 в матриці E:
 [[ True False False]
 [False  True False]
 [False False  True]]
Матриця з центральною діагоналлю нулів:
[[0. 1. 1.]
 [1. 0. 1.]
 [1. 1. 0.]]
C:\Users\schma\AppData\Local\Temp\ipykernel_3436\2325827307.py:11: RuntimeWarning: divide by zero encountered in divide
  Ділення:\n {R / C}
C:\Users\schma\AppData\Local\Temp\ipykernel_3436\2325827307.py:14: RuntimeWarning: divide by zero encountered in divide
  Ділення на 0:\n {O / Z}
```

1. Результати виконання завдань - "Множення матриць":

```py
A = np.array([ [1, 2, 3], [2, 2, 2], [3, 3, 3] ])
B = np.array([ [3, 2, 1], [1, 2, 3], [-1, -2, -3] ])
print(f"Маємо два масиви:\n {A} \n {B}")

R = A * B
print(f"Тут виконується поелементне множення:\n {R}")

R = np.dot(A, B)
print(f"Тут, масиви перемножуються як матриці:\n {R}")

MA = np.mat(A)
MB = np.mat(B)

R = MA * MB
print(f"Тут масиви перетворені на матриці і далі перемножуються:\n {R}")
```

```text
Маємо два масиви:
 [[1 2 3]
 [2 2 2]
 [3 3 3]] 
 [[ 3  2  1]
 [ 1  2  3]
 [-1 -2 -3]]
Тут виконується поелементне множення:
 [[ 3  4  3]
 [ 2  4  6]
 [-3 -6 -9]]
Тут, масиви перемножуються як матриці:
 [[ 2  0 -2]
 [ 6  4  2]
 [ 9  6  3]]
Тут масиви перетворені на матриці і далі перемножуються:
 [[ 2  0 -2]
 [ 6  4  2]
 [ 9  6  3]]
```

1. Результати виконання завдань - "Вирівнювання розмірностей":

```py
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.array([1, 2, 3])
C = B[:, np.newaxis]

print(f"Вектор В є рядком {B.shape}: {B} тому додавання буде по рядках:\n {A + B}")

print(f"""Вектор C є стовпцем {C.shape}:
{C}
тому додавання буде по стовпцям:
{A + C}""")

print(f"У випадку додавання рядка до стовпця буде матриця в якої доповнюються рядки і стовпці:\n {B + C}")
```

```text
Вектор В є рядком (3,): [1 2 3] тому додавання буде по рядках:
 [[12 14 16]
 [22 24 26]
 [32 34 36]]
Вектор C є стовпцем (3, 1):
[[1]
 [2]
 [3]]
тому додавання буде по стовпцям:
[[12 13 14]
 [23 24 25]
 [34 35 36]]
У випадку додавання рядка до стовпця буде матриця в якої доповнюються рядки і стовпці:
 [[2 3 4]
 [3 4 5]
 [4 5 6]]
```

1. Результати виконання завдань - "Конкатенація, повторення та зміна форми (shape)":

```py
D = np.ones(3)
Z = np.zeros((3,1))
print(f"""
При конкатенації рядків маємо: {np.concatenate((D, D))}")
При конкатенації стовпців маємо:\n{np.concatenate((Z, Z))}
Масив D {D} має розмірність {D.shape} тому може виконати операцію конкатенації з В {B} розмірністю {B.shape}:
{np.concatenate((B, D))}
Для конкатенації з С
{C}
де С має розмірність = {C.shape} потрібно змінити розмірність D = {D.shape}
Це можна ось так:
{D[:, np.newaxis].shape}
або
{D.reshape((3,1)).shape}
в результаті ми можем виконати конкатенацію:
{np.concatenate((C, D.reshape((3,1))))}
При повторенні D {D} 2 рази для рядкі та 3 для стовпців будем мати:
{np.tile(D, (2, 3))}
Як бачимо конкатенація та повторення є дещо схожими у деяких випадках:
- конкатенація: {np.concatenate((D, D))}
- повторення: {np.tile(D, 2)}
Також можна перетворити двовимірний масив A розмірністю {A.shape} на рядок: {A.flatten()} з розмірністю {A.flatten().shape}
""")



homework(f"""Створіть двохвимірний масив за допомогою arange та виконайте конкатенацію та повторення.""")

A = np.arange(6).reshape((2, 3))

concatenated_rows = np.concatenate((A, A))

# Конкатенація
concatenated_columns = np.concatenate((A, A), axis=1)

# Повторення для рядків та стовпців
tiled_rows = np.tile(A, (2, 1))
tiled_columns = np.tile(A, (1, 3))

print(f"Двовимірний масив A:\n{A}")
print(f"\nКонкатенація рядків:\n{concatenated_rows}")
print(f"\nКонкатенація стовпців:\n{concatenated_columns}")
print(f"\nПовторення для рядків:\n{tiled_rows}")
print(f"\nПовторення для стовпців:\n{tiled_columns}")

homework(f"""Створіть масив в якому кількість рядкі та стовпців різна. Спробуйте виконати конкатенацію такого масиву з попереднім. Якщо розмірність масивів не спаівпадє використайте reshape.""")

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8], [9, 10], [11, 12]])

# Кількість стовпців у першому масиві
num_columns_array1 = array1.shape[1]

# Зміна розмірності другого масиву за допомогою reshape
reshaped_array2 = array2.reshape((array2.shape[1], num_columns_array1))

# Конкатенація рядків (оскільки тепер кількість стовпців співпадає)
concatenated_rows = np.concatenate((array1, reshaped_array2), axis=0)

print(f"Масив 1:\n{array1}")
print(f"\nМасив 2 (після reshape):\n{reshaped_array2}")
print(f"\nКонкатенація рядків:\n{concatenated_rows}")

homework(f"""Створіть декілька двовимірних масивів з сумарною розмірністю 12 та знайдіть всі можливі комбінції reshape. Наприклад, перша комбінація це рядок - {np.ones((1,12))}""")

array3 = np.ones((1, 12))
array4 = np.arange(12).reshape((2, 6))
array5 = np.zeros((3, 4))

# Знайдемо всі можливі комбінації reshape
reshape_combinations = [array3.reshape((m, n)) for m in range(1, 13) for n in range(1, 13) if m * n == 12]

print(f"\nМасив 3 (рядок):\n{array3}")
print(f"\nМасив 4:\n{array4}")
print(f"\nМасив 5:\n{array5}")
print("\nВсі можливі комбінації reshape:")
for combination in reshape_combinations:
    print(combination.shape)
```

```text
При конкатенації рядків маємо: [1. 1. 1. 1. 1. 1.]")
При конкатенації стовпців маємо:
[[0.]
 [0.]
 [0.]
 [0.]
 [0.]
 [0.]]
Масив D [1. 1. 1.] має розмірність (3,) тому може виконати операцію конкатенації з В [1 2 3] розмірністю (3,):
[1. 2. 3. 1. 1. 1.]
Для конкатенації з С
[[0]
 [1]
 [2]]
де С має розмірність = (3, 1) потрібно змінити розмірність D = (3,)
Це можна ось так:
(3, 1)
або
(3, 1)
в результаті ми можем виконати конкатенацію:
[[0.]
 [1.]
 [2.]
 [1.]
 [1.]
 [1.]]
При повторенні D [1. 1. 1.] 2 рази для рядкі та 3 для стовпців будем мати:
[[1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1.]]
Як бачимо конкатенація та повторення є дещо схожими у деяких випадках:
- конкатенація: [1. 1. 1. 1. 1. 1.]
- повторення: [1. 1. 1. 1. 1. 1.]
Також можна перетворити двовимірний масив A розмірністю (2, 3) на рядок: [0 1 2 3 4 5] з розмірністю (6,)


>>>>> Створіть двохвимірний масив за допомогою arange та виконайте конкатенацію та повторення. 

Двовимірний масив A:
[[0 1 2]
 [3 4 5]]

Конкатенація рядків:
[[0 1 2]
 [3 4 5]
 [0 1 2]
 [3 4 5]]

Конкатенація стовпців:
[[0 1 2 0 1 2]
 [3 4 5 3 4 5]]

Повторення для рядків:
[[0 1 2]
 [3 4 5]
 [0 1 2]
 [3 4 5]]

Повторення для стовпців:
[[0 1 2 0 1 2 0 1 2]
 [3 4 5 3 4 5 3 4 5]]

>>>>> Створіть масив в якому кількість рядкі та стовпців різна. Спробуйте виконати конкатенацію такого масиву з попереднім. Якщо розмірність масивів не спаівпадє використайте reshape. 

Масив 1:
[[1 2 3]
 [4 5 6]]

Масив 2 (після reshape):
[[ 7  8  9]
 [10 11 12]]

Конкатенація рядків:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

>>>>> Створіть декілька двовимірних масивів з сумарною розмірністю 12 та знайдіть всі можливі комбінції reshape. Наприклад, перша комбінація це рядок - [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]] 


Масив 3 (рядок):
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

Масив 4:
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]

Масив 5:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

Всі можливі комбінації reshape:
(1, 12)
(2, 6)
(3, 4)
(4, 3)
(6, 2)
(12, 1)
```

1. Результати виконання завдань - "Трансформації масивів":

```py
O = np.arange(6).reshape(3,2)
O_r = O.reshape((2,3))
O_f = O.flatten()
O_t = O.transpose()
O_fl = np.flip(O)
O_fa = np.flip(O, axis=1)

print(f"""{O}
Змінити розмірність shape {O.shape} на {O_r.shape} при цьому розмір size {O.size} = {O_r.size} та ndim {np.ndim(O)} = {np.ndim(O_r)}:
{O_r}
Також можна перетворити {np.ndim(O)}-х вимірний масив розмірністю {O.shape} на рядок:
{O_f} 
з розмірністю {O_f.shape} при цьому size = {O_f.size} та ndim стане {np.ndim(O_f)}-х вимірним 
Або транспонувати масив щоб він став {O_t.shape} але зверніть увагу на елементи:
{O_t}
Можна обернути масив (обертаємо по стовпцях і рядках одночасно): 
{O_fl}
Або обернути лише елементи в кожному рядку (або стовпці):
{O_fa}
""")

homework("""
- Створіть вектор з 12 елементів, визначте його shape, size та ndim;
- Змініть розмірніть перетворивши вектор у матрицю;
- Здійсніть транспонування отриманої матриці та оберніть її;
- Перетворіть отриманий багатовимірний масив назад у вектор (стрічку);
""")

vector = np.arange(12)

print(f"""
Vector:
{vector}
Shape: {vector.shape}
Size: {vector.size}
Ndim: {np.ndim(vector)}
""")

matr3x4 = vector.reshape((3, 4))

matr4x3 = vector.reshape((4, 3))

print(f"""
Оригінальний Vector:
{vector}

Перетворена Matrix (3x4):
{matr3x4}
Shape: {matr3x4.shape}

Перетворена Matrix (4x3):
{matr4x3}
Shape: {matr4x3.shape}
""")

transposed_matrix = matr3x4.transpose()

inverted_transposed_matrix = np.linalg.pinv(transposed_matrix)

print(f"""
Транспонована Matrix:
{transposed_matrix}
Shape: {transposed_matrix.shape}

Обернута транспонована Matrix:
{inverted_transposed_matrix}
Shape: {inverted_transposed_matrix.shape}
""")

flattened_vector = inverted_transposed_matrix.flatten()
print(f"""
Перетворений назад у вектор Matrix: {flattened_vector}
Shape: {flattened_vector.shape}
""")
```

```text
[[0 1]
 [2 3]
 [4 5]]
Змінити розмірність shape (3, 2) на (2, 3) при цьому розмір size 6 = 6 та ndim 2 = 2:
[[0 1 2]
 [3 4 5]]
Також можна перетворити 2-х вимірний масив розмірністю (3, 2) на рядок:
[0 1 2 3 4 5] 
з розмірністю (6,) при цьому size = 6 та ndim стане 1-х вимірним 
Або транспонувати масив щоб він став (2, 3) але зверніть увагу на елементи:
[[0 2 4]
 [1 3 5]]
Можна обернути масив (обертаємо по стовпцях і рядках одночасно): 
[[5 4]
 [3 2]
 [1 0]]
Або обернути лише елементи в кожному рядку (або стовпці):
[[1 0]
 [3 2]
 [5 4]]


>>>>> 
- Створіть вектор з 12 елементів, визначте його shape, size та ndim;
- Змініть розмірніть перетворивши вектор у матрицю;
- Здійсніть транспонування отриманої матриці та оберніть її;
- Перетворіть отриманий багатовимірний масив назад у вектор (стрічку);
 


Vector:
[ 0  1  2  3  4  5  6  7  8  9 10 11]
Shape: (12,)
Size: 12
Ndim: 1


Оригінальний Vector:
[ 0  1  2  3  4  5  6  7  8  9 10 11]

Перетворена Matrix (3x4):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Shape: (3, 4)

Перетворена Matrix (4x3):
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
Shape: (4, 3)


Транспонована Matrix:
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
Shape: (4, 3)

Обернута транспонована Matrix:
[[-0.3375     -0.13333333  0.07083333  0.275     ]
 [-0.1        -0.03333333  0.03333333  0.1       ]
 [ 0.1375      0.06666667 -0.00416667 -0.075     ]]
Shape: (3, 4)


Перетворений назад у вектор Matrix: [-0.3375     -0.13333333  0.07083333  0.275      -0.1        -0.03333333
  0.03333333  0.1         0.1375      0.06666667 -0.00416667 -0.075     ]
Shape: (12,)
```

Навчитися працювати з числовими даними у мові програмування Python

### Висновок:
- :question: Що зроблено в роботі :arrow_down: 

У цій роботі ми познайомилися з числовими даними у мові програмування Python та навчилися користуватися ними

- :question: Чи досягнуто мети роботи :arrow_down: 

Так, ми освоїли основні концепції використання чисових даних у мові програмування Python.

- :question: Які нові знання отримано :arrow_down:

Я дізнався про основні можливості використання числових даних у Python.

- :question: Чи вдалось відповісти на всі питання задані в ході роботи :arrow_down:

Так, на всі питання були дані повноцінні відповіді.

- :question: Чи вдалося виконати всі завдання :arrow_down:

Так, всі завдання були опрацьовані та виконані відмінно (на думку Chatgpt:smile:).

- :question: Чи виникли складності у виконанні завдання :arrow_down:

Ні, виконання лабораторної роботи було безперешкодним, оскільки з допомогою Chatgpt в мене все вдавалось.

- :question: Чи подобається такий формат здачі роботи (Feedback) :arrow_down:

Так, це достатньо простий та добре структурований формат здачі завдання, у якому можна достатньо легко показати результати виконаних завдань.

- :question: Побажання для покращення (Suggestions) :arrow_down:

Немає!

---