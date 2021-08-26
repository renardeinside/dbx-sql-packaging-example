from dbx_sql_packaging_example.common import Job
import pkg_resources
import pandas as pd
from jinja2 import Template
from pathlib import Path


class SampleJobWithJinja(Job):
    def launch(self):
        self.logger.info("Launching sample job")

        raw_csv_path = pkg_resources.resource_filename(
            "dbx_sql_packaging_example", "resources/raw/username.csv"
        )
        query_path = pkg_resources.resource_filename(
            "dbx_sql_packaging_example", "resources/sql/create_table.sql"
        )

        src_data = self.spark.createDataFrame(pd.read_csv(raw_csv_path, sep=";"))
        src_data.createOrReplaceGlobalTempView("src_data")
        get_query = Template(Path(query_path).read_text()).render(
            src_db="global_temp",
            src_tab="src_data",
        )
        print(f"Executing query {get_query}")
        cnt = self.spark.sql(get_query).count()
        self.logger.info(f"Total amount of records: {cnt}")
        self.logger.info("Sample job finished!")


if __name__ == "__main__":
    job = SampleJobWithJinja()
    job.launch()
