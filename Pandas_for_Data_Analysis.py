"""Generated from Jupyter notebook: Pandas for Data Analysis

Magics and shell lines are commented out. Run with a normal Python interpreter."""
import numpy as np
import pandas as pd
import pandas.io.sql as pds
import sqlite3 as sq3

def year_number(row):
    return str(row['YYYYMM'])[0:4]


def a_quick_example_showing_the_speedup_reached_with() -> None:
    arr, ls = (np.arange(30000), range(30000))


def pd_series_will_create_a_series_if_no_index_is_gi() -> None:
    print('No index \n--------')

    print(pd.Series(np.arange(5)), '\n')

    print('Index \n--------')

    print(pd.Series(np.arange(5), index=['zero', 'one', 'two', 'three', 'four']))


def we_can_create_a_dataframe_from_a_python_dictiona() -> None:
    name_city_dictionary = {'name': ['Mike', 'Andrew'], 'city': ['NYC', 'SF']}

    df = pd.DataFrame(name_city_dictionary)

    df.head()


def we_can_change_the_index_row_name_by_using_the_in() -> None:
    name_city_dictionary = {'name': ['Mike', 'Andrew'], 'city': ['NYC', 'SF']}

    df = pd.DataFrame(name_city_dictionary, index=['person1', 'person2'])

    df.head()


def to_get_the_column_and_row_names_using_columns_an() -> None:
    print('Columns')

    print(list(df.columns), '\n')

    print('Index ')

    print(list(df.index), '\n')

    print('Values are numpy arrays')

    print(type(df.values))

    print(df.values)


def read_csv_takes_the_path_to_a_csv_file_and_return() -> None:
    df_csv = pd.read_csv('data/MER_T02_01.csv')

    df_csv.head()


def energydata_xlsx_is_a_spreadsheet_containing_the() -> None:
    df_excel = pd.read_excel('data/EnergyData.xlsx')

    df_excel.head()


def the_parameter_sheetname_allows_us_to_specify_whi() -> None:
    df_excel_after2000 = pd.read_excel('data/EnergyData.xlsx', sheetname='after2000')

    df_excel_after2000.head()


def we_can_read_in_multiple_sheets_at_the_same_time() -> None:
    df_excel_all = pd.read_excel('data/EnergyData.xlsx', sheetname=None)

    print(type(df_excel_all))

    print(df_excel_all.keys())

    df_excel_all['before2000'].head()


def delete_dataframes_using_del() -> None:
    del df_csv

    del df_excel

    del df_excel_after2000

    del df_excel_all


def notebook_step_012() -> None:
    path = '../../sql'

    query = 'CREATE TABLE instructors (Name varchar(255), City varchar(255))'

    con = sq3.Connection(path + 'instructors.db')

    con.execute(query)

    data = np.array([['Mike', 'Andrew'], ['NYC', 'SF']])

    con.executemany('INSERT INTO instructors VALUES (?, ?)', data)

    con.commit()


def we_ll_cover_databases_more_next_week_but_here_s() -> None:
    con = sq3.Connection(path + 'instructors.db')

    instructors = pds.read_sql('SELECT * FROM instructors', con)

    instructors.head()


def we_can_similarly_write_dataframes_to_files_using() -> None:
    instructors.to_csv('data/instructors.csv')


def notebook_step_015() -> None:
    print(type(df['name']))

    df['name']


def notebook_step_016() -> None:
    print('select by label using loc')

    print(df.loc['person2'], '\n')

    print('select by position using iloc')

    print(df.iloc[0], '\n')


def query_selects_columns_using_a_boolean() -> None:
    # .query() selects columns using a boolean
    print(df.query("name == 'Mike'"))


def notebook_step_018() -> None:
    df = pd.read_csv('data/MER_T02_01.csv')

    df.head()


def apply_will_apply_an_input_function_to_every_colu() -> None:
    df.head().apply(year_number, axis=1)


def we_can_add_a_column_directly() -> None:
    df['Year'] = df.apply(year_number, axis=1)

    df.head()


def dtypes_returns_the_types_of_the_data() -> None:
    print(df.dtypes)


def we_can_use_to_datetime_to_convert_to_a_datetime() -> None:
    df['Year'] = pd.to_datetime(df['Year'])

    print(df.dtypes)


def describe_gives_descriptive_statistics_on_the_dat() -> None:
    df.describe()


def value_counts_give_the_distribution_of_categorica() -> None:
    instructors = pd.DataFrame({'name': ['Andrew', 'Mike', 'Julia'], 'city': ['SF', 'NYC', 'NYC']})

    instructors['city'].value_counts()


def append_appends_rows_to_a_dataframe_new_columns_a() -> None:
    new_instructor = pd.DataFrame({'name': ['Seth', np.nan], 'city': ['CH', np.nan], 'role': ['SDS', np.nan]})

    instructors = instructors.append(new_instructor)

    instructors


def pd_isnull_detects_missing_values_in_a_dataframe() -> None:
    pd.isnull(instructors)


def dropna_drops_rows_with_na_values() -> None:
    print(instructors.dropna(how='any'), '\n')

    print(instructors.dropna(how='all'))


def to_plot_in_pandas_select_the_column_followed_by() -> None:
    new_df = df.query('Value < 20000')

    new_df['Value'].hist(bins=20)


def notebook_step_029() -> None:
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}, index=[0, 1, 2, 3])

    df4 = pd.DataFrame({'E': ['E2', 'E3', 'E6', 'E7'], 'F': ['F2', 'F3', 'F6', 'F7'], 'G': ['G2', 'G3', 'G6', 'G7']}, index=[2, 3, 6, 7])


def let_s_say_we_wanted_to_do_an_inner_join_on_the_f() -> None:
    print(df1, '\n')

    print(df4)


def we_can_do_this_with_join() -> None:
    df1.join(df4, how='inner')


def notebook_step_032() -> None:
    df_gb_example = pd.DataFrame({'Name': ['Mike', 'Andrew', 'Mike'], 'Amount': [1.0, 2.0, 3.0]})

    df_gb_example.groupby('Name').sum()


def notebook_step_033() -> None:
    df2 = pd.DataFrame({'A': 1.0, 'B': pd.Timestamp('20130102'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(['test', 'train', 'test', 'train']), 'F': 'foo'})

    df2


def notebook_step_034() -> None:
    df3 = df2

    df3['A'][0] = 2.0

    df2


def reset_df2() -> None:
    df2 = pd.DataFrame({'A': 1.0, 'B': pd.Timestamp('20130102'), 'C': pd.Series(1, index=list(range(4)), dtype='float32'), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(['test', 'train', 'test', 'train']), 'F': 'foo'})

    df3 = df2.copy(deep=True)

    df3['A'][0] = 2.0

    df2


def notebook_step_036() -> None:
    industrial.to_pickle('industrial.p')


def notebook_step_037() -> None:
    industrial_new = pd.read_pickle('industrial.p')


def notebook_step_038() -> None:
    industrial_new.dtypes


def main() -> None:
    a_quick_example_showing_the_speedup_reached_with()
    pd_series_will_create_a_series_if_no_index_is_gi()
    we_can_create_a_dataframe_from_a_python_dictiona()
    we_can_change_the_index_row_name_by_using_the_in()
    to_get_the_column_and_row_names_using_columns_an()
    read_csv_takes_the_path_to_a_csv_file_and_return()
    energydata_xlsx_is_a_spreadsheet_containing_the()
    the_parameter_sheetname_allows_us_to_specify_whi()
    we_can_read_in_multiple_sheets_at_the_same_time()
    delete_dataframes_using_del()
    notebook_step_012()
    we_ll_cover_databases_more_next_week_but_here_s()
    we_can_similarly_write_dataframes_to_files_using()
    notebook_step_015()
    notebook_step_016()
    query_selects_columns_using_a_boolean()
    notebook_step_018()
    apply_will_apply_an_input_function_to_every_colu()
    we_can_add_a_column_directly()
    dtypes_returns_the_types_of_the_data()
    we_can_use_to_datetime_to_convert_to_a_datetime()
    describe_gives_descriptive_statistics_on_the_dat()
    value_counts_give_the_distribution_of_categorica()
    append_appends_rows_to_a_dataframe_new_columns_a()
    pd_isnull_detects_missing_values_in_a_dataframe()
    dropna_drops_rows_with_na_values()
    to_plot_in_pandas_select_the_column_followed_by()
    notebook_step_029()
    let_s_say_we_wanted_to_do_an_inner_join_on_the_f()
    we_can_do_this_with_join()
    notebook_step_032()
    notebook_step_033()
    notebook_step_034()
    reset_df2()
    notebook_step_036()
    notebook_step_037()
    notebook_step_038()

if __name__ == "__main__":
    main()
