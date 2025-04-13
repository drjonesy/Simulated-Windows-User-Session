import os
import shutil
import platform
import subprocess  # Import the subprocess module

def kill_browser_processes(browsers):
    """Attempts to kill the processes of the specified browsers."""
    for browser in browsers:
        process_name = ""
        if browser == "Edge":
            process_name = "msedge.exe"
        elif browser == "Chrome":
            process_name = "chrome.exe"
        elif browser == "Brave":
            process_name = "brave.exe"

        if process_name:
            try:
                print(f"Attempting to close all instances of {browser}...")
                subprocess.run(f"taskkill /f /im {process_name}", check=False, capture_output=True)
                print(f"Finished attempting to close {browser} processes.")
            except Exception as e:
                print(f"Error trying to close {browser} processes: {e}")

def clear_browser_data(clean_browsers, windows_user):
    """
    Clears history, cache, and potentially other data for specified browsers for a specific user.

    Args:
        clean_browsers (list): A list of browser names (e.g., ["Edge", "Chrome", "Brave"]).
        windows_user (str): The path to the Windows user directory.
    """

    system = platform.system()

    browser_data_paths = {
        "Edge": os.path.join(windows_user, "AppData", "Local", "Microsoft", "Edge", "User Data", "Default"),
        "Chrome": os.path.join(windows_user, "AppData", "Local", "Google", "Chrome", "User Data", "Default"),
        "Brave": os.path.join(windows_user, "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data", "Default"),
        # Add paths for other browsers as needed
    }

    folders_to_clear = [
        "Cache",
        "Code Cache",
        "GPUCache",
        "Media Cache",
        "Network",  # Can contain cookies and other network-related data
        "Session Storage",
        "Local Storage",
        "IndexedDB",
        "Service Worker",
        "Application Cache",  # Deprecated, but might still exist
    ]

    files_to_delete = [
        "History",
        "History Index",
        "Cookies",
        "Cookies-journal",
        "Web Data",  # Can contain autofill data, passwords (handle with extreme caution!)
        "Web Data-journal",
        "Local State",  # Contains some local settings
        # Add other specific files to delete with caution
    ]

    print(f"Starting browser data cleanup for user: {windows_user}...")

    for browser in clean_browsers:
        if browser in browser_data_paths:
            browser_path = browser_data_paths[browser]
            print(f"\nProcessing browser: {browser}")

            if os.path.isdir(browser_path):
                print(f"  Found browser data directory: {browser_path}")

                # Clear specified folders
                for folder in folders_to_clear:
                    folder_path = os.path.join(browser_path, folder)
                    if os.path.isdir(folder_path):
                        try:
                            shutil.rmtree(folder_path)
                            print(f"    Cleared folder: {folder_path}")
                        except Exception as e:
                            print(f"    Error clearing folder '{folder_path}': {e}")

                # Delete specified files
                for file in files_to_delete:
                    file_path = os.path.join(browser_path, file)
                    if os.path.isfile(file_path):
                        try:
                            os.remove(file_path)
                            print(f"    Deleted file: {file_path}")
                        except Exception as e:
                            print(f"    Error deleting file '{file_path}': {e}")
            else:
                print(f"  Warning: Browser data directory not found for {browser} at '{browser_path}'.")
        else:
            print(f"  Warning: No data path defined for browser: {browser}.")

    print("\nBrowser data cleanup complete.")

if __name__ == "__main__":
    # Dynamically get the current user's home directory
    windows_user = os.path.expanduser("~")
    clean_browsers = ["Edge", "Chrome", "Brave"]

    # Attempt to close browser processes before cleaning
    kill_browser_processes(clean_browsers)

    clear_browser_data(clean_browsers, windows_user)