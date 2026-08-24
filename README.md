# Pure Python JSON Parser (Prototype)

[ 🇬🇧 English ](#-pure-python-json-parser-prototype) | [ 🇷🇺 Русский ](#-прототип-json-парсера-на-pure-python)

---

## 🇬🇧 Pure Python JSON Parser (Prototype)

A lightweight, zero-dependency recursive descent JSON parser written in pure Python. 

### 🌟 Features
* **Zero Dependencies:** Written entirely using standard Python primitives.
* **Recursive Descent Parsing:** Clear, explicit logic without third-party regex or black-box wrappers.
* **RFC 8259 Syntax Validation:**
  * Strict handling of trailing commas (`{"a": 1,}`)
  * Detection of unexpected trailing garbage after the root object (`{"a": 1} true`)
  * Support for standard escape sequences (`\n`, `\t`, `\"`, `\\`, etc.)

---

## 🇷🇺 Прототип JSON-парсера на Pure Python

Легковесный JSON-парсер на базе рекурсивного спуска, написанный на чистом Python без внешних зависимостей.

### 🌟 Особенности

* **Zero Dependencies:** Полностью чистый Python без сторонних пакетов.
* **Рекурсивный спуск:** Прозрачная и контролируемая логика обработки данных без регулярок и сторонних библиотек.
* **Валидация синтаксиса по RFC 8259:**
* Строгий отлов висячих запятых (`{"a": 1,}`)
* Проверка на «мусор» после завершения основного JSON-объекта (`{"a": 1} true`)
* Корректная обработка эскейп-последовательностей (`\n`, `\t`, `\"`, `\\` и др.)
