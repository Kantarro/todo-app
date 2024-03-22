Filepath = "todos.txt"


def get_todos(filepath=Filepath): # set default parameter, can be changed with new argument
    """Read a text file and return the list of to-do items.""" # documentation strings (docstrings)
    with open(filepath) as file_local:  # with contex manager, open function mode default is "r"
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=Filepath):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local: # with context manager
        file_local.writelines(todos_arg)


# run this file directly, __name__ = "__main__", run on the main.py file, __name__ = functions
if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())