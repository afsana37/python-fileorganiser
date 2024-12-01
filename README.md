# File Organizer

This Python script, `file_organiser.py`, is designed to organize files in a folder called `files`. The script categorizes files into appropriate subdirectories based on their file types, such as Documents, Images, Videos, Audio, Archives, Scripts, and Others.

## Prerequisites

- **Python 3**: Ensure you have Python 3 installed on your system.
  - To check if Python is installed, run:
    ```bash
    python3 --version
    ```
  - If not installed, download and install Python from [python.org](https://www.python.org/downloads/).

## Getting Started

1. **Clone or Download the Repository**

   - If you have access to a Git repository, clone it using:
     ```bash
     git clone https://github.com/afsana37/python-fileorganiser.git
     ```
   - Otherwise, manually download and place `file_organiser.py` in your desired folder.

2. **Setup the Project Directory**

   Make sure your project directory has the following structure:
   ```
   your_project_directory/
   |-- file_organiser.py
   |-- files/
   ```
   The `files` folder is where the files you want to organize should be located.

3. **Add Files to Organize**

   Place all the files you want to organize inside the `files` folder. The script will move and categorize these files into subdirectories within `files`.

## Running the Script

1. **Navigate to the Project Directory**

   Open a terminal and navigate to the directory containing `file_organiser.py` and the `files` folder:
   ```bash
   cd /path/to/your_project_directory
   ```

2. **Run the File Organizer**

   Execute the script using Python 3:
   ```bash
   python3 file_organiser.py
   ```

3. **Script Execution**

   - The script will automatically create subdirectories within the `files` folder (e.g., `Documents`, `Images`, `Videos`, etc.).
   - It will then move the files from the `files` folder into these subdirectories based on their file extensions.

## Example

- Suppose you have files like `example.jpg`, `document.pdf`, `song.mp3`, and `script.py` in the `files` folder.
- After running the script, the directory structure will look like this:
  ```
  files/
  |-- Documents/
  |   |-- document.pdf
  |
  |-- Images/
  |   |-- example.jpg
  |
  |-- Audio/
  |   |-- song.mp3
  |
  |-- Scripts/
      |-- script.py
  ```

## Notes

- The script uses Python's standard libraries (`os` and `shutil`), so no additional dependencies are required.
- If a file type is not recognized, it will be moved to the `Others` folder.

## Troubleshooting

- **File Not Found Error**: Make sure you are running the script from the directory that contains `file_organiser.py` and the `files` folder.
- **Invalid Path**: Ensure that the `files` folder exists in the same directory as `file_organiser.py`.
