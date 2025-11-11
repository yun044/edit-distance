def edit_distance(word_a: str, word_b: str) -> int:
    """
    Функция вычисляет расстояние Левенштейна (edit distance)
    между двумя строками word_a и word_b.
    """

    len_a = len(word_a)  # длина первой строки
    len_b = len(word_b)  # длина второй строки

    # Создаем таблицу DP размерами (len_a+1) x (len_b+1)
    dp_table = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    # Заполняем первую строку и первый столбец начальными значениями
    # Преобразование строки в пустую — это удаление всех символов
    for i in range(len_a + 1):
        dp_table[i][0] = i

    # Преобразование пустой строки — это вставка всех символов
    for j in range(len_b + 1):
        dp_table[0][j] = j

    # Заполнение таблицы динамического программирования
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):

            # Если символы совпадают — операция замены не нужна (cost = 0)
            # Если различаются — нужна 1 операция замены (cost = 1)
            cost = 0 if word_a[i - 1] == word_b[j - 1] else 1

            # Выбираем минимальную стоимость из трех операций:
            # удаление, вставка, замена
            dp_table[i][j] = min(
                dp_table[i - 1][j] + 1,      # удаление
                dp_table[i][j - 1] + 1,      # вставка
                dp_table[i - 1][j - 1] + cost  # замена / совпадение
            )

    # Результат находится в правом нижнем углу таблицы
    return dp_table[len_a][len_b]


if __name__ == "__main__":
    # Пример использования функции
    text1 = "kitten"
    text2 = "sitting"

    result = edit_distance(text1, text2)
    print(f"Edit distance between '{text1}' and '{text2}' = {result}")
