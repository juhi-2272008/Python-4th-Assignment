# Get user input and write to a file

user_input = input("Enter the text to the file: ")
file_1 = open("output.txt","w")
write_file = file_1.write(user_input+"\n")
file_1.close()

print("Data successfully written to the output.txt")

# get the additional input and append to file

user_input = input("Enter additional text to append: ")

file_1 = open("output.txt","a")
append_file = file_1.write(user_input+"\n")
file_1.close()


print("Data Successfully appended ")

# Read and diaplay the final content

file_1 = open("Output.txt","r")
read_file = file_1.read()
file_1.close()


print("Final content of output.txt: \n",read_file)