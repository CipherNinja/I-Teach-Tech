import csv
import pandas as pd
from step_2_data_cleaning import DataCleaner

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.headers = []
        self.rows = []

    def load_data(self):
        cleaner = DataCleaner(self.data)
        self.rows = cleaner.clean_data()
        self.headers = cleaner.headers

    def convert_screentime(self, screentime):
        if screentime == "More than 6":
            return 7
        elif screentime in ["1-2", "3-4", "5-6"]:
            return float(screentime.split('-')[1])
        return 0

    def analyze_gender(self):
        self.load_data()
        males = []
        females = []
        for row in self.rows:
            if row[2].strip().lower() == "male":
                males.append(row)
            elif row[2].strip().lower() == "female":
                females.append(row)

        print(f"Total Males: {len(males)}")
        print(f"Total Females: {len(females)}")

        for group, label in [(males, "Males"), (females, "Females")]:
            screentimes = [self.convert_screentime(row[7]) for row in group]
            if screentimes:
                avg_screentime = sum(screentimes) / len(screentimes)
                min_screentime = min(screentimes)
                max_screentime = max(screentimes)
                print(f"\n{label} Screen Time (hours/day, non-academic):")
                print(f"  Average: {avg_screentime:.2f}")
                print(f"  Minimum: {min_screentime}")
                print(f"  Maximum: {max_screentime}")

                social_media_freq = {}
                for row in group:
                    sm = row[10]
                    social_media_freq[sm] = social_media_freq.get(sm, 0) + 1
                print(f"\n{label} Social Media Usage:")
                for freq, count in social_media_freq.items():
                    print(f"  {freq}: {count}")

                gpas = [float(row[4]) for row in group]
                avg_gpa = sum(gpas) / len(gpas) if gpas else 0
                print(f"\n{label} Average GPA: {avg_gpa:.2f}")

        return males, females

    def evaluate_performance(self, row):
        score = 0
        # Mental health (Low/Very Low = 2, Moderate = 1, High/Very High = 0)
        mental_health = row[12].lower()
        if mental_health in ["low", "very low"]:
            score += 2
        elif mental_health == "moderate":
            score += 1

        # Physical activity (Always/Often = 2, Sometimes = 1, Never = 0)
        physical = row[8].lower()
        if physical in ["always", "often"]:
            score += 2
        elif physical == "sometimes":
            score += 1

        # Screen time (1-2 = 2, 3-4 = 1, 5-6 or more = 0)
        screentime = self.convert_screentime(row[7])
        if screentime <= 2:
            score += 2
        elif screentime <= 4:
            score += 1

        # Diet (Very healthy = 2, Somewhat healthy/Neutral = 1, Somewhat unhealthy = 0)
        diet = row[9].lower()
        if diet == "very healthy":
            score += 2
        elif diet in ["somewhat healthy", "neutral"]:
            score += 1

        # GPA (close to 10, normalized to 0-2)
        gpa = float(row[4])
        score += min(gpa / 5, 2)  # Scale GPA to 0-2 (10 GPA = 2 points)

        return score

    def find_best_performers(self):
        males, females = self.analyze_gender()
        all_rows = males + females
        all_performers = []

        for row in all_rows:
            score = self.evaluate_performance(row)
            all_performers.append(row + [round(score, 2)])  # Rounded for readability

        # Sort by performance score in descending order
        all_performers.sort(key=lambda x: x[-1], reverse=True)

        print(f"\nPerformance scores assigned to all {len(all_performers)} students.")

        # Define column names explicitly
        df_columns = [
            "Timestamp",
            "age?",
            "gender?",
            "education?",
            "GPA?",
            "sleep",
            "study",
            "screens",
            "activity?",
            "diet?",
            "social?",
            "activities?",
            "mentalH?",
            "Performance"
        ]

        df = pd.DataFrame(all_performers, columns=df_columns)
        df.index = range(1, len(df) + 1)
        df.index.name = "Student"

        # Print top 5 rows
        print("\nTop 5 Performers:")
        print(df.head())

        # Save all performers
        output_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\all_performance_scores.csv"
        df.to_csv(output_path)
        print(f"\nFull performance score data saved to:\n{output_path}")


with open(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\step_2_cleaned_data.csv", mode="r") as file:
    data = csv.reader(file)
    analyzer = DataAnalyzer(data)
    analyzer.find_best_performers()