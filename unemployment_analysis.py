import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('Unemployment in India.csv', skipinitialspace=True)
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'Unemployment in India.csv' file not found. Please check if the file is in the correct directory.")
    exit()

df.columns = df.columns.str.strip()

df = df.dropna()

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print("\n--- First 5 Rows of the Dataset ---")
print(df.head())

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

plt.subplot(1, 2, 1)
state_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=state_unemployment.values, y=state_unemployment.index, hue=state_unemployment.index, palette='viridis', legend=False)
plt.title('Top 10 States by Highest Avg Unemployment (%)', fontsize=12, fontweight='bold')
plt.xlabel('Average Unemployment Rate (%)')
plt.ylabel('State / Region')

plt.subplot(1, 2, 2)
sns.boxplot(x='Area', y='Estimated Unemployment Rate (%)', hue='Area', data=df, palette='pastel', legend=False)
plt.title('Unemployment Rate: Urban vs Rural', fontsize=12, fontweight='bold')
plt.xlabel('Area Type')
plt.ylabel('Unemployment Rate (%)')

plt.tight_layout()
print("\n📊 Generating graphs... Please check the pop-up window.")
plt.show()
