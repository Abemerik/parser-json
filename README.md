# Pure Python JSON Parser (Prototype)

[ 🇬🇧 English ](#-pure-python-json-parser-prototype) | [ 🇷🇺 Русский ](#-прототип-json-парсера-на-pure-python)

---

## 🇬🇧 Pure Python JSON Parser (Prototype)

A lightweight, zero-dependency recursive descent JSON parser written in pure Python. 

This repository serves as a reference implementation and algorithmic prototype. The core parsing logic will be ported to C to build a high-performance JSON library.

### 🌟 Features
* **Zero Dependencies:** Written entirely using standard Python primitives.
* **Recursive Descent Parsing:** Clear, explicit logic without third-party regex or black-box wrappers.
* **RFC 8259 Syntax Validation:**
  * Strict handling of trailing commas (`{"a": 1,}`)
  * Detection of unexpected trailing garbage after the root object (`{"a": 1} true`)
  * Support for standard escape sequences (`\n`, `\t`, `\"`, `\\`, etc.)

### 🚀 Quick Start

```python
from parser import parser

json_data = '''
{
  "name": "Alex",
  "age": 25,
  "is_student": false,
  "score": null,
  "dict": {"key": "value"},
  "massiv": [0, 10, false, "text", {"hull": null}]
}
'''

result = parser(json_data)
print(result)

```

### 🛠️ Roadmap

* [x] Pure Python reference implementation
* [ ] Port core algorithm to C (pointers, zero-copy string views)
* [ ] Add JSON Serializer (`dump` / `dumps`)
* [ ] Benchmarks against standard `json` and `orjson`

---

## 🇷🇺 Прототип JSON-парсера на Pure Python

Легковесный JSON-парсер на базе рекурсивного спуска, написанный на чистом Python без внешних зависимостей.

Этот репозиторий содержит эталонную реализацию алгоритма. Прототип служит фундаментальной базой перед переносом движка на C для создания высокопроизводительной библиотеки.

### 🌟 Особенности

* **Zero Dependencies:** Полностью чистый Python без сторонних пакетов.
* **Рекурсивный спуск:** Прозрачная и контролируемая логика обработки данных без регулярок и сторонних библиотек.
* **Валидация синтаксиса по RFC 8259:**
* Строгий отлов висячих запятых (`{"a": 1,}`)
* Проверка на «мусор» после завершения основного JSON-объекта (`{"a": 1} true`)
* Корректная обработка эскейп-последовательностей (`\n`, `\t`, `\"`, `\\` и др.)



### 🚀 Быстрый старт

```python
from parser import parser

json_data = '''
{
  "name": "Alex",
  "age": 25,
  "is_student": false,
  "score": null,
  "dict": {"key": "value"},
  "massiv": [0, 10, false, "text", {"hull": null}]
}
'''

result = parser(json_data)
print(result)

```

### 🛠️ План разработки (Roadmap)

* [x] Прототип алгоритма на Python
* [ ] Перенос ядра на C (указатели, работа с памятью)
* [ ] Реализация сериализатора (дампер в JSON-строку)
* [ ] Бенчмарки и сравнение производительности с `json` и `orjson`

```

<FollowUp label="Хочешь добавим .gitignore и файл с модульными тестами (pytest) перед выгрузкой на GitHub?" query="Покажи пример файла .gitignore и базовых модульных тестов на pytest для этого JSON-парсера."/>

```
