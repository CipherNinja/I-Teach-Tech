import pandas as pd

# Load your dataset
df = pd.read_csv(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_2\dataset\aircraft_maintenance_logs.csv")  # Replace with your actual filename

# Group by PROBLEM and ACTION to count occurrences
action_counts = df.groupby(['PROBLEM', 'ACTION']).size().reset_index(name='Count')

# For each PROBLEM:
# - Get most frequent ACTION count
# - Get number of unique ACTIONs
summary = (
    action_counts
    .groupby('PROBLEM')
    .agg(
        Most_Common_Action_Count=('Count', 'max'),
        Unique_Action_Count=('ACTION', 'nunique')
    )
    .reset_index()
)

print(summary)
