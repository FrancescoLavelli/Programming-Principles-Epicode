#!/usr/bin/env python3
"""
Script to sort files by creation date and organize them into folders.
This script will:
1. Get the creation date of each file in the current directory
2. Create folders based on creation dates (by day)
3. Move files into their respective folders
"""

import os
import shutil
import datetime
from pathlib import Path


def get_file_creation_date(file_path):
    """Get the creation date of a file."""
    # Get file stats
    stat = os.stat(file_path)

    # Get creation time (ctime on Unix is not creation time, but we'll use mtime)
    # On macOS, st_birthtime is the creation time
    if hasattr(stat, 'st_birthtime'):  # macOS
        creation_time = stat.st_birthtime
    else:  # Fallback to modification time
        creation_time = stat.st_mtime

    # Convert to datetime
    return datetime.datetime.fromtimestamp(creation_time)


def create_date_folder(date):
    """Create a folder based on the date (YYYY-MM-DD format)."""
    folder_name = date.strftime("%Y-%m-%d")
    folder_path = Path(folder_name)

    # Create the folder if it doesn't exist
    if not folder_path.exists():
        folder_path.mkdir()
        print(f"Created folder: {folder_name}")

    return folder_path


def sort_files_by_date():
    """Sort files in the current directory by creation date."""
    # Get the current directory
    current_dir = Path.cwd()

    # Get all files in the current directory and month folders (excluding this script)
    files = []

    # Add files from current directory
    for f in current_dir.iterdir():
        if f.is_file() and f.name != 'sort_files_by_date.py':
            files.append(f)

    # Add files from month folders (2025-03, 2025-04, etc.)
    for folder in current_dir.iterdir():
        if folder.is_dir() and folder.name.startswith('2025-') and len(folder.name) == 7:
            for f in folder.iterdir():
                if f.is_file():
                    files.append(f)

    # Dictionary to store files by date
    files_by_date = {}

    # Group files by creation date
    for file_path in files:
        try:
            # Get creation date
            creation_date = get_file_creation_date(file_path)

            # Format date as YYYY-MM-DD
            date_key = creation_date.strftime("%Y-%m-%d")

            # Add file to the appropriate date group
            if date_key not in files_by_date:
                files_by_date[date_key] = []

            files_by_date[date_key].append(file_path)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Create folders and move files
    for date_key, file_list in files_by_date.items():
        # Create folder for this date
        folder_path = create_date_folder(
            datetime.datetime.strptime(date_key, "%Y-%m-%d"))

        # Move files to the folder
        for file_path in file_list:
            try:
                # Destination path
                dest_path = folder_path / file_path.name

                # Move the file
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved {file_path.name} to {folder_path}")

            except Exception as e:
                print(f"Error moving {file_path}: {e}")


if __name__ == "__main__":
    print("Starting to sort files by creation date...")
    sort_files_by_date()
    print("Finished sorting files.")
