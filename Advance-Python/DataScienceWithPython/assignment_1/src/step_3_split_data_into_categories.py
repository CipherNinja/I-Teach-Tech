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
        best_performers = []

        for row in all_rows:
            score = self.evaluate_performance(row)
            if score >= 8:  # Threshold for "best" performance (out of 10)
                best_performers.append(row + [score])

        # Sort by performance score in descending order
        best_performers.sort(key=lambda x: x[-1], reverse=True)

        print("\nBest Performers (Score >= 8):")
        print(f"Total Best Performers: {len(best_performers)}")
        if best_performers:
            print("\nTop 4 Best Performers:")
            # Define column names explicitly
            df_columns = [
                "Timestamp",
                "What is your age?",
                "What is your gender?",
                "What is your current level of education?",
                "What is your average grade or GPA? (Enter % or GPA)",
                "How many hours do you sleep per night (on average)?",
                "How many hours per day do you study (outside of class)?",
                "How many hours per day do you spend on screens (non-academic)?",
                "How often do you engage in physical activity?",
                "How would you rate your diet/nutrition?",
                "How often do you use social media?",
                "Do you participate in extracurricular activities?",
                "How would you rate your current stress or mental health level?",
                "Performance Score"
            ]
            
            df_data = [row for row in best_performers[:4]]  # Take top 4
            
            for row in df_data:
                if len(row) != 14:
                    print(f"Warning: Row has {len(row)} columns instead of 14: {row}")
            df = pd.DataFrame(df_data, columns=df_columns)
            df.index = range(1, min(len(df_data) + 1, 5))
            df.index.name = "Student"
            print(df)
            output_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\tech-training\DataScience\assignment_1\src\dataset\best_performers.csv"
            df.to_csv(output_path)

with open(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\tech-training\DataScience\assignment_1\src\dataset\step_2_cleaned_data.csv", mode="r") as file:
    data = csv.reader(file)
    analyzer = DataAnalyzer(data)
    analyzer.find_best_performers()