# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print ("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos('files/todos.txt')

        todos.append(todo)

        functions.write_todos('files/todos.txt', todos)

        item = todo.strip('\n')
        print(f'{item.capitalize()} has been added successfully!')

    elif user_action.startswith("show"):

        todos = functions.get_todos('files/todos.txt')

        # todos2 = [item.strip('\n') for item in todos]

        for i, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            print(f"{i+1}-{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])-1

            todos = functions.get_todos('files/todos.txt')

            new_todo = input(f"Enter a new todo to replace {todos[number].capitalize()}")
            todos[number] = new_todo + '\n'

            functions.write_todos('files/todos.txt', todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos('files/todos.txt')

            number = int(user_action[9:]) - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            message = f"Todo {todo_to_remove.capitalize()} was removed from the list."
            print(message)

            functions.write_todos('files/todos.txt', todos)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown command.")

print("The program will now close.")
