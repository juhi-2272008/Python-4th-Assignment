
# Read the content of text file line by line
try:
    with open ("Sample.txt","r") as file1:
        print("Reading the content:")
        line_number = 1
        for line in file1:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
    

except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found")    
