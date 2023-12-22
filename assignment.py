from bs4 import BeautifulSoup
import os
import csv

# Function to parse XML file
def parse_xml(file_path, csv_writer, group_no):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'xml')
        # Extract information from each <testcase> element
        testcases = soup.find_all('testcase')
        class_total_time = sum(float(testcase['time']) for testcase in testcases)
        group_time = class_total_time / 5.0

        # Calculate cumulative time for each group
        cumulative_time = 0
        for testcase in testcases:
            classname = testcase['classname']
            time = int(float(testcase['time']))
            cumulative_time += time

            # Determine the group number
            if cumulative_time >= group_time:
                group_no += 1
                cumulative_time = time

            csv_writer.writerow([classname, time, group_no])

# Folder containing XML files
folder_path = "C:/Users/HP/Downloads/devops-assignment-main/devops-assignment-main/programming/assignment-1/data"
output_csv_path = 'C:/Users/HP/Downloads/devops-assignment-main/devops-assignment-main/programming/assignment-1/output.csv'

# Open a CSV file for writing
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header to the CSV file
    csv_writer.writerow(['classname', 'time', 'groupNo'])

    group_no = 1
    # Iterate through XML files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            parse_xml(file_path, csv_writer, group_no)

print(f"Data has been successfully written to {output_csv_path}.")






