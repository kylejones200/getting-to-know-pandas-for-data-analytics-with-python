"""Pandas analytics patterns — GROUP BY via DuckDB."""

from pathlib import Path

import duckdb
import matplotlib.pyplot as plt
import polars as pl


def aggregate_by_category(
    df: pl.DataFrame, category_col: str, value_cols: list[str]
) -> pl.DataFrame:
    """pandas groupby(category)[cols].mean() → DuckDB GROUP BY."""
    aggs = ", ".join(f'AVG("{c}") AS "{c}"' for c in value_cols)
    return duckdb.sql(f"""
        SELECT "{category_col}", {aggs}
        FROM df
        GROUP BY "{category_col}"
        ORDER BY "{category_col}"
    """).pl()


def summarize_missing(df: pl.DataFrame) -> dict[str, int]:
    counts = df.null_count().row(0, named=True)
    return {c: int(counts[c]) for c in df.columns}


def plot_category_means(
    df: pl.DataFrame,
    category_col: str,
    value_col: str,
    output_path: Path,
    plot: bool = False,
) -> None:
    if not plot:
        return
    cats = df[category_col].to_list()
    vals = df[value_col].to_list()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(range(len(cats)), vals, color="#4A90A4", alpha=0.7)
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=45, ha="right")
    plt.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close()
