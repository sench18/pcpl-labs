"""Ровно три модульных теста на стандартном фреймворке unittest."""

import unittest

from rk_02.solution import (
    Language, Library, LibraryLanguage,
    query_a1, query_a2, query_a3, sample_data,
)


class QueryTests(unittest.TestCase):
    def test_a1_join_and_sort(self):
        libraries, languages, _ = sample_data()
        # Вход намеренно перевёрнут: проверяем ключ сортировки.
        self.assertEqual(query_a1(libraries[::-1], languages[::-1]), [
            ("Boost", 6, "язык C++"),
            ("NumPy", 8, "язык Python"), ("Polars", 12, "язык Python"),
            ("serde", 4, "язык Rust"),
        ])
        self.assertEqual(query_a1([], languages), [])
        self.assertEqual(query_a1(libraries, []), [])

    def test_a2_sum_sort_and_empty_groups(self):
        libraries, languages, _ = sample_data()
        languages.append(Language(4, "язык C"))
        self.assertEqual(query_a2(libraries, languages), [
            ("язык Python", 20), ("язык C++", 6), ("язык Rust", 4),
        ])
        # Равные суммы упорядочиваются по названию; пустая группа исключена.
        self.assertEqual(query_a2([
            Library(1, "Polars", 4, 1), Library(2, "serde", 4, 2),
        ], languages), [("язык Python", 4), ("язык Rust", 4)])
        self.assertEqual(query_a2([], languages), [])

    def test_a3_filter_and_many_to_many(self):
        libraries, languages, links = sample_data()
        self.assertEqual(query_a3(libraries, languages, links), {
            "язык Python": ["Polars", "NumPy"], "язык Rust": ["Polars", "serde"],
            "язык C++": ["Boost"],
        })
        # Polars связан с Rust через таблицу M:N, хотя его основной язык Python.
        # Проверяем регистр, слово целиком и язык без связанных библиотек.
        languages += [Language(4, "ЯЗЫК C"), Language(5, "метаязык")]
        links += [LibraryLanguage(1, 5)]
        result = query_a3(libraries, languages, links)
        self.assertEqual(result["ЯЗЫК C"], [])
        self.assertNotIn("метаязык", result)
        self.assertEqual(query_a3([], languages, []), {
            lang.name: [] for lang in languages
            if lang.id != 5
        })


if __name__ == "__main__":
    unittest.main()
