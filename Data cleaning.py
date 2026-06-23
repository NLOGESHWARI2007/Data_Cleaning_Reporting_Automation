import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

# Generate summary report
report = df.describe()

with open("report.txt", "w") as f:
    f.write(str(report))

print("Data cleaning and report generation completed.")
