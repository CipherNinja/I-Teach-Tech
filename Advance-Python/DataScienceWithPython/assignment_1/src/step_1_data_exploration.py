import csv
import pandas as pd

class Exploration:
    def __init__(self, data):
        self.data = data
        self.rows = []
        self.null_values = {}

    def load_data(self):
        self.rows = list(self.data)
        self.row_count = len(self.rows) - 1  # Exclude header
        self.col_count = len(self.rows[0]) if self.rows else 0

    def count_nulls(self):
        headers = self.rows[0]
        for col_idx in range(len(headers)):
            self.null_values[headers[col_idx]] = 0
        for row in self.rows[1:]:
            for col_idx, value in enumerate(row):
                if value.strip() in ['', 'NAN', '?']:
                    self.null_values[headers[col_idx]] += 1

    def get_data_types(self):
        df = pd.DataFrame(self.rows[1:], columns=self.rows[0])
        data_types = df.dtypes.to_dict()
        return {col: str(dtype) for col, dtype in data_types.items()}

    def explore_dataset(self):
        self.load_data()
        self.count_nulls()
        data_types = self.get_data_types()

        print(f"Dataset Size: {self.row_count} rows, {self.col_count} columns")
        print("\nColumn Names:")
        for col in self.rows[0]:
            print(f"- {col}")

        print("\nData Types:")
        for col, dtype in data_types.items():
            print(f"{col}: {dtype}")

        print("\nNull Values:")
        for col, count in self.null_values.items():
            print(f"{col}: {count} null values")

with open(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\tech-training\DataScience\assignment_1\src\dataset\student_response.csv", mode="r") as file:
    data = csv.reader(file)
    explorer = Exploration(data)
    explorer.explore_dataset()