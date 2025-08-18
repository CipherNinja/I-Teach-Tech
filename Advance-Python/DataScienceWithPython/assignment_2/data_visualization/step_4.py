import pandas as pd
import re
from colorama import Fore, Style, init
import matplotlib.pyplot as plt
import os

init(autoreset=True)

# Load dataset
dataset_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_2\dataset\aircraft_maintenance_logs.csv"
df = pd.read_csv(dataset_path)
df.drop(columns=['IDENT'], inplace=True)
df['PROBLEM'] = df['PROBLEM'].astype(str).str.lower()

# Define fuel-related keywords
fuel_keywords = ['fuel', 'cut off', 'switch', 'valve', 'supply', 'shut', 'block', 'clog', 'pressure', 'flow', 'injector', 'line']
pattern_fuel = re.compile(r'\b(' + '|'.join(fuel_keywords) + r')\b')

# Define co-occurrence keywords
co_keywords = ['shutdown', 'rat', 'hydraulic']
pattern_co = re.compile(r'\b(' + '|'.join(co_keywords) + r')\b')

# Flagging
df['FUEL_RISK_FLAG'] = df['PROBLEM'].apply(lambda x: 1 if pattern_fuel.search(x) else 0)
df['CO_OCCURRENCE_FLAG'] = df['PROBLEM'].apply(lambda x: 1 if pattern_co.search(x) else 0)

# CLI Summary
fuel_count = df['FUEL_RISK_FLAG'].sum()
co_count = df['CO_OCCURRENCE_FLAG'].sum()
both_count = ((df['FUEL_RISK_FLAG'] == 1) & (df['CO_OCCURRENCE_FLAG'] == 1)).sum()

print(Fore.YELLOW + "\n🚨 Fuel Risk Detection Summary")
print(Fore.GREEN + f"Total Logs: {len(df)}")
print(Fore.RED + f"Fuel-Related Issues: {fuel_count}")
print(Fore.CYAN + f"Co-occurrence with Shutdown/RAT/Hydraulic: {co_count}")
print(Fore.MAGENTA + f"Critical Overlap (Fuel + Co-occurrence): {both_count}")

# Keyword frequency
keyword_freq = {kw: df['PROBLEM'].str.count(rf'\b{kw}\b').sum() for kw in fuel_keywords}
freq_df = pd.DataFrame(list(keyword_freq.items()), columns=['Keyword', 'Frequency']).sort_values(by='Frequency', ascending=False)

# Plot
plt.figure(figsize=(10, 5))
bars = plt.bar(freq_df['Keyword'], freq_df['Frequency'], color='#FF5722')
plt.title("🔧 Fuel System Keyword Frequency", fontsize=14)
plt.ylabel("Occurrences", fontsize=12)
plt.xticks(rotation=45)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=9)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Save filtered rows to common file
filtered_df = df[(df['FUEL_RISK_FLAG'] == 1) | (df['CO_OCCURRENCE_FLAG'] == 1)]
save_path = os.path.join(os.path.dirname(dataset_path), "filtered_fuel_risk_logs.csv")
filtered_df.to_csv(save_path, index=False)
print(Fore.BLUE + f"\n📁 Filtered logs saved to: {save_path}")
