import tkinter as tk
from tkcalendar import DateEntry 

def setup_ui(root, on_add, on_delete, on_undo, on_redo):
    # --- Top Input Section ---
    input_frame = tk.Frame(root, bg="#eeeeee", pady=10)
    input_frame.pack(fill="x")

    # Date Input
    tk.Label(input_frame, text="Date:", bg="#eeeeee").grid(row=0, column=0, padx=5)
    date_entry = DateEntry(
        input_frame, width=12, background='darkblue', foreground='white', 
        borderwidth=2, date_pattern='yyyy-mm-dd', selectmode='day',       
        showweeknumbers=False, headersbgcolor='#3c3f41' 
    )
    date_entry.grid(row=0, column=1, padx=5)

    # User Friendly Time Input (Spinboxes)
    time_frame = tk.Frame(input_frame, bg="#eeeeee")
    time_frame.grid(row=0, column=2, padx=5)
    
    tk.Label(time_frame, text="Time:", bg="#eeeeee").pack(side="left")
    hour_spin = tk.Spinbox(time_frame, from_=0, to=23, width=3, format="%02.0f", wrap=True)
    hour_spin.pack(side="left", padx=2)
    tk.Label(time_frame, text=":", bg="#eeeeee").pack(side="left")
    min_spin = tk.Spinbox(time_frame, from_=0, to=59, width=3, format="%02.0f", wrap=True)
    min_spin.pack(side="left", padx=2)

    # Task Input
    tk.Label(input_frame, text="Task:", bg="#eeeeee").grid(row=0, column=3, padx=5)
    task_entry = tk.Entry(input_frame, width=30)
    task_entry.grid(row=0, column=4, padx=5)

    # Add Button
    add_btn = tk.Button(input_frame, text="Add Task", command=on_add, bg="#4caf50", fg="white")
    add_btn.grid(row=0, column=5, padx=10)

    # --- Control Buttons ---
    control_frame = tk.Frame(root, bg="#eeeeee", pady=5)
    control_frame.pack(fill="x")
    tk.Button(control_frame, text="Undo", command=on_undo).pack(side="left", padx=5)
    tk.Button(control_frame, text="Redo", command=on_redo).pack(side="left", padx=5)
    tk.Button(control_frame, text="Clear Completed & Archive", command=on_delete, bg="#f44336", fg="white").pack(side="right", padx=5)

    # --- Display Section ---
    display_frame = tk.Frame(root)
    display_frame.pack(fill="both", expand=True, padx=10, pady=10)

    active_canvas = tk.Canvas(display_frame, bg="#e0f7fa")
    active_scroll = tk.Scrollbar(display_frame, orient="vertical", command=active_canvas.yview)
    active_frame = tk.Frame(active_canvas, bg="#e0f7fa")
    active_canvas.create_window((0, 0), window=active_frame, anchor="nw")
    active_canvas.configure(yscrollcommand=active_scroll.set)
    active_canvas.pack(side="left", fill="both", expand=True)
    active_scroll.pack(side="left", fill="y")

    completed_canvas = tk.Canvas(display_frame, bg="#f1f8e9")
    completed_scroll = tk.Scrollbar(display_frame, orient="vertical", command=completed_canvas.yview)
    completed_frame = tk.Frame(completed_canvas, bg="#f1f8e9")
    completed_canvas.create_window((0, 0), window=completed_frame, anchor="nw")
    completed_canvas.configure(yscrollcommand=completed_scroll.set)
    completed_canvas.pack(side="right", fill="both", expand=True)
    completed_scroll.pack(side="right", fill="y")

    def update_scroll(event):
        active_canvas.configure(scrollregion=active_canvas.bbox("all"))
        completed_canvas.configure(scrollregion=completed_canvas.bbox("all"))
    active_frame.bind("<Configure>", update_scroll)
    completed_frame.bind("<Configure>", update_scroll)

    return date_entry, hour_spin, min_spin, task_entry, active_frame, completed_frame