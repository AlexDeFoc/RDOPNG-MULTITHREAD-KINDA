import os

def rename_png_files(directory):
    png_files = [file for file in os.listdir(directory) if file.lower().endswith('.png')]
    png_files.sort()  # Sort the list of PNG files

    for index, old_name in enumerate(png_files, start=1):
        new_name = f"{index}.png"
        os.rename(old_name, new_name)

if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    rename_png_files(current_directory)
