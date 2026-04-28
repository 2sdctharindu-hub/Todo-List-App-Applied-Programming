# Collaborative To-Do List App

This application is a Python-based task management tool built using the **Tkinter** library. It allows users to schedule tasks by date, track completion times, and archive finished tasks while providing **Undo/Redo** functionality.

---

## 🛠 How the Application Works

The application follows a modular structure to keep the code organized:

* **Data Persistence:** Tasks are loaded and saved via the `storage_module`. This ensures that your task list remains persistent even after closing the application.
* **State Management:** The `logic_module` maintains a history of changes, enabling the **Undo** and **Redo** features by taking "snapshots" of your task list state.
* **Dynamic UI:** The `refresh_ui()` function clears and redraws the interface frames every time a change is made, ensuring the display is always synchronized with the data.
* **Archiving:** When the cleanup process is triggered, completed tasks are moved to an external text file (`completed_history.txt`) with a timestamp for permanent record-keeping.

---

## 🚀 How to Use the Application

### 1. Adding a Task
1.  **Date:** Enter the date in `YYYY-MM-DD` format (The current date is filled by default).
2.  **Task:** Type your task in the input field.
3.  **Add:** Click the **Add** button. The task will appear under the **Active Tasks** section, automatically tagged with its creation time.

### 2. Completing a Task
* Locate your task under the **Active Tasks** list.
* Click the **Checkbox** next to the task.
* The task will immediately move to the **Completed Tasks** section, and the system will record the exact completion timestamp.

### 3. Using Undo and Redo
* If you accidentally add or complete a task, click **Undo** to reverse the last action.
* If you undo something by mistake, click **Redo** to restore that action.

### 4. Cleaning Up (Archiving)
* Click the **Delete/Cleanup** button to clear the "Completed Tasks" view.
* **Note:** These tasks are moved to a file named `completed_history.txt`. This keeps your workspace clean while preserving a record of finished work.

---

## 🏗 Technical Structure

| Function | Description |
| :--- | :--- |
| `on_add()` | Validates the date format and appends the new task with a "Created" timestamp. |
| `toggle()` | Handles the logic of switching a task from "Active" to "Completed" status. |
| `on_delete()` | Exports completed tasks to the archive file and updates the current task dictionary. |
| `refresh_ui()` | Iterates through the `tasks` dictionary and dynamically generates Tkinter widgets. |

---

## ⚠️ Requirements
* **Python 3.x**
* **Local Modules:** `storage_module.py`, `logic_module.py`, `main.py` and `ui_components.py` must be in the same directory.
* **Libraries:** `tkinter`, `tkcalendar`, `babel` .
* **Local Modules:** `storage_module.py`, `logic_module.py`, and `ui_components.py` must be in the same directory.
* **Libraries:** `tkinter`, `datetime`.
