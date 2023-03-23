alp = "аеёиоуыэюя"
word_sug = input('Введите фразу:').split()

result = [sum([True for j in word if j.lower() in alp]) for word in word_sug]
print (result)

if all(result) and len(set(result)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")