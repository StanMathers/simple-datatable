# simpledt


This is a third party party package for the framework **Flet**.

It enables **Flet** users to serialize

- Pandas DataFrame
- SQL
- CSV
- JSON
- Excel

Into Flet's **DataTable**.

For documentation and other details, please visit the project [repository](https://github.com/StanMathers/simple-datatable)

## Release notes:


### Version 0.3.4


- Added **kwargs to every shortcut function


#### Example usage:


```python
import flet as ft
from simpledt import CSVDataTable

def main(page: ft.Page):
    csv = CSVDataTable("MOCK_DATA2.csv", delimiter=";")
    datatable = csv.datatable
    page.add(datatable)

ft.app(target=main)
```
