import os
import time
import datetime

def partition(arr, low, high):
    steps = 0  # Initialize the steps counter

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps += 1  # Increment steps count for each swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps += 1  # Increment steps count for pivot placement
    return i + 1, steps  # Return the index of the pivot and the total steps

def quick_sort(arr):
    size = len(arr)
    stack = [(0, size - 1)]

    total_steps = 0  # Total steps for the entire sorting process

    while stack:
        low, high = stack.pop()

        if low < high:
            p, steps = partition(arr, low, high)
            total_steps += steps

            stack.append((low, p - 1))
            stack.append((p + 1, high))

    return arr, total_steps  # Return sorted array and total steps

    

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
output_directory = "Data_Sorted_Quick_Sort"

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
        
        for i in range(6):  # Run the algorithm 6 times for each dataset. First Iteration just reads the data, but no sorting yet.
            print(f"Processing {filename} - Sorting iteration {i+1}")
            #just printing records to check record values
            for i in range(7):
                print(records[i])
            print('before quick sort')

            start_time = time.time()
            date_time_start = datetime.datetime.fromtimestamp(start_time)
            print(date_time_start.strftime("%Y-%m-%d %H:%M:%S"))

            sorted_records, step_count = quick_sort(records[:])
            
            #just printing records to check record values
            for i in range(7):
                print(records[i])

            print('Sorted Records')

            for i in range(7):
                print(sorted_records[i])

            end_time = time.time()
            date_time_end = datetime.datetime.fromtimestamp(end_time)
            print(date_time_end.strftime("%Y-%m-%d %H:%M:%S"))
            
            execution_time = end_time - start_time
            exec_time_readable = execution_time
            formatted_exectime = str(datetime.timedelta(seconds=exec_time_readable)).split(".")[0]
            print(formatted_exectime)

            steps_list.append(step_count)
            print(steps_list)
            time_list.append(execution_time)
            print(time_list)
        
        avg_execution_time = sum(time_list[1:]) / (len(time_list) - 1) if len(time_list) > 1 else 0
        avg_steps = sum(steps_list[1:]) / (len(steps_list) - 1) if len(steps_list) > 1 else 0
        
        # Save results for each dataset
        results[filename] = {'avg_execution_time': avg_execution_time, 'avg_steps': avg_steps}
        
        sorted_file_name = filename.split('.')[0] + "_quick_sorted.txt"
        sorted_file_path = os.path.join(output_directory, sorted_file_name)
        write_file(sorted_file_path, n, sorted_records)

# Print or store results
for dataset, values in results.items():
    avg_exec_time = values['avg_execution_time']
    formatted_time = str(datetime.timedelta(seconds=avg_exec_time)).split(".")[0]  # Convert seconds to HH:MM:SS
    print(f"Dataset: {dataset}")
    print(f"Avg Execution Time: {formatted_time} | Exact Seconds: {values['avg_execution_time']}")
    print(f"Avg Steps: {values['avg_steps']}\n")

# Saving results in a log text file
results_log_file = "Algorithm_Analysis_Quick.txt"

with open(results_log_file, 'w') as file:
    file.write("Algorithm Analysis Results (Quick Sort)\n\n")
    for dataset, values in results.items():
        avg_exec_time = values['avg_execution_time']
        formatted_time = str(datetime.timedelta(seconds=avg_exec_time)).split(".")[0]  # Convert seconds to HH:MM:SS
        file.write(f"Dataset: {dataset}\n")
        file.write(f"Avg Execution Time: {formatted_time} | Exact Seconds: {values['avg_execution_time']}\n")
        file.write(f"Avg Steps: {values['avg_steps']}\n\n")
