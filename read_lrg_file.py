def read_large_file(file_path):
    with open("large_file.txt",'r') as file:
        for line in file:
            yield line

file_path="large_file.txt"
for line in read_large_file(file_path):
    print(line.strip())