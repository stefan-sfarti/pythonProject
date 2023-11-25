import os
import sys
from os import path, listdir


def rename_sequentially(directory, file_extension):
    try:
        print("Hi, I renamed all your files sequentially!")
        # Check if the directory exists
        if not path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        counter = 1
        # Iterate through the directory's files
        for filename in listdir(directory):
            # Check the file extension and add the extension to the name of the file
            if filename.endswith(file_extension):
                try:
                    old_filepath = os.path.join(directory, filename)
                    new_filename = file_extension + "_file" + "_" + str(counter) + "." + file_extension
                    new_filepath = os.path.join(directory, new_filename)
                    os.rename(old_filepath, new_filepath)
                    counter += 1
                except FileExistsError as e:
                    print("A file with the same name exists already!")
                except OSError as e:
                    print("Could not rename file:", filename, "Exception: ", e)
                except Exception as e:
                    print("Error ", e)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        # Call the function to read and print files
        rename_sequentially(directory_path, file_extension)
