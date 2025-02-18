FILEPATH = "todos.txt"
def read_todos(filepath = FILEPATH):
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todolist, filepath = FILEPATH):
    with open(filepath, "w") as temp_file:
        temp_file.writelines(todolist)

