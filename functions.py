FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns the text file's content as a list here the text file is todos.txt file """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_list_arg, filepath=FILEPATH):
    """Gets a list object and writes the list's items in a text file here the text file is todos.txt file"""
    with open(filepath, "w") as file:
        file.writelines(todos_list_arg)
