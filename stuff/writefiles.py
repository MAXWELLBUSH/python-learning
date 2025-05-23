# writing to a .txt 
"""

A .txt file is a plain text file — no formatting or structure, just characters. Use it when you want to store human-readable notes, logs, or general strings.

with open('example.txt', 'w') as f:
    f.write("Hello, world!\n")
    f.write("This is a new line.")
open('example.txt', 'w'): opens a file named example.txt in write mode.

'w' mode overwrites the file if it exists, or creates it if it doesn’t.

with statement: handles automatic closing of the file.

f.write(...): writes a string to the file.

\n: newline character — moves to the next line.

✅ When to use:
Writing logs

Saving text input from a user

Creating configuration files (if not structured)
"""

# WRITING TO .JSON 
"""

JSON (JavaScript Object Notation) is a structured format used to store objects and arrays (like dictionaries and lists in Python). It is readable by both humans and machines.

import json

data = {
    "name": "Maxwell",
    "age": 20,
    "skills": ["Python", "React", "Node.js"]
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

import json: JSON is built into Python.
json.dump(data, f): converts the Python dictionary into JSON and writes it to the file.
indent=4: makes the output look nice (pretty print).

This results in a file like:
{
    "name": "Maxwell",
    "age": 20,
    "skills": [
        "Python",
        "React",
        "Node.js"
    ]
}
 When to use:
Storing structured data (like objects/lists)

Saving settings/configurations

API responses and data exchange
"""

# WRITING TO.CSV FILES
"""
CSV (Comma-Separated Values) is a table-like text format used to store data as rows and columns, commonly used with Excel and databases.
import csv

rows = [
    ["Name", "Age", "Country"],
    ["Maxwell", 20, "Kenya"],
    ["Jane", 22, "USA"]
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

    ✅ Explanation:
import csv: CSV handling module

open(..., newline=''): prevents blank lines on Windows

csv.writer(f): creates a writer object

writer.writerows(rows): writes multiple rows at once

data = [
    {"Name": "Maxwell", "Age": 20, "Country": "Kenya"},
    {"Name": "Jane", "Age": 22, "Country": "USA"}
]

with open('people_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Country"])
    writer.writeheader()
    writer.writerows(data)

    ✅ Explanation:
DictWriter: writes data from Python dictionaries

fieldnames: specifies the column order

writer.writeheader(): writes the column headers

✅ When to use:
Exporting data to Excel or Google Sheets

Working with spreadsheets or tabular data

Storing large datasets (simpler than JSON)

"""

