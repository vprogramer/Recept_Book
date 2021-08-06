price: int = 5
title: str = "haha"


def indent_right(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent_right(title, price))


