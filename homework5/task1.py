text = input ('Введите текст: ')
fragment = input ('Введите интересующий фрагмент: ')

words = text.split(' ')

# fragment = 'абв'

new_text = []
for word in words:
    if fragment not in word:
        new_text.append(word)

print('Исходный текст:', text)
print('Измененный текст:', ' '.join(new_text))