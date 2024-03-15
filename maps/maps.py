from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        filtered_movies = filter(lambda m: m["country"].count(",") + 1 >= 2, list_of_movies)

        def map_func(m: dict) -> Union[float, None]:
            rat = float(m["rating_kinopoisk"]) if m["rating_kinopoisk"] else None
            return rat if rat and rat > 0 else None

        ratings = map(map_func, filtered_movies)
        filtered_ratings = list(filter(lambda r: r is not None, ratings))
        ratings_sum = sum(filtered_ratings)
        average_rat = ratings_sum / len(filtered_ratings)

        return average_rat

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def map_func(m: dict) -> Union[str, None]:
            rat = float(m["rating_kinopoisk"]) if m["rating_kinopoisk"] else None
            return m["name"].count("и") if rat and rat >= rating else None

        counts = map(map_func, list_of_movies)
        filtered_counts = filter(lambda n: n is not None, counts)

        return sum(filtered_counts)
