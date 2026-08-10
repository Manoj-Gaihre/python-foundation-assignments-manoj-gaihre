# let user to enter the file name
file_name = input("Enter the file name: ")

# convert the file name to lower case and remove any leading or trailing spaces
file_name = file_name.strip().lower()

# check if the file extension is accepted
file_accepted = ["csv", "json", "parquet"]
file_extension = file_name.split(".")[1]

# check if the file extension is accepted and display the appropriate message
if file_extension in file_accepted:
    print(f"The file '{file_name}' is accepted.")
else:
    print(f"The file '{file_name}' is not accepted. Please upload a file with valid extension")


