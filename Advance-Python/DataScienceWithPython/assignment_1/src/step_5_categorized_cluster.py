import csv
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from step_3_split_data_into_categories import DataAnalyzer

def convert_social_usage(value):
    mapping = {
        "constantly": 0,
        "frequently": 1,
        "occasionally": 2,
        "rarely": 3,
        "never": 4
    }
    return mapping.get(value.strip().lower(), 1)  # default to 1 (frequent)

def convert_screen_score(hours):
    if "more" in hours.lower():
        return 0
    elif hours.strip() == "1-2" or hours.strip() == "5-6":
        return 1
    elif hours.strip() == "3-4":
        return 2
    return 1

def convert_mental_health(value):
    mapping = {
        "very low": 2,
        "low": 1.5,
        "moderate": 1,
        "high": 0.5,
        "very high": 0
    }
    return mapping.get(value.strip().lower(), 1)

def convert_study_hours(value):
    if value == "1-2":
        return 1.5
    elif value == "3-4":
        return 3.5
    elif value == "5-6":
        return 5.5
    return 1.5

def clean_gpa(raw):
    import re
    try:
        gpa = re.findall(r'\d+\.?\d*', raw)
        if gpa:
            val = float(gpa[0])
            return val if val <= 10 else (val / 100) * 10
    except:
        pass
    return 0.0

# Load and prepare data
with open(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\step_2_cleaned_data.csv") as file:
    reader = csv.reader(file)
    analyzer = DataAnalyzer(reader)
    analyzer.load_data()

    feature_data = []
    valid_rows = []

    for row in analyzer.rows:
        try:
            mh = convert_mental_health(row[12])
            study = convert_study_hours(row[6])
            gpa = clean_gpa(row[4])
            social = convert_social_usage(row[10])
            screen = convert_screen_score(row[7])

            features = [mh, study, gpa, social, screen]
            if all(f is not None for f in features):
                feature_data.append(features)
                valid_rows.append(row)
        except Exception as e:
            print(f"Skipping row due to error: {e}")

# Convert to DataFrame
X = np.array(feature_data)

# Cluster into 3 groups
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X)

# Reduce to 2D using PCA
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

# Visualize
plt.figure(figsize=(10, 6))
colors = ['red', 'orange', 'green']
labels = ['Poor Performers', 'Average Performers', 'Good Performers']

for i in range(3):
    cluster_points = reduced_X[clusters == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=labels[i], c=colors[i], alpha=0.6)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Student Performance Clusters")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
