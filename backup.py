import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        if not os.path.isdir(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

        if not os.path.isdir(dest_dir):
            print(f"Destination directory '{dest_dir}' does not exist.")
            return

        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)

            if os.path.isfile(source_path):
                dest_path = os.path.join(dest_dir, filename)

                if os.path.exists(dest_path):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{timestamp}{ext}"
                    dest_path = os.path.join(dest_dir, new_filename)

                shutil.copy2(source_path, dest_path)
                print(f"Backed up: {filename} → {dest_path}")

        print("\nBackup completed successfully!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Provide valid source and destination path to backup. Example:- python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    backup_files(source, destination)
