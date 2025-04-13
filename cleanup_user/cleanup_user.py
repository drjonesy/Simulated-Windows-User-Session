import os
import shutil

def cleanup_files(cleanup_folders, ignore_file_extensions=None, ignore_paths=None):
    """
    Removes files and folders from specified user directories, respecting the provided ignore lists.

    Args:
        cleanup_folders (list): A list of subdirectories within the user's profile to clean up.
        ignore_file_extensions (list, optional): A list of file extensions to ignore (e.g., ['.log', '.tmp']). Defaults to None.
        ignore_paths (list, optional): A list of absolute or relative paths to ignore. Defaults to None.
    """

    ignored_extensions = set(x.lstrip('.').lower() for x in (ignore_file_extensions or []))
    ignored_paths = set(ignore_paths or [])

    # Determine the current user's home directory dynamically
    windows_user = os.path.expanduser("~")

    for folder_name in cleanup_folders:
        target_folder = os.path.join(windows_user, folder_name)
        if not os.path.isdir(target_folder):
            print(f"Warning: Folder '{target_folder}' does not exist or is not a directory. Skipping.")
            continue

        print(f"Processing folder: {target_folder}")
        for item_name in os.listdir(target_folder):
            item_path = os.path.join(target_folder, item_name)

            # Construct paths relative to the cleanup folder for ignore matching
            relative_path_from_cleanup = os.path.join(folder_name, item_name)

            # Check if the full path or the relative path is in the ignored paths
            if item_path in ignored_paths or relative_path_from_cleanup in ignored_paths or item_name in ignored_paths:
                print(f"  Ignoring (path): '{item_path}'")
                continue

            if os.path.isfile(item_path):
                _, file_extension = os.path.splitext(item_name)
                if file_extension.lstrip('.').lower() in ignored_extensions:
                    print(f"  Ignoring (extension): '{item_path}'")
                    continue
                else:
                    try:
                        os.remove(item_path)
                        print(f"  Removed file: '{item_path}'")
                    except Exception as e:
                        print(f"  Error removing file '{item_path}': {e}")
            elif os.path.isdir(item_path):
                # Check if the nested folder itself is in the ignored paths
                if item_path in ignored_paths or relative_path_from_cleanup in ignored_paths or item_name in ignored_paths:
                    print(f"  Ignoring (folder): '{item_path}'")
                    continue
                else:
                    try:
                        shutil.rmtree(item_path)
                        print(f"  Removed folder: '{item_path}' (and its contents)")
                    except Exception as e:
                        print(f"  Error removing folder '{item_path}': {e}")

if __name__ == "__main__":
    cleanup_folders = ["Desktop", "Documents", "Downloads", "Pictures", "Videos", "Music"]

    # Define the ignore file extensions: 'strings' separate by commas
    # lnk = shortcut
    ignore_file_extensions_config = ['lnk']

    # Define the ignore specific files
    ignore_paths_config = [
        os.path.join("Desktop", "backup.zip"),
        os.path.join("Downloads", "old_installer.exe"),
        os.path.join("Documents", "nested_folder")
    ]

    # Determine the current user's home directory dynamically for creating dummy files
    windows_user = os.path.expanduser("~")


    print("Starting cleanup...")
    cleanup_files(cleanup_folders, ignore_file_extensions=ignore_file_extensions_config, ignore_paths=ignore_paths_config)
    print("Cleanup complete.")