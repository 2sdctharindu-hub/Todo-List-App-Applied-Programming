import tkinter as tk
from datetime import datetime
import storage_module as storage
import logic_module as logic
import ui_components as ui

tasks = storage.load_tasks_from_file()

def refresh_ui():
    """Refreshes the task list and sorts by time[cite: 2]."""
    for widget in active_frame.winfo_children(): widget.destroy()
    for widget in completed_frame.winfo_children(): widget.destroy()

    tk.Label(active_frame, text="Active Tasks", bg="#e0f7fa", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
    for date in sorted(tasks.keys()):
        active_list = [(i, t) for i, t in enumerate(tasks[date]) if t[1] is False]
        if active_list:
            active_list.sort(key=lambda x: x[1][0].split(" | Time: ")[-1] if " | Time: " in x[1][0] else "00:00")
            tk.Label(active_frame, text=f"📅 {date}", bg="#e0f7fa", font=("Arial", 10, "italic")).pack(anchor="w")
            for original_idx, (task_text, _) in active_list:
                var = tk.BooleanVar(value=False)
                def toggle(d=date, i=original_idx, v=var):
                    logic.save_state(tasks)
                    if v.get():
                        tasks[d][i][1] = datetime.now().strftime("%Y-%m-%d | %H:%M")
                        storage.save_tasks_to_file(tasks)
                        refresh_ui()
                tk.Checkbutton(active_frame, text=task_text, variable=var, bg="#e0f7fa", command=toggle).pack(anchor="w", padx=10)

    tk.Label(completed_frame, text="Completed Tasks", bg="#f1f8e9", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
    for date in sorted(tasks.keys()):
        completed_list = [t for t in tasks[date] if t[1] is not False]
        if completed_list:
            completed_list.sort(key=lambda x: x[1])
            for task_text, finish_stamp in completed_list:
                tk.Label(completed_frame, text=f"✔ {task_text}\n   (Done: {finish_stamp})", bg="#f1f8e9", fg="#555555", font=("Arial", 9), justify="left").pack(anchor="w", padx=5, pady=2)

def on_add():
    """Captures input from Calendar and Spinboxes[cite: 2]."""
    task = task_entry.get().strip()
    date_str = str(date_entry.get_date()) 
    h, m = hour_spin.get().zfill(2), min_spin.get().zfill(2)
    time_str = f"{h}:{m}"
    
    if task:
        logic.save_state(tasks)
        display_text = f"{task} | Time: {time_str}"
        tasks.setdefault(date_str, []).append([display_text, False])
        storage.save_tasks_to_file(tasks)
        task_entry.delete(0, tk.END)
        refresh_ui()

def on_delete():
    logic.save_state(tasks)
    with open("completed_history.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- Cleanup Archive: {datetime.now().strftime('%Y-%m-%d %H:%M')} ---\n")
        for date in list(tasks.keys()):
            completed_list = [t for t in tasks[date] if t[1] is not False]
            for task_text, finish_stamp in completed_list:
                f.write(f"[{date}] {task_text} | Finished: {finish_stamp}\n")
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

# --- Initialize Root and UI ---
root = tk.Tk()
root.title("Collaborative To-Do Manager")
root.geometry("850x600")

# CRITICAL: setup_ui must come AFTER the functions are defined[cite: 2]
date_entry, hour_spin, min_spin, task_entry, active_frame, completed_frame = ui.setup_ui(root, on_add, on_delete, on_undo, on_redo)

refresh_ui()
root.mainloop()