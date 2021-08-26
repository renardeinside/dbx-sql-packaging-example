# dbx-sql-packaging-example

Sample project on how to work with SQL files (and other packaged data) from the inside of Python-based dbx packages.

## Picking up arbitrary files

Do the following:

1. Define a separate folder (let's call it `resources`) inside the python module
2. Reference the filenames which shall be added as non-code data. Example could be found in `setup.py`
3. Pick the file from the inside of Python runtime:
```python
import pkg_resources

raw_csv_path = pkg_resources.resource_filename(
    "<package name>", "resources/raw/username.csv"
)
query_path = pkg_resources.resource_filename(
    "<package name>", "resources/sql/create_table.sql"
)
```

## References

- [Python Package Discovery Docs](https://setuptools.readthedocs.io/en/latest/pkg_resources.html)
- [Handy example from Stackoverflow](https://stackoverflow.com/questions/1395593/managing-resources-in-a-python-project)


