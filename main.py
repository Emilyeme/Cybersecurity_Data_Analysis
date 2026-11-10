import pandas as pd

# Load the cybersecurity dataset
print("Loading cybersecurity dataset...")

df = pd.read_parquet("cic_ids2017.parquet")

# Display the first five records
print("\nFirst five records:")
print(df.head())

# Display dataset information
print("\nDataset information:")
print(df.info())

# Display dataset dimensions
print("\nDataset dimensions:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset loaded successfully!")
# Analyse network traffic labels

print("\n--- CYBERSECURITY TRAFFIC ANALYSIS ---")

# Count each traffic category
traffic_counts = df["Label"].value_counts()

print("\nTraffic categories:")
print(traffic_counts)

# Calculate percentages
traffic_percentages = df["Label"].value_counts(normalize=True) * 100

print("\nTraffic percentages:")
print(traffic_percentages.round(2))

# Count total records
print("\nTotal network traffic records:")
print(len(df))

# Visualise traffic categories

import matplotlib.pyplot as plt

traffic_counts.plot(
    kind="bar",
    title="Cybersecurity Network Traffic Analysis"
)

plt.xlabel("Traffic Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("traffic_analysis.png")

plt.show()
print("\nTraffic analysis completed!")

print("\n--- DATA QUALITY CHECK ---")

# Check missing values
print("\nMissing values:")
print(df.isnull().sum().sum())

# Check duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())

# Check dataset shape
print("\nDataset dimensions before cleaning:")
print(df.shape)

# Remove duplicate records
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

print("\nDataset dimensions after cleaning:")
print(df.shape)

print("\nData cleaning completed!")

# ANALYSE CLEANED DATA

print("\n--- CLEANED TRAFFIC ANALYSIS ---")

print("\nTraffic categories after cleaning:")
print(df["Label"].value_counts())

print("\nTraffic percentages after cleaning:")
print((df["Label"].value_counts(normalize=True) * 100).round(2))

# VISUALISE CLEANED DATA

print("\nCreating cleaned data visualisation...")

cleaned_counts = df["Label"].value_counts()

plt.figure(figsize=(8, 5))

cleaned_counts.plot(
    kind="bar",
    title="Cybersecurity Traffic Analysis After Data Cleaning"
)

plt.xlabel("Traffic Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("cleaned_traffic_analysis.png")

plt.show()

print("\nCleaned data graph saved successfully!")

# COMPARE BENIGN AND PORTSCAN TRAFFIC

print("\n--- NETWORK TRAFFIC CHARACTERISTICS ---")

features = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Flow Bytes/s"
]

traffic_comparison = df.groupby("Label")[features].median()

print("\nMedian network traffic characteristics:")

print(traffic_comparison.round(2).to_string())

print("\nTraffic comparison completed!")