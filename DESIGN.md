Team Members: [Nadeera Tharindu], [Md Ahmed]
Date: [30-03-2026]
Version: 2.0 (Updated for 2-member team)


1. Project Overview
    We are building a simple app called Todo List that helps people write down their daily tasks and get things done more efficiently.
2. Goals & Objectives
Core Goal: (i) We will build a date-based to-do list application that allows users to add, view, and track tasks for specific dates.

Secondary Goal: (i) The program will visually separate active tasks from completed tasks, showing completed tasks in a dedicated section.
                (ii) Users will be able to mark tasks as completed, and completed tasks will persist between sessions by saving to a file.
                (iii) Users will be able to delete completed tasks. The program will group tasks by date and display them in an organized, readable layout.

3. The User Journey
The Experience: When the program starts, the user sees the main window with two sections: Active Tasks on the left and Completed Tasks on the right.
The user can:
              (i) Enter a date and task description in the input fields.
              (ii) Click Add Task to add a new task to the active list.
              (iii) Check the box next to a task to mark it as completed; the task then automatically moves to the completed section.
              (iv) Click Delete Completed Tasks to remove all tasks from the completed section.
              (v) All tasks are grouped by date, making it easy to track tasks scheduled for different days.

Inputs: (i) Keyboard input for the task description.
        (ii) Keyboard input for the date in YYYY-MM-DD format.
        (iii) Mouse clicks for Add Task, Delete Completed Tasks, and marking tasks as completed via checkboxes.

4. Program Logic (Step-by-Step)
Initialization: (i) Import the required modules (tkinter for GUI, datetime for date validation).
                (ii) Initialize the main window and configure its layout, size, and colors.
                (iii) Create global variables and data structures, such as the tasks dictionary to store tasks grouped by date.
                (iv) Set up frames for Active Tasks and Completed Tasks.

Load Phase: (i) Check for the existence of the tasks.txt file.
            (ii) If it exists, read the file line by line and populate the tasks dictionary with stored tasks and their completion status.
            (iii) If it does not exist, start with an empty task list.

Input Phase:   (i) Accept user input for a task description and date through entry fields.
              (ii) Accept user actions such as clicking Add Task, Delete Completed Tasks, or marking tasks as completed via checkboxes.

Processing Phase:
            (i) When the user adds a task, validate the date format and append the task to the appropriate date in the tasks dictionary.
            (ii) When a task is marked completed, update its status in the tasks dictionary.
            (iii) When Delete Completed Tasks is clicked, remove all completed tasks from the dictionary.
            (iv) Save the updated tasks dictionary to the tasks.txt file after each change.

Output Phase: (i) Dynamically update the GUI to reflect the current state of tasks.
              (ii) Display active tasks on the left frame with checkboxes.
              (iii) Display completed tasks on the right frame as read-only, grayed-out labels with checkmarks.
              (iv) Group tasks under their respective dates for clarity.

Loop/Cleanup: * The GUI runs in a continuous event loop, waiting for user interaction.

Changes are immediately reflected in the GUI and saved to the file.

When the user closes the window, the program exits cleanly, with all tasks saved for the next session.

5. Team Responsibility Breakdown
Nadeera Tharindu:
            (i) Responsible for the main entry point and UI integration (main.py and ui_components.py).
            (ii) Managing the GitHub repository, branch merging, and documentation.
            (iii) Handles UI design, including active and completed task sections side by side.

Md Ahmed:
          (i) Responsible for saving and loading tasks to/from tasks.txt (storage_module.py).
          (ii) Handles the core logic, including adding tasks, marking tasks as completed, and grouping tasks by date (logic_module.py).
          (iii) Ensures correct date formats, valid task entries, and overall program testing.

6. Module & Function Breakdown
          *main.py: The entry point that creates the GUI, sets up frames for active and completed tasks, and connects all functions. (Handled by: Nadeera Tharindu)

          *ui_components.py: Contains the visual elements and layout of the application. (Handled by: Nadeera Tharindu)

          *logic_module.py: Functions for managing tasks, adding/completing tasks, and grouping them by date. (Handled by: Md Ahmed)

          *storage_module.py: Functions for saving/loading tasks from tasks.txt to persist data. (Handled by: Md Ahmed)

7. Data Storage & Structures
Variables/Collections: We use a dictionary named tasks to store all tasks, where:
Key: a string representing the date in YYYY-MM-DD format.
Value: a list of lists: [task_description (str), is_completed (bool)].

Persistence: All tasks are saved to a file called tasks.txt in a structured format for long-term storage.

8. Development Timeline (Milestones)
Milestone 1: [14-02-2026] - Basic project structure and main menu working.
Milestone 2: [05-03-2026] - Individual modules connected and talking to each other.
Milestone 3: [28-04-2026] - Final testing, bug fixes, and final submission.

Team Checklist:
Consistency: Follow consistent naming conventions for files and modules.
Communication: Team communicates via WhatsApp for quick updates.
Integration: Regular integration testing to ensure UI and Logic work together correctly.
