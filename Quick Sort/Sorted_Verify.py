import os

def is_sorted(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        data = [line.split() for line in lines[1:]]
        ids = [int(record[0]) for record in data]
        return ids == sorted(ids)

directory = 'Data_Sorted_Quick_Sort'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        if is_sorted(file_path):
            print(f"{filename} is sorted in ascending order by ID number.")
        else:
            print(f"{filename} is NOT sorted in ascending order by ID number.")
