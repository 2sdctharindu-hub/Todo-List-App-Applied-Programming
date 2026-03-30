import tkinter as tk
from datetime import datetime
import storage_module as storage
import logic_module as logic
import ui_components as ui

# Initial Data Load
tasks = storage.load_tasks_from_file()

def refresh_ui():
    for widget in active_frame.winfo_children(): widget.destroy()
    for widget in completed_frame.winfo_children(): widget.destroy()

    # --- Section: Active Tasks ---
    tk.Label(active_frame, text="Active Tasks", bg="#e0f7fa", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
    for date in sorted(tasks.keys()):
        active_list = [(i, t) for i, t in enumerate(tasks[date]) if t[1] is False]
        if active_list:
            tk.Label(active_frame, text=date, bg="#e0f7fa", font=("Arial", 10, "italic")).pack(anchor="w")
            for idx, (task_text, _) in active_list:
                var = tk.BooleanVar(value=False)
                def toggle(d=date, i=idx, v=var):
                    logic.save_state(tasks)
                    if v.get():
                        # Capture completion time
                        completion_time = datetime.now().strftime("%H:%M")
                        tasks[d][i][1] = completion_time
                    storage.save_tasks_to_file(tasks)
                    refresh_ui()
                
                tk.Checkbutton(active_frame, text=task_text, variable=var, bg="#e0f7fa", command=toggle).pack(anchor="w", padx=10)

    # --- Section: Completed Tasks ---
    tk.Label(completed_frame, text="Completed Tasks", bg="#f1f8e9", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
    for date in sorted(tasks.keys()):
        completed_list = [t for t in tasks[date] if t[1] is not False]
        if completed_list:
            for task_text, finish_time in completed_list:
                display = f"✔ {task_text} (Done: {finish_time})"
                tk.Label(completed_frame, text=display, bg="#f1f8e9", fg="gray", font=("Arial", 9)).pack(anchor="w", padx=5)

def on_add():
    task = task_entry.get().strip()
    date_str = date_entry.get().strip()
    if task and date_str:
        try:
            datetime.strptime(date_str, "%Y-%m-%d") # Validate date
            logic.save_state(tasks)
            tasks.setdefault(date_str, []).append([task, False])
            storage.save_tasks_to_file(tasks)
            task_entry.delete(0, tk.END)
            refresh_ui()
        except ValueError:
            pass # Ignore invalid dates

def on_delete():
    logic.save_state(tasks)
    for date in list(tasks.keys()):
        tasks[date] = [t for t in tasks[date] if t[1] is False]
        if not tasks[date]: del tasks[date]
    storage.save_tasks_to_file(tasks)
    refresh_ui()

def on_undo():
    global tasks
    tasks = logic.perform_undo(tasks)
    storage.save_tasks_to_file(tasks)
    refresh_ui()

def on_redo():
    global tasks
    tasks = logic.perform_redo(tasks)
    storage.save_tasks_to_file(tasks)
    refresh_ui()

# --- Application Startup ---
root = tk.Tk()
root.title("Collaborative To-Do")
root.geometry("700x600")

date_entry, task_entry, active_frame, completed_frame = ui.setup_ui(root, on_add, on_delete, on_undo, on_redo)
date_entry.insert(0, datetime.today().strftime("%Y-%m-%d"))

refresh_ui()
root.mainloop()