'''
Write a quick todo list program, add a todo, remove a todo, print todos, mark a todo completed, clear completed
'''
import json

'''
What a todo looks like

todo = {
    "task": str,
    "completed": boolean
}
'''

"""
load todos for a file and return a list of dictionaries
inputs: None
outputs: list of todos
"""
def load_todos():
    todos = []
    try:
        with open("todos.save", "r") as file:
            todos_str = file.read()
        todos = json.loads(todos_str)
    except FileNotFoundError:
        pass
    return todos

"""
inputs: list of todos
outputs: bool
"""
def save_todos(todos):
    with open("todos.save", "w") as file:
        file.write(json.dumps(todos))
    return True


"""
Adds a todo to the global list
inputs: todo
outputs: None
"""
def add_todo(todo):
    todos.append(todo)

"""
removes a todo to the global list
inputs: index in list
outputs: boolean
"""
def remove_todo(index):
    try:
        todos.pop(index)
        return True
    except ValueError:
        return False

"""
Prints out the list of todos, showing which ones are completed
inputs: None
outputs: None
"""
def print_todos():
    for idx, td in enumerate(todos):
        if td["completed"]:
            print("{}: [x] {}".format(idx, td["task"]))
        else:
            print("{}: [ ] {}".format(idx, td["task"]))

"""
Clears all completed todos
input: None
output: None
"""
def clear_completed():
    for td in todos:
        if td["completed"]:
            todos.remove(td)

"""
Marks a todo completed
inputs: index of list
outputs: boolean
"""
def mark_completed(index):
    try:
        todos[index]["completed"] = True
        return True
    except IndexError:
        print("Todo item does not exist")
        return False

# Main Program

print("Your Todo List")
todos = load_todos()
while True:
    print("What would you like todo?")
    user_select = input("A (Add), P (Print), M(Mark Completed), R (Remove), C (Clear Completed), Q(Quit): ").lower()
    if user_select == 'a':
        task = input("Please enter the task: ")
        todo = {"task": task, "completed": False}
        add_todo(todo)
        print("Added {}".format(task))
    elif user_select == 'p':
        print_todos()
    elif user_select == 'm':
        print_todos()
        try:
            index = int(input("What number would you like to mark completed: "))
            mark_completed(index)
            print("Marked {} Completed".format(todos[index]["task"]))
        except ValueError:
            print("Please enter a proper index")
            continue
    elif user_select == 'r':
        print_todos()
        try:
            index = int(input("What number would you like to remove: "))
            remove_todo(index)
        except ValueError:
            print("Please enter a proper index")
            continue
    elif user_select == 'c':
        clear_completed()
        print("Cleared completed")
    elif user_select == 'q':
        print("Program finished!")
        save_todos(todos)
        break
    else:
        print("Please enter an available option")



    