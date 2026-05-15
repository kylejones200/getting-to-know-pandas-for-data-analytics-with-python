"""Generated from Jupyter notebook: Pandas for Data Analysis

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

import numpy as np

# A quick example showing the speedup reached with numpy computations
arr, ls = np.arange(30000), range(30000)
# %timeit arr*10  # Jupyter-only
# %timeit [i*10 for i in ls]  # Jupyter-only


# --- code cell ---

# this is the standard import for pandas
import pandas as pd

# --- code cell ---

# pd.Series will create a series. If no index is given it defaults to the len(data)
print("No index \n--------")
print(pd.Series(np.arange(5)), "\n")

print("Index \n--------")
print(pd.Series(np.arange(5), index=["zero", "one", "two", "three", "four"]))


# --- code cell ---

# We can create a dataframe from a Python dictionary
# The keys will be the column names
# The values will be the values in the cells
# The index (row name) defaults to the row number starting at 0
name_city_dictionary = {"name": ["Mike", "Andrew"], "city": ["NYC", "SF"]}
df = pd.DataFrame(name_city_dictionary)
df.head()


# --- code cell ---

# We can change the index (row name) by using the index parameter as creation
name_city_dictionary = {"name": ["Mike", "Andrew"], "city": ["NYC", "SF"]}
df = pd.DataFrame(name_city_dictionary, index=["person1", "person2"])
df.head()


# --- code cell ---

# To get the column and row names using .columns and .index
print("Columns")
print(list(df.columns), "\n")

print("Index ")
print(list(df.index), "\n")

# Use .values to access the values in the cells. These are numpy arrays
print("Values are numpy arrays")
print(type(df.values))
print(df.values)


# --- code cell ---

# .read_csv() takes the path to a csv file and returns a DataFrame
df_csv = pd.read_csv("data/MER_T02_01.csv")
df_csv.head()


# --- code cell ---

# EnergyData.xlsx is a spreadsheet containing the above energy data
# There are two sheets (before2000, after2000)
# before2000: has the data from before the year 2000
# after2000: has the data from after the year 2000
# By default read_excel only returns the first sheet
df_excel = pd.read_excel("data/EnergyData.xlsx")
df_excel.head()


# --- code cell ---

# the parameter "sheetname" allows us to specify which sheet to read in
df_excel_after2000 = pd.read_excel("data/EnergyData.xlsx", sheetname="after2000")
df_excel_after2000.head()


# --- code cell ---

# We can read in multiple sheets at the same time
# A dictionary will be returned where the key is the sheet name and value is the dataframe

# The list of sheet names can be passed the sheetname or by passing None all sheets will be returned
df_excel_all = pd.read_excel("data/EnergyData.xlsx", sheetname=None)
print(type(df_excel_all))
print(df_excel_all.keys())
df_excel_all["before2000"].head()


# --- code cell ---

# delete dataframes using del
del df_csv
del df_excel
del df_excel_after2000
del df_excel_all


# --- code cell ---

import sqlite3 as sq3

path = "../../sql"
query = "CREATE TABLE instructors (Name varchar(255), City varchar(255))"
con = sq3.Connection(path + "instructors.db")
con.execute(query)
data = np.array([["Mike", "Andrew"], ["NYC", "SF"]])
con.executemany("INSERT INTO instructors VALUES (?, ?)", data)
con.commit()


# --- code cell ---

import sqlite3 as sq3

import pandas.io.sql as pds

# We'll cover databases more next week but here's an example of querying
# the instructors table from a sqlite database engine
con = sq3.Connection(path + "instructors.db")
instructors = pds.read_sql("SELECT * FROM instructors", con)
instructors.head()


# --- code cell ---

# We can similarly write DataFrames to files using similar commands as reading in files
instructors.to_csv("data/instructors.csv")


# --- code cell ---

print(type(df["name"]))
df["name"]


# --- code cell ---

print("select by label using loc")
print(df.loc["person2"], "\n")

print("select by position using iloc")
print(df.iloc[0], "\n")


# --- code cell ---

# .query() selects columns using a boolean
print(df.query("name == 'Mike'"))


# --- code cell ---

df = pd.read_csv("data/MER_T02_01.csv")
df.head()


# --- code cell ---


# .apply() will apply an input function to every column or row.
# axis = 0 or ‘index’: apply function to each column
# axis = 1 or ‘columns’: apply function to each row
def year_number(row):
    return str(row["YYYYMM"])[0:4]



def main():
    df.head().apply(year_number, axis=1)


    # --- code cell ---

    # We can add a column directly
    df["Year"] = df.apply(year_number, axis=1)
    df.head()


    # --- code cell ---

    # .dtypes returns the types of the data
    # Notice that Year is of type object
    print(df.dtypes)


    # --- code cell ---

    # We can use .to_datetime() to convert to a datetime type
    df["Year"] = pd.to_datetime(df["Year"])
    print(df.dtypes)


    # --- code cell ---

    # .describe() gives descriptive statistics on the DataFrame
    df.describe()


    # --- code cell ---

    # .value_counts() give the distribution of categorical variables
    instructors = pd.DataFrame(
        {"name": ["Andrew", "Mike", "Julia"], "city": ["SF", "NYC", "NYC"]}
    )
    instructors["city"].value_counts()


    # --- code cell ---

    # .append() appends rows to a DataFrame. New columns are added with nan values
    new_instructor = pd.DataFrame(
        {"name": ["Seth", np.nan], "city": ["CH", np.nan], "role": ["SDS", np.nan]}
    )
    instructors = instructors.append(new_instructor)
    instructors


    # --- code cell ---

    # pd.isnull() detects missing values in a DataFrame
    pd.isnull(instructors)


    # --- code cell ---

    # .dropna() drops rows with na values
    # how = "any" drops any row with an na value
    # how = "all" drops only rows with all na values
    print(instructors.dropna(how="any"), "\n")
    print(instructors.dropna(how="all"))


    # --- code cell ---

    # to plot in pandas select the column followed by the plot type
    # .hist() is you would create a histogram
    # %matplotlib inline  # Jupyter-only
    new_df = df.query("Value < 20000")
    new_df["Value"].hist(bins=20)


    # --- code cell ---

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


    # --- code cell ---

    # Let's say we wanted to do an inner join on the following two dataframes
    print(df1, "\n")
    print(df4)


    # --- code cell ---

    # we can do this with .join()
    df1.join(df4, how="inner")


    # --- code cell ---

    df_gb_example = pd.DataFrame(
        {"Name": ["Mike", "Andrew", "Mike"], "Amount": [1.00, 2.00, 3.00]}
    )
    df_gb_example.groupby("Name").sum()


    # --- code cell ---

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


    # --- code cell ---

    df3 = df2
    df3["A"][0] = 2.0
    df2


    # --- code cell ---

    # Reset df2
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


    # --- duplicate code cell omitted (identical to earlier cell) ---


    # --- code cell ---

    industrial.to_pickle("industrial.p")


    # --- code cell ---

    industrial_new = pd.read_pickle("industrial.p")


    # --- code cell ---

    industrial_new.dtypes


if __name__ == "__main__":
    main()
