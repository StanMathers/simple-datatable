# Simple DataTable

This is a third party package for a new framework `Flet`. `Simple DataTable` is capable of importing `CSV`, `Excel`, `Json` or `SQL` table into `Flet`'s `DataTable`. `Simple DataTable` **uses a few different libraries for serializtion that must be installed according to requirements.txt**. 

`Simple DataTable` returns `DataTable` instance, there is no hardcoded values and anything can be changed according to [Flet docs](https://flet.dev/docs/controls/datatable/)


# Installation

Note: Publishing this package on PyPi is not planned yet, so you need to clone the repo.

1. Clone the repository into your project directory

    ```bash
    git clone https://github.com/StanMathers/simple-datatable .
    ```

2. Install required packages

    ```bash
    pip3 install -r requirements.txt
    ```

And you're good to go!


# Examples
* **Importing a table from a CSV file**
    ```python
    import flet as ft
    from simpledt import CSVDataTable


    def main(page: ft.Page):
        csv = CSVDataTable("dataset/MOCK_DATA.csv")
        dt = csv.datatable

        page.add(dt)


    ft.app(target=main)

    ```

    ![alt text](/img/csv_file_result.png)

* **Importing a table from a CSV url**
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

* **Importing a table from an Excel file**
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

* **Importing a table from a SQL table**
    ```python
    import flet as ft
    from simpledt import SQLDataTable


    def main(page: ft.Page):
        sql = SQLDataTable('sqlite', 'data.db', 'users')
        dt = sql.datatable

        page.add(dt)


    ft.app(target=main)

    ```

    ![alt text](/img/sql_file_result.png)


# Attributes

Every class returns Flet's **DataTable**, **list of `DataRow` and `DataColumn` instances** as attributes, so they can be changed according to [Flet docs](https://flet.dev/docs/controls/datatable/)

After initializing any of the classes, the following attributes are available

* **datatable** - is a serialized **DataTable** instance
* **datarows**  - is a list of serialized **DataRow** instance included in **datatable** attribute.
* **datacolumns** - is a list of serialized **DataColumn** instance included in **datatable** attribute


# Classes

* **BaseDataTable()**
    
    Implements AbstractDataTable and is a parent class of all the other classess. BaseDataTable ensures setting up **datatable**, **datacolumns** and **datarows** which are common among other classes, so all its attributes are available among child classes.

* **CSVDataTable(csv_file: str)**

    Takes a CSV file, or CSV url as an argument for serialization

* **ExcelDataTable(excel_file: str)**

    Takes an Excel file as an argument for serialization

* **JsonDataTable(json_file: str)**

    Takes a Json file as an argument for serialization

* **SQLDataTable(sql_engine: str, database: str, table: str, user: str = None, password: str = None, host: str = None, port: int = None)**

    Takes a SQL database details as an argument for serialization
    
    Required arguments
    * sql_engine is a literal which can be **sqlite, mysql, postgresql**
    * database is a database file, like **data.sqlite3**
    * table is a SQL table which must be serialized
    
    As for optional arguments, according to your choice of SQL, you can provide the following arguments
    
    * user
    * password
    * host
    * port
