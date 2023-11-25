import sys
import os


def calculate_dir_size(directory):
    global total_size
    try:
        print("Hi, this directory size is: ")
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        total_size = 0
        # Iterate through the directory's files
        for filename in os.listdir(directory):
            try:
                file_path = os.path.join(directory, filename)
                total_size += os.path.getsize(file_path)

            except Exception as e:
                print("Error: ", e)
    except Exception as e:
        print("Error: ", e)

    return total_size

if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]

        # Call the function to read and print files
        print(calculate_dir_size(directory_path), "bytes")
