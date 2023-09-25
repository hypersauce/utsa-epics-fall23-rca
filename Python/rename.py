# Import the os module
import os

# Define a function to rename multiple images in a folder
def rename_images(folder, pattern):
    # Get the list of image files in the folder
    files = [f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".png", ".gif", ".bmp"))]
    # Loop through the files and rename them
    for i, file in enumerate(files):
        # Get the old file name and extension
        old_name, ext = os.path.splitext(file)
        # Build the new file name with the pattern and index
        new_name = pattern % i + ext
        # Rename the file using os.rename
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))

# Define a folder path and a name pattern as inputs
folder = "C:/Users/raulc/OneDrive/UTSA/EPICS"
pattern = "pinguino_%d.jpg"

# Call the rename_images function with the inputs
rename_images(folder, pattern)
