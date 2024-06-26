import functions
import PySimpleGUI as sg
import time

sg.theme('LightBrown4')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="thing_todo")
add_button = sg.Button(image_source='add.png', mouseover_colors='LightBlue2', tooltip='Add todo.', key='Add')
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", mouseover_colors='LightBlue2')
complete_button = sg.Button(image_source='complete.png', mouseover_colors='LightBlue2',
                            tooltip='Complete todo.', key='Complete')
exit_button = sg.Button("Exit", mouseover_colors='LightBlue2')

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica",15))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values["thing_todo"] + "\n"  # values = {"thing_todo": whatever was added}
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["thing_todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 15))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['thing_todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 15))
        case 'Exit':
            break
        case 'todos':
            window["thing_todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
