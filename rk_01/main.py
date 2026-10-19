"""РК-1. Вариант 22, запросы А. Запуск: python3 rk_01/main.py."""

from operator import itemgetter


class Library:
    """Библиотека: ключ, название, число модулей, основной язык."""

    def __init__(self, id, name, module_count, language_id):
        self.id = id
        self.name = name
        self.module_count = module_count
        self.language_id = language_id


class Language:
    """Язык программирования на стороне «один»."""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibraryLanguage:
    """Связь многие-ко-многим по идентификаторам."""

    def __init__(self, library_id, language_id):
        self.library_id = library_id
        self.language_id = language_id


def main():
    # Учебные данные: число модулей задано условно, не взято из релизов.
    # Основной язык задаёт учебную связь 1:N; Polars доступен Python и Rust.
    languages = [
        Language(1, "язык Python"),
        Language(2, "язык Rust"),
        Language(3, "язык C++"),
    ]
    libraries = [
        Library(1, "Polars", 12, 1),
        Library(2, "NumPy", 8, 1),
        Library(3, "Boost", 6, 3),
        Library(4, "serde", 4, 2),
    ]
    links = [
        LibraryLanguage(1, 1),
        LibraryLanguage(1, 2),
        LibraryLanguage(2, 1),
        LibraryLanguage(3, 3),
        LibraryLanguage(4, 2),
    ]

    one_to_many = [
        (lib.name, lib.module_count, lang.name)
        for lang in languages
        for lib in libraries
        if lib.language_id == lang.id
    ]
    many_to_many = [
        (lib.name, lib.module_count, lang.name)
        for link in links
        for lib in libraries
        for lang in languages
        if lib.id == link.library_id and lang.id == link.language_id
    ]

    print("РК-1. Вариант 22. Запросы А")
    print("А1. Библиотеки и языки, сортировка по языкам")
    for row in sorted(one_to_many, key=itemgetter(2, 0)):
        print(row)

    print("\nА2. Суммарное число модулей по языкам, по убыванию")
    totals = [
        (lang.name, sum(row[1] for row in one_to_many
                        if row[2] == lang.name))
        for lang in languages
        if any(row[2] == lang.name for row in one_to_many)
    ]
    for row in sorted(totals, key=lambda row: (-row[1], row[0])):
        print(row)

    print("\nА3. Слово 'язык' в названии, связь M:N")
    result = {
        lang.name: [name for name, _, language in many_to_many
                    if language == lang.name]
        for lang in languages
        if "язык" in lang.name.casefold().split()
    }
    for language, names in result.items():
        print(f"{language}: {', '.join(names)}")


if __name__ == "__main__":
    main()
