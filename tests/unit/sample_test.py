import os
import shutil
import tempfile
import unittest
from pyspark.sql import SparkSession
from unittest.mock import MagicMock

from dbx_sql_packaging_example.jobs.sample.entrypoint import SampleJobWithJinja


class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory().name
        self.spark = SparkSession.builder.master("local[1]").getOrCreate()
        self.spark.sparkContext.setLogLevel("DEBUG")
        self.test_config = {}
        self.job = SampleJobWithJinja(spark=self.spark, init_conf=self.test_config)

    def test_sample(self):
        # feel free to add new methods to this magic mock to mock some particular functionality
        self.job.dbutils = MagicMock()
        self.job.launch()

    def tearDown(self):
        try:
            shutil.rmtree(self.test_dir)
        except FileNotFoundError:
            self.job.logger.info("Skipping test directory deletion")


if __name__ == "__main__":
    unittest.main()
