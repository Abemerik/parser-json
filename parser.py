#constant

NUMBERS = "-0123456789"
BOOLS = "tfn"
SYMBOLS = ' }",]\n\t\r'
ESCAPE = {
    "n": "\n",
    "t": "\t",
    "r": "\r",
    "b": "\b",
    "f": "\f",
    "\\": "\\",
    "/": "/",
    "\"": "\""
    }


def parser(text: str) -> dict:
    LIMIT = len(text)
    i = _crop(text, 0, LIMIT)
    result, i = _read_value(text, i, LIMIT)
    i = _crop(text, i, LIMIT)
    if i < LIMIT:
        raise ValueError()
    return result

def _parse_object(text: str, i: int) -> tuple:
    result = {}
    LIMIT = len(text)
    while i < LIMIT:

        i = _crop(text, i, LIMIT)

        if i < LIMIT and text[i] == '{':
            i += 1
            continue

        elif i < LIMIT and text[i] == '}':
            i += 1
            break
        else:
            if i < LIMIT and text[i] == '"':
                i += 1
                key, i = _read_string(text, i, LIMIT)
                i = _crop(text, i, LIMIT)

                if i < LIMIT and text[i] == ':':
                    #изменить логику и поставить тут _read_value()
                    i += 1
                    i = _crop(text, i, LIMIT)
                    value, i = _read_value(text, i, LIMIT)
                    result[key] = value

                    i = _crop(text, i, LIMIT)

                    if i < LIMIT and text[i] == ",":
                        i += 1
                        i = _crop(text, i, LIMIT)
                        if i < LIMIT and text[i] == "}":
                            raise ValueError()
                        continue
                    elif i < LIMIT and text[i] == "}":
                        i += 1
                        break
                    else: 
                        raise ValueError()

    return result, i


def _crop(text: str, i: int, LIMIT: int) -> int:
    while i < LIMIT and text[i].isspace():
        i += 1
    return i


def _read_string(text: str, i: int, LIMIT: int) -> tuple:
    result = ""
    while i < LIMIT and text[i] != '"':
        if i+1 < LIMIT and text[i] == "\\":
            if text[i+1] in ESCAPE:
                result += ESCAPE[text[i+1]]
                i += 2
                continue
            else:
                result += text[i] + text[i+1]
                i += 2
                continue
        else:
            result += text[i]
            i += 1
            continue
    if i >= LIMIT:
        raise ValueError("Unterminated string")
    return result, i+1


def _read_value(text: str, i: int, LIMIT: int) -> tuple:
    if i < LIMIT and text[i] == '"':
        i += 1
        value, i = _read_string(text, i, LIMIT)
        return value, i

    elif i < LIMIT and text[i] in NUMBERS:
        value, i = _read_data(text, i, LIMIT)
        if '.' in value or 'e' in value or 'E' in value:
            return float(value), i
        else:
            return int(value), i

    elif i < LIMIT and text[i] in BOOLS:
        value, i = _read_data(text, i, LIMIT)
        if value == "true":
            return True, i
        elif value == "false":
            return False, i
        elif value == "null":
            return None, i
        else:
            raise ValueError()

    elif i < LIMIT and text[i] == "{":
        value, i = _parse_object(text, i)
        return value, i

    elif i < LIMIT and text[i] == "[":
        value, i = _parse_array(text, i, LIMIT)
        return value, i
    else:
        raise ValueError()


def _read_data(text: str, i: int, LIMIT: int) -> tuple:
    result = ""
    while i < LIMIT and text[i] not in SYMBOLS:
        result += text[i]
        i += 1
        continue
    return result, i


def _parse_array(text: str, i: int, LIMIT: int) -> tuple:
    result = []
    while i < LIMIT:
        i = _crop(text, i, LIMIT)

        if i < LIMIT and text[i] == '[':
            i += 1
            continue

        elif i < LIMIT and text[i] == ']':
            i += 1
            break
        else:
            value, i = _read_value(text, i, LIMIT)
            result.append(value)
            i = _crop(text, i, LIMIT)
            if i < LIMIT and text[i] == ",":
                i += 1
                i = _crop(text, i, LIMIT)
                if i < LIMIT and text[i] == "]":
                    raise ValueError()
                continue
            elif i < LIMIT and text[i] == "]":
                i += 1
                break
            else:
                raise ValueError()

    return result, i

print(parser(open("test.json", "r", encoding="utf-8").read()))