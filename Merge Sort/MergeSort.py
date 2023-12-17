import os
import time
import datetime

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        steps = 0
        steps += merge_sort(left_half)
        steps += merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            steps += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            steps += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            steps += 1
        return steps
    return 0

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        n = int(data[0])
        records = [[int(line.strip().split(' ')[0]), ' '.join(line.strip().split(' ')[1:])] for line in data[1:]]
        return n, records

def write_file(file_name, n, records):
    with open(file_name, 'w') as file:
        file.write(f"{n}\n")
        for record in records:
            file.write(f"{record[0]} {record[1]}\n")

input_directory = "Data"
output_directory = "Data_Sorted_Merge_Sort"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Dictionary to store steps and execution time for each dataset
results = {}

for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_directory, filename)
        n, records = read_file(file_path)
        
        # Variables to store steps and time for each dataset
        steps_list = []
        time_list = []

        for i in range(5):  # Run the algorithm 5 times for each dataset.
            print(f"Processing {filename} - Sorting iteration {i+1}")
            start_time = time.time()
            steps = merge_sort(records[:])  # Copy of the records list to ensure consistency
            end_time = time.time()
            execution_time = end_time - start_time

            if i > 0:
                steps_list.append(steps)
                time_list.append(execution_time)

        avg_execution_time = sum(time_list[1:]) / (len(time_list)) if len(time_list) > 1 else 0
        avg_steps = sum(steps_list) / (len(steps_list)) if len(steps_list) > 1 else 0

        # Save results for each dataset
        results[filename] = {'avg_execution_time': avg_execution_time, 'avg_steps': avg_steps}

        merge_sort(records)  # Sort the records for final saving
        sorted_file_name = filename.split('.')[0] + "_sorted.txt"
        sorted_file_path = os.path.join(output_directory, sorted_file_name)
        write_file(sorted_file_path, n, records)

# Print or store results
for dataset, values in results.items():
    avg_exec_time = values['avg_execution_time']
    formatted_time = str(datetime.timedelta(seconds=avg_exec_time)).split(".")[0]
    print(f"Dataset: {dataset}")
    print(f"Avg Execution Time: {avg_exec_time} seconds")
    print(f"Formatted Avg Execution Time: {formatted_time}")
    print(f"Avg Steps: {values['avg_steps']}\n")

# Saving results in a log text file
results_log_file = "Algorithm_Analysis_Merge.txt"

with open(results_log_file, 'w') as file:
    file.write("Algorithm Analysis Results (Merge Sort)\n\n")
    for dataset, values in results.items():
        avg_exec_time = values['avg_execution_time']
        formatted_time = str(datetime.timedelta(seconds=avg_exec_time)).split(".")[0]
        file.write(f"Dataset: {dataset}\n")
        file.write(f"Avg Execution Time: {avg_exec_time} seconds\n")
        file.write(f"Formatted Avg Execution Time: {formatted_time}\n")
        file.write(f"Avg Steps: {values['avg_steps']}\n\n")
