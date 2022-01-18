# coding=utf-8
from typing import List, Optional


def divide_for_n(message: str, num: int = 1, divide: str = "\n") -> Optional[List[str]]:
    if (divide == ""):
        return None
    data: list[str] = []
    for i in range(0, num):
        data.append("")
    i = 0
    message = message.split(divide)
    for elem in message:
        data[i % num] = data[i % num] + elem + divide
        i += 1
    data[-1] = data[-1][:-1]
    return data


def divide_message(mess: str, dim_line: int = 50, sep: str = " ") -> str:
    if (dim_line <= 0):
        return mess
    space = -1
    if (len(mess) > dim_line):
        for i in range(0, len(mess)):
            if (mess[i] == sep):
                space = i
            if (i >= dim_line):
                if (space == -1):
                    return mess[:dim_line] + "\n" + divide_message(mess[dim_line:], dim_line)
                else:
                    return mess[:space] + "\n" + divide_message(mess[space + 1:], dim_line)
        return mess
    else:
        return mess


def set_strike_text(text: str) -> str:
    # TODO: fix PyQt6 not working striked text
    return ''.join([u'\u0336{}'.format(c) for c in text])
