# План ревью кода

## Цели ревью кода


1. Проверить, что скрипт корректно получает, обрабатывает и сохраняет данные курсов валют без ошибок.

2. Убедиться, что код структурирован, содержит понятные комментарии и не имеет избыточных операций.

3. Проверить, можно ли легко расширить функционал (например, добавить новые валюты или источники данных).

## Задачи для ревьювера
1. Проверить корректность запросов к API

2. Проанализировать обработку данных

3. Оценить сохранение и визуализацию данных

4. Проверить обработку ошибок и edge-cases

## Объекты проверки
1. HTTP-запросы и API

2. Парсинг XML


3. Структура данных (currency_data)


4. Сохранение в Excel и графики


5. Обработка исключений


## Чек-лист ревью

 1. Проверка импортов

 2. Корректность списка валют

 3. Работа с датами

 4. HTTP-запросы и обработка ответов

 5. Парсинг XML

 6. Структура данных

 7. Сохранение в Excel

 8. Построение графиков

 9. Обработка ошибок

 10. Комментарии и выводы

## План

| Этап                        | Действия                                 | Срок     | Участники        |
|-----------------------------|------------------------------------------|----------|------------------|
| Подготовка                  | Назначение ревьювера                     | 20 мин   | Tech Lead        |
| Анализ                      | Проверка по чек-листу                    | 1 час    | Tech Lead        |
| Обсуждение                  | Созвон в Zoom, оценка кода               | 40 мин   | Tech Lead        |
| Исправление и верификация   | Внесение правок и повторная проверка     | 2 часа   | Tech Lead        |

**Тайминг:**
Объем: ~250 строк -> 2 часа на анализ
