import matplotlib.pyplot as plt
import csv
from step_3_split_data_into_categories import DataAnalyzer
def plot_gender_distribution(males, females):
    labels = ['Males', 'Females']
    sizes = [len(males), len(females)]
    colors = ['skyblue', 'pink']
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Gender Distribution')
    plt.axis('equal')
    plt.show()

def plot_avg_screen_time(males, females, convert_screentime):
    male_screen = [convert_screentime(row[7]) for row in males]
    female_screen = [convert_screentime(row[7]) for row in females]

    plt.bar(['Males', 'Females'], 
            [sum(male_screen)/len(male_screen), sum(female_screen)/len(female_screen)],
            color=['skyblue', 'pink'])
    plt.ylabel('Avg Screen Time (hrs/day)')
    plt.title('Average Screen Time by Gender')
    plt.grid(axis='y')
    plt.show()

def plot_gpa_distribution(males, females):
    gpa_index = 4  # GPA is the 5th column in each row (index starts at 0)

    male_gpas = [float(row[gpa_index]) for row in males if row[gpa_index].replace('.', '', 1).isdigit()]
    female_gpas = [float(row[gpa_index]) for row in females if row[gpa_index].replace('.', '', 1).isdigit()]

    plt.hist(male_gpas, bins=10, alpha=0.6, label='Male', color='blue')
    plt.hist(female_gpas, bins=10, alpha=0.6, label='Female', color='pink')

    plt.xlabel("GPA")
    plt.ylabel("Frequency")
    plt.title("GPA Distribution by Gender")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_mental_health_distribution(rows):
    from collections import Counter
    labels = [row[12].strip().capitalize() for row in rows if row[12].strip()]
    counts = Counter(labels)

    plt.bar(counts.keys(), counts.values(), color='mediumpurple')
    plt.xticks(rotation=45)
    plt.title("Mental Health Status Distribution")
    plt.ylabel("Number of Students")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


def plot_best_performers_scores(best_performers):
    names = [f"{row[1]} ({row[2]})" for row in best_performers]  # Name as Age (Gender)
    scores = [row[-1] for row in best_performers]

    plt.barh(names, scores, color='seagreen')
    plt.xlabel("Performance Score")
    plt.title("Top Performers")
    plt.xlim(0, 10)
    plt.gca().invert_yaxis()
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

# Load the data and get males, females
with open(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\step_2_cleaned_data.csv") as file:
    reader = csv.reader(file)
    data = list(reader)  # Read it once and store
    analyzer = DataAnalyzer(data)

    males, females = analyzer.analyze_gender()
    all_rows = males + females
    best_performers = analyzer.find_best_performers()


plot_gender_distribution(males, females)
plot_avg_screen_time(males, females, analyzer.convert_screentime)
plot_gpa_distribution(males, females)
plot_mental_health_distribution(all_rows)
plot_best_performers_scores(best_performers)
