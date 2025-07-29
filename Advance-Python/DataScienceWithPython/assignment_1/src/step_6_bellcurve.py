import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_1\src\dataset\all_performance_scores.csv")

# Rename columns for consistency
df.columns = [col.strip().lower().replace("?", "") for col in df.columns]

# Convert performance column to numeric
df['performance'] = pd.to_numeric(df['performance'], errors='coerce')
df = df.dropna(subset=['performance', 'gender'])

# Separate by gender
males = df[df['gender'].str.lower() == 'male']
females = df[df['gender'].str.lower() == 'female']

# Bell Curve Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(males['performance'], label='Male', shade=True)
sns.kdeplot(females['performance'], label='Female', shade=True)
plt.title('Performance Bell Curve by Gender')
plt.xlabel('Performance Index')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("performance_bell_curve_by_gender.png")
plt.close()

# Distraction Matrix
distraction_factors = ['screens', 'social', 'activities']
distraction_matrix = df.groupby('gender')[distraction_factors].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else 'N/A')

# Save matrix
distraction_matrix.to_csv("distraction_matrix_by_gender.csv")

print("✅ Bell curve and distraction matrix generated and saved.")
