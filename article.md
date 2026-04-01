# Getting to know Pandas for data analytics with Python Pandas can be as simple or as complex as you need it to be. As an
analysis toolkit, it's designed to be flexible and provide a wide
range...

### **Getting to know Pandas for data analytics with Python**
Pandas can be as simple or as complex as you need it to be. As an
analysis toolkit, it's designed to be flexible and provide a wide range
of functionality so that the same tool can be used for a variety of
tasks. Because of this, it can be a little overwhelming at first. In
this notebook we will introduce some of the essential pandas
functionality and list a few best practices that will make learning
pandas easier as you go.


<figcaption>Photo by Slava Auchynnikau on Unsplash</figcaption>


By now, you should be comfortable with:

- Reading in a CSV file
- Inspecting the first five rows of your data
- Selecting columns / filtering rows
- Creating new columns from existing columns

### What's covered here
In this notebook you will learn:

- Basic indexing and working with dates
- Reading data from multiple sources
- Merging data (joins/vlookup)
- Groupby, pivot_table, transform, melt

Along the way, you will also learn pandas best practices in how to write
your code. For further reading on mastering pandas syntax, [**Minimally
sufficient
Pandas**](https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428) is an excellent resource.

### Tutorial Overview
```python
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.width", 160)
 
 %matplotlib inline
```

Let's break down the code step by step:

**import pandas as pd:** This line imports the pandas library and
assigns it the alias pd. It allows us to use pandas functions and
classes throughout the code.

**import matplotlib.pyplot as plt:** This line imports the pyplot module
from the matplotlib library and assigns it the alias plt. It allows us
to create plots and visualizations.

**pd.set_option("display.expand_frame_repr", False):** This line sets
the option in pandas to not wrap the DataFrame when displaying it in the
console. This ensures that each row of the DataFrame is displayed on a
single line.

**pd.set_option("display.width", 160):** This line sets the option in
pandas to set the maximum width of the displayed DataFrame to 160
characters. This prevents the DataFrame from being truncated and allows
us to see more columns without wrapping.

%matplotlib inline: This is known as a magic command in Jupyter
Notebook. It enables the inline plotting backend for matplotlib, which
means that plots will be displayed directly in the notebook cells.

### Test your knowledge
Before starting, try to complete the exercise below. This tests your
knowledge on topics covered in \[AFU PDA 2 --- Pandas basics\](./AFU PDA
2 --- Pandas basics.ipynb)

Step 1: Choose a file to load

from google.colab import drive\
 drive.mount('/content/drive')\
 \
 # we want to load the sales_fake.csv in the Support_Files directory\
 directory =
'/content/drive/MyDrive/KyleJonesCurrent/WriteUpContent/data/'\
 \
 ## START YOUR CODE HERE\
 file_name = 'us-counties-recent.csv'\
 ## END YOUR CODE HERE\
 path = directory + file_name\
 \
 # check to make sure you have the right path\
 print(path)

Drive already mounted at /content/drive; to attempt to forcibly remount,
call drive.mount("/content/drive", force_remount=True).\
 /content/drive/MyDrive/KyleJonesCurrent/WriteUpContent/data/us-counties-recent.csv

**Step 2:** Read your file into a pandas data frame and view the top 5
rows

``` 
# remember, pandas has built-in methods for reading data.
# If you can't remember which one to use, try pd.read<TAB> to view the available methods
 
# read the csv
df =
 # view the top 5 rows
 # remember, each dataframe also has built-in methods for working with the data.
 # if you can't remember which one to use, try df.<TAB> to view the available methods
 df
```

### Basic Indexing
Indexes in Pandas are like row numbers or labels that help organize and
access the data in a DataFrame. They provide a way to uniquely identify
each row of data. Pandas supports various types of indexes, including a
special type called DatetimeIndex, which is useful for working with
dates.

To start, we read in our data into a DataFrame and inspect the index.
The index is seen as the leftmost column, which contains numbers or
other values that uniquely identify each row. We use this index to
locate and access specific rows of data.

In some cases, the default index is not be ideal for our analysis. We
set a new index that better suits our needs. For example, we set a
DatetimeIndex if our data includes dates. This allows us to easily
perform operations and filtering based on dates.

Once we have our new index, we can leverage its functionality. This
includes filtering the data based on specific dates or date ranges,
grouping the data by time periods, and performing time-based
calculations or analysis.

By understanding and utilizing indexes effectively, we can efficiently
work with our data and perform various operations that are specific to
our analysis requirements.

This concept is crucial for data analysis tasks that involve time series
data or any data that can be uniquely identified using specific values.
It provides a powerful way to manipulate, analyze, and visualize data
based on its index.

```python
# use the same file from before
df = pd.read_csv(path)
print("What type of index?")
print(f"-> {df.index} \n")
 
print("Inspect some values:")
print("-> {df.index.values} \n")
 
# show the first 5 rows
df.head()

print(df.loc[3])
```

If I know the index, I can pull rows by their index

``` 
date 2023–02–22
county Bibb
state Alabama
fips 1007.0
cases 8067
deaths 109.0
Name: 3, dtype: object
```

Or I can pull a whole range using **START:END** notation. This is known
as "Slicing". For **\[1:3\]**, this means start index 1 and go up to 3
but don't include 3.

``` 
print(df.loc[1:3])


date county state fips cases deaths
1 2023–02–22 Baldwin Alabama 1003.0 69641 724.0
2 2023–02–22 Barbour Alabama 1005.0 7451 112.0
3 2023–02–22 Bibb Alabama 1007.0 8067 109.0
```

Before setting a datetime index, it is essential to understand the
different data types in Python.

Python has basic data types such as float, integer, and string. However,
it also supports more advanced data types, such as datetime. Similar to
programs like Excel, Python can automatically detect a column containing
dates and treat it differently from a string or an integer.

To examine the data types in our current DataFrame, we can use the
following code:

``` 
print(df.dtypes)
```

This will display the data types of each column in the DataFrame,
allowing us to identify the columns that contain dates. By understanding
the data types, we can make informed decisions about how to manipulate
and analyze the data effectively.

Setting a datetime index is beneficial when working with time series
data, as it allows us to perform various operations based on dates. With
a datetime index, we can easily filter the data, perform calculations,
and generate meaningful visualizations that are time-dependent.

If the current data types in the DataFrame do not recognize the date
column correctly, we can convert it to a datetime type using the
pd.to_datetime() function. This function allows us to convert a column
to a datetime format, enabling us to work with the data as dates rather
than strings or integers.

Understanding data types is crucial for performing accurate and
meaningful analysis, as it ensures that the data is treated
appropriately and the appropriate operations can be applied to it.

let's consider the "date" column in the dataset and convert it to a
datetime format.

To achieve this, we can use the pd.to_datetime() function provided by
the Pandas library. Here's an example of how you can convert the "date"
column to a datetime format:

``` 
df['date'] = pd.to_datetime(df['date'])
```

This line of code will update the "date" column in the DataFrame,
converting its data type to datetime. Now, you can use the converted
"date" column to perform time-based operations and analysis.

If you want to create a new column based on the converted "date" column,
you can do so by extracting specific components of the date, such as the
year, month, or day. Here's an example of how to create a new column
called "year" based on the "date" column:

``` 
df['year'] = df['date'].dt.year
```

This code will create a new column called "year" in the DataFrame, which
will contain the year component of the "date" column.

By converting columns to the appropriate data types and creating new
columns if needed, you can effectively work with dates and perform
various analyses based on time.

``` 
df['year']
```

We can create a new column and extract the weekday names from the "date"
column using the dt.weekday_name attribute. Here's an example code:

In this code, we create a new column called "weekday_name" by extracting
the weekday names from the "date" column using the dt.day_name()
function. Then, we select the 200 values from the "weekday_name" column
and store them in the variable weekday_names.

By running this code, you will obtain the weekday names for the 3100 to
3299 rows in the "weekday_names" variable. You can further explore and
analyze the weekday patterns in your dataset using this information.

``` 
df['weekday_name'] = df['date'].dt.day_name()
weekday_names = df['weekday_name'][3100:3300]
print(f"Week Days Name :\n weekday_names")
df.head()
df = df.set_index('date', inplace = True)
df.head()
```

### Aggregation
Aggregation refers to the process of summarizing or reducing data to a
single value or a smaller dataset based on certain criteria. It involves
applying functions such as sum, mean, max, min, count, etc., to one or
more columns of a DataFrame.

In simple words, Aggregating functions are the ones that reduce the
dimension of the returned objects. It means output Series/DataFrame have
less or same rows like original.

To apply aggregation functions in pandas, the column on which the
aggregation is performed should typically contain numerical or
quantitative data. These can include columns with data types such as int
(integer), float (floating-point numbers), or datetime (if used for
time-based aggregations). Aggregation functions work by performing
calculations on the values within the specified column(s) and returning
a single value or a new aggregated DataFrame.

For example, when calculating the sum of sales for each category, the
'sales' column should contain numerical values representing the sales
amounts. Similarly, when finding the maximum value of a 'price' column,
the 'price' column should contain numerical data.

It's important to note that aggregation functions may yield different
results depending on the data type of the column. For example, the sum
of integer values will be different from the sum of floating-point
numbers due to differences in precision.

\- Aggregation works with only numeric type columns.

\- Applying aggregation across all the columns

\- Sum and min will be found for each

\- Numeric type column in df dataframe

df.aggregate(\['sum', 'min', 'max'\])

In Pandas, it is possible to apply various aggregation functions to
different columns of a DataFrame. To achieve this, we can utilize a
dictionary where the keys represent the column names and the values
consist of a list of aggregation functions to be applied to each
respective column.

``` 
df.aggregate({'fips':['sum', 'min', 'max'],
 'cases':['sum', 'min', 'max'],
 'deaths':['sum', 'min', 'max']})
```

#### Important Functions of Aggregation:
**Function** **Description**

**mean()** Compute mean of groups

**sum()** Compute sum of group values

**size()** Compute group sizes

**count()** Compute count of group

**std()** Standard deviation of groups

**var()** Compute variance of groups

**sem()** Standard error of the mean of groups

**describe()** Generates descriptive statistics

**first()** Compute first of group values

**last()** Compute last of group values

**nth()** Take nth value, or a subset if n is a list

**min()** Compute min of group values

**max()** Compute max of group values

### Exercise :
1.  [Create a new DataFrame called "new_df" using the "date" column as
    the index. Hint: Use the set_index() function.]
2.  [Re-index the "new_df" DataFrame using the values from the "cases"
    column. Hint: Use the reindex() function.]
3.  [Retrieve the data from the DataFrame for the "deaths" column. How
    would you access only the "deaths" column in the DataFrame?]

Normally, this isn't how you would go about getting an answer like this
using pandas, but it does demonstrate how to easy it is to work with
data using slices and indexes. We could have accomplished the same thing
using special functions, filtering, or groupby's.

### Groupby's and aggregations
In the previous example, we used aggregation functions to analyze the
data. This showcases the power of Aggregations in pandas.

GroupBy allows you to flexibly organize your data by grouping it based
on specific criteria. Once the data is grouped, you can apply various
aggregation functions to each group, such as summing the values, finding
the minimum or maximum, calculating the mean, etc. This enables you to
create summary views of your data.

For example, you can group the data by a specific column, such as
'cases', and then calculate the sum of 'fips' for each record.

Similarly, you can group the data by another column, such as deaths, and
calculate the minimum and maximum values of a specific metric. This will
help identify the number of deaths with the lowest and highest figures.

By utilizing GroupBy and its aggregation functions, you can gain
valuable insights into your data and perform complex analyses easily. It
provides a similar functionality to pivot tables in excel, but with
additional features and flexibility.

``` 
state_cases = df.groupby('state')['cases'].sum()
print(state_cases)
```

In this example, we first read the 'us-counties-recent.csv' dataset into
a DataFrame called df. Then, we group the data by the 'state' column
using groupby('state'). Next, we specify the 'cases' column and apply
the sum() function to calculate the total number of cases for each
state.

The result will be a Series object where the states are the index and
the corresponding values represent the total cases for each state.

In SQL, this is equivalent to:

``` 
SELECT state, SUM(cases) AS total_cases
 FROM us_counties_recent
 GROUP BY state;
```

The above example involves using the .sum() method on a groupby object,
but there is a more general approach that we recommend,
using .aggregate(). In Python, and especially Pandas, there are many
different ways to perform the same operation, and .aggregate() is a
versatile method that can help narrow down your options.

state_cases = df.groupby('state')\['cases'\].aggregate('sum')\
 print(state_cases)

This is particularly helpful if you want to use different aggregate
functions for different columns, which you'll see in the next couple of
examples.

```python
# use the same file from before

df = pd.read_csv(path)
 
# Convert ‘date’ column to datetime type
df['date'] = pd.to_datetime(df['date'])
 
# Set 'date' as the index
df.set_index(‘='date', inplace=True)
 
# Group by ‘state’ and resample by quarter, calculating the sum of ‘cases’ and ‘deaths’
#state_by_qtr = df.groupby('state').resample('Q').sum().head(n=12)
state_by_qtr = df.groupby('state')[['cases', 'deaths']].resample('Q').sum().head(n=12)
 
# Print the result
print(state_by_qtr)
```

In this example, we read the 'us-counties-recent.csv' dataset into a
DataFrame. Then, we convert the **'date'** column to a datetime type and
set it as the index. Next, we use **groupby('state')** to group the data
by the 'state' column and we explicitly specify the columns **\['cases',
'deaths'\]** that we want to include in the aggregation. Finally, we
apply **resample('Q').sum()** to resample the data by **quarter ('Q')**
and calculate the sum of **'cases'** and **'deaths'** for each quarter
within each state.

```python
# use the same file from before

df = pd.read_csv(path)
 
column_list = ['state']
aggregations = {'cases':['sum','mean'],'deaths':['min','max']}
 
df.groupby(column_list).aggregate(aggregations)
```

In this below example, try to run it according to your understanding and
use your column names and practice it.

```python
def summarize_data(df, cols, aggs):
 return df.groupby(cols).aggregate(aggs)
 
 column_list = ['column_name', df.index.quarter]
 aggregations = {'column_name2':['min','max'],’column_name3':['sum','mean']}
 
 summarize_data(df, column_list, aggregations)
```

``` 
#this is to reset the index column
df = df.reset_index('date', inplace=True)
```

### Pivot a dataframe using the .pivot_table() function:
Just as in Excel, we can pivot our data, which typically involves
swapping rows with columns and applying an aggregate function:

```python
# use the same file from before
 df = None
 df = pd.read_csv(path)
 
 # Create a pivot table to calculate the average cases and deaths by state
 pivot_table = df.pivot_table(values=['cases', 'deaths'], index='state', aggfunc=’mean’)
 
 # Print the pivot table
 print(pivot_table)
```

The **pivot_table()** function in pandas is used to create a
spreadsheet-style pivot table based on the provided data. It allows you
to summarize and aggregate data in a tabular format, similar to how
pivot tables work in spreadsheet programs like Excel.

In this example, we are creating a pivot table to calculate the average
number of cases and deaths for each state. We specify the values we want
to aggregate ('cases' and 'deaths'), the column to use as the index
('state'), and the aggregation function to apply ('mean').

The resulting pivot table will have states as rows, cases and deaths as
columns, and the average values for each combination of state, cases,
and deaths.

You can customize the pivot_table() function by specifying different
columns for values, index, and columns, as well as using different
aggregation functions like 'sum', 'count', 'max', 'min', etc., depending
on your specific analysis requirements.

``` 
list(pivot_table.columns)
# Output: ['cases', 'deaths']
```

### Unpivot a dataframe using the .melt() function
```python
# use the same file from before
df = None
df = pd.read_csv(path)
 
# Select the columns to keep as identifiers and the columns to melt
id_vars = ['date', 'county', 'state']
value_vars = ['cases', 'deaths']
 
# Unpivot the DataFrame using the melt() function
melted_df = df.melt(id_vars=id_vars, value_vars=value_vars, var_name='category', value_name=’count’)
 
# Print the melted DataFrame
print(melted_df)
```

By using the .melt() function, we create a melted DataFrame called
melted_df, where each row represents a unique combination of 'date',
'county', 'state', and 'category' (either 'cases' or 'deaths'). The
corresponding 'count' values are stacked under the 'count' column.

The resulting melted_df DataFrame will have a row for each combination
of 'date', 'county', 'state', and 'category', with the corresponding
'count' values.

### Exercise : You Try...!
1.  [Find the top 5 counties with the highest average number of deaths
    per day. Display the county names and the corresponding average
    number of deaths.]
2.  [Calculate the total number of cases and deaths for each state in
    the dataset. Create a new DataFrame that shows the state, total
    cases, and total deaths, sorted in descending order of total
    cases.]
3.  [Identify the county with the highest number of cases in each state.
    Create a new DataFrame that displays the state, county, and the
    corresponding maximum number of cases.]

### Combining multiple data sets with pandas using Merge
Before merging, index of both datasets should match.In our datasets, It
seems that the index of the boolean Series and the indexed object do not
match.

To resolve this issue, make sure that the boolean Series used as an
indexer has the same index as the DataFrame you are trying to subset.
You can do this by either resetting the index of the boolean Series or
setting the index of the DataFrame to match.

```python
import pandas as pd
 
# Read the first dataset
# use the same file from before i.e us-counties-recent.csv

df1 = pd.read_csv(path)
 
# Read the second dataset
url = 'https://gist.githubusercontent.com/shivaas/4758439/raw/'
df2 = pd.read_csv(url)
 
# Perform the merge
merged_df = pd.merge(df1, df2, right_index=True, left_index=True, how='left')
 
# Display the merged dataframe
print(merged_df.head())
 
# Instructions
print("Instructions:")
print("- Make sure both datasets have a common column for merging.")
print("- Verify the data types of the columns to ensure compatibility.")
print("- Handle missing or inconsistent values appropriately.")
print("- Consider the merge type (inner, outer, left, right) based on your requirements.")
```

In the context of merging dataframes using pd.merge, the parameters
right_index and left_index specify whether to use the index of the right
and left dataframes, respectively, as the merging key.

\- When right_index=True, it indicates that the merging operation should
be based on the index of the right dataframe.

\- When left_index=True, it indicates that the merging operation should
be based on the index of the left dataframe.

By setting right_index=True and left_index=True, we are telling pd.merge
to use the index of both dataframes as the merging key. This means that
the rows from both dataframes will be matched based on their index
values, and the resulting merged dataframe will have a new index that
reflects this alignment.

Using index-based merging can be useful when the index represents a
unique identifier or a shared key between the two datasets. It provides
flexibility to merge dataframes even when the column names or values
don't match perfectly.

In the example code provided earlier, right_index=True and
left_index=True were used to merge the two datasets based on their
indices, assuming that the index serves as a suitable key for merging.

It's important to ensure that the index values are aligned correctly and
represent a meaningful relationship between the rows of the two datasets
before using index-based merging.

### Extensions
This section lists some ideas for extending the tutorial that you may
wish to explore.

\* Describe three examples when Pandas would be better than using Excel
directly.

\* Complete the next example that uses Pandas to clean a dataset.

### Further Reading
This section provides more resources on the topic if you are looking to
go deeper.

### Books
\* Python for Data Analysis, by William McKinney.
[http://shop.oreilly.com/product/0636920023784.do](http://shop.oreilly.com/product/0636920023784.do)

### APIs
\* Pandas.
[https://pandas.pydata.org/](https://pandas.pydata.org/)

### Articles
- [Getting started with Pandas in 5 minutes, on Towards Data Science.
  [https://medium.com/bhavaniravi/python-pandas-tutorial-92018da85a33](https://medium.com/bhavaniravi/python-pandas-tutorial-92018da85a33)]
- [My Pandas Cheat Sheet, on Towards Data Science.
  [https://towardsdatascience.com/my-python-pandas-cheat-sheet-746b11e44368](https://towardsdatascience.com/my-python-pandas-cheat-sheet-746b11e44368)]

### Summary
In this tutorial, you used Pandas for more advanced data analysis.
Specifically, you learned:

- Basic indexing and working with dates
- Reading data from multiple sources
- Merging data (joins/vlookup)
- Groupby, pivot_table, melt

### Related Stories
- [[Basic Data Analysis using Pandas Library in
  Python](https://medium.com/@kylejones_47003/basic-data-analysis-using-pandas-library-61ed815b834a)]
- [[Introduction to Statistics for people who do Business
  Analytics](https://medium.com/@kylejones_47003/introduction-to-statistics-for-people-who-do-business-analytics-26878760a14a)]
- [[Linear Regression for Business
  Analysis](https://medium.com/@kylejones_47003/linear-regression-for-business-analysis-2407d9fe2942)]
::::::::By [Kyle Jones](https://medium.com/@kyle-t-jones) on
[April 20, 2024](https://medium.com/p/7386da28dd33).

[Canonical
link](https://medium.com/@kyle-t-jones/getting-to-know-pandas-for-data-analytics-with-python-7386da28dd33)

Exported from [Medium](https://medium.com) on November 10, 2025.
