"""Utility helpers for the tt_gutenberg package.

This module contains helper functions for sorting author aliases by
their translation counts.
"""

from typing import List, Mapping


def sort_by_count(count_dict: Mapping[str, int]) -> List[str]:
    """Return aliases sorted by translation count (descending).

    Ties are broken deterministically by alias (ascending
    alphabetical order).

    Args:
        count_dict: Mapping of alias (str) to count (int).

    Returns:
        List of aliases sorted by count descending.

    Raises:
        TypeError: if the input is not a mapping or contains invalid
            key/value types.
    """
    if not hasattr(count_dict, "items"):
        raise TypeError("count_dict must be a mapping of alias->int")

    items = list(count_dict.items())

    for key, value in items:
        if not isinstance(key, str):
            raise TypeError("alias keys must be strings, got %s" % type(key).__name__)
        if not isinstance(value, int):
            raise TypeError(
                "count for '%s' must be int, got %s" % (key, type(value).__name__)
            )

    # Sort by (-count, alias) so highest counts come first and ties are
    # deterministic by alias.
    items.sort(key=lambda kv: (-kv[1], kv[0]))

    return [k for k, _ in items]
