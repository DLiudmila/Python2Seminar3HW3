# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


def print_most_common_words(text, num_words=10):
    # Удалим знаки препинания и приведем текст к нижнему регистру
    new_text = ''.join([char.lower() if char.isalpha() else ' ' for char in text])

    # Разделим на слова
    words = new_text.split()

    # Подсчитаем слова
    word_count_dictionary = {}
    for word in words:
        word_count_dictionary[word] = word_count_dictionary.get(word, 0) + 1

    # Сортируем словарь
    sorted_dictionary = sorted(word_count_dictionary.items(), key=lambda x: x[1], reverse=True)

    # Возвращаем 10 самых часто встречаемых слов
    for i in range(10):
        print(sorted_dictionary[i])


# Загрузим текст из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

print_most_common_words(input_text)