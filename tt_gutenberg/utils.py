# tt_gutenberg/utils.py
from typing import Mapping, List


def sort_by_count(count_dict: Mapping[str, int]) -> List[str]:
    """Return aliases sorted by translation count (descending).

    Ties are broken deterministically by alias (ascending alphabetical).

    Args:
        count_dict: mapping from alias (str) to count (int).

    Returns:
        List of aliases sorted by count descending.

    Raises:
        TypeError: if input is not a mapping or contains invalid types.
    """
    if not hasattr(count_dict, "items"):
        raise TypeError("count_dict must be a mapping of alias->int")

    items = list(count_dict.items())

    for k, v in items:
        if not isinstance(k, str):
            raise TypeError(f"alias keys must be strings, got {type(k).__name__}")
        if not isinstance(v, int):
            raise TypeError(f"count for '{k}' must be int, got {type(v).__name__}")

    items.sort(key=lambda kv: (-kv[1], kv[0]))
    return [k for k, _ in items]
