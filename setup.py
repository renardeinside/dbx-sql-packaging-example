from setuptools import find_packages, setup
from dbx_sql_packaging_example import __version__

setup(
    name="dbx_sql_packaging_example",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    package_data={'': ['resources/sql/*.sql', "resources/raw/*.csv"]},
    version=__version__,
    description="Sample project on Databricks with SQL files",
    author="Ivan Trusov",
)
