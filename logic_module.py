import copy

undo_stack = []
redo_stack = []

def save_state(tasks):
    undo_stack.append(copy.deepcopy(tasks))
    redo_stack.clear()

def perform_undo(current_tasks):
    if undo_stack:
        redo_stack.append(copy.deepcopy(current_tasks))
        return undo_stack.pop()
    return current_tasks

def perform_redo(current_tasks):
    if redo_stack:
        undo_stack.append(copy.deepcopy(current_tasks))
        return redo_stack.pop()
    return current_tasks