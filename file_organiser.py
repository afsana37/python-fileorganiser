import os
import shutil

# Define categories for organizing files by their extensions
FILE_CATEGORIES = {
    "Documents": ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.pptx'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Videos": ['.mp4', '.mkv', '.flv', '.avi'],
    "Audio": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.tar', '.rar', '.7z'],
    "Scripts": ['.py', '.js', '.sh'],
    "Others": []
}

def organize_files(folder_path):
    # Create directories for each category if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Iterate over each file in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine file category based on extension
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = os.path.join(folder_path, category)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                moved = True
                break

        # If the file does not match any category, move it to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", filename))

    print("Files have been organized successfully!")

if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder you want to organize: ")
    if os.path.exists(folder_to_organize):
        organize_files(folder_to_organize)
    else:
        print("Invalid path. Please try again.")