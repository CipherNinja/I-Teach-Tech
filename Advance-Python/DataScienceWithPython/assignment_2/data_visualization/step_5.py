import pandas as pd
import re
from colorama import Fore, Style, init
import matplotlib.pyplot as plt
import os
import networkx as nx
from collections import defaultdict

init(autoreset=True)

# Load dataset
dataset_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_2\dataset\aircraft_maintenance_logs.csv"
df = pd.read_csv(dataset_path)
df.drop(columns=['IDENT'], inplace=True)
df['PROBLEM'] = df['PROBLEM'].astype(str).str.lower()

# Define fuel-related and co-occurrence keywords
fuel_keywords = ['fuel', 'cut off', 'switch', 'valve', 'supply', 'shut', 'block', 'clog', 'pressure', 'flow', 'injector', 'line']
co_keywords = ['shutdown', 'rat', 'hydraulic']
all_keywords = fuel_keywords + co_keywords

# Compile regex patterns
pattern_fuel = re.compile(r'\b(' + '|'.join(fuel_keywords) + r')\b')
pattern_co = re.compile(r'\b(' + '|'.join(co_keywords) + r')\b')

# 🔗 Build keyword co-occurrence network
log_keywords = df['PROBLEM'].apply(lambda x: [kw for kw in all_keywords if re.search(rf'\b{kw}\b', x)])
pair_counts = defaultdict(int)
for kws in log_keywords:
    unique_kws = list(set(kws))
    for i in range(len(unique_kws)):
        for j in range(i + 1, len(unique_kws)):
            pair = tuple(sorted([unique_kws[i], unique_kws[j]]))
            pair_counts[pair] += 1

# Create graph
G = nx.Graph()
for (kw1, kw2), weight in pair_counts.items():
    if weight >= 2:  # filter weak edges
        G.add_edge(kw1, kw2, weight=weight)

# Plot network
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='#FF9800')
nx.draw_networkx_edges(G, pos, width=[G[u][v]['weight'] for u, v in G.edges()], alpha=0.6)
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
plt.title("Keyword Co-occurrence Network", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()


'''

Current Insight
fuel and line are strongly connected—suggesting they often appear together in logs.

fuel and flow are also linked, but less frequently.

'''