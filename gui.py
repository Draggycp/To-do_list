from modules import functions
import PySimpleGUI as sg
import time


sg.theme("DarkBlack")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(image_source="add.png", mouseover_colors="DarkBlue",
                       tooltip="Add a to-do", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todositems',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", mouseover_colors="DarkBlue",
                       tooltip="Complete a to-do", key="Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todositems'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todositems'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todositems'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todositems'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todositems'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case "todositems":
            window['todo'].update(value=values['todositems'][0])
        case sg.WIN_CLOSED:
            break

window.close()
