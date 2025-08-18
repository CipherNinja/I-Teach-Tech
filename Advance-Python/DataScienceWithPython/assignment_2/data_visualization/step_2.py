import pandas as pd
import matplotlib.pyplot as plt
import re

# Load dataset (IDENT will be dropped)
df = pd.read_csv(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_2\dataset\aircraft_maintenance_logs.csv")
df.drop(columns=['IDENT'], inplace=True)
df['PROBLEM'] = df['PROBLEM'].astype(str).str.lower()

# Define clusters
clusters = {
    "Fluid System Issues": ["leak", "loose", "gasket"],
    "Structural Issues": ["crack", "break", "tear", "damage"],
    "Engine Behavior": ["rough", "idle", "choke", "stall"]
}

# Count matches per cluster
cluster_counts = {}
for cluster_name, keywords in clusters.items():
    total = 0
    for kw in keywords:
        pattern = re.compile(rf"\b{kw}\w*\b")
        count = df['PROBLEM'].apply(lambda x: len(pattern.findall(x))).sum()
        total += count
    cluster_counts[cluster_name] = total

# Convert to DataFrame
cluster_df = pd.DataFrame(list(cluster_counts.items()), columns=['Cluster', 'Frequency'])

# Plot
plt.figure(figsize=(8, 5))
bars = plt.bar(cluster_df['Cluster'], cluster_df['Frequency'], color=['#4CAF50', '#FF9800', '#2196F3'])
plt.title("🧠 Root Cause Clustering of Aircraft Problems", fontsize=14, pad=15)
plt.ylabel("Keyword Match Frequency", fontsize=12)
plt.xticks(rotation=0)

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
