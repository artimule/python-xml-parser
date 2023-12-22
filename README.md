# Assignment 1: XML Data Processing

## Overview
This Python script is designed to process XML files representing test classes, aggregate the time consumed by test cases for each class, and equally distribute classes into groups based on their total time. The output is a CSV file with information about each class, its time, and the assigned group.

## Instructions
1. **Data Folder**: Place your XML files in the `programming/assignment-1/data/` folder.
2. **Run the Script**: Execute the `assignment.py` script to process the XML files.
3. **Output**: Check the generated CSV file (`output.csv`) for the aggregated information.
4. **Submission**: Zip the entire `programming` folder and submit it by replying to the email where you received the assignments.

## Script Functionality
- **XML Parsing**: Parses all XML files in the specified folder, extracting class names and total time consumed by test cases.
- **Time Aggregation**: Aggregates the time for each class.
- **Group Distribution**: Equally distributes classes into 5 groups based on their total time.
- **CSV Output**: Generates a CSV file with columns: `classname`, `time`, and `groupNo`.

## Sample Output

| classname     | time   | groupNo |
| ------------- | ------ | ------- |
| ClassA        | 10     | 1       |
| ClassB        | 8      | 2       |
| ClassC        | 7      | 3       |
| ClassD        | 6      | 4       |
| ...           | ...    | ...     |


## Usage
```bash
python assignment.py
