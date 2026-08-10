# variables
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# calculate the problematic rows and problematic percentage
problematic_rows = missing_rows + duplicate_rows
problematic_percentage = (problematic_rows / total_rows) * 100

# check the data quality
if problematic_percentage <= 2:
    data_quality = "Excellent"
elif problematic_percentage > 2 and problematic_percentage <= 5:
    data_quality = "Acceptable"
else:
    data_quality = "Needs Cleaning"

# display the results
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problematic percentage: {problematic_percentage:.2f}%")
print(f"Final classification: {data_quality}")

