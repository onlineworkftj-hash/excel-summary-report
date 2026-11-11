import pandas as pd
import os

def generate_summary(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    print("File successfully read...")
    print("Total rows:", len(df))
    print("Total columns:", len(df.columns))

    # Create the summary report structure
    summary_data = {
        "Metric": [
            "Total Rows",
            "Total Columns",
            "Column Names"
        ],
        "Value": [
            len(df),
            len(df.columns),
            ", ".join(df.columns.astype(str))
        ]
    }

    # Summary of numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        summary_data["Metric"].append(f"{col} Average")
        summary_data["Value"].append(round(df[col].mean(), 2))

        summary_data["Metric"].append(f"{col} Minimum")
        summary_data["Value"].append(df[col].min())

        summary_data["Metric"].append(f"{col} Maximum")
        summary_data["Value"].append(df[col].max())

    # Convert report to a DataFrame
    summary_df = pd.DataFrame(summary_data)

    # Save the report
    summary_df.to_excel(output_file, index=False)

    print(f"\nSummary report created successfully: {output_file}")

# File names
input_file = "data.xlsx"          # Write your original file name here
output_file = "summary_report.xlsx"

if os.path.exists(input_file):
    generate_summary(input_file, output_file)
else:
    print("File not found. Please check the file name.")