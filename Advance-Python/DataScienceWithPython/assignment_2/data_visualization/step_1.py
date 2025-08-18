import pandas as pd
import matplotlib.pyplot as plt
import re

# Your keyword list
keywords = [
    "leak", "crack", "break", "tear", "fail", "dead", "loose", "damage", "wear", "jam",
    "stuck", "misalign", "bent", "corrosion", "fracture", "deform", "rough", "choke", "idle",
    "stall", "overheat", "spark", "fouled", "power loss", "zero psi", "kill", "short", "fire",
    "smoke", "vibration"
]

# Load dataset
df = pd.read_csv(r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_2\dataset\aircraft_maintenance_logs.csv")  # Replace with your actual file
df['PROBLEM'] = df['PROBLEM'].astype(str).str.lower()

# Count keyword frequencies
freq = {}
for kw in keywords:
    pattern = re.compile(rf"\b{kw}\w*\b")
    count = df['PROBLEM'].apply(lambda x: len(pattern.findall(x))).sum()
    freq[kw] = count

# Convert to DataFrame
freq_df = pd.DataFrame(list(freq.items()), columns=['Keyword', 'Frequency'])
freq_df = freq_df.sort_values(by='Frequency', ascending=False)

# Plotting
plt.figure(figsize=(14, 7))
bars = plt.bar(freq_df['Keyword'], freq_df['Frequency'], color='skyblue')

# Title & labels
plt.title("🔧 Keyword Frequency in Aircraft Maintenance PROBLEM Descriptions", fontsize=16, pad=20)
plt.xlabel("Keyword", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Annotate bars
for bar in bars:
    yval = bar.get_height()
    if yval > 0:
        plt.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom', fontsize=9)

# Add grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
