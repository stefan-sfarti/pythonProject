from os import path, listdir
from sys import argv as argv


def read_files_in_directory(directory, file_extension):
    try:
        # Check if the directory exists
        if not path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")

        # Iterate through files in the directory
        for filename in listdir(directory):
            # Check if the file has the specified extension
            if filename.endswith(file_extension):
                file_path = path.join(directory, filename)

                try:
                    # Read and print the contents of the file
                    with open(file_path, 'r') as file:
                        print(f"Contents of {filename}:")
                        print(file.read())
                        print("=" * 50)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    if len(argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = argv[1]
        file_extension = argv[2]

        # Call the function to read and print files
        read_files_in_directory(directory_path, file_extension)
