class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы
        целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        if not input_list:
            return []

        max_value = input_list[0]
        for el in input_list:
            if el > max_value:
                max_value = el

        replaced_list = [max_value if el > 0 else el for el in input_list]

        return replaced_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        if not input_list:
            return -1

        if len(input_list) == 1:
            if input_list[0] == query:
                return 0
            else:
                return -1

        def search_rec(low: int, high: int) -> int:
            if low > high:
                return -1

            mid = (low + high) // 2

            if input_list[mid] == query:
                return mid
            elif input_list[mid] > query:
                return search_rec(low, mid - 1)
            else:
                return search_rec(mid + 1, high)

        return search_rec(0, len(input_list) - 1)
