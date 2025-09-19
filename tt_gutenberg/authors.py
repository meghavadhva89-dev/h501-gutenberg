"""Author-related helpers for the tt_gutenberg package.

This module exposes `list_authors`, which returns Project Gutenberg
author aliases ordered by translation count.
"""

from typing import List, Optional

import pandas as pd

from .utils import sort_by_count


def list_authors(
    by_languages: bool = True,
    alias: bool = True,
    csv_path: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    alias_col: str = "alias",
) -> List[str]:
    """Return author aliases ordered by translation count (highest first).

    Provide either ``df`` (a pandas DataFrame) or ``csv_path`` (path to
    a CSV). The dataset must contain an ``alias`` column (or pass
    ``alias_col``).

    Args:
        by_languages: Unused for this exercise (kept for compatibility).
        alias: If True, return aliases (required for this exercise).
        csv_path: Optional path to a CSV file containing the dataset.
        df: Optional pandas DataFrame with the dataset.
        alias_col: Column name in the dataset that contains the alias
            values.

    Returns:
        A list of alias strings ordered by translation counts (highest
        first).

    Raises:
        ValueError: If ``alias_col`` is missing from the provided dataset.
    """
    if not alias:
        raise NotImplementedError("Only alias=True is supported for this exercise.")

    if df is None:
        if csv_path is None:
            # Fallback sample data (keeps function usable without dataset).
            sample = {"mark_twain": 5, "jk_rowling": 3, "george_orwell": 8}
            return sort_by_count(sample)

        df = pd.read_csv(csv_path)

    if alias_col not in df.columns:
        raise ValueError(f"Dataset must contain an '{alias_col}' column.")

    # Drop null aliases and compute counts
    alias_counts = df[alias_col].dropna().astype(str).value_counts().to_dict()

    # value_counts yields counts; convert to dict alias->int and sort
    return sort_by_count(alias_counts)
