import json
import csv
import os

# Open the JSON file
path = "D://output.json"
with open(r"D://output.json") as json_file:
    data = json.load(json_file)

# Specify the path to your desktop directory
desktop_path = os.path.expanduser('~/Desktop')

# Specify the path for the output CSV file on your desktop
csv_file_path = os.path.join(desktop_path, 'output.csv')

# Open a CSV file in write mode
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write header row based on keys of the first item in the JSON data
    writer.writerow(data[0].keys())

    # Write data rows
    for item in data:
        writer.writerow(item.values())

print(f"CSV file saved to: {csv_file_path}")