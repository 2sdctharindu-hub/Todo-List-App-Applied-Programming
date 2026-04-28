# Collaborative To-Do List Application

A Python-based desktop application built with Tkinter that features task management with Undo and Redo capabilities. This project was developed as part of an Applied Programming course assignment.

## Features
* **Task Management**: Add tasks with specific dates and track completion status.
* **User-Friendly Input**: Easy date selection via a graphical calendar and precise time selection using spinboxes.
* **Undo/Redo System**: Seamlessly revert or re-apply changes using a stack-based logic.
* **Persistent Storage**: Automatically saves and loads tasks from a local text file.
* **Dynamic UI**: Organized interface with separate, scrollable sections for active and completed tasks.

## Project Structure
* `main.py`: The entry point of the application that initializes the UI and handles the event loop.
* `logic_module.py`: Contains the logic for state management (Undo/Redo).
* `storage_module.py`: Handles file I/O operations for saving and loading task data.
* `ui_components.py`: Defines the layout, styling, and integrated widgets like the Calendar and Time Spinboxes.

## Prerequisites
To run this application, you need Python installed (3.10 or higher recommended). Additionally, you must install the following external libraries:
* **tkcalendar**: For the graphical date selection widget.
* **babel**: Required by tkcalendar for localized date formatting.

## How to Run
1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory and install the required dependencies:
   
   ```bash
   pip install -r requirements.txt

4. Navigate to the project directory and run the following command:
   ```bash
   python main.py
