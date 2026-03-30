# [Todo List App] - Group Design Document

**Team Members:** [Nadeera Hettithanthreege Don], [Md Ahmed], [Viral Patel]  
**Date:** [07-02-2026]  
**Version:** 1.0

---

## 1. Project Overview
    We are building a simple app called Todo List that helps people write down their daily tasks and get things done more efficiently.

## 2. Goals & Objectives
* **Core Goal:** 
    (i) We will build a date-based to-do list application that allows users to add, view, and track tasks for specific dates.
* **Secondary Goal:** 
    (i) The program will visually separate active tasks from completed tasks, showing completed tasks in a dedicated section. 
    (ii) Users will be able to mark tasks as completed, and completed tasks will persist between sessions by saving to a file.
    (iii) Users will be able to delete completed tasks. The program will group tasks by date and display them in an organized, readable layout.

## 3. The User Journey
* **The Experience:** 
    When the program starts, the user sees the main window with two sections: Active Tasks on the left and Completed Tasks on the right.
    The user can:
    (i) Enter a date and task description in the input fields.
    (ii) Click Add Task to add a new task to the active list.
    (iii) Check the box next to a task to mark it as completed; the   task then automatically moves to the completed section.
    (iv) Click Delete Completed Tasks to remove all tasks from the completed section.
    (v) All tasks are grouped by date, making it easy to track tasks scheduled for different days.
* **Inputs:** 
    (i) Keyboard input for the task description.
    (ii) Keyboard input for the date in YYYY-MM-DD format.
    (iii) Mouse clicks for Add Task, Delete Completed Tasks, and marking tasks as completed via checkboxes.

## 4. Program Logic (Step-by-Step)

1. **Initialization:** 

    (i) Import the required modules (tkinter for GUI, datetime for date validation).
    (ii) Initialize the main window and configure its layout, size, and colors.
    (iii) Create global variables and data structures, such as the tasks dictionary to store tasks grouped by date.
    (iv) Set up frames for Active Tasks and Completed Tasks.

2. **Load Phase:** 

    (i) Check for the existence of the tasks.txt file.
    (ii) If it exists, read the file line by line and populate the tasks dictionary with stored tasks and their completion status.
    (iii) If it does not exist, start with an empty task list.

3. **Input Phase:** 

    (i) Accept user input for a task description and date through entry fields.
    (ii) Accept user actions such as clicking Add Task, Delete Completed Tasks, or marking tasks as completed via checkboxes.

3. **Processing Phase:**

    (i) When the user adds a task, validate the date format and append the task to the appropriate date in the tasks dictionary.
    (ii) When a task is marked completed, update its status in the tasks dictionary.
    (iii) When Delete Completed Tasks is clicked, remove all completed tasks from the dictionary.
    (iv) Save the updated tasks dictionary to the tasks.txt file after each change.


4. **Output Phase:** 

    (i) Dynamically update the GUI to reflect the current state of tasks.
    (ii) Display active tasks on the left frame with checkboxes.
    (iii) Display completed tasks on the right frame as read-only, grayed-out labels with checkmarks.
    (iv) Group tasks under their respective dates for clarity.


5. **Loop/Cleanup:** 

    * The GUI runs in a continuous event loop, waiting for user interaction.
    * Changes are immediately reflected in the GUI and saved to the file.
    * When the user closes the window, the program exits cleanly, with all tasks saved for the next session.


## 5. Team Responsibility Breakdown

**Nadeera Hettithanthreege Don:
    (i) Responsible for saving and loading tasks to/from tasks.txt.
    (ii) Handles adding tasks, marking tasks as completed, and grouping tasks by date.
**Md Ahmed:
    (i) Designs the GUI, including active and completed task sections side by side.
    (ii) Handles the visual presentation of tasks and updates to the display when tasks change.
**Viral Patel:
    (i) Ensures correct date formats and valid task entries.
    (ii) Tests all features, finds bugs, and ensures the program runs smoothly.
    (iii) Assists with minor logic or UI tweaks if needed.


## 6. Module & Function Breakdown
*List the main parts of our code and which team member is responsible for them.*
* **`main.py`**: The entry point that creates the GUI, sets up frames for active and completed tasks, and connects all functions. (Handled by: Nadeera Hettithanthreege Don)
* **`logic_module.py`**: Functions for managing tasks, including adding tasks, marking tasks completed, grouping tasks by date, and updating the task lists. (Handled by: Md Ahmed)
* **`storage_module.py`**: Functions for saving tasks to tasks.txt and loading tasks from the file to persist data between sessions. (Handled by: Viral Patel)

## 7. Data Storage & Structures

* **Variables/Collections:** 
    We use a dictionary named tasks to store all tasks, where:
        Key: a string representing the date in YYYY-MM-DD format.
        Value: a list of lists, where each inner list contains:
            (i) The task description (string)
            (ii) A boolean indicating whether the task is completed (True/False)

* **Persistence:** 
    All tasks are saved to a file called tasks.txt in the format

## 8. Development Timeline (Milestones)

1. **Milestone 1:** [14-02-2026] - We will have the basic project structure and main menu working.
2. **Milestone 2:** [20-02-2026] - We will have our individual modules connected and talking to each other.
3. **Milestone 3:** [25-02-2026] - We will finish testing for bugs and submit the final version.

---

### Team Checklist:
* **Consistency:**
    (i) Are we all using the same variable naming style.
    (ii) We will follow consistent naming conventions for files, modules, and classes to avoid confusion.

* **Communication:** 
    (i) The team will communicate primarily via WhatsApp for quick discussions and updates. How will we communicate?

* **Integration:**

    (i) Each module or function developed by one member will be tested with the corresponding modules of other members to ensure they work together correctly.
    (ii) Integration testing will occur at regular checkpoints to catch errors early.
    (iii) Any conflicts or issues will be discussed as a team and resolved before the next milestone.
