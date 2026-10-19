"""Рефакторинг РК-1: неизменяемые данные и чистые функции запросов."""

from dataclasses import dataclass
from operator import itemgetter


@dataclass(frozen=True)
class Library:
    id: int
    name: str
    module_count: int
    language_id: int


@dataclass(frozen=True)
class Language:
    id: int
    name: str


@dataclass(frozen=True)
class LibraryLanguage:
    library_id: int
    language_id: int


def sample_data():
    """Каждый вызов возвращает отдельные коллекции тестовых данных."""
    return (
        [Library(1, "Polars", 12, 1), Library(2, "NumPy", 8, 1),
         Library(3, "Boost", 6, 3), Library(4, "serde", 4, 2)],
        [Language(1, "язык Python"), Language(2, "язык Rust"),
         Language(3, "язык C++")],
        [LibraryLanguage(1, 1), LibraryLanguage(1, 2),
         LibraryLanguage(2, 1), LibraryLanguage(3, 3),
         LibraryLanguage(4, 2)],
    )


def query_a1(libraries, languages):
    """Соединение 1:N; сортировка по языку, затем библиотеке."""
    return sorted(
        [(lib.name, lib.module_count, lang.name)
         for lib in libraries for lang in languages
         if lib.language_id == lang.id],
        key=itemgetter(2, 0),
    )


def query_a2(libraries, languages):
    """Сумма числа модулей; пустые группы исключены, как в примере условия."""
    totals = [
        (lang.name, sum(lib.module_count for lib in libraries
                        if lib.language_id == lang.id))
        for lang in languages
        if any(lib.language_id == lang.id for lib in libraries)
    ]
    return sorted(totals, key=lambda row: (-row[1], row[0]))


def query_a3(libraries, languages, links):
    """Связь M:N независима от language_id основного языка."""
    return {
        lang.name: [lib.name for link in links for lib in libraries
                    if link.language_id == lang.id
                    and lib.id == link.library_id]
        for lang in languages
        if "язык" in lang.name.casefold().split()
    }


def main():
    libraries, languages, links = sample_data()
    for label, result in [
        ("А1", query_a1(libraries, languages)),
        ("А2", query_a2(libraries, languages)),
        ("А3", query_a3(libraries, languages, links)),
    ]:
        print(label)
        if isinstance(result, dict):
            for language, names in result.items():
                print(f"{language}: {', '.join(names)}")
        else:
            for row in result:
                print(row)
        print()


if __name__ == "__main__":
    main()
