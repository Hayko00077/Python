# # Read a File and Print its Content
# # File Name: example.txt
# # Description: The file example.txt contains several lines of text. 
# # Write a program to open the file in read mode and print each line, stripping any leading or trailing whitespace.

# try:
#     with open("example.txt", "r") as file:
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("The file 'example.txt' was not found.")
# print()

# # Write to a File
# # File Name: output.txt
# # Description: Create a file named output.txt and write the text "Python is fun!" into it.
# # Close the file and reopen it to verify its content.

# with open("output.txt", "w") as file:
#     file.write("Python is fun!")
# with open("output.txt", "r") as file:
#     read = file.read()
#     print(read)
# print()

# # Append to a File
# # File Name: notes.txt
# # Description: Open the file notes.txt in append mode and add the text "Remember to review file handling in Python!" as a new line at the end.
# # If the file does not exist, create it.

# with open("output1.txt", "a") as file:
#     file.write("Remember to review file handling in Python!")
# with open("output1.txt", "r") as file:
#     read1 = file.read()
#     print(read1)
# print()

# # Count Words in a File
# # File Name: story.txt
# # Description: Write a program to open the file story.txt, read its content, and count the total number of words in the file.
# # Display the count to the user.
# # Example Content: Once upon a time in a land far, far away, there lived a Python programmer.
# # Expected Output: Total words: 14

# try:
#     with open("output.txt", "r") as file:
#         count = file.read()

#         words = count.split()
#         print(len(words))
# except FileNotFoundError:
#         print(f"The file output.txt was not found.")
# print()

# # Copy File Content
# # Source File: source.txt
# # Description: Write a program to copy the content of source.txt into destination.txt. 
# # If the destination file already exists, overwrite its content.
# # Example Content in source.txt: File handling in Python is powerful and efficient.

# try:
#     with open("source.txt", "r") as source:
#         text = source.read()
#     with open("destination.txt") as destination:
#         destination.write(text)
#     print("Content copied successfully from source.txt to destination.txt")
# except FileNotFoundError:
#     print("The file source.txt was not found")
# except IOError:
#     print("Error: An I/O error occurred")
# print()

# # Remove Blank Lines from a File
# # File Name: data.txt
# # Description: Write a program to remove all blank lines from data.txt and save the cleaned content to cleaned_data.txt.
# # Initial File Content in data.txt:
# # Line 1: Important data.
# # Line 2: More data.
# # Line 3: End of file.

# with open("data.txt", "r") as data:
#     lines = [line for line in data if line.strip()]
    
# with open("cleaned_data.txt") as cleaned_data:
#     cleaned_data.writelines(lines)
# print()

# # Binary File Copy
# # Source File: image.jpg
# # Destination File: copy_image.jpg
# # Description: Write a program to copy the content of a binary file image.jpg into a new file copy_image.jpg. 
# # Ensure that the copied file is identical to the original.

# try:
#     with open("image.jpg", "rb") as source_file:
#         with open("copy_image.jpg", "wb") as dest_file:
#             dest_file.write(source_file.read())
#             print(f"Successfully copied {source_file} to {dest_file}")
# except FileNotFoundError:
#     print("The file image.jpg was not found")
# except IOError:
#     print("Error: An I/O error occurred")
# print()

# # Generate a Summary Report
# # File Name: log.txt
# # Description: Write a program to analyze a log file log.txt and generate a report of the total number of occurrences for each log level (INFO, WARNING, ERROR) in a new file summary.txt.
# # Example Content in log.txt:
# # INFO: Application started.
# # WARNING: Low memory.
# # ERROR: Failed to load module.
# # INFO: User logged in.
# # ERROR: Unable to save file.

# # INFO: 2
# # WARNING: 1
# # ERROR: 2

# log_counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
# try:
#     with open("log.txt", "r") as file:
#         for line in file:
#             for level in log_counts:
#                 if line.startswith(f"{level}:"):
#                     log_counts[level] += 1
#     with open("summary.txt", "w") as sum_file:
#         file.write("Log Level Summary Report\n")
#         file.write("======================\n")
#         for level, count in log_counts.items():
#             sum_file.write(f"{level} : {count}\n")
#     print(f"Summary report generated successfully in {sum_file}")
# except FileExistsError:
#     print("The file log.txt was not found")
# except IOError as e:
#     print(f"Error: Unable to process file. {e}")
# print()

# # Create a File Using a Relative Path
# # Description: Create a new text file named relative_output.txt in a folder called relative_files (located relative to your script's directory). Write "This is a file created using a relative path." into the file.
# # Check if the relative_files directory exists. If not, create it.

# import os

# def creat_file_with_relative_path():
#     folder_path = "relative_files"
#     file_path = os.path.join(folder_path, "relative_output.txt")
#     content = "This is a file created using a relative path."

#     try:
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)
#             print(f"Created directory: {folder_path}")
#         with open(file_path, "w") as file:
#             file.write(content)
#         print(f"Successfully created and wrote to {file_path}")
#     except OSError as e:
#         print(f"Error: Unable to create directory or file. {e}")
#     except IOError as e:
#         print(f"Error: Unable to write to file. {e}")
# creat_file_with_relative_path()
# print()
