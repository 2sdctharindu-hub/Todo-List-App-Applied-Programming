import tkinter as tk

def setup_ui(root, add_cmd, delete_cmd, undo_cmd, redo_cmd):
    root.configure(bg="#b3e5fc")
    
    tk.Label(root, text="Team To-Do List", bg="#0288d1", fg="white", 
             font=("Arial", 16, "bold"), pady=10).pack(fill="x")

    date_ent = tk.Entry(root, width=15, font=("Arial", 12))
    date_ent.pack(pady=5)
    
    task_ent = tk.Entry(root, width=30, font=("Arial", 12))
    task_ent.pack(pady=5)

    # Buttons
    btn_frame = tk.Frame(root, bg="#b3e5fc")
    btn_frame.pack(pady=5)
    
    tk.Button(btn_frame, text="Add Task", bg="#27ae60", fg="white", width=10, command=add_cmd).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Delete Done", bg="#e74c3c", fg="white", width=10, command=delete_cmd).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Undo", bg="#f39c12", fg="white", width=10, command=undo_cmd).grid(row=1, column=0, pady=5)
    tk.Button(btn_frame, text="Redo", bg="#8e44ad", fg="white", width=10, command=redo_cmd).grid(row=1, column=1, pady=5)

    container = tk.Frame(root, bg="#b3e5fc")
    container.pack(fill="both", expand=True, pady=10)

    active_f = tk.Frame(container, bg="#e0f7fa", bd=2, relief="ridge")
    active_f.pack(side="left", fill="both", expand=True, padx=(10,5))

    completed_f = tk.Frame(container, bg="#f1f8e9", bd=2, relief="ridge")
    completed_f.pack(side="right", fill="both", expand=True, padx=(5,10))
    
    return date_ent, task_ent, active_f, completed_f