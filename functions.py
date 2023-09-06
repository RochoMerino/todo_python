FILEPATH = "todo.txt"  # r = raw string


def get_todos(filepath=FILEPATH):
    """Get the to-do's from the text file and returns them as a list"""
    with (open(filepath, "r")) as file_local:
        todolist_local = file_local.readlines()
    return todolist_local


def write_todos(todolist_arg, filepath=FILEPATH):
    """Write the to-do's to the text file"""
    with (open(filepath, "w")) as file_local:
        file_local.writelines(todolist_arg)

