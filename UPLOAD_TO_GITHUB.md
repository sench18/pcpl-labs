# Загрузка в GitHub

В комплект входят шесть лабораторных, отчёты DOCX и PDF, результаты запусков и GitHub Actions. Вариант 22, студент Сердюков А. С., группа ИУ5-32Б.

## Через сайт

1. Распаковать архив на компьютере.
2. В GitHub создать пустой репозиторий `pcpl-labs`, выбрав видимость Public. Не добавлять README, лицензию и gitignore при создании: README и gitignore уже есть в комплекте.
3. Открыть `uploading an existing file` или Add file → Upload files.
4. Перетащить **содержимое** папки `pcpl-labs`, чтобы `README.md`, `lab_01` и остальные лабораторные находились в корне репозитория.
5. Сохранить через Commit changes.

Если интерфейс загрузки не перенёс папку `.github`, загрузить её через Git по инструкции ниже. Без неё код работает, но автоматический запуск тестов не включится.

## Через GitHub CLI

Если Git и GitHub CLI установлены, открыть терминал в распакованной папке `pcpl-labs`:

```bash
gh auth login
git init -b main
git add .
git commit -m "Add six Python labs for variant 22"
gh repo create pcpl-labs --public --source=. --remote=origin --push
```

Для коммита должны быть настроены стандартные параметры Git `user.name` и `user.email`.

## Проверка

В Actions появится процесс Python labs, проверяющий Python 3.10, 3.12 и 3.13. Локальный прогон на Python 3.12 завершился успешно: 61 тест. Журнал находится в `validation/tests.txt`.
