import pandas as pd
import pytest
from tt_gutenberg.authors import list_authors


def test_list_authors_from_df():
    df = pd.DataFrame({"alias": ["a", "b", "a", "c", "b", "a"]})
    assert list_authors(alias=True, df=df) == ["a", "b", "c"]


def test_list_authors_missing_alias_col():
    df = pd.DataFrame({"author": ["a", "b"]})
    with pytest.raises(ValueError):
        list_authors(alias=True, df=df)


def test_list_authors_empty_df():
    df = pd.DataFrame({"alias": []})
    assert list_authors(alias=True, df=df) == []
