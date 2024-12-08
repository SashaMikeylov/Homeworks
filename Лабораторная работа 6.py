# Первое задание

text = "Любой текст"


counts = {}

for word in text.split():
    first= word[0].lower()  
    if first.isalpha():  
        if first in counts:
            counts[first] += 1
        else:
            counts[first] = 1


most_common_letter = ""
max_count = 0
for letter, count in counts.items():
    if count > max_count:
        most_common_letter = letter
        max_count = count

print("Буква" ,most_common_letter ,"чаще всего начинает слова: ",max_count," раз(а).")

#Второе задание

line = "Любой текстпаdurgvgcc"


latin_words = "abcdefghijklmnopqrstuvwxyz"
russian_words = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

count_russian = 0
count_latin = 0

for char in line:
    if char in latin_words:
       count_latin += 1
    elif char in russian_words:
        count_russian += 1
        

print("Общее количество строчных латинских:" ,count_latin, "и русских букв:",count_russian )

#Третье задание

lst = [0, -4, 5, 3, -8, 9, -1]


max_abs_index = 0
for i in range(len(lst)):
    if abs(lst[i]) > abs(lst[max_abs_index]):
        max_abs_index = i
print("Номер элемента с максимальным по модулю значением: ",max_abs_index)


sum_after_positive = 0
found_positive = False
for i in range(len(lst)):
    if found_positive:
        sum_after_positive += lst[i]
    elif lst[i] > 0:
        found_positive = True
print("Сумма элементов после первого положительного: ", sum_after_positive)
