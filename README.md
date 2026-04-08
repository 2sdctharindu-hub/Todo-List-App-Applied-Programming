# Collaborative To-Do List Application

A Python-based desktop application built with Tkinter that features task management with Undo and Redo capabilities. This project was developed as part of an Applied Programming course assignment.

## Features
* **Task Management**: Add tasks with specific dates and track completion status.
* **Undo/Redo System**: Seamlessly revert or re-apply changes using a stack-based logic.
* **Persistent Storage**: Automatically saves and loads tasks from a local text file.
* **Dynamic UI**: Organized interface with separate sections for active and completed tasks.

## Project Structure
* `main.py`: The entry point of the application that initializes the UI and handles the event loop.
* `logic_module.py`: Contains the logic for state management (Undo/Redo).
* `storage_module.py`: Handles file I/O operations for saving and loading task data.
* `ui_components.py`: Defines the layout and styling of the Tkinter widgets.

## How to Run
1. Ensure you have Python installed on your system.(Python 3.10 or higher is recommended)
2. Here is the link for latest python version https://www.python.org/ftp/python/3.14.4/python-3.14.4-amd64.exe
3. Clone or download this repository.
4. Navigate to the project directory and run the following command:
   ```bash
   python main.py
