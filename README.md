# <img src="windows_colorful_icon.png" width="30"> Simulated Windows User Session

This software makes a **Windows user session** feel brand new each time someone logs in—perfect for **public computers**, like in a **library or school**.

It clears browser data and deletes personal files when a user logs in.

---

## 📁 What’s Included

This project has **2 small apps** (`.exe` files) that run automatically when a user logs into Windows:

```sh
C:\Scripts\cleanup_user.exe
C:\Scripts\cleanup_browsers.exe
```

They are created using Python and **PyInstaller** with this command:

```sh
pyinstaller --onefile <filename.py>
```

---

## 🛠 How to Install

1. **Install Python and PyInstaller**:

   ```sh
   pip install pyinstaller
   ```

2. If your terminal doesn’t recognize the `pyinstaller` command, run it like this (change `student` to your username):

   ```sh
   C:\Users\student\AppData\Roaming\Python\Python313\Scripts\pyinstaller.exe --onefile cleanup_user.py
   ```

3. Put both `.exe` files in:

   ```sh
   C:\Scripts\
   ```

---

## 🔁 Make Apps Run When You Log In

We’ll use **Task Scheduler** to make sure the cleanup apps run every time someone logs in.

### ✅ Step-by-Step Setup

1. Press the **Windows key** on your keyboard.
2. Search for `Task Scheduler` and open it.
3. Click **Create Basic Task**.
4. Give it a name like:
   - `Cleanup User`
   - `Cleanup Browsers`
5. Click **Next**.
6. For the **trigger**, choose `When I log on`. Click **Next**.
7. For the **action**, choose `Start a program`. Click **Next**.
8. Browse and select:
   - `C:\Scripts\cleanup_user.exe`
9. Click **Next**, then click **Finish**.

> Repeat the same steps for `cleanup_browsers.exe`.

---

## 🧪 How to Modify the Python Scripts

Here’s the folder structure:

```
\project-folder
├── cleanup_user
│   ├── cleanup_user.py
│   ├── cleanup_user_taskSchedulerDesc.txt
│   └── dist/
│       └── cleanup_user.exe
├── cleanup_browsers
│   ├── cleanup_browsers.py
│   ├── cleanup_browsers_taskSchedulerDesc.txt
│   └── dist/
│       └── cleanup_browsers.exe
```

---

### ✏️ Customizing `cleanup_user.py`

You can change what folders and file types are cleared when a user logs in.

Here’s the section of the code you can edit:

```py
cleanup_folders = ["Desktop", "Documents", "Downloads", "Pictures", "Videos", "Music"]

ignore_file_extensions_config = ['lnk']  # This keeps shortcut files safe

ignore_paths_config = [
    os.path.join("Desktop", "backup.zip"),
    os.path.join("Downloads", "old_installer.exe"),
    os.path.join("Documents", "nested_folder")
]
```

---

### 🌐 Customizing `cleanup_browsers.py`

This lets you pick which browsers get their data cleared:

```py
clean_browsers = ["Edge", "Chrome", "Brave"]
```

It uses the current user's folder automatically, so it works for whoever logs in.

---

## 💡 Summary

- Automatically deletes personal files and browser data on login
- Easy to customize with Python
- Great for shared/public Windows computers

If you can run Python scripts, you can tweak this to do exactly what you want!
