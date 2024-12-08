#  Первое задание


M, N = 4, 5
matrix = [[i + j * N for i in range(1, N + 1)] for j in range(M)]

print("Исходная матрица:")
for row in matrix:
    print(row)


min_value = float('inf')
min_row = 0
min_col = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_row, min_col = i, j

matrix.pop(min_row)  
for row in matrix:
    row.pop(min_col)  

print("\nМатрица после удаления строки и столбца:")
for row in matrix:
    print(row)

# Второе задание


N = 4
matrix = [[i + j * N for i in range(1, N + 1)] for j in range(N)]

print("Исходная матрица:")
for row in matrix:
    print(row)


for i in range(N):
    matrix[i][i], matrix[i][N - i - 1] = matrix[i][N - i - 1], matrix[i][i]

print("\nМатрица после перестановки диагоналей:")
for row in matrix:
    print(row)

# Третье задание


n = int(input("Введите количество слов в словаре: "))


dictionary = {}

for _ in range(n):
    line = input("Введите слова для словаря: ")
    word, definition = line.split(": ", 1)
    dictionary[word] = definition


query = input("Введите слово для поиска: ")

if query in dictionary:
    print(dictionary[query])
else:
    print("Слово не найдено в словаре.")
