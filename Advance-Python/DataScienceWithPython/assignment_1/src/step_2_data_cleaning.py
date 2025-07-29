import csv
from step_1_data_exploration import Exploration

class DataCleaner:
    def __init__(self, data):
        self.data = data
        self.rows = []
        self.headers = []

    def load_data(self):
        self.rows = list(self.data)
        self.headers = self.rows[0]
        self.rows = self.rows[1:]  # Exclude header

    def clean_age(self, age):
        if age.strip() in ['', 'NAN']:
            return '20'  # Replace with median age from previous analysis
        return age

    def clean_gpa(self, gpa):
        if gpa.strip() in ['', '?']:
            return '7.0'  # Replace with approximate median GPA
        # Convert percentage to GPA scale (assuming 100% = 10 GPA)
        gpa = gpa.replace('%', '')
        try:
            gpa_float = float(gpa)
            if gpa_float > 10:  # Likely a percentage
                gpa_float = gpa_float / 10
            return str(round(gpa_float, 1))
        except ValueError:
            return '7.0'

    def clean_diet(self, diet):
        # Split multiple values and take the first one
        return diet.split(';')[0]

    def clean_data(self):
        cleaned_rows = []
        self.load_data()

        for row in self.rows:
            cleaned_row = row.copy()
            # Clean age (column 1)
            cleaned_row[1] = self.clean_age(row[1])
            # Clean GPA (column 4)
            cleaned_row[4] = self.clean_gpa(row[4])
            # Clean diet (column 9)
            cleaned_row[9] = self.clean_diet(row[9])
            cleaned_rows.append(cleaned_row)

        return cleaned_rows

    def save_cleaned_data(self, output_file):
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)  # Write headers
            writer.writerows(self.clean_data())

with open(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\student_response.csv", mode="r") as file:
    data = csv.reader(file)
    cleaner = DataCleaner(data)
    cleaner.save_cleaned_data(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\step_2_cleaned_data.csv")