import flet as ft
import pandas as pd
from abc import ABC, abstractmethod
from typing import Literal, List
from sqlalchemy import create_engine

"""
    For a guide to use this class or contribute, please, read this docstring.\n
    
    `General`:\n
    This package is still in development.\n
    
    `How to use:`\n
    After initializing a object from one of the subclasses, you can access the DataTable, DataRow, or DataColumn using attributes `datatable`, `datarows`, `datacolumns`.\n
    
    `Classes`:\n
    `AbstractDataTable` is an abstract class that defines the basic structure of a simple, autogenerated DataTable.\n
    
    `BaseDataTable` is a class containing the basic structure of a simple, autogenerated DataTable shared among other subclasses.\n
    
    `CSVDataTable` and `ExcelDataTable` are subclasses of `AbstractDataTable` that implement the abstract methods.\n
        `CSVDataTable(csv_file: str)` takes a csv file and generates a DataTable from it.\n
        `ExcelDataTable(excel_file: str)` takes an excel file and generates a DataTable from it.\n
    
    `SQLDataTable` is a class that takes a database details and establishes a connection session to a specific table to generate DataTable from it.\n
        `SQLDataTable(sql_engine: AVAILABLE_ENGINES, database: str, table: str, user: str = None, password: str = None, host: str = None, port: str = None)`\n
        
        - sql_engine is the type of database engine you are using. It can be one of the following: `sqlite`, `mysql`, `postgresql`.\n
        - database` is the name of the database you are using (e.g. data.db...).\n
        - table is the name of the table you are using (e.g. users...).\n
        - user is the username of the database user (e.g. root...).\n
        - password is the password of the database, used by your MySQL or Postgresql (e.g. 123456...).\n
        - host is the host of the database (e.g. localhost...).\n
        - port is the port of the database (e.g. 3306...).\n
        


"""


class AbstractDataTable(ABC):
    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def _set_attrs(self) -> None:
        ...

    @property
    @abstractmethod
    def _df(self) -> pd.DataFrame:
        ...

    @property
    @abstractmethod
    def _cols(self) -> List[str]:
        ...

    @property
    def _rows(self) -> List[List[str]]:
        ...


class BaseDataTable(AbstractDataTable):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._set_attrs()

    def _set_attrs(self) -> None:
        # Translating rows and columns to DataTable rows and columns
        _dt_columns = [ft.DataColumn(ft.Text(column)) for column in self._cols]
        _dt_rows = [
            ft.DataRow([ft.DataCell(ft.Text(cell)) for cell in row])
            for row in self._rows
        ]

        # Initializing DataTable
        dt = ft.DataTable(columns=_dt_columns, rows=_dt_rows)

        # Setting DataTable attributes
        setattr(self, "datacolumns", _dt_columns)
        setattr(self, "datarows", _dt_rows)
        setattr(self, "datatable", dt)

    @property
    def _df(self) -> pd.DataFrame:
        return pd.read_csv(self.filename)

    @property
    def _cols(self) -> List[str]:
        return self._df.columns.to_list()

    @property
    def _rows(self) -> List[List[str]]:
        return self._df.values.tolist()


class CSVDataTable(BaseDataTable):
    def __init__(self, csv_file: str) -> None:
        self.csv_file = csv_file
        self._set_attrs()

    @property
    def _df(self) -> pd.DataFrame:
        return pd.read_csv(self.csv_file)


class ExcelDataTable(BaseDataTable):
    def __init__(self, excel_file: str) -> None:
        self.excel_file = excel_file
        self._set_attrs()

    @property
    def _df(self) -> pd.DataFrame:
        return pd.read_excel(self.excel_file)


class JsonDataTable(BaseDataTable):
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self._set_attrs()

    @property
    def _df(self) -> pd.DataFrame:
        return pd.read_json(self.json_file)


class SQLDataTable(BaseDataTable):
    def __init__(
        self,
        sql_engine: Literal["sqlite", "mysql", "postgresql"],
        database: str,
        table: str,
        user: str = None,
        password: str = None,
        host: str = None,
        port: str = None,
    ) -> None:
        self.sql_engine = sql_engine
        self.database = database
        self.table = table
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.__engine = self.__create_engine()

        self._set_attrs()

    def __create_engine(self):
        if self.sql_engine == "sqlite":
            return create_engine(
                f"sqlite:///{self.database}", connect_args={"check_same_thread": False}
            )
        elif self.sql_engine == "mysql":
            return create_engine(
                f"mysql://{self.user}:{self.password}@{self.host}/{self.database}"
            )
        elif self.sql_engine == "postgresql":
            return create_engine(
                f"postgresql://{self.user}:{self.password}@{self.host}/{self.database}"
            )
        else:
            raise Exception("Invalid engine")

    @property
    def _df(self) -> pd.DataFrame:
        return pd.read_sql_table(self.table, self.__engine)
