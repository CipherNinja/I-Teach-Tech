import pandas as pd
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Load your dataset
file_path = r"C:\Users\Priyesh Pandey\OneDrive\Desktop\I-Teach-Tech\Advance-Python\DataScienceWithPython\assignment_2\dataset\aircraft_maintenance_logs.csv"
df = pd.read_csv(file_path)

print(Fore.CYAN + Style.BRIGHT + "\n--- Null Value Check ---")
null_counts = df.isnull().sum()
for column, count in null_counts.items():
    color = Fore.RED if count > 0 else Fore.GREEN
    print(f"{color}{column}: {count} null values")

print(Fore.CYAN + Style.BRIGHT + "\n--- Repeated Problems ---")
problem_counts = df['PROBLEM'].value_counts()
repeated = problem_counts[problem_counts > 1]

if not repeated.empty:
    for problem, count in repeated.items():
        print(f"{Fore.YELLOW}{problem}: {count} occurrences")
else:
    print(Fore.GREEN + "No repeated problems found.")
