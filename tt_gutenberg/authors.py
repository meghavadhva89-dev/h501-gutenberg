from typing import List, Optional
import pandas as pd
from .utils import sort_by_count


def list_authors(by_languages: bool = True,
                 alias: bool = True,
                 csv_path: Optional[str] = None,
                 df: Optional[pd.DataFrame] = None,
                 alias_col: str = "alias") -> List[str]:
    """Return author aliases ordered by translation count (highest first).

    Provide either `df` (a pandas DataFrame) or `csv_path` (path to CSV).
    The dataset must contain an `alias` column (or pass `alias_col`).

    Args:
        by_languages: unused for this exercise (kept for signature compatibility).
        alias: if True, return aliases (required for this exercise).
        csv_path: optional path to a CSV file containing the dataset.
        df: optional pandas DataFrame with the dataset.
        alias_col: column name in the dataset that contains the alias values.

    Returns:
        A list of alias strings ordered by translation counts (highest first).

    Raises:
        ValueError: if alias_col is missing from dataset.
    """
    if not alias:
        raise NotImplementedError("Only alias=True is supported for this exercise.")

    if df is None:
        if csv_path is None:
            # Fallback sample data (keeps function usable without dataset)
            sample = {"mark_twain": 5, "jk_rowling": 3, "george_orwell": 8}
            return sort_by_count(sample)
        df = pd.read_csv(csv_path)

    if alias_col not in df.columns:
        raise ValueError(f"Dataset must contain an '{alias_col}' column.")

    # compute alias counts, drop NaN and coerce to string keys
    counts = df[alias_col].dropna().astype(str).value_counts().to_dict()
    # value_counts returns a Series sorted by count; convert to dict and sort deterministically
    return sort_by_count({str(k): int(v) for k, v in counts.items()})
