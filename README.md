# Getting to Know Pandas for Data Analytics with Python

This project demonstrates getting started with Pandas for data analytics.

## Business context

Pandas can be as simple or as complex as you need it to be. As an analysis toolkit, it's designed to be flexible and provide a wide range of functionality so that the same tool can be used for a variety of tasks. Because of this, it can be a little overwhelming at first. In this notebook we will introduce some of the essential pandas functionality and list a few best practices that will make learning pandas easier as you go.

- Reading in a CSV file - Inspecting the first five rows of your data - Selecting columns / filtering rows - Creating new columns from existing columns

- Basic indexing and working with dates - Reading data from multiple sources - Merging data (joins/vlookup) - Groupby, pivot_table, transform, melt

## Article

Medium article: [Getting to Know Pandas for Data Analytics with Python](https://medium.com/@kylejones_47003/getting-to-know-pandas-for-data-analytics-with-python-7386da28dd33)

## Project Structure

```
.
├── README.md           # This file
├── main.py            # Main entry point
├── config.yaml        # Configuration file
├── requirements.txt   # Python dependencies
├── src/               # Core functions
│   ├── core.py        # Pandas analytics functions
│   └── plotting.py    # Tufte-style plotting utilities
├── tests/             # Unit tests
├── data/              # Data files
└── images/            # Generated plots and figures
```

## Configuration

Edit `config.yaml` to customize:
- Data source or synthetic generation
- Operations to perform (groupby, sort, filter)
- Output settings

## Pandas Operations

Common operations demonstrated:
- GroupBy: Aggregate data by categories
- Sort: Sort by values
- Filter: Filter based on conditions
- Data Analysis: Info, head, tail, missing values

## Caveats

- By default, generates synthetic data for demonstration.
- Operations depend on data structure.
- Customize operations list in config.yaml.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).