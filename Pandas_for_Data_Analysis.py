"""Generated from Jupyter notebook: Pandas for Data Analysis

Magics and shell lines are commented out. Run with a normal Python interpreter."""

import sqlite3 as sq3

import numpy as np
import pandas as pd
import pandas.io.sql as pds


def main():
    df.head().apply(year_number, axis=1)
    df["Year"] = df.apply(year_number, axis=1)
    df.head()
    print(df.dtypes)
    df["Year"] = pd.to_datetime(df["Year"])
    print(df.dtypes)
    df.describe()
    instructors = pd.DataFrame(
        {"name": ["Andrew", "Mike", "Julia"], "city": ["SF", "NYC", "NYC"]}
    )
    instructors["city"].value_counts()
    new_instructor = pd.DataFrame(
        {"name": ["Seth", np.nan], "city": ["CH", np.nan], "role": ["SDS", np.nan]}
    )
    instructors = instructors.append(new_instructor)
    instructors
    pd.isnull(instructors)
    print(instructors.dropna(how="any"), "\n")
    print(instructors.dropna(how="all"))
    new_df = df.query("Value < 20000")
    new_df["Value"].hist(bins=20)
    df1 = pd.DataFrame(
        {
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )
    df4 = pd.DataFrame(
        {
            "E": ["E2", "E3", "E6", "E7"],
            "F": ["F2", "F3", "F6", "F7"],
            "G": ["G2", "G3", "G6", "G7"],
        },
        index=[2, 3, 6, 7],
    )
    print(df1, "\n")
    print(df4)
    df1.join(df4, how="inner")
    df_gb_example = pd.DataFrame(
        {"Name": ["Mike", "Andrew", "Mike"], "Amount": [1.0, 2.0, 3.0]}
    )
    df_gb_example.groupby("Name").sum()
    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    df2
    df3 = df2
    df3["A"][0] = 2.0
    df2
    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    df3 = df2.copy(deep=True)
    df3["A"][0] = 2.0
    df2


def year_number(row):
    return str(row["YYYYMM"])[0:4]


def main() -> None:
    arr, ls = (np.arange(30000), range(30000))

    print("No index \n--------")

    print(pd.Series(np.arange(5)), "\n")

    print("Index \n--------")

    print(pd.Series(np.arange(5), index=["zero", "one", "two", "three", "four"]))

    name_city_dictionary = {"name": ["Mike", "Andrew"], "city": ["NYC", "SF"]}

    df = pd.DataFrame(name_city_dictionary)

    df.head()

    name_city_dictionary = {"name": ["Mike", "Andrew"], "city": ["NYC", "SF"]}

    df = pd.DataFrame(name_city_dictionary, index=["person1", "person2"])

    df.head()

    print("Columns")

    print(list(df.columns), "\n")

    print("Index ")

    print(list(df.index), "\n")

    print("Values are numpy arrays")

    print(type(df.values))

    print(df.values)

    df_csv = pd.read_csv("data/MER_T02_01.csv")

    df_csv.head()

    df_excel = pd.read_excel("data/EnergyData.xlsx")

    df_excel.head()

    df_excel_after2000 = pd.read_excel("data/EnergyData.xlsx", sheetname="after2000")

    df_excel_after2000.head()

    df_excel_all = pd.read_excel("data/EnergyData.xlsx", sheetname=None)

    print(type(df_excel_all))

    print(df_excel_all.keys())

    df_excel_all["before2000"].head()

    del df_csv

    del df_excel

    del df_excel_after2000

    del df_excel_all

    path = "../../sql"

    query = "CREATE TABLE instructors (Name varchar(255), City varchar(255))"

    con = sq3.Connection(path + "instructors.db")

    con.execute(query)

    data = np.array([["Mike", "Andrew"], ["NYC", "SF"]])

    con.executemany("INSERT INTO instructors VALUES (?, ?)", data)

    con.commit()

    con = sq3.Connection(path + "instructors.db")

    instructors = pds.read_sql("SELECT * FROM instructors", con)

    instructors.head()

    instructors.to_csv("data/instructors.csv")

    print(type(df["name"]))

    df["name"]

    print("select by label using loc")

    print(df.loc["person2"], "\n")

    print("select by position using iloc")

    print(df.iloc[0], "\n")

    print(df.query("name == 'Mike'"))

    df = pd.read_csv("data/MER_T02_01.csv")

    df.head()

    # --- notebook cell (unparsed) ---
    # # --- code cell ---

    #     industrial.to_pickle("industrial.p")

    #     # --- code cell ---

    #     industrial_new = pd.read_pickle("industrial.p")

    #     # --- code cell ---

    #     industrial_new.dtypes

    # if __name__ == "__main__":
    #     main()


if __name__ == "__main__":
    main()
