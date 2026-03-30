import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "tasks.txt")

def load_tasks_from_file():
    tasks = {}
    try:
        with open(DB_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if " : " in line:
                    parts = line.split(" : ")
                    if len(parts) == 3:
                        date_str, task, completed_val = parts
                        # If it's '0', it's False. Otherwise, it's the completion time string.
                        status = False if completed_val == "0" else completed_val
                        tasks.setdefault(date_str, []).append([task, status])
    except FileNotFoundError:
        pass
    return tasks

def save_tasks_to_file(tasks):
    with open(DB_PATH, "w") as f:
        for date_str, task_list in tasks.items():
            for task, status in task_list:
                # Save '0' for False, or the time string if completed
                val_to_save = "0" if status is False else str(status)
                f.write(f"{date_str} : {task} : {val_to_save}\n")