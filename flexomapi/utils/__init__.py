from typing import Optional


def search_item(array: list, cmp_function) -> Optional:
    for item in array:
        if cmp_function(item):
            return item
    return None
