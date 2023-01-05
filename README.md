# simpledt


This is a third party party package for the framework **Flet**.

It enables **Flet** users to serialize

- Pandas DataFrame
- SQL
- CSV
- JSON
- Excel

Into Flet's **DataTable**.

simpledt is mainly based on pandas, SQLAlchemy and Flet's DataTable, DataRow, DataColumn and DataCell.

**Note:** Every class instance of simpledt package, has the following attributes

- **datatable** 
- **datarows** 
- **datacolumns** 

simpledt package does not have any hardcoded values and any change can be done to the DataTable, list of DataRow and DataColumn according to [Flet docs](https://flet.dev/docs/controls/datatable/)


# Installation


```bash
pip install simpledatatable
```


# Quickstart

## Display pandas dataframe

```python
import pandas as pd
import flet as ft
from simpledt import DataFrame


def main(page: ft.Page):
    df = pd.read_excel("dataset/Excel_MOCK_DATA.xlsx")
    simpledt_df = DataFrame(df)  # Initialize simpledt DataFrame object
    simpledt_dt = simpledt_df.datatable  # Extract DataTable instance from simpledt

    page.add(simpledt_dt)


ft.app(target=main)
```

![alt text](/img/dataframe_file_result.png)

So far, we've generated Flet's **DataTable** from pandas dataframe using simpledt package.

**Take in consideration** that every class instance from simpledt package has **datatable**, **datarows** and **datacolumns** attributes.

- **datatable** returns a Flet's **DataTable** instance, which already consists of **DataColumn**, **DataRow** and **DataCell**

- **datarows** returns a list of Flet's **DataRow** instance

- **datacolumns** returns a list of Flet's **DataColumn** instance

**Note:** any change of these attributes can be done according to [Flet docs](https://flet.dev/docs/controls/datatable/#datacolumn). *There is no limitations, or hardcoded values*.

## Modify `datarows`

To see how to modify **datarows**, lets move and change color of rows whose rownum is even.

```python
import pandas as pd
import flet as ft
from simpledt import DataFrame


def main(page: ft.Page):
    df = pd.read_excel("dataset/Excel_MOCK_DATA.xlsx")
    simpledt_df = DataFrame(df)  # Initialize simpledt DataFrame object
    simpledt_dt = simpledt_df.datatable  # Extract DataTable instance from simpledt
    
    simpledt_dt.bgcolor = ft.colors.RED # Change background color of generated DataTable
    simpledt_dt.border = ft.border.all(10, ft.colors.PINK_600) # Add ping border to DataTable

    dr = simpledt_df.datarows

    for i in dr:
        rownum = i.cells[0].content.value # Getting the first instance of DataCell, which consists of `id` and getting its `content` and `value`
        if int(rownum) % 2 == 0: # If rownum is even, change row color to green
            i.color = ft.colors.GREEN
        
    page.add(simpledt_dt)


ft.app(target=main)
```

![alt text](/img/dataframe_file_modify_rows_result.png)

## Modify `datacolumns`

To see how to modify **datacolumns**, add snowflakes at the end of every column name

```python
import pandas as pd
import flet as ft
from simpledt import DataFrame


def main(page: ft.Page):
    df = pd.read_excel("dataset/Excel_MOCK_DATA.xlsx")
    simpledt_df = DataFrame(df)  # Initialize simpledt DataFrame object
    simpledt_dt = simpledt_df.datatable  # Extract DataTable instance from simpledt
    
    simpledt_dt.bgcolor = ft.colors.RED # Change background color of generated DataTable
    simpledt_dt.border = ft.border.all(10, ft.colors.PINK_600) # Add ping border to DataTable

    dr = simpledt_df.datarows

    for i in dr:
        rownum = i.cells[0].content.value
        if int(rownum) % 2 == 0:
            i.color = ft.colors.GREEN
        
    dc = simpledt_df.datacolumns

    for i in dc:
        i.label=ft.Row([i.label, ft.Icon(ft.icons.AC_UNIT)])
    

    page.add(simpledt_dt)


ft.app(target=main)
```

![alt text](/img/dataframe_file_modify_columns_result.png)
## Use shortcut classes

### CSVDataTable

```python
import flet as ft
from simpledt import CSVDataTable


def main(page: ft.Page):
    csv = CSVDataTable("https://raw.githubusercontent.com/kb22/Heart-Disease-Prediction/master/dataset.csv")
    dt = csv.datatable

    page.add(dt)


ft.app(target=main)

```

![alt text](/img/online_csv_result.png)

### ExcelDataTable

```python
import flet as ft
from simpledt import ExcelDataTable


def main(page: ft.Page):
    excel = ExcelDataTable('dataset/Excel_MOCK_DATA.xlsx')
    dt = excel.datatable

    page.add(dt)


ft.app(target=main)

```
![alt text](/img/excel_file_result.png)

### SQLDataTable

Serialize everything from *users* table

```python
import flet as ft
from simpledt import SQLDataTable


def main(page: ft.Page):
    sql = SQLDataTable('sqlite', 'data.db', 'users') # Serialize everything from `users` table
    dt = sql.datatable

    page.add(dt)


ft.app(target=main)

```

![alt text](/img/sql_file_result.png)

Write a custom query *statement*

```python
import flet as ft
from simpledt import SQLDataTable


def main(page: ft.Page):
    sql = SQLDataTable('sqlite', 'dataset/data.db', statement="SELECT name, surname, LENGTH(name || surname) as len_name_surname FROM users") # Write a custom query statement
    dt = sql.datatable

    page.add(dt)


ft.app(target=main)
```

![alt text](/img/sql_file_code_statement_result.png)

## Docs

### Classes

**Note:** you can pass IO to DataFrame constructor as a source argument, but it's recommended to have your pandas dataframe and pass it as a source argument

- DataFrame(source: Union[pd.DataFrame, IO], **kwargs)
    - **source**: You can pass your own pandas DataFrame as an argument, or any file like 'json', 'excel', 'csv'...
    - ****kwargs**: you can pass keyword arguments if only **IO** is provided insted of DataFrame

### Shortcut Classes

If you don't want to create your own pandas dataframe, these classes does it for you. You just have to pass source

- CSVDataTable(csv_file: str)
- ExcelDataTable(excel_file: str)
- JsonDataTable(json_file: str)
- SQLDataTable(sql_engine: str, database: str, table: str = None, statement: str = None, user: str = None, password: str = None, host: str = None, port: str = None)
    
    - Required arguments
        - **sql_engine** is a literal, you can choose **sqlite**, **mysql**, **postgresql**
        - **database** is a database binary file, like "data.sqlite3"
        - **table** or **statement**, you can choose one of these, but not both. If **table** is provided, it'll serialize everything from that table. Else, you can write your own custom sql **statement**
    
    - Optional arguments
        - **user** is a username for your choice of **sql_engine** (sqlite does not need user)
        - **password** is a password for your choice of **sql_engine** (sqlite does not need password)
        - **host** is a host for your choice of **sql_engine**
        - **port** is a port for your choice of **sql_engine**




